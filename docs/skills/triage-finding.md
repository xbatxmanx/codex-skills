# Triage a supplied finding

**فرز تقرير ثغرة وارد** · `triage-finding`

[العربية](#arabic) · [English](#english) · [الفهرس / Catalog](../../README.md#catalog) · [المصدر الأصلي / Original instructions](../../skills/triage-finding/SKILL.md)

<a id="arabic"></a>

## العربية

### ما وظيفة المهارة؟

تقييم أثر تقرير أمني وارد على المستودع بتحليل ثابت.

### متى تستخدمها؟

استخدمها عندما يكون هدفك: تقييم للأثر والانطباق وحدود الأدلة، دون إصلاح تلقائي. راجع حدود الاستخدام في الملف الأصلي قبل الاستدعاء، خصوصًا الفرق بين الفحص والإصلاح والتحقق.

### ماذا تجهّز؟

تقرير موجود أو تذكرة أو نتائج مستوردة مع المصدر المتأثر. حدّد النطاق والهدف بوضوح، وأرفق المصادر التي تملك صلاحية استخدامها. المعلومات الناقصة تحتاج إلى توضيح؛ لا يُفترض توفر أدوات التشغيل بمجرد نسخ الملفات.

### ما النتيجة المتوقعة؟

تقييم للأثر والانطباق وحدود الأدلة، دون إصلاح تلقائي.

### مثال استدعاء

```text
$triage-finding قيّم انطباق هذا التقرير الأمني على المستودع.
```

المثال قالب طلب، وليس نتيجة تشغيل. استبدل الإشارة العامة بالملف أو النطاق أو البيانات المطلوبة.

<a id="english"></a>

## English

### What does it do?

Assess a supplied security report’s repository impact through static analysis.

### When should you use it?

Use it when you need: An impact and applicability assessment with evidence limits, without automatic remediation. Read the original usage boundaries before invoking it, especially the distinction between scanning, fixing, and verification.

### What should you provide?

An existing report, ticket, or imported findings and affected source. Specify the scope and goal, and supply sources you are authorized to use. Missing inputs require clarification; copying files does not provide the runtime tools.

### What can you expect?

An impact and applicability assessment with evidence limits, without automatic remediation.

### Example invocation

```text
$triage-finding Assess whether this supplied security report affects the repository.
```

This is a request template, not an execution result. Replace the generic reference with the relevant artifact, scope, or data.

## الملفات المساعدة / Supporting files

- [`references/triage-result-contract.md`](../../skills/triage-finding/references/triage-result-contract.md)
- [`references/ticket-intake.md`](../../skills/triage-finding/references/ticket-intake.md)
- [`references/github-rest-intake.md`](../../skills/triage-finding/references/github-rest-intake.md)

## المتطلبات وحدود النسخة / Requirements and archive limits

بعض المهارات تعتمد على مراجع مشتركة أو أدوات MCP أو موصلات غير مرفقة. الملفات المساعدة أعلاه هي الملفات المتاحة فقط، وليست إثباتًا لاكتمال الاعتماديات. راجع [تقرير الاستيراد](../../IMPORT-REPORT.md) و[سجل المصادر](../../IMPORT-MANIFEST.json) و[دليل الاستخدام](../USAGE.md). لم يُختبر تشغيل هذه المهارة ضمن إعداد هذه الوثائق.

Some skills depend on shared references, MCP tools, or connectors that are not bundled. The list above shows available files, not proof of complete dependencies. See the [import report](../../IMPORT-REPORT.md), [source manifest](../../IMPORT-MANIFEST.json), and [usage guide](../USAGE.md). This documentation work did not execute the skill workflow.

هذا شرح مستقل؛ محتوى `SKILL.md` الأصلي محفوظ دون تغيير. عند اختلاف الملخص عن التفاصيل، اقرأ التعليمات الأصلية.

This is a separate explanatory guide; the original `SKILL.md` is unchanged. Consult the original instructions for complete behavior and constraints.
