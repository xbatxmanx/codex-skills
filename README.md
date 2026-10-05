<div align="center">

# Codex Skills

**مكتبة منظّمة للمهارات وسير العمل في Codex**

الأمان · تحليل البيانات · الاستثمار · تجهيز البيئة

![Skills](https://img.shields.io/badge/skills-32-2563eb?style=flat-square)
![Supporting files](https://img.shields.io/badge/supporting_files-39-0f766e?style=flat-square)
![Format](https://img.shields.io/badge/format-Markdown-475569?style=flat-square)
![Content](https://img.shields.io/badge/source_content-preserved-7c3aed?style=flat-square)

[تصفّح المهارات](#catalog) · [ابدأ الاستخدام](#quick-start) · [دليل الاستخدام](docs/USAGE.md) · [تقرير الاستيراد](IMPORT-REPORT.md)

</div>

---

يضم هذا المستودع **32 مهارة و39 ملفًا مساعدًا** من المصادر المتاحة، مع الحفاظ على النصوص الأصلية. يجمعها في مجلدات مستقلة وفهرس يسهل تصفّحه حسب المجال.

> **حالة الحزمة:** نسخة أرشيفية من التعليمات المتاحة. بعض المهارات تعتمد على مراجع مشتركة أو أدوات الإضافات الأصلية غير المرفقة. راجع [حدود النسخة](IMPORT-REPORT.md) قبل الاستخدام.

<a id="catalog"></a>

## فهرس المهارات

| المجال | عدد المهارات | الاستخدام |
| :--- | :---: | :--- |
| [الأمان](#security) | 15 | الفحص، نمذجة التهديدات، الإصلاح والتوثيق |
| [تحليل البيانات](#data) | 15 | التحليل، مؤشرات الأداء، التقارير واللوحات |
| [الاستثمار](#investing) | 1 | بحث الشركات والأسهم المدرجة |
| [البيئة السحابية](#environment) | 1 | تجهيز بيئات التطوير والتحقق منها |

<a id="security"></a>

### الأمان

| المهارة | الغرض |
| :--- | :--- |
| [`assess-patch-risk`](skills/assess-patch-risk/SKILL.md) | تقييم أثر التغييرات ومخاطر الانحدار وأهلية الدمج. |
| [`attack-path-analysis`](skills/attack-path-analysis/SKILL.md) | تتبّع مسار الهجوم وتقدير شدة الثغرات. |
| [`deep-security-scan`](skills/deep-security-scan/SKILL.md) | فحص أمني معمّق عبر جولات مستقلة. |
| [`define-security-policy`](skills/define-security-policy/SKILL.md) | صياغة سياسات SECURITY.md ومراجعتها. |
| [`finding-discovery`](skills/finding-discovery/SKILL.md) | اكتشاف مشكلات أمنية محتملة في المصدر. |
| [`fix-finding`](skills/fix-finding/SKILL.md) | إصلاح الثغرات الأمنية والتحقق من التعديل. |
| [`propose-security-hardening`](skills/propose-security-hardening/SKILL.md) | اقتراح تحسينات بنيوية للحد من المخاطر. |
| [`security-diff-scan`](skills/security-diff-scan/SKILL.md) | مراجعة أمنية لتغييرات الفروع والـ PRs. |
| [`security-scan`](skills/security-scan/SKILL.md) | فحص أمني للمستودع أو نطاق محدد. |
| [`threat-model`](skills/threat-model/SKILL.md) | إنشاء نموذج تهديدات مبني على المصدر. |
| [`track-findings`](skills/track-findings/SKILL.md) | تتبّع النتائج الأمنية في أدوات إدارة العمل. |
| [`triage-finding`](skills/triage-finding/SKILL.md) | تقييم أثر تقارير الثغرات الواردة على المستودع. |
| [`validation`](skills/validation/SKILL.md) | التحقق من صحة النتائج الأمنية المحتملة. |
| [`verify-fix`](skills/verify-fix/SKILL.md) | التحقق من معالجة ثغرة بعد إصلاحها. |
| [`vulnerability-writeup`](skills/vulnerability-writeup/SKILL.md) | إعداد تقارير ثغرات واضحة ومدعومة بالأدلة. |

<a id="data"></a>

### تحليل البيانات

| المهارة | الغرض |
| :--- | :--- |
| [`analyze-data-quality`](skills/analyze-data-quality/SKILL.md) | فحص جودة البيانات واتساقها وقابليتها للاستخدام. |
| [`build-dashboard`](skills/build-dashboard/SKILL.md) | إنشاء لوحات تفاعلية مبنية على مصادر البيانات. |
| [`build-report`](skills/build-report/SKILL.md) | إعداد تقارير تحليلية موثّقة للأعمال والفرق التقنية. |
| [`create-data-context`](skills/create-data-context/SKILL.md) | حفظ تعريفات البيانات والتفضيلات والسياق التحليلي. |
| [`design-kpis`](skills/design-kpis/SKILL.md) | تصميم مؤشرات الأداء وتعريفاتها وخطط قياسها. |
| [`gather-business-context`](skills/gather-business-context/SKILL.md) | جمع سياق الأعمال قبل بدء التحليل. |
| [`index`](skills/index/SKILL.md) | توجيه طلبات البيانات إلى سير العمل المناسب. |
| [`jupyter-notebooks`](skills/jupyter-notebooks/SKILL.md) | إنشاء دفاتر SQL وPython قابلة لإعادة التشغيل. |
| [`kpi-reporting`](skills/kpi-reporting/SKILL.md) | إعداد ملخصات الأداء ومقارنات النتائج بالأهداف. |
| [`market-sizing`](skills/market-sizing/SKILL.md) | تقدير حجم السوق والفرص مع توضيح الافتراضات. |
| [`metric-diagnostics`](skills/metric-diagnostics/SKILL.md) | تشخيص أسباب تغير المؤشرات والانحرافات. |
| [`product-business-analysis`](skills/product-business-analysis/SKILL.md) | دعم قرارات المنتجات والأعمال بتحليل البيانات. |
| [`publish-artifact-to-sites`](skills/publish-artifact-to-sites/SKILL.md) | نشر التقارير واللوحات الموجودة إلى Sites. |
| [`validate-data`](skills/validate-data/SKILL.md) | مراجعة المصادر والحسابات والاستنتاجات التحليلية. |
| [`visualize-data`](skills/visualize-data/SKILL.md) | تصميم الرسوم الكمية والتحقق من دقتها. |

<a id="investing"></a>

### الاستثمار

| المهارة | الغرض |
| :--- | :--- |
| [`public-equity-investing`](skills/public-equity-investing/SKILL.md) | بحث الأسهم المدرجة والتقييم والأطروحات الاستثمارية. |

<a id="environment"></a>

### البيئة السحابية

| المهارة | الغرض |
| :--- | :--- |
| [`setup`](skills/setup/SKILL.md) | تجهيز بيئات Codex السحابية واختبار جاهزيتها. |

<a id="quick-start"></a>

## ابدأ الاستخدام

1. اختر المهارة من الفهرس، واقرأ متطلباتها في `SKILL.md`.
2. انسخ مجلد المهارة كاملًا إلى موقع المهارات الذي يدعمه إصدار Codex لديك.
3. افتح جلسة جديدة عند الحاجة، واستدعِ المهارة باسم حقل `name` في ملفها.

**مثال لتثبيت مهارة واحدة على مستوى مشروع:**

```bash
# من جذر مشروعك؛ استبدل المسار بموقع هذه المكتبة.
mkdir -p .agents/skills
cp -Rn /path/to/codex-skills/skills/assess-patch-risk .agents/skills/
```

ثم اطلب في Codex:

```text
$assess-patch-risk قيّم مخاطر ملف التغييرات الذي سأحدده لك.
```

المثال ينسخ الملفات فقط. تشغيل المهارة يتطلب توفير اعتمادياتها الأصلية؛ راجع [دليل الاستخدام](docs/USAGE.md) للتفاصيل.

## تنظيم المستودع

```text
codex-skills/
├── README.md                 # الفهرس ونقطة البداية
├── CONTRIBUTING.md           # قواعد الحفاظ على المصادر
├── IMPORT-MANIFEST.json      # المصادر وبصمات SHA-256
├── IMPORT-REPORT.md          # نتائج الفحص والموارد غير المتاحة
├── docs/
│   └── USAGE.md              # التثبيت والاستخدام والتحقق
└── skills/
    └── <skill-name>/
        ├── SKILL.md          # التعليمات الأصلية
        ├── references/       # مراجع متاحة، حيث توجد
        ├── scripts/          # سكربتات متاحة، حيث توجد
        └── specifications/   # مواصفات متاحة، حيث توجد
```

## المصادر والتحقق

| الوثيقة | ما الذي توضّحه؟ |
| :--- | :--- |
| [سجل المصادر](IMPORT-MANIFEST.json) | مصدر كل ملف مستورد، بصمته، ومحاولات القراءة الفاشلة |
| [تقرير الاستيراد](IMPORT-REPORT.md) | مطابقة المحتوى، فحص البيانات الحساسة، والاعتماديات المفقودة |
| [دليل الاستخدام](docs/USAGE.md) | طريقة التثبيت والاستدعاء والتحقق من الملفات |
| [دليل المساهمة](CONTRIBUTING.md) | الحفاظ على المحتوى الأصلي ومراجعة التغييرات |

الملفات الأصلية داخل `skills/` محفوظة دون تحرير. أوصاف الفهرس إرشادية؛ المرجع الكامل لسلوك كل مهارة هو ملفها `SKILL.md`.
