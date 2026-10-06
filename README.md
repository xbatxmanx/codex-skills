<div align="center">

# Codex Skills

**مكتبة مهارات منظّمة لـ Codex · A curated Codex skill library**

الأمان · البيانات · الاستثمار · الأفكار · البيئة السحابية

Security · Data · Public equities · Ideas · Cloud environment

![Skills](https://img.shields.io/badge/skills-33-2563eb?style=flat-square)
![Supporting files](https://img.shields.io/badge/supporting_files-42-0f766e?style=flat-square)
![Languages](https://img.shields.io/badge/docs-Arabic_%2B_English-7c3aed?style=flat-square)
![Content](https://img.shields.io/badge/original_content-preserved-475569?style=flat-square)

[المهارات / Catalog](#catalog) · [البداية / Quick start](#quick-start) · [دليل الاستخدام / Usage guide](docs/USAGE.md) · [تقرير الاستيراد / Import report](IMPORT-REPORT.md)

</div>

---

**العربية:** مكتبة تضم 33 مهارة و41 ملفًا مساعدًا أصليًا، بالإضافة إلى ملف اختبارات مساعد جديد، مع شرح عربي وإنجليزي مستقل لكل مهارة. النصوص الأصلية محفوظة دون تغيير؛ اختر المجال، واقرأ الشرح، ثم راجع التعليمات الأصلية.

**English:** A library of 33 skills and 41 original supporting files, plus one newly authored test supplement, with a separate Arabic and English guide for every skill. Original content is preserved. Choose a category, read its guide, then consult the original instructions.

> **حالة النسخة / Archive status:** بعض المراجع المشتركة وأدوات التشغيل غير مرفقة؛ راجع تقرير الاستيراد قبل الاستخدام. / Some shared references and runtime tools are not bundled; review the import report before use.

<a id="catalog"></a>

## فهرس المهارات / Skill catalog

| المجال / Category | العدد / Count | المجال / Scope |
| :--- | :---: | :--- |
| [الأمان / Security](#security) | 15 | الفحص والإصلاح والتحقق / Audit, remediation, verification |
| [البيانات / Data analytics](#data) | 15 | التحليل والتقارير واللوحات / Analysis, reports, dashboards |
| [الاستثمار / Public equities](#investing) | 1 | بحث الأسهم المدرجة / Listed-company research |
| [الأفكار / Idea evaluation](#ideas) | 1 | مجلس لتقييم المشروعات / Business idea council |
| [البيئة / Cloud environment](#environment) | 1 | الإعداد والتحقق / Setup and readiness |

<a id="security"></a>

### الأمان / Security

| المهارة / Skill | الشرح بالعربية | English overview | الروابط / Links |
| :--- | :--- | :--- | :--- |
| `assess-patch-risk` | تقييم أثر تعديل ثابت على سلوك البرنامج ومخاطر الانحدار وإمكانية الدمج. | Assess an immutable patch’s runtime impact, regression risk, and merge eligibility. | [الشرح / Guide](docs/skills/assess-patch-risk.md) · [SKILL.md](skills/assess-patch-risk/SKILL.md) |
| `attack-path-analysis` | تتبّع نتيجة أمنية محددة من مدخل المهاجم إلى الأثر مع معايرة الشدة. | Trace a specific security finding from attacker-controlled input to impact and calibrate severity. | [الشرح / Guide](docs/skills/attack-path-analysis.md) · [SKILL.md](skills/attack-path-analysis/SKILL.md) |
| `deep-security-scan` | تنفيذ جولات مستقلة من فحص المستودع لتقليل احتمال تفويت ثغرات. | Run independent repository audits to reduce missed findings. | [الشرح / Guide](docs/skills/deep-security-scan.md) · [SKILL.md](skills/deep-security-scan/SKILL.md) |
| `define-security-policy` | صياغة أو مراجعة SECURITY.md لتحديد الحدود الأمنية وما يستحق المراجعة. | Define or review SECURITY.md to establish security boundaries and review scope. | [الشرح / Guide](docs/skills/define-security-policy.md) · [SKILL.md](skills/define-security-policy/SKILL.md) |
| `finding-discovery` | اكتشاف مشكلات أمنية محتملة كمرحلة متخصصة أو عند طلبها صراحة. | Discover candidate security issues as a dedicated phase or explicit task. | [الشرح / Guide](docs/skills/finding-discovery.md) · [SKILL.md](skills/finding-discovery/SKILL.md) |
| `fix-finding` | إصلاح ثغرة محددة مع التحقق من المعالجة وتأثيرها على السلوك. | Remediate a specific vulnerability and check the fix’s behavior. | [الشرح / Guide](docs/skills/fix-finding.md) · [SKILL.md](skills/fix-finding/SKILL.md) |
| `propose-security-hardening` | اقتراح حلول بنيوية تعالج الأسباب المشتركة بدل الاكتفاء بإصلاح منفرد. | Propose structural improvements addressing systemic security causes. | [الشرح / Guide](docs/skills/propose-security-hardening.md) · [SKILL.md](skills/propose-security-hardening/SKILL.md) |
| `security-diff-scan` | مراجعة التغييرات في PR أو commit أو فرع أو ملفات العمل بحثًا عن ثغرات. | Review a PR, commit, branch diff, or working-tree patch for vulnerabilities. | [الشرح / Guide](docs/skills/security-diff-scan.md) · [SKILL.md](skills/security-diff-scan/SKILL.md) |
| `security-scan` | فحص أمني مرة واحدة لمستودع أو نطاق محدد دون فرق تغييرات. | Run a single-pass security audit of a repository or scoped paths without a diff. | [الشرح / Guide](docs/skills/security-scan.md) · [SKILL.md](skills/security-scan/SKILL.md) |
| `threat-model` | توضيح الأصول والمهاجمين وحدود الثقة ومسارات التهديد استنادًا إلى المصدر. | Model assets, attackers, trust boundaries, and threats from source evidence. | [الشرح / Guide](docs/skills/threat-model.md) · [SKILL.md](skills/threat-model/SKILL.md) |
| `track-findings` | تحويل نتائج أمنية مختارة إلى سجلات في أدوات التتبع مع منع التكرار. | Track selected security findings with duplicate checks and reviewed writes. | [الشرح / Guide](docs/skills/track-findings.md) · [SKILL.md](skills/track-findings/SKILL.md) |
| `triage-finding` | تقييم أثر تقرير أمني وارد على المستودع بتحليل ثابت. | Assess a supplied security report’s repository impact through static analysis. | [الشرح / Guide](docs/skills/triage-finding.md) · [SKILL.md](skills/triage-finding/SKILL.md) |
| `validation` | تحديد ما إذا كانت نتيجة أمنية محتملة صحيحة اعتمادًا على الأدلة. | Determine whether a candidate security finding is valid. | [الشرح / Guide](docs/skills/validation.md) · [SKILL.md](skills/validation/SKILL.md) |
| `verify-fix` | التحقق عند الطلب من أن إصلاحًا موجودًا يعالج ثغرة معروفة. | Verify on request that an existing fix remediates a reported vulnerability. | [الشرح / Guide](docs/skills/verify-fix.md) · [SKILL.md](skills/verify-fix/SKILL.md) |
| `vulnerability-writeup` | تحويل الملاحظات والأدلة إلى تقرير ثغرة واضح وقابل للمراجعة. | Turn vulnerability notes and evidence into a clear, reviewable report. | [الشرح / Guide](docs/skills/vulnerability-writeup.md) · [SKILL.md](skills/vulnerability-writeup/SKILL.md) |

<a id="data"></a>

### تحليل البيانات / Data analytics

| المهارة / Skill | الشرح بالعربية | English overview | الروابط / Links |
| :--- | :--- | :--- | :--- |
| `analyze-data-quality` | فحص موثوقية البيانات من حيث الحداثة والتكرار والقيم الناقصة والربط. | Investigate freshness, duplicates, missingness, and join quality. | [الشرح / Guide](docs/skills/analyze-data-quality.md) · [SKILL.md](skills/analyze-data-quality/SKILL.md) |
| `build-dashboard` | بناء لوحة تفاعلية تربط المؤشرات والمرئيات بمصادر قابلة للفحص. | Build an interactive dashboard with inspectable source-backed metrics. | [الشرح / Guide](docs/skills/build-dashboard.md) · [SKILL.md](skills/build-dashboard/SKILL.md) |
| `build-report` | تقديم إجابة تحليلية منظمة ومدعومة بالأدلة لجمهور محدد. | Produce a structured, evidence-backed analytical answer for a defined audience. | [الشرح / Guide](docs/skills/build-report.md) · [SKILL.md](skills/build-report/SKILL.md) |
| `create-data-context` | حفظ تعريفات البيانات والتفضيلات والتعليمات ليستفاد منها في تحليلات لاحقة. | Preserve data definitions, preferences, and instructions for future analysis. | [الشرح / Guide](docs/skills/create-data-context.md) · [SKILL.md](skills/create-data-context/SKILL.md) |
| `design-kpis` | اختيار مؤشرات تقيس النجاح مع تعريفات وأهداف وضوابط قياس. | Design success metrics with definitions, targets, and guardrails. | [الشرح / Guide](docs/skills/design-kpis.md) · [SKILL.md](skills/design-kpis/SKILL.md) |
| `gather-business-context` | جمع المعلومات التي تؤثر في تفسير السؤال قبل التحليل. | Gather decision-shaping context before analysis. | [الشرح / Guide](docs/skills/gather-business-context.md) · [SKILL.md](skills/gather-business-context/SKILL.md) |
| `index` | تحديد سير عمل البيانات المناسب للسؤال والنتيجة المطلوبة. | Route data questions to the appropriate analytical workflow. | [الشرح / Guide](docs/skills/index.md) · [SKILL.md](skills/index/SKILL.md) |
| `jupyter-notebooks` | إنشاء أو مراجعة دفاتر SQL وPython توثق التحليل وتسمح بإعادته. | Create or review SQL and Python notebooks for reproducible analysis. | [الشرح / Guide](docs/skills/jupyter-notebooks.md) · [SKILL.md](skills/jupyter-notebooks/SKILL.md) |
| `kpi-reporting` | عرض حالة المؤشرات ومقارنتها بالأهداف مع تفسير الانحرافات المدعومة. | Report metric status against targets and explain validated drivers. | [الشرح / Guide](docs/skills/kpi-reporting.md) · [SKILL.md](skills/kpi-reporting/SKILL.md) |
| `market-sizing` | تقدير حجم السوق أو الفرصة بافتراضات معلنة ومصادر واضحة. | Estimate market or opportunity size with transparent assumptions and sources. | [الشرح / Guide](docs/skills/market-sizing.md) · [SKILL.md](skills/market-sizing/SKILL.md) |
| `metric-diagnostics` | التحقق من أسباب تغير مؤشر أو اختلافه عن المتوقع. | Investigate why a metric changed or differs from expectation. | [الشرح / Guide](docs/skills/metric-diagnostics.md) · [SKILL.md](skills/metric-diagnostics/SKILL.md) |
| `product-business-analysis` | استخدام البيانات لتقييم البدائل ودعم توصية مرتبطة بقرار محدد. | Use data to compare alternatives and support a concrete decision. | [الشرح / Guide](docs/skills/product-business-analysis.md) · [SKILL.md](skills/product-business-analysis/SKILL.md) |
| `publish-artifact-to-sites` | نشر منتج تحليلي موجود عبر أدوات Sites مع التحقق من الحزمة والوصول. | Publish an existing analytical artifact through Sites with packaging and access checks. | [الشرح / Guide](docs/skills/publish-artifact-to-sites.md) · [SKILL.md](skills/publish-artifact-to-sites/SKILL.md) |
| `validate-data` | مراجعة المنهجية والمصادر والحسابات والمرئيات والاستنتاجات. | Review methodology, sources, calculations, visuals, and conclusions. | [الشرح / Guide](docs/skills/validate-data.md) · [SKILL.md](skills/validate-data/SKILL.md) |
| `visualize-data` | تصميم رسوم كمية واضحة والتحقق من المقاييس والسياق والمصدر. | Design clear quantitative charts and verify scales, context, and provenance. | [الشرح / Guide](docs/skills/visualize-data.md) · [SKILL.md](skills/visualize-data/SKILL.md) |

<a id="investing"></a>

### الاستثمار / Public equities

| المهارة / Skill | الشرح بالعربية | English overview | الروابط / Links |
| :--- | :--- | :--- | :--- |
| `public-equity-investing` | توجيه بحث الشركات المدرجة والتقييم والأرباح والأطروحات الاستثمارية. | Route listed-company research, valuation, earnings, and investment thesis work. | [الشرح / Guide](docs/skills/public-equity-investing.md) · [SKILL.md](skills/public-equity-investing/SKILL.md) |

<a id="ideas"></a>

### تقييم الأفكار / Idea evaluation

| المهارة / Skill | الشرح بالعربية | English overview | الروابط / Links |
| :--- | :--- | :--- | :--- |
| `ai-shark-tank-council` | اختبار فكرة مشروع عبر ستة أدوار ورئيس مجلس قبل إصدار قرار مدعوم بالأدلة. | Evaluate a business idea through six roles and a chair before issuing an evidence-backed decision. | [الشرح / Guide](docs/skills/ai-shark-tank-council.md) · [SKILL.md](skills/ai-shark-tank-council/SKILL.md) |

<a id="environment"></a>

### البيئة السحابية / Cloud environment

| المهارة / Skill | الشرح بالعربية | English overview | الروابط / Links |
| :--- | :--- | :--- | :--- |
| `setup` | تجهيز المستودعات وتثبيت المتطلبات والتحقق من سير التطوير وحفظ تعليمات الإعداد. | Prepare repositories, install prerequisites, verify development, and save reusable setup instructions. | [الشرح / Guide](docs/skills/setup.md) · [SKILL.md](skills/setup/SKILL.md) |

<a id="quick-start"></a>

## ابدأ الاستخدام / Quick start

**العربية**

1. اختر المهارة وافتح صفحة شرحها، ثم اقرأ ملف `SKILL.md` ومتطلباته.
2. انسخ مجلد المهارة كاملًا إلى موقع المهارات الذي يدعمه إصدار Codex لديك.
3. افتح جلسة جديدة عند الحاجة، ثم استدعِ الاسم الموجود في حقل `name` باستخدام `$`.

**English**

1. Choose a skill, read its guide, then review `SKILL.md` and its prerequisites.
2. Copy the entire skill folder to a skill location supported by your Codex version.
3. Start a new session if needed and invoke the frontmatter `name` with `$`.

```bash
# من جذر مشروعك؛ عدّل مسار المكتبة.
# From your project root; replace the library path.
mkdir -p .agents/skills
cp -Rn /path/to/codex-skills/skills/ai-shark-tank-council .agents/skills/
```

```text
$ai-shark-tank-council قيّم هذه الفكرة ووضّح الأدلة الناقصة.
$ai-shark-tank-council Evaluate this idea and identify missing evidence.
```

الأمر ينسخ الملفات فقط؛ لا يثبّت الأدوات الخارجية. / This copies files only; it does not install external tools.

## تنظيم المستودع / Repository layout

```text
codex-skills/
├── README.md                   # الفهرس / Catalog
├── CONTRIBUTING.md             # قواعد المساهمة / Contribution rules
├── IMPORT-MANIFEST.json        # المصادر والبصمات / Sources and hashes
├── IMPORT-REPORT.md            # سجل الاستيراد / Import report
├── docs/
│   ├── USAGE.md                # دليل الاستخدام / Usage guide
│   ├── AI-SHARK-TANK-COUNCIL.md # شرح موسّع / Extended guide
│   └── skills/                 # 33 شرحًا ثنائي اللغة / 33 bilingual guides
└── skills/
    └── <skill-name>/
        ├── SKILL.md            # التعليمات الأصلية / Original instructions
        └── ...                 # ملفات مساعدة متاحة / Available supporting files
```

## التوثيق والمصادر / Documentation and provenance

| الوثيقة / Document | الغرض / Purpose |
| :--- | :--- |
| [دليل الاستخدام / Usage](docs/USAGE.md) | التثبيت والتحقق / Installation and verification |
| [AI Shark Tank Council](docs/AI-SHARK-TANK-COUNCIL.md) | الأدوار والدرجات والقرارات / Roles, scoring, decisions |
| [المساهمة / Contributing](CONTRIBUTING.md) | الحفاظ على المصادر / Preserving source content |
| [تقرير الاستيراد / Import report](IMPORT-REPORT.md) | الاعتماديات المفقودة والفحص / Missing dependencies and checks |
| [سجل المصادر / Manifest](IMPORT-MANIFEST.json) | مصادر الملفات وبصماتها / File sources and SHA-256 hashes |

الشرح ثنائي اللغة موجود خارج ملفات المهارات الأصلية. لم تُضف مهارة CEO أو مهارة تعليم الصيدلة. / Bilingual explanations are separate from original skill files. The CEO and pharmacy tutoring skills are not included.


## الجودة والحقوق / Quality and rights

تُفحص مطابقة المصادر والروابط والتوثيق والأيقونات وأنماط البيانات الحساسة بواسطة `Repository validation`. الفحص لا يشغّل سلوك المهارات أو يثبت اكتمال الموارد الخارجية.

`Repository validation` checks source integrity, links, documentation, icons, and sensitive-data patterns. It does not execute skill behavior or certify external dependencies.

- [حالة المستودع / Repository health](docs/REPOSITORY-HEALTH.md)
- [اعتماديات كل مهارة / Skill dependencies](docs/DEPENDENCIES.md)
- [إشعار الحقوق / Rights notice](LICENSE)

**لا يوجد ترخيص إعادة استخدام عام:** ملفات المصدر خاضعة لحقوق أصحابها، والتوثيق والأدوات الجديدة لا تمنح إذنًا مفتوحًا. / **No blanket reuse license:** source files remain subject to their owners’ rights, and no open reuse permission is granted for newly authored documentation or tools.
