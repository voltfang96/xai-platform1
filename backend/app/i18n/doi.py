"""Dogri (डोगरी) - Devanagari.

Core catalog. REQUIREMENT_TEXT and CHECKS fall back to English; see coverage.
"""

META = {
    "code": "doi", "name_native": "डोगरी", "name_en": "Dogri",
    "script": "Devanagari", "rtl": False, "scheduled": True,
    "review_status": "needs_native_review",
}

FEATURES = {
    "annual_income": "सालाना आमद", "credit_history_months": "करजे दा इतिहास (म्हीने)",
    "existing_loans": "मौजूदा करजे", "loan_amount_requested": "मंगी गेई करजे दी रकम",
    "employment_years": "नौकरी दा समां (साल)", "monthly_expenses": "म्हीनेवार खर्च",
    "age": "उमर", "defaults_in_past": "पैहले दियां चुकां",
    "bmi": "शरीर भार सूचक", "smoking_status": "सिगरेटनोशी दी हालत",
    "pre_existing_conditions": "पैहले शा मौजूद बमारियां",
    "family_history_score": "खानदानी इतिहास अंक", "occupation_risk": "पेशेवर खतरा",
    "coverage_amount": "बीमा कवरेज रकम", "symptoms_severity": "लच्छणें दी तीव्रता",
    "lab_results_abnormal": "असामान्य प्रयोगशाला नतीजे",
    "medical_history_score": "डाक्टरी इतिहास अंक",
    "vitals_risk_score": "जीवन संकेत खतरा अंक", "treatment_urgency": "इलाज दी फौरी लोड़",
}

DECISIONS = {
    "APPROVED": "मंजूर", "REJECTED": "नामंजूर", "REVIEW_REQUIRED": "समीक्षा दी लोड़",
    "STANDARD_PREMIUM": "मानक प्रीमियम", "LOADED_PREMIUM": "बद्धा प्रीमियम",
    "DECLINED": "इनकार", "HIGH_RISK_INTERVENTION": "उच्च खतरा - दखल",
    "MODERATE_RISK_MONITORING": "मध्यम खतरा - निगरानी",
    "LOW_RISK_ROUTINE": "घट्ट खतरा - आम",
}

EXPLANATION = {
    "positive_high": "{feature} दा उच्चा मोल ({value}) फैसले गी अनुकूल पासे लेई गेआ",
    "positive_low": "{feature} ने फैसले च थोड़ा अनुकूल योगदान दित्ता",
    "negative_high": "{feature} दा मोल ({value}) फैसले गी प्रतिकूल पासे लेई गेआ",
    "negative_low": "{feature} ने फैसले च थोड़ा प्रतिकूल योगदान दित्ता",
}

SUMMARY = {
    "credit_approved": "करजे दी अर्जी मंजूर होई। मुक्ख कारक: {factors}",
    "credit_rejected": "करजे दी अर्जी नामंजूर होई। मुक्ख कारण: {factors}",
    "credit_review": "करजे दी अर्जी समीक्षा लेई भेजी गेई। विचारे गेदे कारक: {factors}",
    "insurance_standard": "मानक प्रीमियम लागू। मूल्यांकन कारक: {factors}",
    "insurance_loaded": "बद्धा प्रीमियम लागू। खतरा कारक: {factors}",
    "insurance_declined": "बीमे दी अर्जी शा इनकार। खतरा कारक: {factors}",
    "health_high": "उच्च खतरा - फौरन दखल दी सलाह। कारक: {factors}",
    "health_moderate": "मध्यम खतरा - नियमित निगरानी दी सलाह। कारक: {factors}",
    "health_low": "घट्ट खतरा - आम पिच्छा। कारक: {factors}",
}

REPORT = {
    "title": "नियामक अनुपालन रिपोर्ट", "report_id": "रिपोर्ट नंबर",
    "generated_at": "तैयार करने दा समां", "regulator": "नियामक", "domain": "क्षेत्र",
    "model_version": "माडल संस्करण", "algorithm": "अलगोरिदम",
    "explanation_method": "व्याख्या दा तरीका", "decision": "फैसला",
    "confidence": "भरोसे दा स्तर", "risk_score": "खतरा अंक",
    "audit_id": "आडिट ट्रेल नंबर",
    "guidelines_heading": "लागू दिशा-निर्देश", "checks_heading": "अनुपालन जांचां",
    "requirements_heading": "नियामक लोड़ां", "recommendations_heading": "सलाहां",
    "explainability_heading": "व्याख्याजोगता रिपोर्ट",
    "top_factors": "मुक्ख योगदान कारक", "features_explained": "व्याख्या कीतियां खासियतां",
    "explanation_language": "व्याख्या दी बोली",
    "compliance_note": "एह् व्याख्या {regulator} दे मसनूई अकल व्याख्याजोगता दिशा-निर्देशें मताबक तैयार कीती गेई",
    "disclaimer": "एह् रिपोर्ट {framework} दे दिशा-निर्देशें दी पालना दा दस्तावेज ऐ। आखरी अनुपालन निर्धारण नियुक्त अनुपालन अफसर दी जिम्मेवारी ऐ।",
    "translation_notice": "एह् रिपोर्ट {language} च मशीनी अनुवाद ऐ। नियामक पेशकारी लेई अंग्रेजी पाठ प्रमाणिक ऐ।",
}

STATUS = {
    "COMPLIANT": "अनुपालित", "REVIEW_NEEDED": "समीक्षा दी लोड़",
    "PASS": "पास", "FAIL": "फेल", "REVIEW": "समीक्षा",
}

DOMAINS = {
    "credit_scoring": "करजे दा मूल्यांकन", "insurance_underwriting": "बीमा अंडररायटिंग",
    "healthcare": "सेहत खतरा मूल्यांकन",
}

REGULATORS = {
    "RBI": "भारतीय रिजर्व बैंक",
    "IRDAI": "भारतीय बीमा नियामक ते विकास प्राधिकरण",
    "SEBI": "भारतीय प्रतिभूति ते विनिमय बोर्ड",
    "IndiaAI": "इंडियाएआई मिशन - जिम्मेवार मसनूई अकल ढांचा",
}

REQUIREMENT_LABELS = {
    "explainability": "व्याख्याजोगता", "transparency": "पारदर्शता",
    "fairness": "निष्पक्षता", "audit_trail": "आडिट ट्रेल",
    "grievance_redressal": "शिकैत निवारण", "human_oversight": "मानवी निगरानी",
    "data_privacy": "डेटा गुप्तता", "model_governance": "माडल प्रशासन",
    "risk_disclosure": "खतरा जाहर करना", "investor_protection": "निवेशक सुरक्षा",
    "accountability": "जवाबदेही", "privacy": "गुप्तता",
    "safety": "सुरक्षा", "inclusivity": "समावेश",
}

RECOMMENDATIONS = {
    "all_passed": "सब्भै अनुपालन जांचां पास। मौजूदा नियंत्रण बनाई रक्खो।",
    "schedule_review": "{regulator} दियां समें-समें दियां समीक्षा लोड़ें मताबक अगली समीक्षा तै करो।",
    "revalidate": "प्रशासन समां-सूची मताबक माडल दी समें-समें फिरी पड़ताल यकीनी बनाओ।",
    "retain_logs": "व्याख्या दे रिकार्ड तै कीते नियामक समें तकर संभालो।",
    "address_failed": "फेल होई जांच दा हल करो: {check}",
}

UI = {
    "app_title": "एक्सएआई प्लेटफार्म",
    "app_subtitle": "नियमित उद्योगें लेई बहुभाशी व्याख्याजोग मसनूई अकल",
    "select_domain": "फैसला क्षेत्र चुनो", "input_params": "इनपुट पैरामीटर",
    "load_sample": "नमूना डेटा भरो", "language_label": "व्याख्या दी बोली",
    "generate_btn": "व्याख्या बनाओ", "generating": "बनी दी ऐ...",
    "decision_label": "फैसला", "confidence_label": "भरोसा",
    "risk_label": "खतरा अंक", "audit_label": "आडिट नंबर",
    "explanation_heading": "मसनूई अकल फैसला ते व्याख्या",
    "contributions_heading": "खासियतें दा योगदान", "summary_heading": "व्याख्या सार",
    "report_btn": "अनुपालन रिपोर्ट बनाओ",
    "print_btn": "रिपोर्ट छापो", "report_generating": "रिपोर्ट बनी दी ऐ...",
    "coverage_label": "अनुवाद दा फैलाव", "needs_review_badge": "मां-बोली समीक्षा दी लोड़",
    "footer_note": "अठमीं सूची दियां २२ बोलियें दा समर्थन | आडिट-जोग व्याख्यां",
    "yes": "हां", "no": "नेईं",
}
