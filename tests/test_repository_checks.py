import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('checker', Path(__file__).resolve().parents[1] / 'scripts/check_repository.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)

class CheckerTests(unittest.TestCase):
    def test_sensitive_tokens_are_detected_without_echoing_values(self):
        token = 'ghp_' + 'a' * 36
        matches = checker.sensitive_matches('access token: ' + token)
        self.assertEqual(matches, [('API credential', 1)])
        self.assertNotIn(token, repr(matches))

    def test_literal_credentials_are_detected(self):
        secret = 'demo-' + 'secret-value'
        self.assertEqual(checker.sensitive_matches('password = "' + secret + '"'), [('literal credential', 1)])

    def test_ssh_example_is_not_personal_email(self):
        self.assertEqual(checker.sensitive_matches('git@github.com:owner/repo.git'), [])

    def test_path_escape_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError): checker.within(Path(directory), '../outside.md')

    def test_missing_link_and_anchor_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'target.md').write_text('<a id="good"></a>\n')
            errors = checker.link_errors(root, Path('README.md'), '[x](absent.md) [y](target.md#bad)')
            self.assertEqual(len(errors), 2)
            self.assertEqual(checker.link_errors(root, Path('README.md'), '[x](target.md#good)'), [])

    def test_symlink_escape_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory, tempfile.TemporaryDirectory() as outside:
            root = Path(directory)
            (root / 'link').symlink_to(outside, target_is_directory=True)
            with self.assertRaises(ValueError): checker.within(root, 'link/file.md')

if __name__ == '__main__': unittest.main()
