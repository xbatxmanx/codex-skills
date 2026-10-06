# Gather business context

**جمع سياق الأعمال** · `gather-business-context`

[العربية](#arabic) · [English](#english) · [الفهرس / Catalog](../../README.md#catalog) · [المصدر الأصلي / Original instructions](../../skills/gather-business-context/SKILL.md)

<a id="arabic"></a>

## العربية

### ما وظيفة المهارة؟

جمع المعلومات التي تؤثر في تفسير السؤال قبل التحليل.

### متى تستخدمها؟

استخدمها عندما يكون هدفك: موجز سياق منسوب إلى مصادره يوضح التعريفات والتعارضات. راجع حدود الاستخدام في الملف الأصلي قبل الاستدعاء، خصوصًا الفرق بين الفحص والإصلاح والتحقق.

### ماذا تجهّز؟

السؤال ومصادر الأعمال أو الروابط المتاحة. حدّد النطاق والهدف بوضوح، وأرفق المصادر التي تملك صلاحية استخدامها. المعلومات الناقصة تحتاج إلى توضيح؛ لا يُفترض توفر أدوات التشغيل بمجرد نسخ الملفات.

### ما النتيجة المتوقعة؟

موجز سياق منسوب إلى مصادره يوضح التعريفات والتعارضات.

### مثال استدعاء

```text
$gather-business-context اجمع سياق هذا المؤشر قبل تحليل تغيره.
```

المثال قالب طلب، وليس نتيجة تشغيل. استبدل الإشارة العامة بالملف أو النطاق أو البيانات المطلوبة.

<a id="english"></a>

## English

### What does it do?

Gather decision-shaping context before analysis.

### When should you use it?

Use it when you need: An attributed context brief clarifying definitions and conflicts. Read the original usage boundaries before invoking it, especially the distinction between scanning, fixing, and verification.

### What should you provide?

The question and available business sources or links. Specify the scope and goal, and supply sources you are authorized to use. Missing inputs require clarification; copying files does not provide the runtime tools.

### What can you expect?

An attributed context brief clarifying definitions and conflicts.

### Example invocation

```text
$gather-business-context Gather context for this metric before diagnosing its change.
```

This is a request template, not an execution result. Replace the generic reference with the relevant artifact, scope, or data.

## الملفات المساعدة / Supporting files

لا توجد ملفات مساعدة مرفقة لهذه المهارة. / No supporting files are bundled for this skill.

## المتطلبات وحدود النسخة / Requirements and archive limits

بعض المهارات تعتمد على مراجع مشتركة أو أدوات MCP أو موصلات غير مرفقة. الملفات المساعدة أعلاه هي الملفات المتاحة فقط، وليست إثباتًا لاكتمال الاعتماديات. راجع [تقرير الاستيراد](../../IMPORT-REPORT.md) و[سجل المصادر](../../IMPORT-MANIFEST.json) و[دليل الاستخدام](../USAGE.md). لم يُختبر تشغيل هذه المهارة ضمن إعداد هذه الوثائق.

Some skills depend on shared references, MCP tools, or connectors that are not bundled. The list above shows available files, not proof of complete dependencies. See the [import report](../../IMPORT-REPORT.md), [source manifest](../../IMPORT-MANIFEST.json), and [usage guide](../USAGE.md). This documentation work did not execute the skill workflow.

هذا شرح مستقل؛ محتوى `SKILL.md` الأصلي محفوظ دون تغيير. عند اختلاف الملخص عن التفاصيل، اقرأ التعليمات الأصلية.

This is a separate explanatory guide; the original `SKILL.md` is unchanged. Consult the original instructions for complete behavior and constraints.
