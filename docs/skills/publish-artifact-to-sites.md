# Publish an artifact to Sites

**نشر تقرير أو لوحة إلى Sites** · `publish-artifact-to-sites`

[العربية](#arabic) · [English](#english) · [الفهرس / Catalog](../../README.md#catalog) · [المصدر الأصلي / Original instructions](../../skills/publish-artifact-to-sites/SKILL.md)

<a id="arabic"></a>

## العربية

### ما وظيفة المهارة؟

نشر منتج تحليلي موجود عبر أدوات Sites مع التحقق من الحزمة والوصول.

### متى تستخدمها؟

استخدمها عندما يكون هدفك: نشر متحقق منه أو تقرير واضح بالخطوة المحجوبة. راجع حدود الاستخدام في الملف الأصلي قبل الاستدعاء، خصوصًا الفرق بين الفحص والإصلاح والتحقق.

### ماذا تجهّز؟

منتج موجود وموقع مستهدف وصلاحيات وأدوات النشر. حدّد النطاق والهدف بوضوح، وأرفق المصادر التي تملك صلاحية استخدامها. المعلومات الناقصة تحتاج إلى توضيح؛ لا يُفترض توفر أدوات التشغيل بمجرد نسخ الملفات.

### ما النتيجة المتوقعة؟

نشر متحقق منه أو تقرير واضح بالخطوة المحجوبة.

### مثال استدعاء

```text
$publish-artifact-to-sites راجع متطلبات نشر هذا التقرير، ولا تنشر قبل إذني.
```

المثال قالب طلب، وليس نتيجة تشغيل. استبدل الإشارة العامة بالملف أو النطاق أو البيانات المطلوبة.

<a id="english"></a>

## English

### What does it do?

Publish an existing analytical artifact through Sites with packaging and access checks.

### When should you use it?

Use it when you need: A verified publication or a clear report of the blocked step. Read the original usage boundaries before invoking it, especially the distinction between scanning, fixing, and verification.

### What should you provide?

An existing artifact, destination, permissions, and publishing tools. Specify the scope and goal, and supply sources you are authorized to use. Missing inputs require clarification; copying files does not provide the runtime tools.

### What can you expect?

A verified publication or a clear report of the blocked step.

### Example invocation

```text
$publish-artifact-to-sites Review publishing prerequisites for this report; do not publish without my authorization.
```

This is a request template, not an execution result. Replace the generic reference with the relevant artifact, scope, or data.

## الملفات المساعدة / Supporting files

- [`references/windows-publication.md`](../../skills/publish-artifact-to-sites/references/windows-publication.md)
- [`references/publication-source.md`](../../skills/publish-artifact-to-sites/references/publication-source.md)
- [`scripts/package-data-app-for-sites.mjs`](../../skills/publish-artifact-to-sites/scripts/package-data-app-for-sites.mjs)
- [`scripts/upload-data-app-assets.mjs`](../../skills/publish-artifact-to-sites/scripts/upload-data-app-assets.mjs)
- [`scripts/publish-data-app.mjs`](../../skills/publish-artifact-to-sites/scripts/publish-data-app.mjs)
- [`scripts/publication-source.mjs`](../../skills/publish-artifact-to-sites/scripts/publication-source.mjs)
- [`scripts/publication-secrets.mjs`](../../skills/publish-artifact-to-sites/scripts/publication-secrets.mjs)
- [`scripts/publication-assets.mjs`](../../skills/publish-artifact-to-sites/scripts/publication-assets.mjs)
- [`scripts/publication-snapshot-index.mjs`](../../skills/publish-artifact-to-sites/scripts/publication-snapshot-index.mjs)
- [`scripts/publication-archive.mjs`](../../skills/publish-artifact-to-sites/scripts/publication-archive.mjs)
- [`scripts/publication-git.mjs`](../../skills/publish-artifact-to-sites/scripts/publication-git.mjs)
- [`scripts/publication-git-process.mjs`](../../skills/publish-artifact-to-sites/scripts/publication-git-process.mjs)
- [`scripts/publication-scan-streams.mjs`](../../skills/publish-artifact-to-sites/scripts/publication-scan-streams.mjs)

## المتطلبات وحدود النسخة / Requirements and archive limits

بعض المهارات تعتمد على مراجع مشتركة أو أدوات MCP أو موصلات غير مرفقة. الملفات المساعدة أعلاه هي الملفات المتاحة فقط، وليست إثباتًا لاكتمال الاعتماديات. راجع [تقرير الاستيراد](../../IMPORT-REPORT.md) و[سجل المصادر](../../IMPORT-MANIFEST.json) و[دليل الاستخدام](../USAGE.md). لم يُختبر تشغيل هذه المهارة ضمن إعداد هذه الوثائق.

Some skills depend on shared references, MCP tools, or connectors that are not bundled. The list above shows available files, not proof of complete dependencies. See the [import report](../../IMPORT-REPORT.md), [source manifest](../../IMPORT-MANIFEST.json), and [usage guide](../USAGE.md). This documentation work did not execute the skill workflow.

هذا شرح مستقل؛ محتوى `SKILL.md` الأصلي محفوظ دون تغيير. عند اختلاف الملخص عن التفاصيل، اقرأ التعليمات الأصلية.

This is a separate explanatory guide; the original `SKILL.md` is unchanged. Consult the original instructions for complete behavior and constraints.
