#!/usr/bin/env python3
"""Validate the preserved skill archive without external dependencies or network calls."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET

TOKEN_PATTERNS = {
    'private key': re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----'),
    'API credential': re.compile(r'\b(?:sk-[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[A-Z0-9]{16}|AIza[A-Za-z0-9_-]{30,}|xox[baprs]-[A-Za-z0-9-]{20,})\b'),
    'literal credential': re.compile(r'''(?i)\b(?:password|passwd|api[_-]?key|client[_-]?secret|access[_-]?token|secret[_-]?key)\b\s*[:=]\s*["']([^"'\n]{4,})["']'''),
    'credential URL': re.compile(r'https?://[^\s/:]+:[^\s/@]+@'),
    'personal email': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'),
    'international phone': re.compile(r'(?<!\w)\+\d[\d ()-]{8,}\d\b'),
}

def sensitive_matches(text):
    """Return locations only; never include matched secret values in logs."""
    results = []
    for kind, pattern in TOKEN_PATTERNS.items():
        for match in pattern.finditer(text):
            if kind == 'personal email' and match.group() == 'git@github.com':
                continue  # Generic SSH example used by the preserved source.
            results.append((kind, text.count('\n', 0, match.start()) + 1))
    return results

def within(root, relative):
    path = root / relative
    resolved = path.resolve()
    if not resolved.is_relative_to(root.resolve()):
        raise ValueError(f'Path escapes repository: {relative}')
    return path

def anchors(text):
    found = set(re.findall(r'<a\s+id="([^"]+)"', text))
    for heading in re.findall(r'^#{1,6}\s+(.+)$', text, re.M):
        heading = ''.join(c for c in heading.lower() if c in '-_ ' or unicodedata.category(c)[0] in 'LN')
        found.add(heading.replace(' ', '-'))
    return found

def link_errors(root, source, text):
    errors = []
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
        if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:', target):
            continue
        name, _, fragment = target.partition('#')
        try:
            dest = within(root, str(source.parent / name)) if name else root / source
        except ValueError as exc:
            errors.append(str(exc)); continue
        if not dest.is_file():
            errors.append(f'{source}: missing link target {target}')
        elif fragment and fragment not in anchors(dest.read_text(encoding='utf-8')):
            errors.append(f'{source}: missing anchor {target}')
    return errors

def validate(root):
    errors = []
    manifest = json.loads((root / 'IMPORT-MANIFEST.json').read_text(encoding='utf-8'))
    actual = {str(p.relative_to(root)) for p in (root / 'skills').glob('*/SKILL.md')}
    expected = {s['path'] for s in manifest['skills']}
    if actual != expected or len(expected) != len(manifest['skills']):
        errors.append('Skill folders differ from the selected manifest inventory')
    if len({f['path'] for f in manifest['files']}) != len(manifest['files']):
        errors.append('Duplicate original-file paths in manifest')
    for entry in manifest['files'] + manifest.get('maintainer_added_files', []):
        try:
            path = within(root, entry['path'])
            if not path.is_file(): errors.append(f"Missing original file: {entry['path']}"); continue
            if hashlib.sha256(path.read_bytes()).hexdigest() != entry['sha256']:
                errors.append(f"Changed original file: {entry['path']}")
        except ValueError as exc:
            errors.append(str(exc))
    for entry in manifest['skills']:
        path = within(root, entry['path'])
        if not path.is_file(): continue
        text = path.read_text(encoding='utf-8')
        parts = text.split('---', 2)
        if not text.startswith('---\n') or len(parts) < 3:
            errors.append(f"Missing frontmatter: {entry['path']}"); continue
        name = re.search(r'^name:\s*([\w-]+)\s*$', parts[1], re.M)
        if not name or name.group(1) != path.parent.name or not re.search(r'^description:', parts[1], re.M):
            errors.append(f"Invalid name or description: {entry['path']}")
        guide = root / 'docs' / 'skills' / f'{path.parent.name}.md'
        if not guide.is_file(): errors.append(f'Missing bilingual guide: {guide.name}')
        elif not {'arabic', 'english'}.issubset(anchors(guide.read_text(encoding='utf-8'))):
            errors.append(f'Missing language sections: {guide.name}')
    docs = [p for p in root.glob('*.md')] + list((root / 'docs').rglob('*.md'))
    for path in docs:
        errors.extend(link_errors(root, path.relative_to(root), path.read_text(encoding='utf-8')))
    for svg in (root / 'skills').rglob('*.svg'):
        try:
            tree = ET.parse(svg)
            for element in tree.iter():
                if element.tag.rsplit('}', 1)[-1] in ('script', 'foreignObject'):
                    errors.append(f'Active SVG content: {svg.relative_to(root)}')
                for key, value in element.attrib.items():
                    if key.lower().startswith('on') or key.rsplit('}', 1)[-1] in ('href', 'src') and re.match(r'(?i)(?:https?:|javascript:|data:)', value):
                        errors.append(f'Unsafe SVG attribute: {svg.relative_to(root)}')
        except ET.ParseError:
            errors.append(f'Invalid SVG: {svg.relative_to(root)}')
    for config in (root / 'skills').glob('*/agents/openai.yaml'):
        text = config.read_text(encoding='utf-8')
        for icon in re.findall(r'^\s*icon_(?:small|large):\s*["\']?([^\n"\']+)', text, re.M):
            try:
                if not within(root, str(config.parent.parent.relative_to(root) / icon.strip())).is_file():
                    errors.append(f'Missing interface icon: {config.relative_to(root)}')
            except ValueError as exc:
                errors.append(str(exc))
    # Tracked source only: exclude Git metadata, caches, and uploaded/local files.
    try:
        import subprocess
        tracked = subprocess.check_output(['git', '-C', str(root), 'ls-files', '-z']).decode().split('\0')
    except (OSError, subprocess.CalledProcessError):
        tracked = [str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts]
    for relative in filter(None, tracked):
        path = within(root, relative)
        if path.is_file():
            try: text = path.read_text(encoding='utf-8')
            except UnicodeDecodeError: continue
            for kind, line in sensitive_matches(text): errors.append(f'{relative}:{line}: possible {kind}; review without logging its value')
    return errors, {'skills': len(expected), 'original_files': len(manifest['files']), 'documentation_files': len(docs)}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        errors, summary = validate(args.root.resolve())
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(f'Validation failed: {exc}', file=sys.stderr); return 1
    if errors:
        print('\n'.join(errors), file=sys.stderr); return 1
    print('Repository validation passed: ' + json.dumps(summary))
    print('Archive integrity checks do not execute skill workflows or certify missing dependencies or licenses.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
