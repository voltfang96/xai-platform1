"""Nepali (नेपाली) - Devanagari.

Nepali is one of the 22 Eighth Schedule languages but was absent from the
original language list, which counted English toward the 22. Added here.

Core catalog. REQUIREMENT_TEXT and CHECKS fall back to English; see coverage.
"""

META = {
    "code": "ne", "name_native": "नेपाली", "name_en": "Nepali",
    "script": "Devanagari", "rtl": False, "scheduled": True,
    "review_status": "needs_native_review",
}

FEATURES = {
    "annual_income": "वार्षिक आय", "credit_history_months": "ऋण इतिहास (महिना)",
    "existing_loans": "विद्यमान ऋणहरू", "loan_amount_requested": "अनुरोध गरिएको ऋण रकम",
    "employment_years": "रोजगारी अवधि (वर्ष)", "monthly_expenses": "मासिक खर्च",
    "age": "उमेर", "defaults_in_past": "विगतको भुक्तानी चुक",
    "bmi": "शारीरिक भार सूचकाङ्क", "smoking_status": "धूमपान स्थिति",
    "pre_existing_conditions": "पहिले नै रहेका रोगहरू",
    "family_history_score": "पारिवारिक इतिहास अङ्क", "occupation_risk": "पेशागत जोखिम",
    "coverage_amount": "बीमा कभरेज रकम", "symptoms_severity": "लक्षणको गम्भीरता",
    "lab_results_abnormal": "असामान्य प्रयोगशाला नतिजा",
    "medical_history_score": "चिकित्सा इतिहास अङ्क",
    "vitals_risk_score": "जीवन सङ्केत जोखिम अङ्क", "treatment_urgency": "उपचारको तत्कालता",
}

DECISIONS = {
    "APPROVED": "स्वीकृत", "REJECTED": "अस्वीकृत", "REVIEW_REQUIRED": "पुनरावलोकन आवश्यक",
    "STANDARD_PREMIUM": "मानक बीमा शुल्क", "LOADED_PREMIUM": "थप बीमा शुल्क",
    "DECLINED": "अस्वीकृत", "HIGH_RISK_INTERVENTION": "उच्च जोखिम - हस्तक्षेप",
    "MODERATE_RISK_MONITORING": "मध्यम जोखिम - अनुगमन",
    "LOW_RISK_ROUTINE": "न्यून जोखिम - सामान्य",
}

EXPLANATION = {
    "positive_high": "{feature} को उच्च मान ({value}) ले निर्णयलाई अनुकूल दिशामा लग्यो",
    "positive_low": "{feature} ले निर्णयमा थोरै अनुकूल योगदान दियो",
    "negative_high": "{feature} को मान ({value}) ले निर्णयलाई प्रतिकूल दिशामा लग्यो",
    "negative_low": "{feature} ले निर्णयमा थोरै प्रतिकूल योगदान दियो",
}

SUMMARY = {
    "credit_approved": "ऋण आवेदन स्वीकृत भयो। मुख्य कारकहरू: {factors}",
    "credit_rejected": "ऋण आवेदन अस्वीकृत भयो। मुख्य कारणहरू: {factors}",
    "credit_review": "ऋण आवेदन पुनरावलोकनका लागि पठाइयो। विचार गरिएका कारकहरू: {factors}",
    "insurance_standard": "मानक बीमा शुल्क लागू। मूल्याङ्कन कारकहरू: {factors}",
    "insurance_loaded": "थप बीमा शुल्क लागू। जोखिम कारकहरू: {factors}",
    "insurance_declined": "बीमा आवेदन अस्वीकृत। जोखिम कारकहरू: {factors}",
    "health_high": "उच्च जोखिम - तत्काल हस्तक्षेप सिफारिस। कारकहरू: {factors}",
    "health_moderate": "मध्यम जोखिम - नियमित अनुगमन सिफारिस। कारकहरू: {factors}",
    "health_low": "न्यून जोखिम - सामान्य अनुसरण। कारकहरू: {factors}",
}

REPORT = {
    "title": "नियामक अनुपालन प्रतिवेदन", "report_id": "प्रतिवेदन क्रमाङ्क",
    "generated_at": "तयार पारिएको समय", "regulator": "नियामक", "domain": "क्षेत्र",
    "model_version": "मोडेल संस्करण", "algorithm": "अल्गोरिदम",
    "explanation_method": "स्पष्टीकरण विधि", "decision": "निर्णय",
    "confidence": "विश्वास स्तर", "risk_score": "जोखिम अङ्क",
    "audit_id": "लेखापरीक्षण अभिलेख क्रमाङ्क",
    "guidelines_heading": "लागू निर्देशिकाहरू", "checks_heading": "अनुपालन जाँचहरू",
    "requirements_heading": "नियामक आवश्यकताहरू", "recommendations_heading": "सिफारिसहरू",
    "explainability_heading": "स्पष्टीकरणयोग्यता प्रतिवेदन",
    "top_factors": "मुख्य योगदान कारकहरू", "features_explained": "स्पष्ट पारिएका विशेषताहरू",
    "explanation_language": "स्पष्टीकरणको भाषा",
    "compliance_note": "यो स्पष्टीकरण {regulator} को कृत्रिम बुद्धिमत्ता स्पष्टीकरणयोग्यता निर्देशिका अनुसार तयार पारिएको छ",
    "disclaimer": "यो प्रतिवेदन {framework} को निर्देशिका पालनाको अभिलेख हो। अन्तिम अनुपालन निर्धारण तोकिएको अनुपालन अधिकारीको जिम्मेवारी हो।",
    "translation_notice": "यो प्रतिवेदन {language} मा मसिन-अनुवादित छ। नियामक दाखिलाका लागि अङ्ग्रेजी पाठ प्रामाणिक हो।",
}

STATUS = {
    "COMPLIANT": "अनुपालित", "REVIEW_NEEDED": "पुनरावलोकन आवश्यक",
    "PASS": "उत्तीर्ण", "FAIL": "अनुत्तीर्ण", "REVIEW": "पुनरावलोकन",
}

DOMAINS = {
    "credit_scoring": "ऋण मूल्याङ्कन", "insurance_underwriting": "बीमा अन्डरराइटिङ",
    "healthcare": "स्वास्थ्य जोखिम मूल्याङ्कन",
}

REGULATORS = {
    "RBI": "भारतीय रिजर्भ बैंक",
    "IRDAI": "भारतीय बीमा नियामक तथा विकास प्राधिकरण",
    "SEBI": "भारतीय धितोपत्र तथा विनिमय बोर्ड",
    "IndiaAI": "इन्डियाएआई मिसन - जिम्मेवार कृत्रिम बुद्धिमत्ता संरचना",
}

REQUIREMENT_LABELS = {
    "explainability": "स्पष्टीकरणयोग्यता", "transparency": "पारदर्शिता",
    "fairness": "निष्पक्षता", "audit_trail": "लेखापरीक्षण अभिलेख",
    "grievance_redressal": "गुनासो सम्बोधन", "human_oversight": "मानवीय पर्यवेक्षण",
    "data_privacy": "तथ्याङ्क गोपनीयता", "model_governance": "मोडेल सुशासन",
    "risk_disclosure": "जोखिम प्रकटीकरण", "investor_protection": "लगानीकर्ता संरक्षण",
    "accountability": "उत्तरदायित्व", "privacy": "गोपनीयता",
    "safety": "सुरक्षा", "inclusivity": "समावेशिता",
}

RECOMMENDATIONS = {
    "all_passed": "सबै अनुपालन जाँच उत्तीर्ण। हालका नियन्त्रणहरू कायम राख्नुहोस्।",
    "schedule_review": "{regulator} को आवधिक पुनरावलोकन आवश्यकता अनुसार अर्को पुनरावलोकन तय गर्नुहोस्।",
    "revalidate": "सुशासन तालिका अनुसार मोडेलको आवधिक पुनःप्रमाणीकरण सुनिश्चित गर्नुहोस्।",
    "retain_logs": "स्पष्टीकरण अभिलेख तोकिएको नियामक अवधिसम्म सुरक्षित राख्नुहोस्।",
    "address_failed": "अनुत्तीर्ण जाँचको समाधान गर्नुहोस्: {check}",
}

UI = {
    "app_title": "एक्सएआई प्लेटफर्म",
    "app_subtitle": "नियमित उद्योगका लागि बहुभाषिक स्पष्टीकरणयोग्य कृत्रिम बुद्धिमत्ता",
    "select_domain": "निर्णय क्षेत्र छान्नुहोस्", "input_params": "इनपुट प्यारामिटर",
    "load_sample": "नमुना तथ्याङ्क भर्नुहोस्", "language_label": "स्पष्टीकरणको भाषा",
    "generate_btn": "स्पष्टीकरण बनाउनुहोस्", "generating": "बनिरहेको छ...",
    "decision_label": "निर्णय", "confidence_label": "विश्वास",
    "risk_label": "जोखिम अङ्क", "audit_label": "लेखापरीक्षण क्रमाङ्क",
    "explanation_heading": "कृत्रिम बुद्धिमत्ता निर्णय र स्पष्टीकरण",
    "contributions_heading": "विशेषताको योगदान", "summary_heading": "स्पष्टीकरण सारांश",
    "report_btn": "अनुपालन प्रतिवेदन बनाउनुहोस्", "report_generating": "प्रतिवेदन बनिरहेको छ...",
    "coverage_label": "अनुवाद व्याप्ति", "needs_review_badge": "मातृभाषी पुनरावलोकन आवश्यक",
    "footer_note": "आठौं अनुसूचीका २२ भाषाको समर्थन | लेखापरीक्षणयोग्य स्पष्टीकरण",
    "yes": "हो", "no": "होइन",
}
