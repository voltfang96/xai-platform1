"""Punjabi (ਪੰਜਾਬੀ) - Gurmukhi."""

META = {
    "code": "pa", "name_native": "ਪੰਜਾਬੀ", "name_en": "Punjabi",
    "script": "Gurmukhi", "rtl": False, "scheduled": True,
    "review_status": "verified",
}

FEATURES = {
    "annual_income": "ਸਾਲਾਨਾ ਆਮਦਨ", "credit_history_months": "ਕਰਜ਼ਾ ਇਤਿਹਾਸ (ਮਹੀਨੇ)",
    "existing_loans": "ਮੌਜੂਦਾ ਕਰਜ਼ੇ", "loan_amount_requested": "ਮੰਗੀ ਗਈ ਕਰਜ਼ਾ ਰਕਮ",
    "employment_years": "ਨੌਕਰੀ ਦਾ ਸਮਾਂ (ਸਾਲ)", "monthly_expenses": "ਮਹੀਨਾਵਾਰ ਖਰਚ",
    "age": "ਉਮਰ", "defaults_in_past": "ਪਿਛਲੀਆਂ ਕੁਤਾਹੀਆਂ",
    "bmi": "ਸਰੀਰਕ ਭਾਰ ਸੂਚਕ", "smoking_status": "ਸਿਗਰਟਨੋਸ਼ੀ ਦੀ ਸਥਿਤੀ",
    "pre_existing_conditions": "ਪਹਿਲਾਂ ਤੋਂ ਮੌਜੂਦ ਰੋਗ",
    "family_history_score": "ਪਰਿਵਾਰਕ ਇਤਿਹਾਸ ਅੰਕ", "occupation_risk": "ਪੇਸ਼ੇਵਰ ਜੋਖਮ",
    "coverage_amount": "ਬੀਮਾ ਕਵਰੇਜ ਰਕਮ", "symptoms_severity": "ਲੱਛਣਾਂ ਦੀ ਤੀਬਰਤਾ",
    "lab_results_abnormal": "ਅਸਾਧਾਰਨ ਪ੍ਰਯੋਗਸ਼ਾਲਾ ਨਤੀਜੇ",
    "medical_history_score": "ਡਾਕਟਰੀ ਇਤਿਹਾਸ ਅੰਕ",
    "vitals_risk_score": "ਜੀਵਨ-ਸੰਕੇਤ ਜੋਖਮ ਅੰਕ", "treatment_urgency": "ਇਲਾਜ ਦੀ ਤਤਕਾਲਤਾ",
}

DECISIONS = {
    "APPROVED": "ਮਨਜ਼ੂਰ", "REJECTED": "ਨਾਮਨਜ਼ੂਰ", "REVIEW_REQUIRED": "ਸਮੀਖਿਆ ਲੋੜੀਂਦੀ",
    "STANDARD_PREMIUM": "ਮਿਆਰੀ ਪ੍ਰੀਮੀਅਮ", "LOADED_PREMIUM": "ਵਾਧੂ ਪ੍ਰੀਮੀਅਮ",
    "DECLINED": "ਇਨਕਾਰ", "HIGH_RISK_INTERVENTION": "ਉੱਚ ਜੋਖਮ - ਦਖਲ",
    "MODERATE_RISK_MONITORING": "ਮੱਧਮ ਜੋਖਮ - ਨਿਗਰਾਨੀ",
    "LOW_RISK_ROUTINE": "ਘੱਟ ਜੋਖਮ - ਸਧਾਰਨ",
}

EXPLANATION = {
    "positive_high": "{feature} ਦਾ ਉੱਚਾ ਮੁੱਲ ({value}) ਫੈਸਲੇ ਨੂੰ ਅਨੁਕੂਲ ਦਿਸ਼ਾ ਵੱਲ ਲੈ ਗਿਆ",
    "positive_low": "{feature} ਨੇ ਫੈਸਲੇ ਵਿੱਚ ਥੋੜ੍ਹਾ ਅਨੁਕੂਲ ਯੋਗਦਾਨ ਪਾਇਆ",
    "negative_high": "{feature} ਦਾ ਮੁੱਲ ({value}) ਫੈਸਲੇ ਨੂੰ ਪ੍ਰਤੀਕੂਲ ਦਿਸ਼ਾ ਵੱਲ ਲੈ ਗਿਆ",
    "negative_low": "{feature} ਨੇ ਫੈਸਲੇ ਵਿੱਚ ਥੋੜ੍ਹਾ ਪ੍ਰਤੀਕੂਲ ਯੋਗਦਾਨ ਪਾਇਆ",
}

SUMMARY = {
    "credit_approved": "ਕਰਜ਼ਾ ਅਰਜ਼ੀ ਮਨਜ਼ੂਰ ਹੋਈ। ਮੁੱਖ ਕਾਰਕ: {factors}",
    "credit_rejected": "ਕਰਜ਼ਾ ਅਰਜ਼ੀ ਨਾਮਨਜ਼ੂਰ ਹੋਈ। ਮੁੱਖ ਕਾਰਨ: {factors}",
    "credit_review": "ਕਰਜ਼ਾ ਅਰਜ਼ੀ ਸਮੀਖਿਆ ਲਈ ਭੇਜੀ ਗਈ। ਵਿਚਾਰੇ ਗਏ ਕਾਰਕ: {factors}",
    "insurance_standard": "ਮਿਆਰੀ ਪ੍ਰੀਮੀਅਮ ਲਾਗੂ। ਮੁਲਾਂਕਣ ਕਾਰਕ: {factors}",
    "insurance_loaded": "ਵਾਧੂ ਪ੍ਰੀਮੀਅਮ ਲਾਗੂ। ਜੋਖਮ ਕਾਰਕ: {factors}",
    "insurance_declined": "ਬੀਮਾ ਅਰਜ਼ੀ ਤੋਂ ਇਨਕਾਰ। ਜੋਖਮ ਕਾਰਕ: {factors}",
    "health_high": "ਉੱਚ ਜੋਖਮ - ਤੁਰੰਤ ਦਖਲ ਦੀ ਸਿਫਾਰਸ਼। ਕਾਰਕ: {factors}",
    "health_moderate": "ਮੱਧਮ ਜੋਖਮ - ਨਿਯਮਤ ਨਿਗਰਾਨੀ ਦੀ ਸਿਫਾਰਸ਼। ਕਾਰਕ: {factors}",
    "health_low": "ਘੱਟ ਜੋਖਮ - ਸਧਾਰਨ ਪਿੱਛਾ। ਕਾਰਕ: {factors}",
}

REPORT = {
    "title": "ਨਿਯਾਮਕ ਪਾਲਣਾ ਰਿਪੋਰਟ", "report_id": "ਰਿਪੋਰਟ ਨੰਬਰ",
    "generated_at": "ਤਿਆਰ ਕਰਨ ਦਾ ਸਮਾਂ", "regulator": "ਨਿਯਾਮਕ", "domain": "ਖੇਤਰ",
    "model_version": "ਮਾਡਲ ਸੰਸਕਰਣ", "algorithm": "ਐਲਗੋਰਿਦਮ",
    "explanation_method": "ਵਿਆਖਿਆ ਵਿਧੀ", "decision": "ਫੈਸਲਾ",
    "confidence": "ਭਰੋਸਾ ਪੱਧਰ", "risk_score": "ਜੋਖਮ ਅੰਕ",
    "audit_id": "ਆਡਿਟ ਟ੍ਰੇਲ ਨੰਬਰ",
    "guidelines_heading": "ਲਾਗੂ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼", "checks_heading": "ਪਾਲਣਾ ਜਾਂਚਾਂ",
    "requirements_heading": "ਨਿਯਾਮਕ ਲੋੜਾਂ", "recommendations_heading": "ਸਿਫਾਰਸ਼ਾਂ",
    "explainability_heading": "ਵਿਆਖਿਆਯੋਗਤਾ ਰਿਪੋਰਟ",
    "top_factors": "ਮੁੱਖ ਯੋਗਦਾਨ ਕਾਰਕ", "features_explained": "ਵਿਆਖਿਆ ਕੀਤੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ",
    "explanation_language": "ਵਿਆਖਿਆ ਦੀ ਭਾਸ਼ਾ",
    "compliance_note": "ਇਹ ਵਿਆਖਿਆ {regulator} ਦੇ ਬਣਾਵਟੀ ਬੁੱਧੀ ਵਿਆਖਿਆਯੋਗਤਾ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼ਾਂ ਅਨੁਸਾਰ ਤਿਆਰ ਕੀਤੀ ਗਈ ਹੈ",
    "disclaimer": "ਇਹ ਰਿਪੋਰਟ {framework} ਦੇ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼ਾਂ ਦੀ ਪਾਲਣਾ ਦਾ ਦਸਤਾਵੇਜ਼ ਹੈ। ਅੰਤਿਮ ਪਾਲਣਾ ਨਿਰਧਾਰਨ ਨਿਯੁਕਤ ਪਾਲਣਾ ਅਧਿਕਾਰੀ ਦੀ ਜ਼ਿੰਮੇਵਾਰੀ ਹੈ।",
    "translation_notice": "ਇਹ ਰਿਪੋਰਟ {language} ਵਿੱਚ ਮਸ਼ੀਨ-ਅਨੁਵਾਦਿਤ ਹੈ। ਨਿਯਾਮਕ ਪੇਸ਼ਕਾਰੀ ਲਈ ਅੰਗਰੇਜ਼ੀ ਪਾਠ ਪ੍ਰਮਾਣਿਕ ਹੈ।",
}

STATUS = {
    "COMPLIANT": "ਪਾਲਣਾ ਵਿੱਚ", "REVIEW_NEEDED": "ਸਮੀਖਿਆ ਲੋੜੀਂਦੀ",
    "PASS": "ਪਾਸ", "FAIL": "ਫੇਲ", "REVIEW": "ਸਮੀਖਿਆ",
}

DOMAINS = {
    "credit_scoring": "ਕਰਜ਼ਾ ਮੁਲਾਂਕਣ", "insurance_underwriting": "ਬੀਮਾ ਅੰਡਰਰਾਈਟਿੰਗ",
    "healthcare": "ਸਿਹਤ ਜੋਖਮ ਮੁਲਾਂਕਣ",
}

REGULATORS = {
    "RBI": "ਭਾਰਤੀ ਰਿਜ਼ਰਵ ਬੈਂਕ",
    "IRDAI": "ਭਾਰਤੀ ਬੀਮਾ ਨਿਯਾਮਕ ਅਤੇ ਵਿਕਾਸ ਅਥਾਰਟੀ",
    "SEBI": "ਭਾਰਤੀ ਪ੍ਰਤੀਭੂਤੀ ਅਤੇ ਵਟਾਂਦਰਾ ਬੋਰਡ",
    "IndiaAI": "ਇੰਡੀਆਏਆਈ ਮਿਸ਼ਨ - ਜ਼ਿੰਮੇਵਾਰ ਬਣਾਵਟੀ ਬੁੱਧੀ ਢਾਂਚਾ",
}

REQUIREMENT_LABELS = {
    "explainability": "ਵਿਆਖਿਆਯੋਗਤਾ", "transparency": "ਪਾਰਦਰਸ਼ਤਾ",
    "fairness": "ਨਿਰਪੱਖਤਾ", "audit_trail": "ਆਡਿਟ ਟ੍ਰੇਲ",
    "grievance_redressal": "ਸ਼ਿਕਾਇਤ ਨਿਵਾਰਨ", "human_oversight": "ਮਨੁੱਖੀ ਨਿਗਰਾਨੀ",
    "data_privacy": "ਡਾਟਾ ਗੁਪਤਤਾ", "model_governance": "ਮਾਡਲ ਪ੍ਰਸ਼ਾਸਨ",
    "risk_disclosure": "ਜੋਖਮ ਪ੍ਰਗਟਾਵਾ", "investor_protection": "ਨਿਵੇਸ਼ਕ ਸੁਰੱਖਿਆ",
    "accountability": "ਜਵਾਬਦੇਹੀ", "privacy": "ਗੁਪਤਤਾ",
    "safety": "ਸੁਰੱਖਿਆ", "inclusivity": "ਸ਼ਾਮਲ ਕਰਨਾ",
}

REQUIREMENT_TEXT = {
    "explainability": "ਸਵੈਚਾਲਿਤ ਫੈਸਲਿਆਂ ਨਾਲ ਸਪਸ਼ਟ ਅਤੇ ਸਮਝਣ ਯੋਗ ਕਾਰਨ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ",
    "transparency": "ਫੈਸਲੇ ਵਿੱਚ ਬਣਾਵਟੀ ਬੁੱਧੀ ਦੀ ਵਰਤੋਂ ਬਾਰੇ ਸੰਬੰਧਿਤ ਵਿਅਕਤੀ ਨੂੰ ਸੂਚਿਤ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ",
    "fairness": "ਸੁਰੱਖਿਅਤ ਵਰਗਾਂ ਦੇ ਸੰਦਰਭ ਵਿੱਚ ਮਾਡਲ ਦੀ ਪੱਖਪਾਤ ਜਾਂਚ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ",
    "audit_trail": "ਫੈਸਲਿਆਂ ਦਾ ਪੂਰਾ ਆਡਿਟ ਟ੍ਰੇਲ ਨਿਰਧਾਰਿਤ ਸਮੇਂ ਤੱਕ ਰੱਖਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ",
    "grievance_redressal": "ਸਵੈਚਾਲਿਤ ਫੈਸਲੇ ਨੂੰ ਚੁਣੌਤੀ ਦੇਣ ਦੀ ਸਪਸ਼ਟ ਵਿਵਸਥਾ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ",
    "human_oversight": "ਨਿਰਧਾਰਿਤ ਹੱਦ ਤੋਂ ਉੱਪਰ ਦੇ ਫੈਸਲਿਆਂ ਦੀ ਮਨੁੱਖੀ ਸਮੀਖਿਆ ਜ਼ਰੂਰੀ ਹੈ",
    "data_privacy": "ਨਿੱਜੀ ਡਾਟਾ ਪ੍ਰਬੰਧਨ ਡੀਪੀਡੀਪੀ ਐਕਟ 2023 ਅਨੁਸਾਰ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ",
    "model_governance": "ਮਾਡਲਾਂ ਦੀ ਸਮੇਂ-ਸਮੇਂ ਪੜਤਾਲ ਅਤੇ ਮੁੜ-ਪੜਤਾਲ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ",
    "risk_disclosure": "ਜੋਖਮ ਮੁਲਾਂਕਣ ਵਿੱਚ ਮਾਡਲ ਦੀਆਂ ਸੀਮਾਵਾਂ ਅਤੇ ਧਾਰਨਾਵਾਂ ਪ੍ਰਗਟ ਹੋਣੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ",
    "investor_protection": "ਪ੍ਰਚੂਨ ਨਿਵੇਸ਼ਕਾਂ ਨੂੰ ਸਰਲ ਵਿਆਖਿਆ ਮਿਲਣੀ ਚਾਹੀਦੀ ਹੈ",
    "accountability": "ਫੈਸਲੇ ਲਈ ਸਪਸ਼ਟ ਜਵਾਬਦੇਹੀ ਲੜੀ ਦਰਜ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ",
    "privacy": "ਡਾਟਾ ਪ੍ਰਕਿਰਿਆ ਲਾਗੂ ਗੁਪਤਤਾ ਕਾਨੂੰਨ ਅਨੁਸਾਰ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ",
    "safety": "ਵਿਅਕਤੀ ਜਾਂ ਸਮਾਜ ਨੂੰ ਸੰਭਾਵੀ ਨੁਕਸਾਨ ਦਾ ਮੁਲਾਂਕਣ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ",
    "inclusivity": "ਵਿਆਖਿਆ ਵਿਅਕਤੀ ਦੀ ਖੇਤਰੀ ਭਾਸ਼ਾ ਵਿੱਚ ਉਪਲਬਧ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ",
}

CHECKS = {
    "feature_explanation_provided": ("ਵਿਸ਼ੇਸ਼ਤਾ ਵਿਆਖਿਆ ਦਿੱਤੀ", "ਯੋਗਦਾਨ ਪਾਉਣ ਵਾਲੀ ਹਰ ਵਿਸ਼ੇਸ਼ਤਾ ਮਹੱਤਵ ਅੰਕ ਨਾਲ ਦਰਜ ਹੈ"),
    "bias_metrics_documented": ("ਪੱਖਪਾਤ ਮਾਪਦੰਡ ਦਰਜ", "ਪੱਖਪਾਤ ਜਾਂਚ ਮਾਪਦੰਡ ਦਰਜ ਹਨ ਅਤੇ ਸਵੀਕਾਰਯੋਗ ਹੱਦ ਵਿੱਚ ਹਨ"),
    "model_version_tracked": ("ਮਾਡਲ ਸੰਸਕਰਣ ਦਰਜ", "ਫੈਸਲੇ ਨਾਲ ਮਾਡਲ ਸੰਸਕਰਣ ਅਤੇ ਪੜਤਾਲ ਸਥਿਤੀ ਦਰਜ ਹੈ"),
    "decision_rationale_clear": ("ਫੈਸਲੇ ਦਾ ਤਰਕ ਸਪਸ਼ਟ", "ਤਰਕ ਅਜਿਹੀ ਭਾਸ਼ਾ ਵਿੱਚ ਹੈ ਜੋ ਗੈਰ-ਮਾਹਿਰ ਵੀ ਸਮਝ ਸਕੇ"),
    "customer_notification_ready": ("ਗਾਹਕ ਸੂਚਨਾ ਤਿਆਰ", "ਚੁਣੀ ਭਾਸ਼ਾ ਵਿੱਚ ਗਾਹਕ ਲਈ ਵਿਆਖਿਆ ਉਪਲਬਧ ਹੈ"),
    "audit_trail_complete": ("ਆਡਿਟ ਟ੍ਰੇਲ ਪੂਰਾ", "ਵੱਖਰੀ ਪਛਾਣ ਵਾਲਾ ਟ੍ਰੇਲ ਜਾਂਚ ਲਈ ਸੁਰੱਖਿਅਤ ਹੈ"),
    "underwriting_factors_disclosed": ("ਅੰਡਰਰਾਈਟਿੰਗ ਕਾਰਕ ਪ੍ਰਗਟ", "ਅੰਡਰਰਾਈਟਿੰਗ ਨਤੀਜੇ ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕਰਨ ਵਾਲੇ ਸਾਰੇ ਕਾਰਕ ਪ੍ਰਗਟ ਹਨ"),
    "premium_rationale_clear": ("ਪ੍ਰੀਮੀਅਮ ਆਧਾਰ ਸਪਸ਼ਟ", "ਪ੍ਰੀਮੀਅਮ ਵਾਧੇ ਦਾ ਆਧਾਰ ਸਪਸ਼ਟ ਦੱਸਿਆ ਗਿਆ ਹੈ"),
    "no_genetic_discrimination": ("ਜੈਨੇਟਿਕ ਵਿਤਕਰਾ ਨਹੀਂ", "ਫੈਸਲੇ ਵਿੱਚ ਕੋਈ ਜੈਨੇਟਿਕ ਜਾਣਕਾਰੀ ਨਹੀਂ ਵਰਤੀ ਗਈ"),
    "data_privacy_compliant": ("ਡਾਟਾ ਗੁਪਤਤਾ ਪਾਲਣਾ", "ਨਿੱਜੀ ਡਾਟਾ ਪ੍ਰਬੰਧਨ ਡੀਪੀਡੀਪੀ ਐਕਟ 2023 ਦੀ ਪਾਲਣਾ ਕਰਦਾ ਹੈ"),
    "policyholder_notification": ("ਪਾਲਿਸੀਧਾਰਕ ਸੂਚਨਾ", "ਬਣਾਵਟੀ ਬੁੱਧੀ ਸਹਾਇਤ ਮੁਲਾਂਕਣ ਦੀ ਸੂਚਨਾ ਤਿਆਰ ਹੈ"),
    "model_validation_current": ("ਮਾਡਲ ਪੜਤਾਲ ਮੌਜੂਦਾ", "ਮਾਡਲ ਆਪਣੀ ਨਿਰਧਾਰਿਤ ਪੜਤਾਲ ਮਿਆਦ ਵਿੱਚ ਹੈ"),
    "risk_factors_explained": ("ਜੋਖਮ ਕਾਰਕ ਵਿਆਖਿਆਏ", "ਮੁਲਾਂਕਣ ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕਰਨ ਵਾਲਾ ਹਰ ਜੋਖਮ ਕਾਰਕ ਵਿਆਖਿਆਇਆ ਗਿਆ ਹੈ"),
    "model_limitations_disclosed": ("ਮਾਡਲ ਸੀਮਾਵਾਂ ਪ੍ਰਗਟ", "ਮਾਡਲ ਦੀਆਂ ਜਾਣੀਆਂ ਸੀਮਾਵਾਂ ਅਤੇ ਧਾਰਨਾਵਾਂ ਦੱਸੀਆਂ ਗਈਆਂ ਹਨ"),
    "no_market_manipulation": ("ਬਾਜ਼ਾਰ ਹੇਰਾਫੇਰੀ ਨਹੀਂ", "ਫੈਸਲੇ ਦੇ ਤਰਕ ਵਿੱਚ ਕੋਈ ਹੇਰਾਫੇਰੀ ਪ੍ਰਵਿਰਤੀ ਨਹੀਂ ਮਿਲੀ"),
    "stress_test_documented": ("ਦਬਾਅ ਜਾਂਚ ਦਰਜ", "ਪ੍ਰਤੀਕੂਲ ਹਾਲਾਤ ਵਿੱਚ ਵਿਹਾਰ ਦਰਜ ਹੈ"),
    "investor_notification": ("ਨਿਵੇਸ਼ਕ ਸੂਚਨਾ", "ਬਣਾਵਟੀ ਬੁੱਧੀ ਸਹਾਇਤ ਮੁਲਾਂਕਣ ਦੀ ਸੂਚਨਾ ਤਿਆਰ ਹੈ"),
    "audit_trail_maintained": ("ਆਡਿਟ ਟ੍ਰੇਲ ਸਾਂਭਿਆ", "ਨਿਯਾਮਕ ਜਾਂਚ ਲਈ ਪੂਰਾ ਟ੍ਰੇਲ ਸਾਂਭਿਆ ਗਿਆ ਹੈ"),
    "explanation_human_readable": ("ਵਿਆਖਿਆ ਮਨੁੱਖ-ਪੜ੍ਹਨਯੋਗ", "ਵਿਆਖਿਆ ਸਰਲ, ਮਨੁੱਖ-ਪੜ੍ਹਨਯੋਗ ਰੂਪ ਵਿੱਚ ਹੈ"),
    "multilingual_support": ("ਬਹੁਭਾਸ਼ੀ ਸਮਰਥਨ", "ਵਿਆਖਿਆ ਅੱਠਵੀਂ ਸੂਚੀ ਦੀਆਂ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਉਪਲਬਧ ਹੈ"),
    "bias_testing_done": ("ਪੱਖਪਾਤ ਜਾਂਚ ਪੂਰੀ", "ਸੁਰੱਖਿਅਤ ਵਰਗਾਂ ਵਿੱਚ ਪੱਖਪਾਤ ਜਾਂਚ ਪੂਰੀ ਹੋਈ ਹੈ"),
    "accountability_assigned": ("ਜਵਾਬਦੇਹੀ ਨਿਰਧਾਰਿਤ", "ਇਸ ਫੈਸਲੇ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਵਿਅਕਤੀ ਦਰਜ ਹੈ"),
    "privacy_compliant": ("ਗੁਪਤਤਾ ਪਾਲਣਾ", "ਪ੍ਰਕਿਰਿਆ ਲਾਗੂ ਗੁਪਤਤਾ ਕਾਨੂੰਨ ਅਨੁਸਾਰ ਹੈ"),
    "safety_assessed": ("ਸੁਰੱਖਿਆ ਮੁਲਾਂਕਿਤ", "ਸੁਰੱਖਿਆ ਮੁਲਾਂਕਣ ਪੂਰਾ, ਕੋਈ ਨੁਕਸਾਨ ਨਹੀਂ ਮਿਲਿਆ"),
    "inclusive_design": ("ਸ਼ਾਮਲ ਕਰਨ ਵਾਲੀ ਬਣਤਰ", "ਖੇਤਰੀ ਭਾਸ਼ਾ ਪਹੁੰਚ ਬਣਤਰ ਵਿੱਚ ਹੀ ਦਿੱਤੀ ਗਈ ਹੈ"),
}

RECOMMENDATIONS = {
    "all_passed": "ਸਾਰੀਆਂ ਪਾਲਣਾ ਜਾਂਚਾਂ ਪਾਸ। ਮੌਜੂਦਾ ਨਿਯੰਤਰਣ ਬਰਕਰਾਰ ਰੱਖੋ।",
    "schedule_review": "{regulator} ਦੀਆਂ ਸਮੇਂ-ਸਮੇਂ ਸਮੀਖਿਆ ਲੋੜਾਂ ਅਨੁਸਾਰ ਅਗਲੀ ਸਮੀਖਿਆ ਨਿਰਧਾਰਿਤ ਕਰੋ।",
    "revalidate": "ਪ੍ਰਸ਼ਾਸਨ ਸਮਾਂ-ਸੂਚੀ ਅਨੁਸਾਰ ਮਾਡਲ ਦੀ ਸਮੇਂ-ਸਮੇਂ ਮੁੜ-ਪੜਤਾਲ ਯਕੀਨੀ ਬਣਾਓ।",
    "retain_logs": "ਵਿਆਖਿਆ ਰਿਕਾਰਡ ਨਿਰਧਾਰਿਤ ਨਿਯਾਮਕ ਮਿਆਦ ਤੱਕ ਸਾਂਭੋ।",
    "address_failed": "ਫੇਲ ਹੋਈ ਜਾਂਚ ਦਾ ਹੱਲ ਕਰੋ: {check}",
}

UI = {
    "app_title": "ਐਕਸਏਆਈ ਪਲੇਟਫਾਰਮ",
    "app_subtitle": "ਨਿਯਮਿਤ ਉਦਯੋਗਾਂ ਲਈ ਬਹੁਭਾਸ਼ੀ ਵਿਆਖਿਆਯੋਗ ਬਣਾਵਟੀ ਬੁੱਧੀ",
    "select_domain": "ਫੈਸਲਾ ਖੇਤਰ ਚੁਣੋ", "input_params": "ਇਨਪੁਟ ਪੈਰਾਮੀਟਰ",
    "load_sample": "ਨਮੂਨਾ ਡਾਟਾ ਭਰੋ", "language_label": "ਵਿਆਖਿਆ ਦੀ ਭਾਸ਼ਾ",
    "generate_btn": "ਵਿਆਖਿਆ ਬਣਾਓ", "generating": "ਬਣ ਰਹੀ ਹੈ...",
    "decision_label": "ਫੈਸਲਾ", "confidence_label": "ਭਰੋਸਾ",
    "risk_label": "ਜੋਖਮ ਅੰਕ", "audit_label": "ਆਡਿਟ ਨੰਬਰ",
    "explanation_heading": "ਬਣਾਵਟੀ ਬੁੱਧੀ ਫੈਸਲਾ ਅਤੇ ਵਿਆਖਿਆ",
    "contributions_heading": "ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦਾ ਯੋਗਦਾਨ", "summary_heading": "ਵਿਆਖਿਆ ਸਾਰ",
    "report_btn": "ਪਾਲਣਾ ਰਿਪੋਰਟ ਬਣਾਓ",
    "print_btn": "ਰਿਪੋਰਟ ਪ੍ਰਿੰਟ ਕਰੋ", "report_generating": "ਰਿਪੋਰਟ ਬਣ ਰਹੀ ਹੈ...",
    "coverage_label": "ਅਨੁਵਾਦ ਵਿਸਤਾਰ", "needs_review_badge": "ਮਾਂ-ਬੋਲੀ ਸਮੀਖਿਆ ਲੋੜੀਂਦੀ",
    "footer_note": "ਅੱਠਵੀਂ ਸੂਚੀ ਦੀਆਂ 22 ਭਾਸ਼ਾਵਾਂ ਦਾ ਸਮਰਥਨ | ਆਡਿਟ-ਯੋਗ ਵਿਆਖਿਆਵਾਂ",
    "yes": "ਹਾਂ", "no": "ਨਹੀਂ",
}
