# Report KPIs

**إعداد ملخص مؤشرات الأداء** · `kpi-reporting`

[العربية](#arabic) · [English](#english) · [الفهرس / Catalog](../../README.md#catalog) · [المصدر الأصلي / Original instructions](../../skills/kpi-reporting/SKILL.md)

<a id="arabic"></a>

## العربية

### ما وظيفة المهارة؟

عرض حالة المؤشرات ومقارنتها بالأهداف مع تفسير الانحرافات المدعومة.

### متى تستخدمها؟

استخدمها عندما يكون هدفك: ملخص أداء أو scorecard يوضح النتائج وآثارها التشغيلية. راجع حدود الاستخدام في الملف الأصلي قبل الاستدعاء، خصوصًا الفرق بين الفحص والإصلاح والتحقق.

### ماذا تجهّز؟

المؤشرات وتعريفاتها والأهداف والفترة ومصادر الأرقام. حدّد النطاق والهدف بوضوح، وأرفق المصادر التي تملك صلاحية استخدامها. المعلومات الناقصة تحتاج إلى توضيح؛ لا يُفترض توفر أدوات التشغيل بمجرد نسخ الملفات.

### ما النتيجة المتوقعة؟

ملخص أداء أو scorecard يوضح النتائج وآثارها التشغيلية.

### مثال استدعاء

```text
$kpi-reporting جهّز تقرير أداء شهريًا لهذه المؤشرات والأهداف.
```

المثال قالب طلب، وليس نتيجة تشغيل. استبدل الإشارة العامة بالملف أو النطاق أو البيانات المطلوبة.

<a id="english"></a>

## English

### What does it do?

Report metric status against targets and explain validated drivers.

### When should you use it?

Use it when you need: A readout or scorecard explaining results and operating implications. Read the original usage boundaries before invoking it, especially the distinction between scanning, fixing, and verification.

### What should you provide?

Metrics, definitions, targets, period, and source data. Specify the scope and goal, and supply sources you are authorized to use. Missing inputs require clarification; copying files does not provide the runtime tools.

### What can you expect?

A readout or scorecard explaining results and operating implications.

### Example invocation

```text
$kpi-reporting Prepare a monthly KPI readout against these targets.
```

This is a request template, not an execution result. Replace the generic reference with the relevant artifact, scope, or data.

## الملفات المساعدة / Supporting files

- [`references/report-templates.md`](../../skills/kpi-reporting/references/report-templates.md)

## المتطلبات وحدود النسخة / Requirements and archive limits

بعض المهارات تعتمد على مراجع مشتركة أو أدوات MCP أو موصلات غير مرفقة. الملفات المساعدة أعلاه هي الملفات المتاحة فقط، وليست إثباتًا لاكتمال الاعتماديات. راجع [تقرير الاستيراد](../../IMPORT-REPORT.md) و[سجل المصادر](../../IMPORT-MANIFEST.json) و[دليل الاستخدام](../USAGE.md). لم يُختبر تشغيل هذه المهارة ضمن إعداد هذه الوثائق.

Some skills depend on shared references, MCP tools, or connectors that are not bundled. The list above shows available files, not proof of complete dependencies. See the [import report](../../IMPORT-REPORT.md), [source manifest](../../IMPORT-MANIFEST.json), and [usage guide](../USAGE.md). This documentation work did not execute the skill workflow.

هذا شرح مستقل؛ محتوى `SKILL.md` الأصلي محفوظ دون تغيير. عند اختلاف الملخص عن التفاصيل، اقرأ التعليمات الأصلية.

This is a separate explanatory guide; the original `SKILL.md` is unchanged. Consult the original instructions for complete behavior and constraints.
