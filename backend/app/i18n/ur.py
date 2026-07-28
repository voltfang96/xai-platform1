"""Urdu (اردو) - Perso-Arabic, right-to-left."""

META = {
    "code": "ur", "name_native": "اردو", "name_en": "Urdu",
    "script": "Perso-Arabic", "rtl": True, "scheduled": True,
    "review_status": "verified",
}

FEATURES = {
    "annual_income": "سالانہ آمدنی", "credit_history_months": "قرض کی تاریخ (مہینے)",
    "existing_loans": "موجودہ قرضے", "loan_amount_requested": "درخواست کردہ قرض کی رقم",
    "employment_years": "ملازمت کی مدت (سال)", "monthly_expenses": "ماہانہ اخراجات",
    "age": "عمر", "defaults_in_past": "ماضی کی نادہندگی",
    "bmi": "جسمانی وزن اشاریہ", "smoking_status": "تمباکو نوشی کی حالت",
    "pre_existing_conditions": "پہلے سے موجود بیماریاں",
    "family_history_score": "خاندانی تاریخ اسکور", "occupation_risk": "پیشہ ورانہ خطرہ",
    "coverage_amount": "بیمہ کوریج کی رقم", "symptoms_severity": "علامات کی شدت",
    "lab_results_abnormal": "غیر معمولی لیبارٹری نتائج",
    "medical_history_score": "طبی تاریخ اسکور",
    "vitals_risk_score": "حیاتی علامات خطرہ اسکور", "treatment_urgency": "علاج کی فوری ضرورت",
}

DECISIONS = {
    "APPROVED": "منظور", "REJECTED": "مسترد", "REVIEW_REQUIRED": "جائزہ درکار",
    "STANDARD_PREMIUM": "معیاری پریمیم", "LOADED_PREMIUM": "اضافی پریمیم",
    "DECLINED": "انکار", "HIGH_RISK_INTERVENTION": "زیادہ خطرہ - مداخلت",
    "MODERATE_RISK_MONITORING": "درمیانہ خطرہ - نگرانی",
    "LOW_RISK_ROUTINE": "کم خطرہ - معمول",
}

EXPLANATION = {
    "positive_high": "{feature} کی زیادہ قیمت ({value}) نے فیصلے کو سازگار رخ دیا",
    "positive_low": "{feature} نے فیصلے میں معمولی سازگار حصہ ڈالا",
    "negative_high": "{feature} کی قیمت ({value}) نے فیصلے کو ناسازگار رخ دیا",
    "negative_low": "{feature} نے فیصلے میں معمولی ناسازگار حصہ ڈالا",
}

SUMMARY = {
    "credit_approved": "قرض کی درخواست منظور ہوئی۔ بنیادی عوامل: {factors}",
    "credit_rejected": "قرض کی درخواست مسترد ہوئی۔ بنیادی وجوہات: {factors}",
    "credit_review": "قرض کی درخواست جائزے کے لیے بھیجی گئی۔ زیرِ غور عوامل: {factors}",
    "insurance_standard": "معیاری پریمیم لاگو۔ تشخیصی عوامل: {factors}",
    "insurance_loaded": "اضافی پریمیم لاگو۔ خطرے کے عوامل: {factors}",
    "insurance_declined": "بیمہ کی درخواست مسترد۔ خطرے کے عوامل: {factors}",
    "health_high": "زیادہ خطرہ - فوری مداخلت کی سفارش۔ عوامل: {factors}",
    "health_moderate": "درمیانہ خطرہ - باقاعدہ نگرانی کی سفارش۔ عوامل: {factors}",
    "health_low": "کم خطرہ - معمول کی پیروی۔ عوامل: {factors}",
}

REPORT = {
    "title": "ضابطہ جاتی تعمیل رپورٹ", "report_id": "رپورٹ شناخت",
    "generated_at": "تیاری کا وقت", "regulator": "ضابطہ کار", "domain": "شعبہ",
    "model_version": "ماڈل ورژن", "algorithm": "الگورتھم",
    "explanation_method": "وضاحت کا طریقہ", "decision": "فیصلہ",
    "confidence": "اعتماد کی سطح", "risk_score": "خطرہ اسکور",
    "audit_id": "آڈٹ ٹریل شناخت",
    "guidelines_heading": "قابلِ اطلاق ہدایات", "checks_heading": "تعمیل جانچ",
    "requirements_heading": "ضابطہ جاتی تقاضے", "recommendations_heading": "سفارشات",
    "explainability_heading": "وضاحت پذیری رپورٹ",
    "top_factors": "بنیادی معاون عوامل", "features_explained": "وضاحت شدہ خصوصیات",
    "explanation_language": "وضاحت کی زبان",
    "compliance_note": "یہ وضاحت {regulator} کی مصنوعی ذہانت وضاحت پذیری ہدایات کے مطابق تیار کی گئی ہے",
    "disclaimer": "یہ رپورٹ {framework} کی ہدایات کی پابندی کی دستاویز ہے۔ حتمی تعمیل کا تعین نامزد تعمیل افسر کی ذمہ داری ہے۔",
    "translation_notice": "یہ رپورٹ {language} میں مشینی ترجمہ شدہ ہے۔ ضابطہ جاتی جمع آوری کے لیے انگریزی متن معتبر ہے۔",
}

STATUS = {
    "COMPLIANT": "تعمیل شدہ", "REVIEW_NEEDED": "جائزہ درکار",
    "PASS": "کامیاب", "FAIL": "ناکام", "REVIEW": "جائزہ",
}

DOMAINS = {
    "credit_scoring": "قرض کی تشخیص", "insurance_underwriting": "بیمہ انڈر رائٹنگ",
    "healthcare": "صحت خطرہ تشخیص",
}

REGULATORS = {
    "RBI": "ریزرو بینک آف انڈیا",
    "IRDAI": "بھارتی بیمہ ضابطہ کار و ترقیاتی ادارہ",
    "SEBI": "بھارتی سیکیورٹیز اینڈ ایکسچینج بورڈ",
    "IndiaAI": "انڈیا اے آئی مشن - ذمہ دار مصنوعی ذہانت ڈھانچہ",
}

REQUIREMENT_LABELS = {
    "explainability": "وضاحت پذیری", "transparency": "شفافیت",
    "fairness": "غیر جانبداری", "audit_trail": "آڈٹ ٹریل",
    "grievance_redressal": "شکایت ازالہ", "human_oversight": "انسانی نگرانی",
    "data_privacy": "ڈیٹا رازداری", "model_governance": "ماڈل انتظام",
    "risk_disclosure": "خطرہ افشا", "investor_protection": "سرمایہ کار تحفظ",
    "accountability": "جوابدہی", "privacy": "رازداری",
    "safety": "سلامتی", "inclusivity": "شمولیت",
}

REQUIREMENT_TEXT = {
    "explainability": "خودکار فیصلوں کے ساتھ واضح اور قابلِ فہم وجوہات ہونی چاہئیں",
    "transparency": "فیصلے میں مصنوعی ذہانت کے استعمال کی اطلاع متاثرہ فرد کو دی جانی چاہیے",
    "fairness": "محفوظ اقسام کے تناظر میں ماڈل کی تعصب جانچ ہونی چاہیے",
    "audit_trail": "فیصلوں کا مکمل آڈٹ ٹریل مقررہ مدت تک محفوظ رکھا جانا چاہیے",
    "grievance_redressal": "خودکار فیصلے کو چیلنج کرنے کا واضح طریقہ ہونا چاہیے",
    "human_oversight": "مقررہ حد سے زائد فیصلوں کا انسانی جائزہ لازم ہے",
    "data_privacy": "ذاتی ڈیٹا کا انتظام ڈی پی ڈی پی ایکٹ 2023 کے مطابق ہونا چاہیے",
    "model_governance": "ماڈلز کی وقتاً فوقتاً توثیق اور دوبارہ توثیق ہونی چاہیے",
    "risk_disclosure": "خطرہ تشخیص میں ماڈل کی حدود اور مفروضات ظاہر کیے جانے چاہئیں",
    "investor_protection": "خوردہ سرمایہ کاروں کو سادہ وضاحت ملنی چاہیے",
    "accountability": "فیصلے کے لیے واضح جوابدہی کا سلسلہ درج ہونا چاہیے",
    "privacy": "ڈیٹا پروسیسنگ قابلِ اطلاق رازداری قانون کے مطابق ہونی چاہیے",
    "safety": "فرد یا معاشرے کو ممکنہ نقصان کا جائزہ لیا جانا چاہیے",
    "inclusivity": "وضاحت فرد کی علاقائی زبان میں دستیاب ہونی چاہیے",
}

CHECKS = {
    "feature_explanation_provided": ("خصوصیت کی وضاحت فراہم", "حصہ ڈالنے والی ہر خصوصیت اہمیت اسکور کے ساتھ درج ہے"),
    "bias_metrics_documented": ("تعصب پیمانے درج", "تعصب جانچ کے پیمانے درج ہیں اور قابلِ قبول حد میں ہیں"),
    "model_version_tracked": ("ماڈل ورژن درج", "فیصلے کے ساتھ ماڈل ورژن اور توثیقی حالت درج ہے"),
    "decision_rationale_clear": ("فیصلے کی دلیل واضح", "دلیل ایسی زبان میں ہے جو غیر ماہر بھی سمجھ سکے"),
    "customer_notification_ready": ("گاہک اطلاع تیار", "منتخب زبان میں گاہک کے لیے وضاحت دستیاب ہے"),
    "audit_trail_complete": ("آڈٹ ٹریل مکمل", "منفرد شناخت والا ٹریل معائنے کے لیے محفوظ ہے"),
    "underwriting_factors_disclosed": ("انڈر رائٹنگ عوامل افشا", "انڈر رائٹنگ نتیجے پر اثر انداز تمام عوامل ظاہر ہیں"),
    "premium_rationale_clear": ("پریمیم کی بنیاد واضح", "پریمیم اضافے کی بنیاد واضح طور پر بیان کی گئی ہے"),
    "no_genetic_discrimination": ("جینیاتی امتیاز نہیں", "فیصلے میں کوئی جینیاتی معلومات استعمال نہیں ہوئی"),
    "data_privacy_compliant": ("ڈیٹا رازداری تعمیل", "ذاتی ڈیٹا کا انتظام ڈی پی ڈی پی ایکٹ 2023 کی پیروی کرتا ہے"),
    "policyholder_notification": ("بیمہ دار اطلاع", "مصنوعی ذہانت معاون تشخیص کی اطلاع تیار ہے"),
    "model_validation_current": ("ماڈل توثیق حالیہ", "ماڈل اپنی مقررہ توثیقی مدت میں ہے"),
    "risk_factors_explained": ("خطرہ عوامل بیان شدہ", "تشخیص پر اثر انداز ہر خطرہ عامل بیان کیا گیا ہے"),
    "model_limitations_disclosed": ("ماڈل حدود افشا", "ماڈل کی معلوم حدود اور مفروضات بیان کیے گئے ہیں"),
    "no_market_manipulation": ("مارکیٹ ہیرا پھیری نہیں", "فیصلے کی منطق میں کوئی ہیرا پھیری کا رجحان نہیں ملا"),
    "stress_test_documented": ("دباؤ جانچ درج", "ناسازگار حالات میں طرزِ عمل درج ہے"),
    "investor_notification": ("سرمایہ کار اطلاع", "مصنوعی ذہانت معاون تشخیص کی اطلاع تیار ہے"),
    "audit_trail_maintained": ("آڈٹ ٹریل برقرار", "ضابطہ جاتی معائنے کے لیے مکمل ٹریل برقرار ہے"),
    "explanation_human_readable": ("وضاحت انسانی پڑھنے کے قابل", "وضاحت سادہ، انسانی پڑھنے کے قابل شکل میں ہے"),
    "multilingual_support": ("کثیر لسانی معاونت", "وضاحت آٹھویں شیڈول کی زبانوں میں دستیاب ہے"),
    "bias_testing_done": ("تعصب جانچ مکمل", "محفوظ اقسام میں تعصب جانچ مکمل ہو چکی ہے"),
    "accountability_assigned": ("جوابدہی متعین", "اس فیصلے کے لیے ذمہ دار فرد درج ہے"),
    "privacy_compliant": ("رازداری تعمیل", "پروسیسنگ قابلِ اطلاق رازداری قانون کے مطابق ہے"),
    "safety_assessed": ("سلامتی جانچی گئی", "سلامتی جانچ مکمل، کوئی نقصان شناخت نہیں ہوا"),
    "inclusive_design": ("شمولیتی ڈیزائن", "علاقائی زبان تک رسائی ڈیزائن میں ہی فراہم ہے"),
}

RECOMMENDATIONS = {
    "all_passed": "تمام تعمیل جانچ کامیاب۔ موجودہ کنٹرول برقرار رکھیں۔",
    "schedule_review": "{regulator} کے وقتی جائزے کے تقاضوں کے مطابق اگلا جائزہ مقرر کریں۔",
    "revalidate": "انتظامی نظام الاوقات کے مطابق ماڈل کی وقتی دوبارہ توثیق یقینی بنائیں۔",
    "retain_logs": "وضاحتی ریکارڈ مقررہ ضابطہ جاتی مدت تک محفوظ رکھیں۔",
    "address_failed": "ناکام جانچ کا حل کریں: {check}",
}

UI = {
    "app_title": "ایکس اے آئی پلیٹ فارم",
    "app_subtitle": "ضابطہ بند صنعتوں کے لیے کثیر لسانی وضاحت پذیر مصنوعی ذہانت",
    "select_domain": "فیصلہ شعبہ منتخب کریں", "input_params": "ان پٹ پیرامیٹر",
    "load_sample": "نمونہ ڈیٹا بھریں", "language_label": "وضاحت کی زبان",
    "generate_btn": "وضاحت بنائیں", "generating": "بن رہی ہے...",
    "decision_label": "فیصلہ", "confidence_label": "اعتماد",
    "risk_label": "خطرہ اسکور", "audit_label": "آڈٹ شناخت",
    "explanation_heading": "مصنوعی ذہانت فیصلہ اور وضاحت",
    "contributions_heading": "خصوصیات کا حصہ", "summary_heading": "وضاحت کا خلاصہ",
    "report_btn": "تعمیل رپورٹ بنائیں", "report_generating": "رپورٹ بن رہی ہے...",
    "coverage_label": "ترجمے کا احاطہ", "needs_review_badge": "مادری زبان جائزہ درکار",
    "footer_note": "آٹھویں شیڈول کی 22 زبانوں کی معاونت | آڈٹ کے قابل وضاحتیں",
    "yes": "ہاں", "no": "نہیں",
}
