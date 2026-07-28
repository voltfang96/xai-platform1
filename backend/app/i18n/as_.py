"""Assamese (অসমীয়া) - Bengali-Assamese script.

Core catalog: explanation output, report labels/statuses and UI are translated.
REQUIREMENT_TEXT and CHECKS evidence lines fall back to English; see coverage.
"""

META = {
    "code": "as", "name_native": "অসমীয়া", "name_en": "Assamese",
    "script": "Bengali-Assamese", "rtl": False, "scheduled": True,
    "review_status": "needs_native_review",
}

FEATURES = {
    "annual_income": "বাৰ্ষিক আয়", "credit_history_months": "ঋণ ইতিহাস (মাহ)",
    "existing_loans": "বৰ্তমানৰ ঋণ", "loan_amount_requested": "অনুৰোধ কৰা ঋণৰ পৰিমাণ",
    "employment_years": "নিয়োগ কাল (বছৰ)", "monthly_expenses": "মাহেকীয়া ব্যয়",
    "age": "বয়স", "defaults_in_past": "পূৰ্বৰ ঋণ খেলাপ",
    "bmi": "শৰীৰ ভৰ সূচক", "smoking_status": "ধূমপানৰ অৱস্থা",
    "pre_existing_conditions": "পূৰ্বৰে থকা ৰোগ",
    "family_history_score": "পাৰিবাৰিক ইতিহাস স্কোৰ", "occupation_risk": "বৃত্তিগত বিপদ",
    "coverage_amount": "বীমা সুৰক্ষাৰ পৰিমাণ", "symptoms_severity": "লক্ষণৰ তীব্ৰতা",
    "lab_results_abnormal": "অসাধাৰণ পৰীক্ষাগাৰ ফলাফল",
    "medical_history_score": "চিকিৎসা ইতিহাস স্কোৰ",
    "vitals_risk_score": "জীৱন সংকেত বিপদ স্কোৰ", "treatment_urgency": "চিকিৎসাৰ ততালিকে প্ৰয়োজন",
}

DECISIONS = {
    "APPROVED": "অনুমোদিত", "REJECTED": "প্ৰত্যাখ্যাত", "REVIEW_REQUIRED": "পুনৰীক্ষণ প্ৰয়োজন",
    "STANDARD_PREMIUM": "মানক প্ৰিমিয়াম", "LOADED_PREMIUM": "অতিৰিক্ত প্ৰিমিয়াম",
    "DECLINED": "প্ৰত্যাখ্যাত", "HIGH_RISK_INTERVENTION": "উচ্চ বিপদ - হস্তক্ষেপ",
    "MODERATE_RISK_MONITORING": "মধ্যম বিপদ - নিৰীক্ষণ",
    "LOW_RISK_ROUTINE": "কম বিপদ - সাধাৰণ",
}

EXPLANATION = {
    "positive_high": "{feature} ৰ উচ্চ মান ({value}) সিদ্ধান্তক অনুকূল দিশত লৈ গ'ল",
    "positive_low": "{feature} সিদ্ধান্তত অলপ অনুকূল অৱদান আগবঢ়ালে",
    "negative_high": "{feature} ৰ মান ({value}) সিদ্ধান্তক প্ৰতিকূল দিশত লৈ গ'ল",
    "negative_low": "{feature} সিদ্ধান্তত অলপ প্ৰতিকূল অৱদান আগবঢ়ালে",
}

SUMMARY = {
    "credit_approved": "ঋণৰ আবেদন অনুমোদিত হ'ল। মুখ্য কাৰক: {factors}",
    "credit_rejected": "ঋণৰ আবেদন প্ৰত্যাখ্যাত হ'ল। মুখ্য কাৰণ: {factors}",
    "credit_review": "ঋণৰ আবেদন পুনৰীক্ষণৰ বাবে পঠিয়াইছে। বিবেচিত কাৰক: {factors}",
    "insurance_standard": "মানক প্ৰিমিয়াম প্ৰযোজ্য। মূল্যায়ন কাৰক: {factors}",
    "insurance_loaded": "অতিৰিক্ত প্ৰিমিয়াম প্ৰযোজ্য। বিপদ কাৰক: {factors}",
    "insurance_declined": "বীমাৰ আবেদন প্ৰত্যাখ্যাত। বিপদ কাৰক: {factors}",
    "health_high": "উচ্চ বিপদ - ততালিকে হস্তক্ষেপৰ পৰামৰ্শ। কাৰক: {factors}",
    "health_moderate": "মধ্যম বিপদ - নিয়মীয়া নিৰীক্ষণৰ পৰামৰ্শ। কাৰক: {factors}",
    "health_low": "কম বিপদ - সাধাৰণ অনুসৰণ। কাৰক: {factors}",
}

REPORT = {
    "title": "নিয়ন্ত্ৰক অনুপালন প্ৰতিবেদন", "report_id": "প্ৰতিবেদন পৰিচয়",
    "generated_at": "প্ৰস্তুত কৰা সময়", "regulator": "নিয়ন্ত্ৰক", "domain": "ক্ষেত্ৰ",
    "model_version": "মডেল সংস্কৰণ", "algorithm": "এলগৰিদম",
    "explanation_method": "ব্যাখ্যাৰ পদ্ধতি", "decision": "সিদ্ধান্ত",
    "confidence": "বিশ্বাসৰ স্তৰ", "risk_score": "বিপদ স্কোৰ",
    "audit_id": "নিৰীক্ষা চিহ্ন পৰিচয়",
    "guidelines_heading": "প্ৰযোজ্য নিৰ্দেশনা", "checks_heading": "অনুপালন পৰীক্ষা",
    "requirements_heading": "নিয়ন্ত্ৰক প্ৰয়োজনীয়তা", "recommendations_heading": "পৰামৰ্শ",
    "explainability_heading": "ব্যাখ্যাযোগ্যতা প্ৰতিবেদন",
    "top_factors": "মুখ্য অৱদানকাৰী কাৰক", "features_explained": "ব্যাখ্যা কৰা বৈশিষ্ট্য",
    "explanation_language": "ব্যাখ্যাৰ ভাষা",
    "compliance_note": "এই ব্যাখ্যা {regulator} ৰ কৃত্ৰিম বুদ্ধিমত্তা ব্যাখ্যাযোগ্যতা নিৰ্দেশনা অনুসৰি প্ৰস্তুত",
    "disclaimer": "এই প্ৰতিবেদন {framework} ৰ নিৰ্দেশনা পালনৰ নথি। চূড়ান্ত অনুপালন নিৰ্ধাৰণ নিযুক্ত অনুপালন অধিকাৰীৰ দায়িত্ব।",
    "translation_notice": "এই প্ৰতিবেদন {language} ত যন্ত্ৰ-অনুবাদিত। নিয়ন্ত্ৰক দাখিলৰ বাবে ইংৰাজী পাঠ প্ৰামাণিক।",
}

STATUS = {
    "COMPLIANT": "অনুপালিত", "REVIEW_NEEDED": "পুনৰীক্ষণ প্ৰয়োজন",
    "PASS": "উত্তীৰ্ণ", "FAIL": "অনুত্তীৰ্ণ", "REVIEW": "পুনৰীক্ষণ",
}

DOMAINS = {
    "credit_scoring": "ঋণ মূল্যায়ন", "insurance_underwriting": "বীমা আণ্ডাৰৰাইটিং",
    "healthcare": "স্বাস্থ্য বিপদ মূল্যায়ন",
}

REGULATORS = {
    "RBI": "ভাৰতীয় ৰিজাৰ্ভ বেংক",
    "IRDAI": "ভাৰতীয় বীমা নিয়ন্ত্ৰক আৰু বিকাশ প্ৰাধিকৰণ",
    "SEBI": "ভাৰতীয় প্ৰতিভূতি আৰু বিনিময় ব'ৰ্ড",
    "IndiaAI": "ইণ্ডিয়াএআই মিছন - দায়িত্বশীল কৃত্ৰিম বুদ্ধিমত্তা ঢাঁচা",
}

REQUIREMENT_LABELS = {
    "explainability": "ব্যাখ্যাযোগ্যতা", "transparency": "পাৰদৰ্শিতা",
    "fairness": "নিৰপেক্ষতা", "audit_trail": "নিৰীক্ষা চিহ্ন",
    "grievance_redressal": "অভিযোগ নিবাৰণ", "human_oversight": "মানৱ তত্ত্বাৱধান",
    "data_privacy": "তথ্য গোপনীয়তা", "model_governance": "মডেল পৰিচালনা",
    "risk_disclosure": "বিপদ প্ৰকাশ", "investor_protection": "বিনিয়োগকাৰী সুৰক্ষা",
    "accountability": "জবাবদিহিতা", "privacy": "গোপনীয়তা",
    "safety": "সুৰক্ষা", "inclusivity": "সাঙুৰণ",
}

RECOMMENDATIONS = {
    "all_passed": "সকলো অনুপালন পৰীক্ষা উত্তীৰ্ণ। বৰ্তমানৰ নিয়ন্ত্ৰণ বজাই ৰাখক।",
    "schedule_review": "{regulator} ৰ সাময়িক পুনৰীক্ষণ প্ৰয়োজনীয়তা অনুসৰি পৰৱৰ্তী পুনৰীক্ষণ নিৰ্ধাৰণ কৰক।",
    "revalidate": "পৰিচালনা সময়সূচী অনুসৰি মডেলৰ সাময়িক পুনঃপ্ৰমাণীকৰণ নিশ্চিত কৰক।",
    "retain_logs": "ব্যাখ্যাৰ নথি নিৰ্ধাৰিত নিয়ন্ত্ৰক সময়সীমালৈ সংৰক্ষণ কৰক।",
    "address_failed": "অনুত্তীৰ্ণ পৰীক্ষাৰ সমাধান কৰক: {check}",
}

UI = {
    "app_title": "এক্সএআই প্লেটফৰ্ম",
    "app_subtitle": "নিয়ন্ত্ৰিত উদ্যোগৰ বাবে বহুভাষিক ব্যাখ্যাযোগ্য কৃত্ৰিম বুদ্ধিমত্তা",
    "select_domain": "সিদ্ধান্তৰ ক্ষেত্ৰ বাছনি কৰক", "input_params": "ইনপুট পেৰামিটাৰ",
    "load_sample": "নমুনা তথ্য ভৰাওক", "language_label": "ব্যাখ্যাৰ ভাষা",
    "generate_btn": "ব্যাখ্যা প্ৰস্তুত কৰক", "generating": "প্ৰস্তুত হৈ আছে...",
    "decision_label": "সিদ্ধান্ত", "confidence_label": "বিশ্বাস",
    "risk_label": "বিপদ স্কোৰ", "audit_label": "নিৰীক্ষা পৰিচয়",
    "explanation_heading": "কৃত্ৰিম বুদ্ধিমত্তা সিদ্ধান্ত আৰু ব্যাখ্যা",
    "contributions_heading": "বৈশিষ্ট্যৰ অৱদান", "summary_heading": "ব্যাখ্যাৰ সাৰাংশ",
    "report_btn": "অনুপালন প্ৰতিবেদন প্ৰস্তুত কৰক", "report_generating": "প্ৰতিবেদন প্ৰস্তুত হৈ আছে...",
    "coverage_label": "অনুবাদৰ পৰিসৰ", "needs_review_badge": "মাতৃভাষী পুনৰীক্ষণ প্ৰয়োজন",
    "footer_note": "অষ্টম অনুসূচীৰ ২২ ভাষাৰ সমৰ্থন | নিৰীক্ষাযোগ্য ব্যাখ্যা",
    "yes": "হয়", "no": "নহয়",
}
