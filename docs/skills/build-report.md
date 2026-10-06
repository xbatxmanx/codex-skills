# Build an analytical report

**إعداد تقرير تحليلي** · `build-report`

[العربية](#arabic) · [English](#english) · [الفهرس / Catalog](../../README.md#catalog) · [المصدر الأصلي / Original instructions](../../skills/build-report/SKILL.md)

<a id="arabic"></a>

## العربية

### ما وظيفة المهارة؟

تقديم إجابة تحليلية منظمة ومدعومة بالأدلة لجمهور محدد.

### متى تستخدمها؟

استخدمها عندما يكون هدفك: تقرير يجمع الاستنتاج والأدلة والتفسير والقيود. راجع حدود الاستخدام في الملف الأصلي قبل الاستدعاء، خصوصًا الفرق بين الفحص والإصلاح والتحقق.

### ماذا تجهّز؟

السؤال والبيانات والجمهور وشكل التقرير المطلوب. حدّد النطاق والهدف بوضوح، وأرفق المصادر التي تملك صلاحية استخدامها. المعلومات الناقصة تحتاج إلى توضيح؛ لا يُفترض توفر أدوات التشغيل بمجرد نسخ الملفات.

### ما النتيجة المتوقعة؟

تقرير يجمع الاستنتاج والأدلة والتفسير والقيود.

### مثال استدعاء

```text
$build-report اكتب تقريرًا تنفيذيًا يشرح النتائج من هذه البيانات.
```

المثال قالب طلب، وليس نتيجة تشغيل. استبدل الإشارة العامة بالملف أو النطاق أو البيانات المطلوبة.

<a id="english"></a>

## English

### What does it do?

Produce a structured, evidence-backed analytical answer for a defined audience.

### When should you use it?

Use it when you need: A report connecting conclusions, evidence, interpretation, and limitations. Read the original usage boundaries before invoking it, especially the distinction between scanning, fixing, and verification.

### What should you provide?

The question, data, audience, and requested report format. Specify the scope and goal, and supply sources you are authorized to use. Missing inputs require clarification; copying files does not provide the runtime tools.

### What can you expect?

A report connecting conclusions, evidence, interpretation, and limitations.

### Example invocation

```text
$build-report Create an executive report explaining these data findings.
```

This is a request template, not an execution result. Replace the generic reference with the relevant artifact, scope, or data.

## الملفات المساعدة / Supporting files

- [`references/narrative-style.md`](../../skills/build-report/references/narrative-style.md)
- [`references/report-archetypes.md`](../../skills/build-report/references/report-archetypes.md)
- [`specifications/executive-report.md`](../../skills/build-report/specifications/executive-report.md)
- [`specifications/technical-report.md`](../../skills/build-report/specifications/technical-report.md)

## المتطلبات وحدود النسخة / Requirements and archive limits

بعض المهارات تعتمد على مراجع مشتركة أو أدوات MCP أو موصلات غير مرفقة. الملفات المساعدة أعلاه هي الملفات المتاحة فقط، وليست إثباتًا لاكتمال الاعتماديات. راجع [تقرير الاستيراد](../../IMPORT-REPORT.md) و[سجل المصادر](../../IMPORT-MANIFEST.json) و[دليل الاستخدام](../USAGE.md). لم يُختبر تشغيل هذه المهارة ضمن إعداد هذه الوثائق.

Some skills depend on shared references, MCP tools, or connectors that are not bundled. The list above shows available files, not proof of complete dependencies. See the [import report](../../IMPORT-REPORT.md), [source manifest](../../IMPORT-MANIFEST.json), and [usage guide](../USAGE.md). This documentation work did not execute the skill workflow.

هذا شرح مستقل؛ محتوى `SKILL.md` الأصلي محفوظ دون تغيير. عند اختلاف الملخص عن التفاصيل، اقرأ التعليمات الأصلية.

This is a separate explanatory guide; the original `SKILL.md` is unchanged. Consult the original instructions for complete behavior and constraints.
