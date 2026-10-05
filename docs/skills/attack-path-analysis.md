# Analyze attack paths

**تحليل مسار الهجوم** · `attack-path-analysis`

[العربية](#arabic) · [English](#english) · [الفهرس / Catalog](../../README.md#catalog) · [المصدر الأصلي / Original instructions](../../skills/attack-path-analysis/SKILL.md)

<a id="arabic"></a>

## العربية

### ما وظيفة المهارة؟

تتبّع نتيجة أمنية محددة من مدخل المهاجم إلى الأثر مع معايرة الشدة.

### متى تستخدمها؟

استخدمها عندما يكون هدفك: تحليل لمسار الهجوم والافتراضات والأدلة المضادة وتقدير الشدة. راجع حدود الاستخدام في الملف الأصلي قبل الاستدعاء، خصوصًا الفرق بين الفحص والإصلاح والتحقق.

### ماذا تجهّز؟

نتيجة أمنية محتملة ومسار المصدر والسياسة الأمنية. حدّد النطاق والهدف بوضوح، وأرفق المصادر التي تملك صلاحية استخدامها. المعلومات الناقصة تحتاج إلى توضيح؛ لا يُفترض توفر أدوات التشغيل بمجرد نسخ الملفات.

### ما النتيجة المتوقعة؟

تحليل لمسار الهجوم والافتراضات والأدلة المضادة وتقدير الشدة.

### مثال استدعاء

```text
$attack-path-analysis تتبّع مسار استغلال هذه النتيجة الأمنية وحدّد الأثر.
```

المثال قالب طلب، وليس نتيجة تشغيل. استبدل الإشارة العامة بالملف أو النطاق أو البيانات المطلوبة.

<a id="english"></a>

## English

### What does it do?

Trace a specific security finding from attacker-controlled input to impact and calibrate severity.

### When should you use it?

Use it when you need: An attack-path assessment with assumptions, counterevidence, and severity. Read the original usage boundaries before invoking it, especially the distinction between scanning, fixing, and verification.

### What should you provide?

A candidate finding, source paths, and security policy. Specify the scope and goal, and supply sources you are authorized to use. Missing inputs require clarification; copying files does not provide the runtime tools.

### What can you expect?

An attack-path assessment with assumptions, counterevidence, and severity.

### Example invocation

```text
$attack-path-analysis Trace the exploit path and impact of this security finding.
```

This is a request template, not an execution result. Replace the generic reference with the relevant artifact, scope, or data.

## الملفات المساعدة / Supporting files

- [`references/severity-policy.md`](../../skills/attack-path-analysis/references/severity-policy.md)
- [`references/attack-path-facts.md`](../../skills/attack-path-analysis/references/attack-path-facts.md)

## المتطلبات وحدود النسخة / Requirements and archive limits

بعض المهارات تعتمد على مراجع مشتركة أو أدوات MCP أو موصلات غير مرفقة. الملفات المساعدة أعلاه هي الملفات المتاحة فقط، وليست إثباتًا لاكتمال الاعتماديات. راجع [تقرير الاستيراد](../../IMPORT-REPORT.md) و[سجل المصادر](../../IMPORT-MANIFEST.json) و[دليل الاستخدام](../USAGE.md). لم يُختبر تشغيل هذه المهارة ضمن إعداد هذه الوثائق.

Some skills depend on shared references, MCP tools, or connectors that are not bundled. The list above shows available files, not proof of complete dependencies. See the [import report](../../IMPORT-REPORT.md), [source manifest](../../IMPORT-MANIFEST.json), and [usage guide](../USAGE.md). This documentation work did not execute the skill workflow.

هذا شرح مستقل؛ محتوى `SKILL.md` الأصلي محفوظ دون تغيير. عند اختلاف الملخص عن التفاصيل، اقرأ التعليمات الأصلية.

This is a separate explanatory guide; the original `SKILL.md` is unchanged. Consult the original instructions for complete behavior and constraints.
