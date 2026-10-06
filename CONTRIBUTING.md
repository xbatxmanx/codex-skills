# المساهمة / Contributing

[العربية](#arabic) · [English](#english)

<a id="arabic"></a>

[العودة إلى الفهرس](README.md)

## نطاق المكتبة

تضم المكتبة المهارات الـ33 المختارة في [سجل المصادر](IMPORT-MANIFEST.json). إضافة مهارات مستقلة جديدة تحتاج إلى اختيار صريح من صاحب المستودع.

## الحفاظ على محتوى المصادر

- احتفظ بتعليمات المهارات والملفات المساعدة الأصلية دون إعادة صياغة أو تعديل الروابط.
- ضع تحسينات العرض والشرح في `README.md` أو `docs/`.
- عند تحديث مهارة من مصدرها، وثّق المصدر وأعد التحقق من المطابقة والبصمات.
- سجّل الموارد التي تعذّر الوصول إليها؛ لا تستبدلها بملفات أو تعليمات مختلقة.

حافظ على اتساق الشرح العربي والإنجليزي عند تعديل التوثيق. اتبع تعليمات صاحب المستودع الحالية بشأن النشر؛ تجهيز الملفات محليًا لا يمنح إذنًا بإنشاء commit أو رفع التغييرات أو فتح pull request.

## مراجعة التغييرات

قبل إنشاء commit أو pull request، اعرض ملخص الملفات والتغييرات ونتائج الفحص. افحص الملفات الجديدة بحثًا عن مفاتيح API وكلمات مرور وبيانات شخصية، وتحقق من الروابط المحلية وبصمات الملفات المستوردة.

اذكر الاعتماديات المفقودة وحدود التحقق في وصف pull request. لا تصف المهارات بأنها مكتملة التشغيل اعتمادًا على وجود الملفات فقط.


---

<a id="english"></a>

## English — Contributing

[Back to the catalog](README.md#catalog)

### Scope

The library contains the 33 explicitly selected skills recorded in the manifest. Adding an independent skill requires an explicit selection by the repository owner.

### Preserve original content

- Do not rewrite original skill instructions or supporting resources, including their links.
- Put Arabic and English explanations in `README.md` or `docs/`.
- Document the source and recheck content and hashes when refreshing a skill from its source.
- Record unavailable resources instead of inventing replacements.
- Keep both language sections consistent when changing explanatory content.

### Review changes

Before a commit or pull request, show the file-change summary and check results. Scan new files for API keys, passwords, and personal data, then verify local links and original-file hashes.

Document missing dependencies and verification limits. File presence alone does not prove runtime readiness. Follow the owner’s current publishing instructions; local preparation does not authorize a commit, push, pull request, or deployment.


## فحوص ما قبل الدمج / Pre-merge checks

```bash
python3 scripts/check_repository.py
python3 -m unittest discover -s tests -v
```

لا تغيّر بصمات الملفات لإخفاء تعديل غير مقصود. ملفات الاختبار والأدوات الجديدة تُوثّق منفصلة عن المصادر الأصلية. راجع [إشعار الحقوق](LICENSE) قبل إعادة توزيع مواد المصدر.

Do not change recorded hashes to hide an unintended source edit. New test supplements and tools are documented separately from original material. Review the [rights notice](LICENSE) before redistributing source content.
