# codex-skills

مجموعة من 32 مهارة لـ Codex، نُقلت من المصادر المتاحة دون تحرير محتواها. لم تُدرج مهارة تعليم الصيدلة.

## المحتويات

- `skills/<name>/SKILL.md`: التعليمات الأصلية لكل مهارة.
- ملفات `references/` و`scripts/` و`specifications/` التابعة للمهارات، حيث أمكن الوصول إليها.
- `IMPORT-MANIFEST.json`: أسماء المهارات، مصادر الملفات، ومحاولات قراءة الموارد التي تعذّرت.
- `IMPORT-REPORT.md`: نتيجة المطابقة والفحص وحدود اكتمال الحزمة.

## المهارات

- [`codex-security:assess-patch-risk`](skills/assess-patch-risk/SKILL.md)
- [`codex-security:attack-path-analysis`](skills/attack-path-analysis/SKILL.md)
- [`codex-security:deep-security-scan`](skills/deep-security-scan/SKILL.md)
- [`codex-security:define-security-policy`](skills/define-security-policy/SKILL.md)
- [`codex-security:finding-discovery`](skills/finding-discovery/SKILL.md)
- [`codex-security:fix-finding`](skills/fix-finding/SKILL.md)
- [`codex-security:propose-security-hardening`](skills/propose-security-hardening/SKILL.md)
- [`codex-security:security-diff-scan`](skills/security-diff-scan/SKILL.md)
- [`codex-security:security-scan`](skills/security-scan/SKILL.md)
- [`codex-security:threat-model`](skills/threat-model/SKILL.md)
- [`codex-security:track-findings`](skills/track-findings/SKILL.md)
- [`codex-security:triage-finding`](skills/triage-finding/SKILL.md)
- [`codex-security:validation`](skills/validation/SKILL.md)
- [`codex-security:verify-fix`](skills/verify-fix/SKILL.md)
- [`codex-security:vulnerability-writeup`](skills/vulnerability-writeup/SKILL.md)
- [`public-equity-investing:public-equity-investing`](skills/public-equity-investing/SKILL.md)
- [`data-analytics:analyze-data-quality`](skills/analyze-data-quality/SKILL.md)
- [`data-analytics:build-dashboard`](skills/build-dashboard/SKILL.md)
- [`data-analytics:build-report`](skills/build-report/SKILL.md)
- [`data-analytics:create-data-context`](skills/create-data-context/SKILL.md)
- [`data-analytics:design-kpis`](skills/design-kpis/SKILL.md)
- [`data-analytics:gather-business-context`](skills/gather-business-context/SKILL.md)
- [`data-analytics:index`](skills/index/SKILL.md)
- [`data-analytics:jupyter-notebooks`](skills/jupyter-notebooks/SKILL.md)
- [`data-analytics:kpi-reporting`](skills/kpi-reporting/SKILL.md)
- [`data-analytics:market-sizing`](skills/market-sizing/SKILL.md)
- [`data-analytics:metric-diagnostics`](skills/metric-diagnostics/SKILL.md)
- [`data-analytics:product-business-analysis`](skills/product-business-analysis/SKILL.md)
- [`data-analytics:publish-artifact-to-sites`](skills/publish-artifact-to-sites/SKILL.md)
- [`data-analytics:validate-data`](skills/validate-data/SKILL.md)
- [`data-analytics:visualize-data`](skills/visualize-data/SKILL.md)
- [`cloud-environment-onboarding:setup`](skills/setup/SKILL.md)

## الاستخدام

1. اقرأ ملف `SKILL.md` للمهارة المطلوبة وتحقق من متطلباتها والملفات المساعدة المذكورة فيه.
2. لاستخدام مهارة في Codex، انسخ مجلدها كاملًا إلى موقع المهارات الذي يدعمه إصدارك، مثل `~/.agents/skills/<name>/` للمهارات الشخصية أو `.agents/skills/<name>/` داخل مشروعك. احتفظ بالملفات المساعدة بجوار `SKILL.md`.
3. أعد فتح جلسة Codex إن احتاج إصدارك ذلك، ثم استدعِ المهارة باسم حقل `name` في ملفها، مثل `$assess-patch-risk`.

هذه نسخة أرشيفية من التعليمات المتاحة، وليست تثبيتًا للإضافات أو أدوات MCP أو الموصلات. تحتاج بعض المهارات إلى أدوات خاصة بالإضافات الأصلية، أو مراجع مشتركة لم تتوفر للقراءة. لذلك لا يمكن ضمان تشغيل جميع المهارات من هذه النسخة وحدها.

حُفظت الروابط والمسارات الأصلية دون تعديل. الروابط إلى موارد مشتركة خارج مجلد المهارة أو مهارات مصاحبة غير موجودة تظل متطلبات خارجية؛ راجع سجل الاستيراد قبل الاستخدام. لم تُضف مهارات مصاحبة غير مدرجة في الاختيار.
