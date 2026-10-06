# Track security findings

**تتبّع النتائج الأمنية** · `track-findings`

[العربية](#arabic) · [English](#english) · [الفهرس / Catalog](../../README.md#catalog) · [المصدر الأصلي / Original instructions](../../skills/track-findings/SKILL.md)

<a id="arabic"></a>

## العربية

### ما وظيفة المهارة؟

تحويل نتائج أمنية مختارة إلى سجلات في أدوات التتبع مع منع التكرار.

### متى تستخدمها؟

استخدمها عندما يكون هدفك: سجلات متحقق منها في الوجهة بعد معاينة واتباع الموافقات المطلوبة. راجع حدود الاستخدام في الملف الأصلي قبل الاستدعاء، خصوصًا الفرق بين الفحص والإصلاح والتحقق.

### ماذا تجهّز؟

نتائج محددة ووجهة صريحة وصلاحيات الموصل المناسب. حدّد النطاق والهدف بوضوح، وأرفق المصادر التي تملك صلاحية استخدامها. المعلومات الناقصة تحتاج إلى توضيح؛ لا يُفترض توفر أدوات التشغيل بمجرد نسخ الملفات.

### ما النتيجة المتوقعة؟

سجلات متحقق منها في الوجهة بعد معاينة واتباع الموافقات المطلوبة.

### مثال استدعاء

```text
$track-findings جهّز هذه النتائج للتتبع واعرض النص قبل أي كتابة خارجية.
```

المثال قالب طلب، وليس نتيجة تشغيل. استبدل الإشارة العامة بالملف أو النطاق أو البيانات المطلوبة.

<a id="english"></a>

## English

### What does it do?

Track selected security findings with duplicate checks and reviewed writes.

### When should you use it?

Use it when you need: Verified destination records after previews and required approvals. Read the original usage boundaries before invoking it, especially the distinction between scanning, fixing, and verification.

### What should you provide?

Selected findings, an explicit destination, and connector access. Specify the scope and goal, and supply sources you are authorized to use. Missing inputs require clarification; copying files does not provide the runtime tools.

### What can you expect?

Verified destination records after previews and required approvals.

### Example invocation

```text
$track-findings Prepare these findings for tracking and preview external writes.
```

This is a request template, not an execution result. Replace the generic reference with the relevant artifact, scope, or data.

## الملفات المساعدة / Supporting files

- [`references/github-security-advisories.md`](../../skills/track-findings/references/github-security-advisories.md)
- [`references/jira.md`](../../skills/track-findings/references/jira.md)

## المتطلبات وحدود النسخة / Requirements and archive limits

بعض المهارات تعتمد على مراجع مشتركة أو أدوات MCP أو موصلات غير مرفقة. الملفات المساعدة أعلاه هي الملفات المتاحة فقط، وليست إثباتًا لاكتمال الاعتماديات. راجع [تقرير الاستيراد](../../IMPORT-REPORT.md) و[سجل المصادر](../../IMPORT-MANIFEST.json) و[دليل الاستخدام](../USAGE.md). لم يُختبر تشغيل هذه المهارة ضمن إعداد هذه الوثائق.

Some skills depend on shared references, MCP tools, or connectors that are not bundled. The list above shows available files, not proof of complete dependencies. See the [import report](../../IMPORT-REPORT.md), [source manifest](../../IMPORT-MANIFEST.json), and [usage guide](../USAGE.md). This documentation work did not execute the skill workflow.

هذا شرح مستقل؛ محتوى `SKILL.md` الأصلي محفوظ دون تغيير. عند اختلاف الملخص عن التفاصيل، اقرأ التعليمات الأصلية.

This is a separate explanatory guide; the original `SKILL.md` is unchanged. Consult the original instructions for complete behavior and constraints.
