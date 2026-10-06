# Standard security scan

**فحص أمني قياسي** · `security-scan`

[العربية](#arabic) · [English](#english) · [الفهرس / Catalog](../../README.md#catalog) · [المصدر الأصلي / Original instructions](../../skills/security-scan/SKILL.md)

<a id="arabic"></a>

## العربية

### ما وظيفة المهارة؟

فحص أمني مرة واحدة لمستودع أو نطاق محدد دون فرق تغييرات.

### متى تستخدمها؟

استخدمها عندما يكون هدفك: نتائج متحقق منها ووصف للتغطية وحدود الفحص. راجع حدود الاستخدام في الملف الأصلي قبل الاستدعاء، خصوصًا الفرق بين الفحص والإصلاح والتحقق.

### ماذا تجهّز؟

المستودع والنطاق المطلوب وسياق الأمان. حدّد النطاق والهدف بوضوح، وأرفق المصادر التي تملك صلاحية استخدامها. المعلومات الناقصة تحتاج إلى توضيح؛ لا يُفترض توفر أدوات التشغيل بمجرد نسخ الملفات.

### ما النتيجة المتوقعة؟

نتائج متحقق منها ووصف للتغطية وحدود الفحص.

### مثال استدعاء

```text
$security-scan افحص هذا المستودع أمنيًا ضمن النطاق المحدد.
```

المثال قالب طلب، وليس نتيجة تشغيل. استبدل الإشارة العامة بالملف أو النطاق أو البيانات المطلوبة.

<a id="english"></a>

## English

### What does it do?

Run a single-pass security audit of a repository or scoped paths without a diff.

### When should you use it?

Use it when you need: Validated findings, coverage, and audit limitations. Read the original usage boundaries before invoking it, especially the distinction between scanning, fixing, and verification.

### What should you provide?

The repository, requested scope, and security context. Specify the scope and goal, and supply sources you are authorized to use. Missing inputs require clarification; copying files does not provide the runtime tools.

### What can you expect?

Validated findings, coverage, and audit limitations.

### Example invocation

```text
$security-scan Audit this repository within the specified scope.
```

This is a request template, not an execution result. Replace the generic reference with the relevant artifact, scope, or data.

## الملفات المساعدة / Supporting files

- [`references/desktop-scan.md`](../../skills/security-scan/references/desktop-scan.md)
- [`references/scan-artifacts-and-ledger.md`](../../skills/security-scan/references/scan-artifacts-and-ledger.md)

## المتطلبات وحدود النسخة / Requirements and archive limits

بعض المهارات تعتمد على مراجع مشتركة أو أدوات MCP أو موصلات غير مرفقة. الملفات المساعدة أعلاه هي الملفات المتاحة فقط، وليست إثباتًا لاكتمال الاعتماديات. راجع [تقرير الاستيراد](../../IMPORT-REPORT.md) و[سجل المصادر](../../IMPORT-MANIFEST.json) و[دليل الاستخدام](../USAGE.md). لم يُختبر تشغيل هذه المهارة ضمن إعداد هذه الوثائق.

Some skills depend on shared references, MCP tools, or connectors that are not bundled. The list above shows available files, not proof of complete dependencies. See the [import report](../../IMPORT-REPORT.md), [source manifest](../../IMPORT-MANIFEST.json), and [usage guide](../USAGE.md). This documentation work did not execute the skill workflow.

هذا شرح مستقل؛ محتوى `SKILL.md` الأصلي محفوظ دون تغيير. عند اختلاف الملخص عن التفاصيل، اقرأ التعليمات الأصلية.

This is a separate explanatory guide; the original `SKILL.md` is unchanged. Consult the original instructions for complete behavior and constraints.
