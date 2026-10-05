# Build a dashboard

**إنشاء لوحة بيانات** · `build-dashboard`

[العربية](#arabic) · [English](#english) · [الفهرس / Catalog](../../README.md#catalog) · [المصدر الأصلي / Original instructions](../../skills/build-dashboard/SKILL.md)

<a id="arabic"></a>

## العربية

### ما وظيفة المهارة؟

بناء لوحة تفاعلية تربط المؤشرات والمرئيات بمصادر قابلة للفحص.

### متى تستخدمها؟

استخدمها عندما يكون هدفك: لوحة تفاعلية مع تحقق من البيانات والعرض وفق أدوات التشغيل المتاحة. راجع حدود الاستخدام في الملف الأصلي قبل الاستدعاء، خصوصًا الفرق بين الفحص والإصلاح والتحقق.

### ماذا تجهّز؟

مصادر البيانات والجمهور والقرار والمؤشرات المطلوبة. حدّد النطاق والهدف بوضوح، وأرفق المصادر التي تملك صلاحية استخدامها. المعلومات الناقصة تحتاج إلى توضيح؛ لا يُفترض توفر أدوات التشغيل بمجرد نسخ الملفات.

### ما النتيجة المتوقعة؟

لوحة تفاعلية مع تحقق من البيانات والعرض وفق أدوات التشغيل المتاحة.

### مثال استدعاء

```text
$build-dashboard ابنِ لوحة لمتابعة هذه المؤشرات من البيانات المرفقة.
```

المثال قالب طلب، وليس نتيجة تشغيل. استبدل الإشارة العامة بالملف أو النطاق أو البيانات المطلوبة.

<a id="english"></a>

## English

### What does it do?

Build an interactive dashboard with inspectable source-backed metrics.

### When should you use it?

Use it when you need: An interactive dashboard with data and presentation checks using available tools. Read the original usage boundaries before invoking it, especially the distinction between scanning, fixing, and verification.

### What should you provide?

Data sources, audience, decision, and required metrics. Specify the scope and goal, and supply sources you are authorized to use. Missing inputs require clarification; copying files does not provide the runtime tools.

### What can you expect?

An interactive dashboard with data and presentation checks using available tools.

### Example invocation

```text
$build-dashboard Build a dashboard tracking these metrics from the supplied data.
```

This is a request template, not an execution result. Replace the generic reference with the relevant artifact, scope, or data.

## الملفات المساعدة / Supporting files

لا توجد ملفات مساعدة مرفقة لهذه المهارة. / No supporting files are bundled for this skill.

## المتطلبات وحدود النسخة / Requirements and archive limits

بعض المهارات تعتمد على مراجع مشتركة أو أدوات MCP أو موصلات غير مرفقة. الملفات المساعدة أعلاه هي الملفات المتاحة فقط، وليست إثباتًا لاكتمال الاعتماديات. راجع [تقرير الاستيراد](../../IMPORT-REPORT.md) و[سجل المصادر](../../IMPORT-MANIFEST.json) و[دليل الاستخدام](../USAGE.md). لم يُختبر تشغيل هذه المهارة ضمن إعداد هذه الوثائق.

Some skills depend on shared references, MCP tools, or connectors that are not bundled. The list above shows available files, not proof of complete dependencies. See the [import report](../../IMPORT-REPORT.md), [source manifest](../../IMPORT-MANIFEST.json), and [usage guide](../USAGE.md). This documentation work did not execute the skill workflow.

هذا شرح مستقل؛ محتوى `SKILL.md` الأصلي محفوظ دون تغيير. عند اختلاف الملخص عن التفاصيل، اقرأ التعليمات الأصلية.

This is a separate explanatory guide; the original `SKILL.md` is unchanged. Consult the original instructions for complete behavior and constraints.
