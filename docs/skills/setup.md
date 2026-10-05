# Set up a cloud environment

**تجهيز البيئة السحابية** · `setup`

[العربية](#arabic) · [English](#english) · [الفهرس / Catalog](../../README.md#catalog) · [المصدر الأصلي / Original instructions](../../skills/setup/SKILL.md)

<a id="arabic"></a>

## العربية

### ما وظيفة المهارة؟

تجهيز المستودعات وتثبيت المتطلبات والتحقق من سير التطوير وحفظ تعليمات الإعداد.

### متى تستخدمها؟

استخدمها عندما يكون هدفك: بيئة متحقق منها وتعليمات قابلة لإعادة الاستخدام أو عائق محدد. راجع حدود الاستخدام في الملف الأصلي قبل الاستدعاء، خصوصًا الفرق بين الفحص والإصلاح والتحقق.

### ماذا تجهّز؟

المستودعات وسير التطوير المطلوب والإعدادات المتاحة. حدّد النطاق والهدف بوضوح، وأرفق المصادر التي تملك صلاحية استخدامها. المعلومات الناقصة تحتاج إلى توضيح؛ لا يُفترض توفر أدوات التشغيل بمجرد نسخ الملفات.

### ما النتيجة المتوقعة؟

بيئة متحقق منها وتعليمات قابلة لإعادة الاستخدام أو عائق محدد.

### مثال استدعاء

```text
$setup جهّز البيئة لهذا المستودع واختبر سير التطوير.
```

المثال قالب طلب، وليس نتيجة تشغيل. استبدل الإشارة العامة بالملف أو النطاق أو البيانات المطلوبة.

<a id="english"></a>

## English

### What does it do?

Prepare repositories, install prerequisites, verify development, and save reusable setup instructions.

### When should you use it?

Use it when you need: A validated environment with reusable instructions or a concrete blocker. Read the original usage boundaries before invoking it, especially the distinction between scanning, fixing, and verification.

### What should you provide?

Repositories, intended development workflow, and available configuration. Specify the scope and goal, and supply sources you are authorized to use. Missing inputs require clarification; copying files does not provide the runtime tools.

### What can you expect?

A validated environment with reusable instructions or a concrete blocker.

### Example invocation

```text
$setup Set up this repository’s environment and verify its development workflow.
```

This is a request template, not an execution result. Replace the generic reference with the relevant artifact, scope, or data.

## الملفات المساعدة / Supporting files

- [`references/onboarding.md`](../../skills/setup/references/onboarding.md)

## المتطلبات وحدود النسخة / Requirements and archive limits

بعض المهارات تعتمد على مراجع مشتركة أو أدوات MCP أو موصلات غير مرفقة. الملفات المساعدة أعلاه هي الملفات المتاحة فقط، وليست إثباتًا لاكتمال الاعتماديات. راجع [تقرير الاستيراد](../../IMPORT-REPORT.md) و[سجل المصادر](../../IMPORT-MANIFEST.json) و[دليل الاستخدام](../USAGE.md). لم يُختبر تشغيل هذه المهارة ضمن إعداد هذه الوثائق.

Some skills depend on shared references, MCP tools, or connectors that are not bundled. The list above shows available files, not proof of complete dependencies. See the [import report](../../IMPORT-REPORT.md), [source manifest](../../IMPORT-MANIFEST.json), and [usage guide](../USAGE.md). This documentation work did not execute the skill workflow.

هذا شرح مستقل؛ محتوى `SKILL.md` الأصلي محفوظ دون تغيير. عند اختلاف الملخص عن التفاصيل، اقرأ التعليمات الأصلية.

This is a separate explanatory guide; the original `SKILL.md` is unchanged. Consult the original instructions for complete behavior and constraints.
