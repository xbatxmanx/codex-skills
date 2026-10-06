# Discover candidate findings

**اكتشاف نتائج أمنية محتملة** · `finding-discovery`

[العربية](#arabic) · [English](#english) · [الفهرس / Catalog](../../README.md#catalog) · [المصدر الأصلي / Original instructions](../../skills/finding-discovery/SKILL.md)

<a id="arabic"></a>

## العربية

### ما وظيفة المهارة؟

اكتشاف مشكلات أمنية محتملة كمرحلة متخصصة أو عند طلبها صراحة.

### متى تستخدمها؟

استخدمها عندما يكون هدفك: نتائج محتملة مدعومة بمواقع المصدر، تحتاج إلى التحقق والمعايرة. راجع حدود الاستخدام في الملف الأصلي قبل الاستدعاء، خصوصًا الفرق بين الفحص والإصلاح والتحقق.

### ماذا تجهّز؟

المصدر أو التغييرات المصرح بمراجعتها والسياسة المعتمدة. حدّد النطاق والهدف بوضوح، وأرفق المصادر التي تملك صلاحية استخدامها. المعلومات الناقصة تحتاج إلى توضيح؛ لا يُفترض توفر أدوات التشغيل بمجرد نسخ الملفات.

### ما النتيجة المتوقعة؟

نتائج محتملة مدعومة بمواقع المصدر، تحتاج إلى التحقق والمعايرة.

### مثال استدعاء

```text
$finding-discovery اكتشف النتائج الأمنية المحتملة في هذا النطاق.
```

المثال قالب طلب، وليس نتيجة تشغيل. استبدل الإشارة العامة بالملف أو النطاق أو البيانات المطلوبة.

<a id="english"></a>

## English

### What does it do?

Discover candidate security issues as a dedicated phase or explicit task.

### When should you use it?

Use it when you need: Source-backed candidates requiring validation and calibration. Read the original usage boundaries before invoking it, especially the distinction between scanning, fixing, and verification.

### What should you provide?

Authorized source or changes and the applicable policy. Specify the scope and goal, and supply sources you are authorized to use. Missing inputs require clarification; copying files does not provide the runtime tools.

### What can you expect?

Source-backed candidates requiring validation and calibration.

### Example invocation

```text
$finding-discovery Discover candidate security findings in this scope.
```

This is a request template, not an execution result. Replace the generic reference with the relevant artifact, scope, or data.

## الملفات المساعدة / Supporting files

لا توجد ملفات مساعدة مرفقة لهذه المهارة. / No supporting files are bundled for this skill.

## المتطلبات وحدود النسخة / Requirements and archive limits

بعض المهارات تعتمد على مراجع مشتركة أو أدوات MCP أو موصلات غير مرفقة. الملفات المساعدة أعلاه هي الملفات المتاحة فقط، وليست إثباتًا لاكتمال الاعتماديات. راجع [تقرير الاستيراد](../../IMPORT-REPORT.md) و[سجل المصادر](../../IMPORT-MANIFEST.json) و[دليل الاستخدام](../USAGE.md). لم يُختبر تشغيل هذه المهارة ضمن إعداد هذه الوثائق.

Some skills depend on shared references, MCP tools, or connectors that are not bundled. The list above shows available files, not proof of complete dependencies. See the [import report](../../IMPORT-REPORT.md), [source manifest](../../IMPORT-MANIFEST.json), and [usage guide](../USAGE.md). This documentation work did not execute the skill workflow.

هذا شرح مستقل؛ محتوى `SKILL.md` الأصلي محفوظ دون تغيير. عند اختلاف الملخص عن التفاصيل، اقرأ التعليمات الأصلية.

This is a separate explanatory guide; the original `SKILL.md` is unchanged. Consult the original instructions for complete behavior and constraints.
