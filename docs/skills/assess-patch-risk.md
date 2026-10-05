# Assess patch risk

**تقييم مخاطر التغييرات** · `assess-patch-risk`

[العربية](#arabic) · [English](#english) · [الفهرس / Catalog](../../README.md#catalog) · [المصدر الأصلي / Original instructions](../../skills/assess-patch-risk/SKILL.md)

<a id="arabic"></a>

## العربية

### ما وظيفة المهارة؟

تقييم أثر تعديل ثابت على سلوك البرنامج ومخاطر الانحدار وإمكانية الدمج.

### متى تستخدمها؟

استخدمها عندما يكون هدفك: تقرير بالمخاطر والأدلة والاختبارات وإمكانية استعادة الحالة السابقة؛ لا يطبق التعديل. راجع حدود الاستخدام في الملف الأصلي قبل الاستدعاء، خصوصًا الفرق بين الفحص والإصلاح والتحقق.

### ماذا تجهّز؟

ملف patch أو نطاق commits ثابت مع سياق المشروع. حدّد النطاق والهدف بوضوح، وأرفق المصادر التي تملك صلاحية استخدامها. المعلومات الناقصة تحتاج إلى توضيح؛ لا يُفترض توفر أدوات التشغيل بمجرد نسخ الملفات.

### ما النتيجة المتوقعة؟

تقرير بالمخاطر والأدلة والاختبارات وإمكانية استعادة الحالة السابقة؛ لا يطبق التعديل.

### مثال استدعاء

```text
$assess-patch-risk قيّم مخاطر هذا التعديل قبل مراجعته للدمج.
```

المثال قالب طلب، وليس نتيجة تشغيل. استبدل الإشارة العامة بالملف أو النطاق أو البيانات المطلوبة.

<a id="english"></a>

## English

### What does it do?

Assess an immutable patch’s runtime impact, regression risk, and merge eligibility.

### When should you use it?

Use it when you need: An evidence-backed risk assessment with checks and recoverability; the patch is not applied. Read the original usage boundaries before invoking it, especially the distinction between scanning, fixing, and verification.

### What should you provide?

An immutable patch or commit range and repository context. Specify the scope and goal, and supply sources you are authorized to use. Missing inputs require clarification; copying files does not provide the runtime tools.

### What can you expect?

An evidence-backed risk assessment with checks and recoverability; the patch is not applied.

### Example invocation

```text
$assess-patch-risk Assess the risks of this patch before merge review.
```

This is a request template, not an execution result. Replace the generic reference with the relevant artifact, scope, or data.

## الملفات المساعدة / Supporting files

- [`references/risk-rubric.md`](../../skills/assess-patch-risk/references/risk-rubric.md)
- [`scripts/validate_patch_risk_assessment.py`](../../skills/assess-patch-risk/scripts/validate_patch_risk_assessment.py)

## المتطلبات وحدود النسخة / Requirements and archive limits

بعض المهارات تعتمد على مراجع مشتركة أو أدوات MCP أو موصلات غير مرفقة. الملفات المساعدة أعلاه هي الملفات المتاحة فقط، وليست إثباتًا لاكتمال الاعتماديات. راجع [تقرير الاستيراد](../../IMPORT-REPORT.md) و[سجل المصادر](../../IMPORT-MANIFEST.json) و[دليل الاستخدام](../USAGE.md). لم يُختبر تشغيل هذه المهارة ضمن إعداد هذه الوثائق.

Some skills depend on shared references, MCP tools, or connectors that are not bundled. The list above shows available files, not proof of complete dependencies. See the [import report](../../IMPORT-REPORT.md), [source manifest](../../IMPORT-MANIFEST.json), and [usage guide](../USAGE.md). This documentation work did not execute the skill workflow.

هذا شرح مستقل؛ محتوى `SKILL.md` الأصلي محفوظ دون تغيير. عند اختلاف الملخص عن التفاصيل، اقرأ التعليمات الأصلية.

This is a separate explanatory guide; the original `SKILL.md` is unchanged. Consult the original instructions for complete behavior and constraints.
