# دليل الاستخدام / Usage guide

[العربية](#arabic) · [English](#english)

<a id="arabic"></a>

[العودة إلى الفهرس](../README.md)

## اختيار مهارة

ابدأ من [فهرس المهارات](../README.md#catalog)، ثم اقرأ ملف `SKILL.md` كاملًا. تحقّق من الأدوات المطلوبة والملفات المرجعية قبل تنفيذ سير العمل.

أسماء المجموعات في الفهرس توضّح مصدر المهارة. للاستدعاء استخدم حقل `name` الموجود في ملف `SKILL.md`، فقد يختلف عن الاسم المؤهّل بالمجموعة في سجل المصادر.

## مواقع التثبيت

استخدم الموقع الذي يدعمه إصدار Codex لديك:

| النطاق | الموقع المعتاد |
| :--- | :--- |
| مشروع واحد | `.agents/skills/<skill-name>/` داخل مشروعك |
| المستخدم | `~/.agents/skills/<skill-name>/` |

انسخ مجلد المهارة كاملًا، مع المراجع والسكربتات والمواصفات التابعة له. لا تنسخ `SKILL.md` وحده. افحص الوجهة أولًا إذا كانت المهارة مثبتة بالفعل؛ لا تستبدل ملفاتك المحلية دون مراجعة.

```bash
# من جذر مشروعك، مع تعديل مسار المكتبة.
mkdir -p .agents/skills
cp -Rn /path/to/codex-skills/skills/assess-patch-risk .agents/skills/
```

قد يحتاج Codex إلى جلسة جديدة لاكتشاف المهارة. بعد اكتشافها استخدم `$` مع اسمها، وأرفق هدفًا محددًا أو مدخلات مناسبة.

## الاعتماديات والموارد غير المتاحة

نسخ المهارة لا يثبّت إضافة المصدر أو أدوات MCP أو الموصلات أو صلاحيات الخدمات الخارجية.

تحتوي التعليمات الأصلية على روابط إلى موارد مشتركة خارج مجلد المهارة، وأحيانًا مهارات مصاحبة غير مرفقة. حُفظت هذه المسارات كما هي. نقل مجلد المهارة وحده لا يحل تلك الاعتماديات.

راجع [تقرير الاستيراد](../IMPORT-REPORT.md) و[سجل المصادر](../IMPORT-MANIFEST.json). إذا كان مورد مطلوب غير متاح، وفّره من مصدره المعتمد قبل تشغيل الخطوة التي تعتمد عليه. السكربتات المرفقة تُقرأ وتُراجع قبل تشغيلها؛ لم يُتحقق من تشغيل جميع مساراتها في هذه النسخة.

## التحقق من مطابقة الملفات المستوردة

نفّذ الأمر التالي من جذر هذه المكتبة. يتحقق من بصمات الملفات الـ74 الواردة في سجل المصادر؛ ملفات التوثيق الجديدة ليست ضمن هذه البصمات.

```bash
python3 - <<'PYTHON'
from pathlib import Path
import hashlib
import json

manifest = json.loads(Path("IMPORT-MANIFEST.json").read_text())
failures = []
for item in manifest["files"]:
    path = Path(item["path"])
    if not path.is_file():
        failures.append(f"Missing: {path}")
        continue
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != item["sha256"]:
        failures.append(f"Changed: {path}")
if failures:
    raise SystemExit("\n".join(failures))
print(f"Verified {len(manifest['files'])} imported files")
PYTHON
```

نجاح المطابقة يؤكد ثبات الملفات مقارنة بنسخة الاستيراد. لا يثبت توفر أدوات التشغيل أو صحة عمل كل مهارة.


---

<a id="english"></a>

## English — Usage guide

[Back to the catalog](../README.md#catalog)

### Choose a skill

Start with the [skill catalog](../README.md#catalog). Each skill has its own Arabic and English explanation with inputs, expected output, examples, and supporting-file links. Read the original `SKILL.md` for complete behavior and requirements.

The category prefix in the manifest identifies provenance. Invoke the `name` in the skill’s frontmatter, which may differ from the category-qualified manifest name.

### Install the entire folder

Use a location supported by your Codex version:

| Scope | Typical path |
| :--- | :--- |
| A single project | `.agents/skills/<skill-name>/` in the project |
| Your user account | `~/.agents/skills/<skill-name>/` |

Copy the complete folder, including references, scripts, specifications, agents, and assets where present. Inspect an existing destination before updating it; preserve local customizations.

```bash
# From your project root; replace the library path.
mkdir -p .agents/skills
cp -Rn /path/to/codex-skills/skills/ai-shark-tank-council .agents/skills/
```

Start a new Codex session if needed for discovery. Invoke the skill with `$` and a concrete task:

```text
$ai-shark-tank-council Evaluate this idea in economic mode. Respond in English.
```

Some original skills default to a particular response language. Request the desired language explicitly. Bilingual documentation does not change the original skill’s rules.

### Dependencies and unavailable resources

Copying a skill does not install its source plugin, MCP tools, connectors, or external-service permissions. Original links may reference shared resources outside the folder or companion skills that are not included. Review the [import report](../IMPORT-REPORT.md) and [manifest](../IMPORT-MANIFEST.json) before use.

Obtain required missing resources from their authoritative source before using the step that depends on them. Read bundled scripts before running them; their presence does not imply every execution path has been tested.

### Verify imported files

Run this from the library root. It checks all 74 original-file hashes in the manifest; newly written explanatory documentation is outside this set.

```bash
python3 - <<'PYTHON'
from pathlib import Path
import hashlib
import json

manifest = json.loads(Path("IMPORT-MANIFEST.json").read_text())
failures = []
for item in manifest["files"]:
    path = Path(item["path"])
    if not path.is_file():
        failures.append(f"Missing: {path}")
        continue
    if hashlib.sha256(path.read_bytes()).hexdigest() != item["sha256"]:
        failures.append(f"Changed: {path}")
if failures:
    raise SystemExit("\n".join(failures))
print(f"Verified {len(manifest['files'])} imported files")
PYTHON
```

A successful check confirms that files still match the recorded import, not that runtime dependencies are present or that all skills execute successfully.
