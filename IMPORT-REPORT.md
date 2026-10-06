# تقرير استيراد المهارات

## الملفات والتغييرات

- أضيفت 32 مهارة داخل `skills/`، لكل منها `SKILL.md`.
- أضيفت 39 ملفات مساعدة أمكن الوصول إليها؛ الإجمالي 71 ملفًا أصليًا.
- جرى تحديث `README.md` بشرح المحتويات وطريقة الاستخدام والمتطلبات الخارجية.
- أضيف `IMPORT-MANIFEST.json` لتوثيق المصادر وبصمات SHA-256 ومحاولات القراءة التي تعذّرت.
- لم تُدرج مهارة تعليم الصيدلة، ولم تُضف أي مهارة مستقلة أخرى. ملف `sample-context-skill.md` مثال مساعد أصلي، وليس مهارة إضافية مثبتة.

## الحفاظ على المحتوى

قورنت الملفات المنقولة بالنصوص الكاملة التي أعادتها أداة قراءة المصادر، باستخدام تمثيل UTF-8، وحُفظت دون تحرير أو تغيير نهايات الأسطر. البصمات في السجل تسمح بالتحقق من ثبات النسخة بعد الاستيراد؛ لا تمثل إثباتًا لبصمات ملفات المصدر الخام، إذ توفّر الأداة محتوى نصيًا فقط.

## فحص الأسرار والبيانات الشخصية

فُحصت الملفات النصية بحثًا عن أنماط مفاتيح API المعروفة، المفاتيح الخاصة، كلمات المرور والتوكنات المسندة كنصوص ثابتة، بيانات اعتماد في عناوين URL، عناوين البريد، أرقام الهاتف الدولية وأرقام الهوية الأمريكية.
النتيجة: لم تظهر أسرار فعلية أو بيانات شخصية واضحة. التطابق الوحيد كان المثال `git@github.com:owner/repo.git` في `skills/triage-finding/references/github-rest-intake.md:21`، وهو عنوان Git بصيغة SSH وليس بريدًا شخصيًا. فُحصت قوالب الأمثلة بوصفها محتوى مساعدًا، وحُفظت دون تعديل.
هذا فحص أنماط مع مراجعة التطابقات، وليس ضمانًا لاكتشاف كل شكل ممكن من البيانات الحساسة.

## الملفات التي تعذّر الوصول إليها

يسرد `IMPORT-MANIFEST.json` محاولات القراءة الفاشلة مع المصدر والمهارة. بعض المحاولات تخص مواقع بديلة تم اختبارها؛ عدد المحاولات لا يساوي عدد الملفات المطلوبة المفقودة.

من المتطلبات غير المتاحة:
- مراجع الأمان المشتركة، مثل `references/artifact-storage.md` و`references/core-scan.md`، وسكربتات الأمان ومخططات JSON الموجودة خارج مجلدات المهارات.
- ملفات البيانات المشتركة، مثل `shared/shared-skill-instructions.md` و`shared/data-app.md`، وقوالب `templates/data-app/` وملفات المثال المشتركة.
- ملفات الاستثمار المشتركة وسكربت `user_context_preflight.py`.
- بعض المراجع المحلية، مثل إرشادات الرسوم المضمنة، وبعض اعتماديات سكربتات النشر.
- مهارات مصاحبة تذكرها التعليمات الأصلية ولم تظهر في الفهرس المتاح، مثل `schedule-refresh-jobs` و`share-artifact-summary` و`convert-to-doc` و`convert-to-slides` و`report-to-pdf`. لم تُنشأ بدائل لها.

حُفظت الروابط الأصلية دون تعديل. الموارد المشتركة لم تُستبدل بمحتوى مختلق، ولذلك توجد متطلبات وروابط غير مكتملة. لم يُدّع اختبار تشغيل المهارات أو تثبيت أدواتها وموصلاتها الأصلية.

## نطاق النشر

هذه نسخة أرشيفية من التعليمات والملفات المساعدة التي أتيحت قراءتها. نشر المستودع لا يجعل الحزمة مكتملة التشغيل، ولا يمنح الوصول إلى أدوات الإضافات.


## إضافة محلية: AI Shark Tank Council

أضيفت مهارة `ai-shark-tank-council` بطلب صريح من صاحب المستودع، من ملف `SKILL.md` المرفق. قورنت النسخة بالمرفق بايتًا ببايت دون تغيير المحتوى. أصبح الإجمالي 33 مهارة و74 ملفًا أصليًا، منها 41 ملفًا مساعدًا. الأعداد في الأقسام السابقة توثّق دفعة الاستيراد الأولى.

أضيف شرح مستقل في `docs/AI-SHARK-TANK-COUNCIL.md` مع المدخلات والأدوار والقرارات ومثال استخدام. يشير المصدر إلى `references/evaluation-cases.md` الذي لم يُرفق؛ لم يُختلق بديل ولم تُشغّل اختبارات المهارة. يوضح الدليل صياغة معادلة الأوزان وفق المعادلة الصريحة الموجودة في المصدر، دون تحرير الأصل.

جُهّزت هذه الإضافة محليًا أولًا؛ راجع سجل Git وطلبات الدمج لمعرفة حالة نشرها.

أُرفقت لاحقًا إعدادات الواجهة `agents/openai.yaml` والأيقونة `assets/icon.svg` لمهارة Shark Tank، وأضيفتا دون تعديل. المرفقات الأخرى تخص مهارة مستقلة اسمها `ceo`، ولم تُضف ضمن هذا الطلب دون تحديد صريح. ملف اختبارات `references/evaluation-cases.md` لا يزال غير مرفق.


## English — Import summary and current local additions

The initial import contained 32 selected skills and 39 supporting files. The explicitly requested AI Shark Tank Council addition brings the current local total to **33 skills and 41 supporting files**, comprising **74 original files**. The CEO and pharmacy tutoring skills are excluded.

The original files are preserved. Cloud-reader imports were matched against the complete UTF-8 text returned by that reader; uploaded Shark Tank files were compared byte-for-byte with the attachments. `IMPORT-MANIFEST.json` records provenance and SHA-256 hashes. Its failed-read entries may include attempted alternative locations, so their count is not a count of distinct missing dependencies.

Known gaps include shared security references, scripts and schemas; shared Data instructions, templates and assets; investment plugin prerequisites; and some local helper dependencies. The Shark Tank skill refers to `references/evaluation-cases.md`, which was not uploaded. Its four evaluation tests have not been run.

The import scan found no clear actual secrets or personal information; its only initial email-pattern match was the generic SSH example `git@github.com:owner/repo.git`. Pattern checks cannot establish that every possible form of sensitive information is absent.

Arabic and English explanations are written separately from original skill content, with one guide for each skill. This documentation work does not execute skill workflows, install their source plugins, or establish runtime readiness. The Shark Tank and bilingual documentation additions were prepared locally first. Consult the Git history and pull requests for their publication status.


## معالجة جودة المستودع / Repository quality improvements

أُضيف فحص تلقائي للسلامة والروابط والشرح الثنائي والأيقونات وأنماط البيانات الحساسة، مع اختبارات سلبية لأداة الفحص وملف CODEOWNERS. أضيف إشعار حقوق محافظ؛ لا يحوّل مواد المصدر إلى مواد مفتوحة الترخيص ولا يثبت إذن إعادة توزيعها.

أضيف `references/evaluation-cases.md` لـShark Tank من إنشاء المستودع، موسوم بوضوح بأنه ليس ملف المصدر المفقود، ومسجل منفصلًا. الملفات الأصلية الـ74 لم تتغير. حالات التقييم الأربع لم تُنفّذ؛ اختبارات أداة سلامة المستودع مستقلة عنها.

Repository checks now cover integrity, links, bilingual guides, icons, and sensitive-data patterns, with negative tests for the checker and a CODEOWNERS file. A conservative rights notice does not relicense source material or establish redistribution permission.

A clearly identified maintainer-authored Shark Tank evaluation supplement supplies the missing reference path and is recorded separately. The 74 original files remain unchanged. Its four behavioral cases are unrun; checker unit tests are a separate suite.
