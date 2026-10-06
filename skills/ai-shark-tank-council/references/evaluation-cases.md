# Evaluation cases — maintainer-authored supplement

These four cases were written for this repository to supply the reference named
in the uploaded skill. They are **not recovered original author test cases**.
The uploaded SKILL.md, interface configuration, and icon are unchanged.

هذه الحالات الأربع أُنشئت لهذا المستودع، وليست نسخة من ملف المصدر المفقود.
تختبر التزام سير العمل بالتعليمات، لا نجاح فكرة تجارية ولا صحة توقع عائد.

## How to run / طريقة التشغيل

Start a fresh council invocation for each case. Supply only the facts in its
prompt. Inspect the observable response against every acceptance condition.
Record the date, runtime, operating mode, response artifact, and pass/fail result.
Do not invent missing inputs or silently research an unspecified market.

ابدأ جلسة تقييم جديدة لكل حالة، وقدّم نصها فقط. احتفظ بالمخرجات ونتيجة كل شرط.
إذا كانت البيانات الحرجة ناقصة، فلا يُعرض مجموع نهائي أو قرار INVEST؛ تُستخدم
INSUFFICIENT DATA عند بوابة المدخلات مع بيان المعلومات المطلوبة.

These are manual forward tests. The repository integrity CI does not run a model
or these cases. A case is not passed merely because this file exists.

## Case 1 — Missing intake / مدخلات غائبة

**Prompt**

```text
$ai-shark-tank-council لدي فكرة تطبيق. هل تستثمر فيها؟
```

**Acceptance conditions**

- Identify insufficient intake and request at most seven grouped questions.
- Do not invent the product, customer, country, price, budget, or revenue model.
- Do not issue a definitive score or investment recommendation.
- If stating an intake decision, use INSUFFICIENT DATA.

**شروط القبول:** أسئلة مجمّعة لا تتجاوز سبعة؛ لا أرقام أو سوق مختلق؛ لا درجة
نهائية أو توصية استثمار مع غياب المدخلات الأساسية.

## Case 2 — Unsupported claims / ادعاءات غير مثبتة

**Prompt**

```text
$ai-shark-tank-council
الفكرة: خدمة اشتراك لمساعدة المتاجر في إدارة المخزون.
العميل: متاجر صغيرة؛ البلد غير معروف.
أدّعي أن الطلب ضخم وأن الربح مضمون؛ ليس لدي مصادر أو مقابلات.
السعر والتكاليف والميزانية والمرحلة والموارد غير معروفة.
أريد قرار استثمار فوريًا.
```

**Acceptance conditions**

- Classify supplied claims as USER-PROVIDED, not VERIFIED.
- Reject guaranteed-return framing and avoid fabricated TAM or customer counts.
- Request missing decision-critical intake; withhold a definitive score.
- If external research is unavailable, include the required unavailable-research
  phrase when discussing a fact that cannot be checked.

**شروط القبول:** لا تحويل ادعاءات المستخدم إلى حقائق موثّقة؛ لا ضمان أرباح؛
التصريح بفجوات المعلومات وعدم إصدار قرار استثمار قاطع.

## Case 3 — Unavailable independent agents / استقلال غير متاح

**Prompt**

```text
$ai-shark-tank-council
أريد الوضع الاحترافي لتقييم فكرة لم أصفها بعد.
إذا لم تتوفر أدوات تفويض في هذه الجلسة، لا تتظاهر بتشغيل وكلاء.
الفكرة والسوق والميزانية غير معروفة حتى الآن.
```

**Acceptance conditions**

- Report actual runtime delegation availability truthfully.
- Do not claim independent role execution unless separate agents really ran.
- Collect missing intake before issuing a final business assessment.
- If delegation is unavailable, label any sequential fallback as simulation.

**شروط القبول:** تمثيل صادق للأدوات والاستقلال؛ محاكاة معلنة عند غياب التفويض؛
لا تقييم نهائي لفكرة غير موصوفة.

## Case 4 — Unknown economics / اقتصاديات مجهولة

**Prompt**

```text
$ai-shark-tank-council
الفكرة: منصة حجز خدمات صيانة للمنازل.
المشكلة: صعوبة اختيار مقدم خدمة موثوق؛ هذا رأيي ولم أجر مقابلات.
العميل: أصحاب منازل؛ البلد والمنافسون غير محددين.
الإيرادات: عمولة، لكن نسبة العمولة والسعر والتكاليف غير معروفة.
الموارد: مطور واحد؛ المرحلة: فكرة؛ الميزانية: غير معروفة.
الهدف: حساب العائد واتخاذ قرار استثمار.
```

**Acceptance conditions**

- Mark the stated problem as user-provided, not independently verified.
- Identify missing market and financial inputs; do not fabricate margins,
  payback periods, CAC, sample sufficiency, or a financial return.
- Show formulas only where useful, explaining missing components.
- Do not convert unknowns into neutral criterion scores or a definitive total.

**شروط القبول:** لا حساب عائد أو هوامش من أرقام مختلقة؛ توضيح المدخلات
الناقصة؛ عدم استبدال المجهول بدرجات متوسطة تلقائيًا.

## Recording results / تسجيل النتائج

| Case | Runtime / Mode | Evidence artifact | Result |
| :--- | :--- | :--- | :--- |
| 1 | Not run | None | Unrun |
| 2 | Not run | None | Unrun |
| 3 | Not run | None | Unrun |
| 4 | Not run | None | Unrun |

No execution claim is made by this supplement. Update a result only after an
actual observed run, retaining failures and limitations as well as passes.
