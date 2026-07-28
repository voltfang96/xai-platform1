"""Maithili (मैथिली) - Devanagari.

Core catalog. REQUIREMENT_TEXT and CHECKS fall back to English; see coverage.
"""

META = {
    "code": "mai", "name_native": "मैथिली", "name_en": "Maithili",
    "script": "Devanagari", "rtl": False, "scheduled": True,
    "review_status": "needs_native_review",
}

FEATURES = {
    "annual_income": "वार्षिक आय", "credit_history_months": "ऋण इतिहास (मास)",
    "existing_loans": "वर्तमान ऋण", "loan_amount_requested": "मांगल गेल ऋण राशि",
    "employment_years": "रोजगारक अवधि (वर्ष)", "monthly_expenses": "मासिक व्यय",
    "age": "उमेर", "defaults_in_past": "पूर्वक चूक",
    "bmi": "देह भार सूचक", "smoking_status": "धूम्रपानक स्थिति",
    "pre_existing_conditions": "पहिनहि सँ रहल रोग",
    "family_history_score": "पारिवारिक इतिहास अंक", "occupation_risk": "व्यावसायिक जोखिम",
    "coverage_amount": "बीमा सुरक्षा राशि", "symptoms_severity": "लक्षणक तीव्रता",
    "lab_results_abnormal": "असामान्य प्रयोगशाला परिणाम",
    "medical_history_score": "चिकित्सा इतिहास अंक",
    "vitals_risk_score": "जीवन संकेत जोखिम अंक", "treatment_urgency": "उपचारक तत्कालता",
}

DECISIONS = {
    "APPROVED": "स्वीकृत", "REJECTED": "अस्वीकृत", "REVIEW_REQUIRED": "पुनरीक्षण आवश्यक",
    "STANDARD_PREMIUM": "मानक प्रीमियम", "LOADED_PREMIUM": "बढ़ल प्रीमियम",
    "DECLINED": "अस्वीकृत", "HIGH_RISK_INTERVENTION": "उच्च जोखिम - हस्तक्षेप",
    "MODERATE_RISK_MONITORING": "मध्यम जोखिम - निगरानी",
    "LOW_RISK_ROUTINE": "कम जोखिम - सामान्य",
}

EXPLANATION = {
    "positive_high": "{feature} क उच्च मान ({value}) निर्णयकेँ अनुकूल दिशामे लऽ गेल",
    "positive_low": "{feature} निर्णयमे थोड़ अनुकूल योगदान देलक",
    "negative_high": "{feature} क मान ({value}) निर्णयकेँ प्रतिकूल दिशामे लऽ गेल",
    "negative_low": "{feature} निर्णयमे थोड़ प्रतिकूल योगदान देलक",
}

SUMMARY = {
    "credit_approved": "ऋण आवेदन स्वीकृत भेल। मुख्य कारक: {factors}",
    "credit_rejected": "ऋण आवेदन अस्वीकृत भेल। मुख्य कारण: {factors}",
    "credit_review": "ऋण आवेदन पुनरीक्षण हेतु पठाओल गेल। विचारल गेल कारक: {factors}",
    "insurance_standard": "मानक प्रीमियम लागू। मूल्यांकन कारक: {factors}",
    "insurance_loaded": "बढ़ल प्रीमियम लागू। जोखिम कारक: {factors}",
    "insurance_declined": "बीमा आवेदन अस्वीकृत। जोखिम कारक: {factors}",
    "health_high": "उच्च जोखिम - तत्काल हस्तक्षेपक अनुशंसा। कारक: {factors}",
    "health_moderate": "मध्यम जोखिम - नियमित निगरानीक अनुशंसा। कारक: {factors}",
    "health_low": "कम जोखिम - सामान्य अनुसरण। कारक: {factors}",
}

REPORT = {
    "title": "नियामक अनुपालन प्रतिवेदन", "report_id": "प्रतिवेदन संख्या",
    "generated_at": "तैयार करबाक समय", "regulator": "नियामक", "domain": "क्षेत्र",
    "model_version": "मॉडल संस्करण", "algorithm": "अल्गोरिदम",
    "explanation_method": "व्याख्या विधि", "decision": "निर्णय",
    "confidence": "विश्वासक स्तर", "risk_score": "जोखिम अंक",
    "audit_id": "अंकेक्षण अभिलेख संख्या",
    "guidelines_heading": "लागू निर्देश", "checks_heading": "अनुपालन जाँच",
    "requirements_heading": "नियामक आवश्यकता", "recommendations_heading": "अनुशंसा",
    "explainability_heading": "व्याख्येयता प्रतिवेदन",
    "top_factors": "मुख्य योगदान कारक", "features_explained": "व्याख्या कएल गेल विशेषता",
    "explanation_language": "व्याख्याक भाषा",
    "compliance_note": "ई व्याख्या {regulator} क कृत्रिम बुद्धि व्याख्येयता निर्देशक अनुसार तैयार कएल गेल",
    "disclaimer": "ई प्रतिवेदन {framework} क निर्देशक पालनक अभिलेख अछि। अन्तिम अनुपालन निर्धारण नियुक्त अनुपालन अधिकारीक दायित्व अछि।",
    "translation_notice": "ई प्रतिवेदन {language} मे यन्त्र-अनूदित अछि। नियामक प्रस्तुति हेतु अंग्रेजी पाठ प्रामाणिक अछि।",
}

STATUS = {
    "COMPLIANT": "अनुपालित", "REVIEW_NEEDED": "पुनरीक्षण आवश्यक",
    "PASS": "उत्तीर्ण", "FAIL": "अनुत्तीर्ण", "REVIEW": "पुनरीक्षण",
}

DOMAINS = {
    "credit_scoring": "ऋण मूल्यांकन", "insurance_underwriting": "बीमा अंडरराइटिंग",
    "healthcare": "स्वास्थ्य जोखिम मूल्यांकन",
}

REGULATORS = {
    "RBI": "भारतीय रिजर्व बैंक",
    "IRDAI": "भारतीय बीमा नियामक आ विकास प्राधिकरण",
    "SEBI": "भारतीय प्रतिभूति आ विनिमय बोर्ड",
    "IndiaAI": "इंडियाएआई मिशन - उत्तरदायी कृत्रिम बुद्धि ढाँचा",
}

REQUIREMENT_LABELS = {
    "explainability": "व्याख्येयता", "transparency": "पारदर्शिता",
    "fairness": "निष्पक्षता", "audit_trail": "अंकेक्षण अभिलेख",
    "grievance_redressal": "शिकायत निवारण", "human_oversight": "मानवीय पर्यवेक्षण",
    "data_privacy": "आँकड़ा गोपनीयता", "model_governance": "मॉडल शासन",
    "risk_disclosure": "जोखिम प्रकटीकरण", "investor_protection": "निवेशक संरक्षण",
    "accountability": "जवाबदेही", "privacy": "गोपनीयता",
    "safety": "सुरक्षा", "inclusivity": "समावेशिता",
}

RECOMMENDATIONS = {
    "all_passed": "सभ अनुपालन जाँच उत्तीर्ण। वर्तमान नियंत्रण बनाए रखू।",
    "schedule_review": "{regulator} क सामयिक पुनरीक्षण आवश्यकताक अनुसार अगिला पुनरीक्षण निर्धारित करू।",
    "revalidate": "शासन समयसूचीक अनुसार मॉडलक सामयिक पुनःप्रमाणीकरण सुनिश्चित करू।",
    "retain_logs": "व्याख्या अभिलेख निर्धारित नियामक अवधि धरि सुरक्षित रखू।",
    "address_failed": "अनुत्तीर्ण जाँचक समाधान करू: {check}",
}

UI = {
    "app_title": "एक्सएआई प्लेटफॉर्म",
    "app_subtitle": "नियमित उद्योग हेतु बहुभाषी व्याख्येय कृत्रिम बुद्धि",
    "select_domain": "निर्णय क्षेत्र चुनू", "input_params": "इनपुट पैरामीटर",
    "load_sample": "नमूना आँकड़ा भरू", "language_label": "व्याख्याक भाषा",
    "generate_btn": "व्याख्या बनाबू", "generating": "बनि रहल अछि...",
    "decision_label": "निर्णय", "confidence_label": "विश्वास",
    "risk_label": "जोखिम अंक", "audit_label": "अंकेक्षण संख्या",
    "explanation_heading": "कृत्रिम बुद्धि निर्णय आ व्याख्या",
    "contributions_heading": "विशेषताक योगदान", "summary_heading": "व्याख्या सारांश",
    "report_btn": "अनुपालन प्रतिवेदन बनाबू", "report_generating": "प्रतिवेदन बनि रहल अछि...",
    "coverage_label": "अनुवाद विस्तार", "needs_review_badge": "मातृभाषी पुनरीक्षण आवश्यक",
    "footer_note": "अष्टम अनुसूचीक २२ भाषाक समर्थन | अंकेक्षणयोग्य व्याख्या",
    "yes": "हँ", "no": "नहि",
}
