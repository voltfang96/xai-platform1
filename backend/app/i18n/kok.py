"""Konkani (कोंकणी) - Devanagari.

Core catalog. REQUIREMENT_TEXT and CHECKS fall back to English; see coverage.
"""

META = {
    "code": "kok", "name_native": "कोंकणी", "name_en": "Konkani",
    "script": "Devanagari", "rtl": False, "scheduled": True,
    "review_status": "needs_native_review",
}

FEATURES = {
    "annual_income": "वर्सुकी आदाय", "credit_history_months": "रीण इतिहास (म्हयने)",
    "existing_loans": "सद्याचीं रिणां", "loan_amount_requested": "मागणी केल्ली रीण रक्कम",
    "employment_years": "नोकरेचो काळ (वर्सां)", "monthly_expenses": "म्हयनावळी खर्च",
    "age": "वय", "defaults_in_past": "आदल्यो चुको",
    "bmi": "कुडीचो भार सुचकांक", "smoking_status": "धुम्रपानाची स्थिती",
    "pre_existing_conditions": "पयलीं आशिल्ल्यो बिमारी",
    "family_history_score": "कुटुंब इतिहास गुण", "occupation_risk": "वेवसायीक धोको",
    "coverage_amount": "विमो संरक्षण रक्कम", "symptoms_severity": "लक्षणांची तीव्रताय",
    "lab_results_abnormal": "असामान्य प्रयोगशाळा निकाल",
    "medical_history_score": "वैजकी इतिहास गुण",
    "vitals_risk_score": "जीवीत चिन्न धोको गुण", "treatment_urgency": "उपचाराची गरज",
}

DECISIONS = {
    "APPROVED": "मान्य", "REJECTED": "नामान्य", "REVIEW_REQUIRED": "फेरतपासणी गरजेची",
    "STANDARD_PREMIUM": "प्रमाणीत हप्तो", "LOADED_PREMIUM": "वाडीव हप्तो",
    "DECLINED": "न्हयकारलां", "HIGH_RISK_INTERVENTION": "चड धोको - हस्तक्षेप",
    "MODERATE_RISK_MONITORING": "मध्यम धोको - देखरेख",
    "LOW_RISK_ROUTINE": "उणो धोको - सादो",
}

EXPLANATION = {
    "positive_high": "{feature} हाचें चड मोल ({value}) निर्णय अनुकूल दिशेन व्हेलें",
    "positive_low": "{feature} हाणें निर्णयांत थोडें अनुकूल योगदान दिलें",
    "negative_high": "{feature} हाचें मोल ({value}) निर्णय प्रतिकूल दिशेन व्हेलें",
    "negative_low": "{feature} हाणें निर्णयांत थोडें प्रतिकूल योगदान दिलें",
}

SUMMARY = {
    "credit_approved": "रीण अर्ज मान्य जालो. मुखेल घटक: {factors}",
    "credit_rejected": "रीण अर्ज नामान्य जालो. मुखेल कारणां: {factors}",
    "credit_review": "रीण अर्ज फेरतपासणेक धाडलो. विचार केल्ले घटक: {factors}",
    "insurance_standard": "प्रमाणीत हप्तो लागू. मूल्यमापन घटक: {factors}",
    "insurance_loaded": "वाडीव हप्तो लागू. धोको घटक: {factors}",
    "insurance_declined": "विमो अर्ज न्हयकारलो. धोको घटक: {factors}",
    "health_high": "चड धोको - तुरंत हस्तक्षेपाची शिफारस. घटक: {factors}",
    "health_moderate": "मध्यम धोको - नेमाळी देखरेखेची शिफारस. घटक: {factors}",
    "health_low": "उणो धोको - सादी फाटपुरवण. घटक: {factors}",
}

REPORT = {
    "title": "नियामक अनुपालन अहवाल", "report_id": "अहवाल क्रमांक",
    "generated_at": "तयार केल्लो वेळ", "regulator": "नियामक", "domain": "मळ",
    "model_version": "प्रतिमान आवृत्ती", "algorithm": "अल्गोरिदम",
    "explanation_method": "स्पश्टीकरण पद्दत", "decision": "निर्णय",
    "confidence": "विस्वास पातळी", "risk_score": "धोको गुण",
    "audit_id": "लेखापरिक्षण खूण क्रमांक",
    "guidelines_heading": "लागू मार्गदर्शक तत्वां", "checks_heading": "अनुपालन तपासण्यो",
    "requirements_heading": "नियामक गरजो", "recommendations_heading": "शिफारशी",
    "explainability_heading": "स्पश्टीकरणक्षमताय अहवाल",
    "top_factors": "मुखेल योगदान घटक", "features_explained": "स्पश्ट केल्ल्यो खाशेल्यायो",
    "explanation_language": "स्पश्टीकरणाची भास",
    "compliance_note": "हो स्पश्टीकरण {regulator} हाच्या कृत्रीम बुद्दीमत्ता स्पश्टीकरणक्षमताय मार्गदर्शक तत्वां प्रमाण तयार केल्लो",
    "disclaimer": "हो अहवाल {framework} हाच्या मार्गदर्शक तत्वांच्या पालनाचो दस्तावेज. निमाणें अनुपालन निर्धारण नेमिल्ल्या अनुपालन अधिकाऱ्याची जापसालदारकी.",
    "translation_notice": "हो अहवाल {language} भाशेंत यंत्र-अणकारीत. नियामक सादरीकरणाक इंग्लीश मजकूर प्रमाणीत.",
}

STATUS = {
    "COMPLIANT": "अनुपालीत", "REVIEW_NEEDED": "फेरतपासणी गरजेची",
    "PASS": "उत्तीर्ण", "FAIL": "अनुत्तीर्ण", "REVIEW": "फेरतपासणी",
}

DOMAINS = {
    "credit_scoring": "रीण मूल्यमापन", "insurance_underwriting": "विमो अंडररायटिंग",
    "healthcare": "भलायकी धोको मूल्यमापन",
}

REGULATORS = {
    "RBI": "भारतीय रिझर्व बॅंक",
    "IRDAI": "भारतीय विमो नियामक आनी विकास प्राधिकरण",
    "SEBI": "भारतीय रोखे आनी विनिमय मंडळ",
    "IndiaAI": "इंडियाएआय अभियान - जापसालदार कृत्रीम बुद्दीमत्ता चौकट",
}

REQUIREMENT_LABELS = {
    "explainability": "स्पश्टीकरणक्षमताय", "transparency": "पारदर्शकताय",
    "fairness": "निश्पक्षताय", "audit_trail": "लेखापरिक्षण खूण",
    "grievance_redressal": "कागाळ निवारण", "human_oversight": "मनीस देखरेख",
    "data_privacy": "म्हायती गुपीतताय", "model_governance": "प्रतिमान प्रशासन",
    "risk_disclosure": "धोको उगडावणी", "investor_protection": "गुंतवणूकदार संरक्षण",
    "accountability": "जापसालदारकी", "privacy": "गुपीतताय",
    "safety": "सुरक्षितताय", "inclusivity": "सगळ्यांक सांबाळप",
}

RECOMMENDATIONS = {
    "all_passed": "सगळ्यो अनुपालन तपासण्यो उत्तीर्ण. सद्याचें नियंत्रण तशेंच दवरात.",
    "schedule_review": "{regulator} हाच्या नेमाळ्या फेरतपासणी गरजे प्रमाण फुडली फेरतपासणी थारायात.",
    "revalidate": "प्रशासन वेळापत्रका प्रमाण प्रतिमानाची नेमाळी फेरपडताळणी खात्री करात.",
    "retain_logs": "स्पश्टीकरण नोंदी थारायिल्ल्या नियामक काळा मेरेन सांबाळात.",
    "address_failed": "अनुत्तीर्ण तपासणेचो निवाडो करात: {check}",
}

UI = {
    "app_title": "एक्सएआय प्लॅटफॉर्म",
    "app_subtitle": "नियमीत उद्देगांक बहुभाशीक स्पश्टीकरणक्षम कृत्रीम बुद्दीमत्ता",
    "select_domain": "निर्णय मळ वेंचात", "input_params": "इनपुट घटक",
    "load_sample": "नमुनो म्हायती भरात", "language_label": "स्पश्टीकरणाची भास",
    "generate_btn": "स्पश्टीकरण तयार करात", "generating": "तयार जाता...",
    "decision_label": "निर्णय", "confidence_label": "विस्वास",
    "risk_label": "धोको गुण", "audit_label": "लेखापरिक्षण क्रमांक",
    "explanation_heading": "कृत्रीम बुद्दीमत्ता निर्णय आनी स्पश्टीकरण",
    "contributions_heading": "खाशेल्यायांचें योगदान", "summary_heading": "स्पश्टीकरण सार",
    "report_btn": "अनुपालन अहवाल तयार करात",
    "print_btn": "अहवाल छापात", "report_generating": "अहवाल तयार जाता...",
    "coverage_label": "अणकार व्याप्ती", "needs_review_badge": "मातृभाशीक फेरतपासणी गरजेची",
    "footer_note": "आठव्या अनुसुचेच्यो २२ भासो आदार | लेखापरिक्षणयोग्य स्पश्टीकरणां",
    "yes": "हंय", "no": "ना",
}
