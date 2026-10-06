# Create reusable data context

**حفظ سياق البيانات** · `create-data-context`

[العربية](#arabic) · [English](#english) · [الفهرس / Catalog](../../README.md#catalog) · [المصدر الأصلي / Original instructions](../../skills/create-data-context/SKILL.md)

<a id="arabic"></a>

## العربية

### ما وظيفة المهارة؟

حفظ تعريفات البيانات والتفضيلات والتعليمات ليستفاد منها في تحليلات لاحقة.

### متى تستخدمها؟

استخدمها عندما يكون هدفك: سياق قابل لإعادة الاستخدام مع مصادر واضحة وحدود مشاركة. راجع حدود الاستخدام في الملف الأصلي قبل الاستدعاء، خصوصًا الفرق بين الفحص والإصلاح والتحقق.

### ماذا تجهّز؟

المصادر والتعريفات والتفضيلات والنطاق أو الجمهور. حدّد النطاق والهدف بوضوح، وأرفق المصادر التي تملك صلاحية استخدامها. المعلومات الناقصة تحتاج إلى توضيح؛ لا يُفترض توفر أدوات التشغيل بمجرد نسخ الملفات.

### ما النتيجة المتوقعة؟

سياق قابل لإعادة الاستخدام مع مصادر واضحة وحدود مشاركة.

### مثال استدعاء

```text
$create-data-context احفظ تعريفات المؤشرات وتفضيلاتي للتحليلات القادمة.
```

المثال قالب طلب، وليس نتيجة تشغيل. استبدل الإشارة العامة بالملف أو النطاق أو البيانات المطلوبة.

<a id="english"></a>

## English

### What does it do?

Preserve data definitions, preferences, and instructions for future analysis.

### When should you use it?

Use it when you need: Reusable context with source references and sharing boundaries. Read the original usage boundaries before invoking it, especially the distinction between scanning, fixing, and verification.

### What should you provide?

Sources, definitions, preferences, and scope or audience. Specify the scope and goal, and supply sources you are authorized to use. Missing inputs require clarification; copying files does not provide the runtime tools.

### What can you expect?

Reusable context with source references and sharing boundaries.

### Example invocation

```text
$create-data-context Save these metric definitions and preferences for future analysis.
```

This is a request template, not an execution result. Replace the generic reference with the relevant artifact, scope, or data.

## الملفات المساعدة / Supporting files

- [`references/data-context-authoring.md`](../../skills/create-data-context/references/data-context-authoring.md)
- [`references/sample-context-skill.md`](../../skills/create-data-context/references/sample-context-skill.md)
- [`references/packaging-and-sharing.md`](../../skills/create-data-context/references/packaging-and-sharing.md)

## المتطلبات وحدود النسخة / Requirements and archive limits

بعض المهارات تعتمد على مراجع مشتركة أو أدوات MCP أو موصلات غير مرفقة. الملفات المساعدة أعلاه هي الملفات المتاحة فقط، وليست إثباتًا لاكتمال الاعتماديات. راجع [تقرير الاستيراد](../../IMPORT-REPORT.md) و[سجل المصادر](../../IMPORT-MANIFEST.json) و[دليل الاستخدام](../USAGE.md). لم يُختبر تشغيل هذه المهارة ضمن إعداد هذه الوثائق.

Some skills depend on shared references, MCP tools, or connectors that are not bundled. The list above shows available files, not proof of complete dependencies. See the [import report](../../IMPORT-REPORT.md), [source manifest](../../IMPORT-MANIFEST.json), and [usage guide](../USAGE.md). This documentation work did not execute the skill workflow.

هذا شرح مستقل؛ محتوى `SKILL.md` الأصلي محفوظ دون تغيير. عند اختلاف الملخص عن التفاصيل، اقرأ التعليمات الأصلية.

This is a separate explanatory guide; the original `SKILL.md` is unchanged. Consult the original instructions for complete behavior and constraints.
