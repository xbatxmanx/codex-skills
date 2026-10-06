# Diagnose metric changes

**تشخيص تغير المؤشرات** · `metric-diagnostics`

[العربية](#arabic) · [English](#english) · [الفهرس / Catalog](../../README.md#catalog) · [المصدر الأصلي / Original instructions](../../skills/metric-diagnostics/SKILL.md)

<a id="arabic"></a>

## العربية

### ما وظيفة المهارة؟

التحقق من أسباب تغير مؤشر أو اختلافه عن المتوقع.

### متى تستخدمها؟

استخدمها عندما يكون هدفك: تفسير مدعوم للمحركات مع فصل الأدلة عن الفرضيات. راجع حدود الاستخدام في الملف الأصلي قبل الاستدعاء، خصوصًا الفرق بين الفحص والإصلاح والتحقق.

### ماذا تجهّز؟

تعريف المؤشر والفترة والبيانات والمقارنة المطلوبة. حدّد النطاق والهدف بوضوح، وأرفق المصادر التي تملك صلاحية استخدامها. المعلومات الناقصة تحتاج إلى توضيح؛ لا يُفترض توفر أدوات التشغيل بمجرد نسخ الملفات.

### ما النتيجة المتوقعة؟

تفسير مدعوم للمحركات مع فصل الأدلة عن الفرضيات.

### مثال استدعاء

```text
$metric-diagnostics شخّص أسباب انخفاض هذا المؤشر خلال الفترة المحددة.
```

المثال قالب طلب، وليس نتيجة تشغيل. استبدل الإشارة العامة بالملف أو النطاق أو البيانات المطلوبة.

<a id="english"></a>

## English

### What does it do?

Investigate why a metric changed or differs from expectation.

### When should you use it?

Use it when you need: An evidence-backed driver analysis distinguishing facts from hypotheses. Read the original usage boundaries before invoking it, especially the distinction between scanning, fixing, and verification.

### What should you provide?

Metric definition, period, data, and comparison. Specify the scope and goal, and supply sources you are authorized to use. Missing inputs require clarification; copying files does not provide the runtime tools.

### What can you expect?

An evidence-backed driver analysis distinguishing facts from hypotheses.

### Example invocation

```text
$metric-diagnostics Diagnose why this metric declined during the specified period.
```

This is a request template, not an execution result. Replace the generic reference with the relevant artifact, scope, or data.

## الملفات المساعدة / Supporting files

لا توجد ملفات مساعدة مرفقة لهذه المهارة. / No supporting files are bundled for this skill.

## المتطلبات وحدود النسخة / Requirements and archive limits

بعض المهارات تعتمد على مراجع مشتركة أو أدوات MCP أو موصلات غير مرفقة. الملفات المساعدة أعلاه هي الملفات المتاحة فقط، وليست إثباتًا لاكتمال الاعتماديات. راجع [تقرير الاستيراد](../../IMPORT-REPORT.md) و[سجل المصادر](../../IMPORT-MANIFEST.json) و[دليل الاستخدام](../USAGE.md). لم يُختبر تشغيل هذه المهارة ضمن إعداد هذه الوثائق.

Some skills depend on shared references, MCP tools, or connectors that are not bundled. The list above shows available files, not proof of complete dependencies. See the [import report](../../IMPORT-REPORT.md), [source manifest](../../IMPORT-MANIFEST.json), and [usage guide](../USAGE.md). This documentation work did not execute the skill workflow.

هذا شرح مستقل؛ محتوى `SKILL.md` الأصلي محفوظ دون تغيير. عند اختلاف الملخص عن التفاصيل، اقرأ التعليمات الأصلية.

This is a separate explanatory guide; the original `SKILL.md` is unchanged. Consult the original instructions for complete behavior and constraints.
