# حالة المستودع / Repository health

[الفهرس / Catalog](../README.md#catalog)

## ما الذي تحميه الفحوص؟ / What do checks protect?

الفحص `Repository validation` يعمل على طلبات الدمج ودفعات main. يتحقق من
بصمات الملفات الأصلية، مخزون المهارات، أقسام الشرح باللغتين، الروابط المحلية،
الأيقونات، وأنماط بيانات حساسة. يعمل دون تحميل تبعيات أو إرسال المحتوى لخدمة خارجية.

The `Repository validation` check runs on pull requests and main pushes. It
checks original-file hashes, the skill inventory, bilingual sections, local
links, icons, and sensitive-data patterns without downloading dependencies or
sending repository content to an external service.

```bash
python3 scripts/check_repository.py
python3 -m unittest discover -s tests -v
```

اختبارات أداة الفحص تتأكد أن تسرب بيانات اعتماد أو مسار خارج المستودع أو رابط
مكسور يؤدي إلى فشل حقيقي. الفحص لا يختبر سلوك نموذج أو يثبت صحة تحليل استثماري.

The checker tests verify that credential patterns, escaping paths, and broken
links cause real failures. They do not evaluate model behavior or certify an
investment analysis.

## حماية مناسبة لصاحب مستودع واحد / Solo-maintainer protection

الإعداد المقترح لفرع main:

- منع الحذف والـforce push، مع عدم السماح بالتجاوز.
- اشتراط pull request وحل نقاشات المراجعة.
- صفر موافقات إلزامية، دون اشتراط موافقة شخص آخر على آخر دفعة.
- عدم اشتراط مراجعة CODEOWNERS؛ الملف يحدد المسؤول ولا يجبره على مراجعة طلبه.
- إضافة فحص Repository validation المطلوب بعد التأكد من نجاح أول تشغيل.

Recommended main settings: block deletion and force pushes; no bypass; require
pull requests and resolved conversations; zero required approvals; no last-push
or code-owner approval requirement. CODEOWNERS routes ownership without requiring
self-approval. Require `Repository validation` after confirming its first run.

هذه توصية إعداد، وليست ادعاء بأن واجهة GitHub قبلت التعديل. راجع الحالة الحالية
في Settings → Rules → Rulesets. تطبيقها يحتاج إلى صلاحية إدارة Rulesets.

These are recommended settings, not a claim that GitHub accepted an update.
Check Settings → Rules → Rulesets for current enforcement. Applying them requires
permission to administer repository rulesets.

## ملفات المصدر والملفات الجديدة / Source and authored content

المهارات الأصلية الـ74 محفوظة ببصماتها. أضيف ملف اختبار مساعد لـShark Tank من
إنشاء المستودع، موثّق منفصلًا في السجل؛ لم يُقدّم على أنه الملف الأصلي المفقود.
الاختبارات الأربعة تحتاج إلى تشغيل فعلي منفصل؛ وجودها لا يعني نجاحها.

All 74 original files retain their recorded hashes. A repository-authored Shark
Tank test supplement is recorded separately; it is not presented as the missing
original file. Its four cases require actual separate runs, not merely existence.

## الاعتماديات الخارجية / External dependencies

راجع [مخزون الاعتماديات](DEPENDENCIES.md). بعض المهارات تستخدم أدوات وموارد
خاصة بالإضافة الأصلية؛ لا يمكن جعل نسخ تعليماتها مستقلًا بإنشاء ملفات بديلة
لأدوات مغلقة أو غير متاحة. الشرح وحده لا يثبت التشغيل.

See the [dependency inventory](DEPENDENCIES.md). Some skills use source-plugin
resources or runtime tools. Instruction copies cannot be made self-contained by
inventing replacements for unavailable tools. Explanatory documentation is not
proof of execution.

## حقوق الاستخدام / Usage rights

راجع [إشعار الحقوق](../LICENSE). لا يمنح المستودع ترخيص إعادة استخدام عام، ولا
يفرض ترخيصًا جديدًا على مواد الغير. تحتاج حقوق إعادة توزيع المصادر إلى دليل
من أصحابها؛ الإشعار لا يعوّض ذلك الدليل.

See the [rights notice](../LICENSE). No blanket reuse license is granted, and no
new license is imposed on third-party material. Source redistribution permissions
require evidence from their rights holders; this notice does not supply it.
