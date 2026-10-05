# Validate analysis

**مراجعة التحليل والنتائج** · `validate-data`

[العربية](#arabic) · [English](#english) · [الفهرس / Catalog](../../README.md#catalog) · [المصدر الأصلي / Original instructions](../../skills/validate-data/SKILL.md)

<a id="arabic"></a>

## العربية

### ما وظيفة المهارة؟

مراجعة المنهجية والمصادر والحسابات والمرئيات والاستنتاجات.

### متى تستخدمها؟

استخدمها عندما يكون هدفك: حكم على الجاهزية ومشكلات محددة وحدود نطاق المراجعة. راجع حدود الاستخدام في الملف الأصلي قبل الاستدعاء، خصوصًا الفرق بين الفحص والإصلاح والتحقق.

### ماذا تجهّز؟

التحليل أو التقرير ومصادره وسؤال المراجعة. حدّد النطاق والهدف بوضوح، وأرفق المصادر التي تملك صلاحية استخدامها. المعلومات الناقصة تحتاج إلى توضيح؛ لا يُفترض توفر أدوات التشغيل بمجرد نسخ الملفات.

### ما النتيجة المتوقعة؟

حكم على الجاهزية ومشكلات محددة وحدود نطاق المراجعة.

### مثال استدعاء

```text
$validate-data راجع صحة هذا التحليل واستنتاجاته.
```

المثال قالب طلب، وليس نتيجة تشغيل. استبدل الإشارة العامة بالملف أو النطاق أو البيانات المطلوبة.

<a id="english"></a>

## English

### What does it do?

Review methodology, sources, calculations, visuals, and conclusions.

### When should you use it?

Use it when you need: A readiness assessment with specific issues and review scope limits. Read the original usage boundaries before invoking it, especially the distinction between scanning, fixing, and verification.

### What should you provide?

The analysis or report, its sources, and review question. Specify the scope and goal, and supply sources you are authorized to use. Missing inputs require clarification; copying files does not provide the runtime tools.

### What can you expect?

A readiness assessment with specific issues and review scope limits.

### Example invocation

```text
$validate-data Validate this analysis and its conclusions.
```

This is a request template, not an execution result. Replace the generic reference with the relevant artifact, scope, or data.

## الملفات المساعدة / Supporting files

- [`references/deep-review.md`](../../skills/validate-data/references/deep-review.md)
- [`references/component-verification.md`](../../skills/validate-data/references/component-verification.md)
- [`references/coverage-record.md`](../../skills/validate-data/references/coverage-record.md)

## المتطلبات وحدود النسخة / Requirements and archive limits

بعض المهارات تعتمد على مراجع مشتركة أو أدوات MCP أو موصلات غير مرفقة. الملفات المساعدة أعلاه هي الملفات المتاحة فقط، وليست إثباتًا لاكتمال الاعتماديات. راجع [تقرير الاستيراد](../../IMPORT-REPORT.md) و[سجل المصادر](../../IMPORT-MANIFEST.json) و[دليل الاستخدام](../USAGE.md). لم يُختبر تشغيل هذه المهارة ضمن إعداد هذه الوثائق.

Some skills depend on shared references, MCP tools, or connectors that are not bundled. The list above shows available files, not proof of complete dependencies. See the [import report](../../IMPORT-REPORT.md), [source manifest](../../IMPORT-MANIFEST.json), and [usage guide](../USAGE.md). This documentation work did not execute the skill workflow.

هذا شرح مستقل؛ محتوى `SKILL.md` الأصلي محفوظ دون تغيير. عند اختلاف الملخص عن التفاصيل، اقرأ التعليمات الأصلية.

This is a separate explanatory guide; the original `SKILL.md` is unchanged. Consult the original instructions for complete behavior and constraints.
