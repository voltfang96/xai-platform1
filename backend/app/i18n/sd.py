"""Sindhi (سنڌي) - Perso-Arabic, right-to-left.

Core catalog. REQUIREMENT_TEXT and CHECKS fall back to English; see coverage.
"""

META = {
    "code": "sd", "name_native": "سنڌي", "name_en": "Sindhi",
    "script": "Perso-Arabic", "rtl": True, "scheduled": True,
    "review_status": "needs_native_review",
}

FEATURES = {
    "annual_income": "سالياني آمدني", "credit_history_months": "قرض جي تاريخ (مهينا)",
    "existing_loans": "موجود قرض", "loan_amount_requested": "درخواست ڪيل قرض جي رقم",
    "employment_years": "نوڪري جو عرصو (سال)", "monthly_expenses": "مهيني جو خرچ",
    "age": "عمر", "defaults_in_past": "اڳوڻيون ڪوتاهيون",
    "bmi": "جسماني وزن اشاريو", "smoking_status": "تماڪ نوشي جي حالت",
    "pre_existing_conditions": "اڳ ۾ موجود بيماريون",
    "family_history_score": "خانداني تاريخ اسڪور", "occupation_risk": "پيشيوراڻو خطرو",
    "coverage_amount": "بيمہ ڪوريج رقم", "symptoms_severity": "علامتن جي شدت",
    "lab_results_abnormal": "غير معمولي ليبارٽري نتيجا",
    "medical_history_score": "طبي تاريخ اسڪور",
    "vitals_risk_score": "حياتي علامتن جو خطرو اسڪور", "treatment_urgency": "علاج جي فوري ضرورت",
}

DECISIONS = {
    "APPROVED": "منظور", "REJECTED": "رد", "REVIEW_REQUIRED": "جائزو ضروري",
    "STANDARD_PREMIUM": "معياري پريميم", "LOADED_PREMIUM": "وڌيڪ پريميم",
    "DECLINED": "انڪار", "HIGH_RISK_INTERVENTION": "وڌيڪ خطرو - مداخلت",
    "MODERATE_RISK_MONITORING": "وچولو خطرو - نگراني",
    "LOW_RISK_ROUTINE": "گھٽ خطرو - عام",
}

EXPLANATION = {
    "positive_high": "{feature} جي وڌيڪ قيمت ({value}) فيصلي کي سازگار رخ ڏنو",
    "positive_low": "{feature} فيصلي ۾ ٿورو سازگار حصو ڏنو",
    "negative_high": "{feature} جي قيمت ({value}) فيصلي کي ناسازگار رخ ڏنو",
    "negative_low": "{feature} فيصلي ۾ ٿورو ناسازگار حصو ڏنو",
}

SUMMARY = {
    "credit_approved": "قرض جي درخواست منظور ٿي. بنيادي عنصر: {factors}",
    "credit_rejected": "قرض جي درخواست رد ٿي. بنيادي سبب: {factors}",
    "credit_review": "قرض جي درخواست جائزي لاءِ موڪلي وئي. غور ھيٺ عنصر: {factors}",
    "insurance_standard": "معياري پريميم لاڳو. تشخيصي عنصر: {factors}",
    "insurance_loaded": "وڌيڪ پريميم لاڳو. خطري جا عنصر: {factors}",
    "insurance_declined": "بيمہ جي درخواست رد. خطري جا عنصر: {factors}",
    "health_high": "وڌيڪ خطرو - فوري مداخلت جي سفارش. عنصر: {factors}",
    "health_moderate": "وچولو خطرو - باقاعده نگراني جي سفارش. عنصر: {factors}",
    "health_low": "گھٽ خطرو - عام پيروي. عنصر: {factors}",
}

REPORT = {
    "title": "ضابطي جي تعميل جي رپورٽ", "report_id": "رپورٽ سڃاڻپ",
    "generated_at": "تياري جو وقت", "regulator": "ضابطي وارو", "domain": "شعبو",
    "model_version": "ماڊل ورجن", "algorithm": "الگورٿم",
    "explanation_method": "وضاحت جو طريقو", "decision": "فيصلو",
    "confidence": "اعتماد جي سطح", "risk_score": "خطرو اسڪور",
    "audit_id": "آڊٽ ٽريل سڃاڻپ",
    "guidelines_heading": "لاڳو ھدايتون", "checks_heading": "تعميل جاچ",
    "requirements_heading": "ضابطي جا تقاضا", "recommendations_heading": "سفارشون",
    "explainability_heading": "وضاحت پذيري رپورٽ",
    "top_factors": "بنيادي مددگار عنصر", "features_explained": "وضاحت ڪيل خاصيتون",
    "explanation_language": "وضاحت جي ٻولي",
    "compliance_note": "ھي وضاحت {regulator} جي مصنوعي ذھانت وضاحت پذيري ھدايتن مطابق تيار ڪئي وئي آھي",
    "disclaimer": "ھي رپورٽ {framework} جي ھدايتن جي پيروي جو دستاويز آھي. آخري تعميل جو تعين نامزد تعميل آفيسر جي ذميواري آھي.",
    "translation_notice": "ھي رپورٽ {language} ۾ مشيني ترجمو ٿيل آھي. ضابطي جي جمع ڪرائڻ لاءِ انگريزي متن معتبر آھي.",
}

STATUS = {
    "COMPLIANT": "تعميل ٿيل", "REVIEW_NEEDED": "جائزو ضروري",
    "PASS": "ڪامياب", "FAIL": "ناڪام", "REVIEW": "جائزو",
}

DOMAINS = {
    "credit_scoring": "قرض جي تشخيص", "insurance_underwriting": "بيمہ انڊر رائٽنگ",
    "healthcare": "صحت جي خطري جي تشخيص",
}

REGULATORS = {
    "RBI": "ريزرو بينڪ آف انڊيا",
    "IRDAI": "ڀارتي بيمہ ضابطي ۽ ترقياتي اداره",
    "SEBI": "ڀارتي سيڪيورٽيز ۽ ايڪسچينج بورڊ",
    "IndiaAI": "انڊيا اي آءِ مشن - ذميوار مصنوعي ذھانت جو ڍانچو",
}

REQUIREMENT_LABELS = {
    "explainability": "وضاحت پذيري", "transparency": "شفافيت",
    "fairness": "غير جانبداري", "audit_trail": "آڊٽ ٽريل",
    "grievance_redressal": "شڪايت جو ازالو", "human_oversight": "انساني نگراني",
    "data_privacy": "ڊيٽا رازداري", "model_governance": "ماڊل انتظام",
    "risk_disclosure": "خطري جو ظاهر ڪرڻ", "investor_protection": "سيڙپڪار جي حفاظت",
    "accountability": "جوابدهي", "privacy": "رازداري",
    "safety": "سلامتي", "inclusivity": "شموليت",
}

RECOMMENDATIONS = {
    "all_passed": "سڀ تعميل جاچ ڪامياب. موجوده ڪنٽرول برقرار رکو.",
    "schedule_review": "{regulator} جي وقتي جائزي جي تقاضن مطابق ايندڙ جائزو مقرر ڪريو.",
    "revalidate": "انتظامي نظام الاوقات مطابق ماڊل جي وقتي ٻيهر تصديق يقيني بڻايو.",
    "retain_logs": "وضاحتي رڪارڊ مقرر ڪيل ضابطي جي مدت تائين محفوظ رکو.",
    "address_failed": "ناڪام جاچ جو حل ڪريو: {check}",
}

UI = {
    "app_title": "ايڪس اي آءِ پليٽ فارم",
    "app_subtitle": "ضابطي ھيٺ صنعتن لاءِ گھڻ ٻوليائي وضاحت پذير مصنوعي ذھانت",
    "select_domain": "فيصلي جو شعبو چونڊيو", "input_params": "ان پُٽ پيرا ميٽر",
    "load_sample": "نمونو ڊيٽا ڀريو", "language_label": "وضاحت جي ٻولي",
    "generate_btn": "وضاحت تيار ڪريو", "generating": "تيار ٿي رهي آهي...",
    "decision_label": "فيصلو", "confidence_label": "اعتماد",
    "risk_label": "خطرو اسڪور", "audit_label": "آڊٽ سڃاڻپ",
    "explanation_heading": "مصنوعي ذھانت جو فيصلو ۽ وضاحت",
    "contributions_heading": "خاصيتن جو حصو", "summary_heading": "وضاحت جو خلاصو",
    "report_btn": "تعميل رپورٽ تيار ڪريو", "report_generating": "رپورٽ تيار ٿي رهي آهي...",
    "coverage_label": "ترجمي جو احاطو", "needs_review_badge": "مادري ٻولي جو جائزو ضروري",
    "footer_note": "اٺين شيڊول جي 22 ٻولين جي مدد | آڊٽ لائق وضاحتون",
    "yes": "ها", "no": "نه",
}
