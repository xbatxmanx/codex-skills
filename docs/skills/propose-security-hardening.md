# Propose security hardening

**اقتراح تقوية أمنية** · `propose-security-hardening`

[العربية](#arabic) · [English](#english) · [الفهرس / Catalog](../../README.md#catalog) · [المصدر الأصلي / Original instructions](../../skills/propose-security-hardening/SKILL.md)

<a id="arabic"></a>

## العربية

### ما وظيفة المهارة؟

اقتراح حلول بنيوية تعالج الأسباب المشتركة بدل الاكتفاء بإصلاح منفرد.

### متى تستخدمها؟

استخدمها عندما يكون هدفك: بدائل مدعومة بالأدلة ومقارنة للمخاطر والتكلفة وخطة تطبيق. راجع حدود الاستخدام في الملف الأصلي قبل الاستدعاء، خصوصًا الفرق بين الفحص والإصلاح والتحقق.

### ماذا تجهّز؟

نتائج أو تقارير ثغرات ومعمارية النظام والقيود الهندسية. حدّد النطاق والهدف بوضوح، وأرفق المصادر التي تملك صلاحية استخدامها. المعلومات الناقصة تحتاج إلى توضيح؛ لا يُفترض توفر أدوات التشغيل بمجرد نسخ الملفات.

### ما النتيجة المتوقعة؟

بدائل مدعومة بالأدلة ومقارنة للمخاطر والتكلفة وخطة تطبيق.

### مثال استدعاء

```text
$propose-security-hardening اقترح تحسينات بنيوية بناءً على هذه النتائج الأمنية.
```

المثال قالب طلب، وليس نتيجة تشغيل. استبدل الإشارة العامة بالملف أو النطاق أو البيانات المطلوبة.

<a id="english"></a>

## English

### What does it do?

Propose structural improvements addressing systemic security causes.

### When should you use it?

Use it when you need: Evidence-backed alternatives with tradeoffs and implementation guidance. Read the original usage boundaries before invoking it, especially the distinction between scanning, fixing, and verification.

### What should you provide?

Findings or vulnerability reports, architecture, and engineering constraints. Specify the scope and goal, and supply sources you are authorized to use. Missing inputs require clarification; copying files does not provide the runtime tools.

### What can you expect?

Evidence-backed alternatives with tradeoffs and implementation guidance.

### Example invocation

```text
$propose-security-hardening Propose structural improvements based on these security findings.
```

This is a request template, not an execution result. Replace the generic reference with the relevant artifact, scope, or data.

## الملفات المساعدة / Supporting files

- [`references/proposal-format.md`](../../skills/propose-security-hardening/references/proposal-format.md)

## المتطلبات وحدود النسخة / Requirements and archive limits

بعض المهارات تعتمد على مراجع مشتركة أو أدوات MCP أو موصلات غير مرفقة. الملفات المساعدة أعلاه هي الملفات المتاحة فقط، وليست إثباتًا لاكتمال الاعتماديات. راجع [تقرير الاستيراد](../../IMPORT-REPORT.md) و[سجل المصادر](../../IMPORT-MANIFEST.json) و[دليل الاستخدام](../USAGE.md). لم يُختبر تشغيل هذه المهارة ضمن إعداد هذه الوثائق.

Some skills depend on shared references, MCP tools, or connectors that are not bundled. The list above shows available files, not proof of complete dependencies. See the [import report](../../IMPORT-REPORT.md), [source manifest](../../IMPORT-MANIFEST.json), and [usage guide](../USAGE.md). This documentation work did not execute the skill workflow.

هذا شرح مستقل؛ محتوى `SKILL.md` الأصلي محفوظ دون تغيير. عند اختلاف الملخص عن التفاصيل، اقرأ التعليمات الأصلية.

This is a separate explanatory guide; the original `SKILL.md` is unchanged. Consult the original instructions for complete behavior and constraints.
