"""Sanskrit (संस्कृतम्) - Devanagari.

Core catalog. REQUIREMENT_TEXT and CHECKS fall back to English; see coverage.
"""

META = {
    "code": "sa", "name_native": "संस्कृतम्", "name_en": "Sanskrit",
    "script": "Devanagari", "rtl": False, "scheduled": True,
    "review_status": "needs_native_review",
}

FEATURES = {
    "annual_income": "वार्षिकम् आयः", "credit_history_months": "ऋणवृत्तम् (मासाः)",
    "existing_loans": "वर्तमानऋणानि", "loan_amount_requested": "प्रार्थिता ऋणराशिः",
    "employment_years": "सेवाकालः (वर्षाणि)", "monthly_expenses": "मासिकव्ययः",
    "age": "वयः", "defaults_in_past": "पूर्वप्रमादाः",
    "bmi": "देहभारसूचकः", "smoking_status": "धूमपानस्थितिः",
    "pre_existing_conditions": "पूर्वविद्यमानरोगाः",
    "family_history_score": "कुलवृत्तमानम्", "occupation_risk": "वृत्तिसम्बद्धसंकटम्",
    "coverage_amount": "बीमारक्षणराशिः", "symptoms_severity": "लक्षणतीव्रता",
    "lab_results_abnormal": "असामान्यपरीक्षाफलानि",
    "medical_history_score": "चिकित्सावृत्तमानम्",
    "vitals_risk_score": "प्राणचिह्नसंकटमानम्", "treatment_urgency": "चिकित्सायाः आवश्यकता",
}

DECISIONS = {
    "APPROVED": "अनुमोदितम्", "REJECTED": "निराकृतम्", "REVIEW_REQUIRED": "पुनरीक्षणम् आवश्यकम्",
    "STANDARD_PREMIUM": "प्रामाणिकः प्रीमियमः", "LOADED_PREMIUM": "अधिकः प्रीमियमः",
    "DECLINED": "निराकृतम्", "HIGH_RISK_INTERVENTION": "उच्चसंकटम् - हस्तक्षेपः",
    "MODERATE_RISK_MONITORING": "मध्यमसंकटम् - निरीक्षणम्",
    "LOW_RISK_ROUTINE": "अल्पसंकटम् - सामान्यम्",
}

EXPLANATION = {
    "positive_high": "{feature} इत्यस्य उच्चं मानम् ({value}) निर्णयम् अनुकूलदिशि अनयत्",
    "positive_low": "{feature} निर्णये अल्पम् अनुकूलं योगदानम् अदात्",
    "negative_high": "{feature} इत्यस्य मानम् ({value}) निर्णयं प्रतिकूलदिशि अनयत्",
    "negative_low": "{feature} निर्णये अल्पं प्रतिकूलं योगदानम् अदात्",
}

SUMMARY = {
    "credit_approved": "ऋणप्रार्थना अनुमोदिता। प्रमुखकारणानि: {factors}",
    "credit_rejected": "ऋणप्रार्थना निराकृता। प्रमुखकारणानि: {factors}",
    "credit_review": "ऋणप्रार्थना पुनरीक्षणार्थं प्रेषिता। विचारितकारणानि: {factors}",
    "insurance_standard": "प्रामाणिकः प्रीमियमः प्रयुज्यते। मूल्यांकनकारणानि: {factors}",
    "insurance_loaded": "अधिकः प्रीमियमः प्रयुज्यते। संकटकारणानि: {factors}",
    "insurance_declined": "बीमाप्रार्थना निराकृता। संकटकारणानि: {factors}",
    "health_high": "उच्चसंकटम् - सद्यः हस्तक्षेपः अनुशंसितः। कारणानि: {factors}",
    "health_moderate": "मध्यमसंकटम् - नियमितनिरीक्षणम् अनुशंसितम्। कारणानि: {factors}",
    "health_low": "अल्पसंकटम् - सामान्यम् अनुसरणम्। कारणानि: {factors}",
}

REPORT = {
    "title": "नियामकानुपालनप्रतिवेदनम्", "report_id": "प्रतिवेदनसंकेतः",
    "generated_at": "निर्मितसमयः", "regulator": "नियामकः", "domain": "क्षेत्रम्",
    "model_version": "प्रतिमानसंस्करणम्", "algorithm": "गणनविधिः",
    "explanation_method": "व्याख्याविधिः", "decision": "निर्णयः",
    "confidence": "विश्वासस्तरः", "risk_score": "संकटमानम्",
    "audit_id": "अंकेक्षणचिह्नसंकेतः",
    "guidelines_heading": "प्रयोज्यनिर्देशाः", "checks_heading": "अनुपालनपरीक्षाः",
    "requirements_heading": "नियामकापेक्षाः", "recommendations_heading": "अनुशंसाः",
    "explainability_heading": "व्याख्येयताप्रतिवेदनम्",
    "top_factors": "प्रमुखयोगदानकारणानि", "features_explained": "व्याख्यातलक्षणानि",
    "explanation_language": "व्याख्याभाषा",
    "compliance_note": "इदं व्याख्यानं {regulator} इत्यस्य कृत्रिमबुद्धिव्याख्येयतानिर्देशानुसारं निर्मितम्",
    "disclaimer": "इदं प्रतिवेदनं {framework} इत्यस्य निर्देशपालनस्य अभिलेखः। अन्तिमानुपालननिर्णयः नियुक्तानुपालनाधिकारिणः दायित्वम्।",
    "translation_notice": "इदं प्रतिवेदनं {language} भाषायां यन्त्रानूदितम्। नियामकप्रस्तुत्यर्थम् आङ्ग्लपाठः प्रामाणिकः।",
}

STATUS = {
    "COMPLIANT": "अनुपालितम्", "REVIEW_NEEDED": "पुनरीक्षणम् आवश्यकम्",
    "PASS": "उत्तीर्णम्", "FAIL": "अनुत्तीर्णम्", "REVIEW": "पुनरीक्षणम्",
}

DOMAINS = {
    "credit_scoring": "ऋणमूल्यांकनम्", "insurance_underwriting": "बीमास्वीकरणम्",
    "healthcare": "स्वास्थ्यसंकटमूल्यांकनम्",
}

REGULATORS = {
    "RBI": "भारतीयरिज़र्वबैङ्कः",
    "IRDAI": "भारतीयबीमानियामकविकासप्राधिकरणम्",
    "SEBI": "भारतीयप्रतिभूतिविनिमयमण्डलम्",
    "IndiaAI": "इण्डियाए॰आइ॰ अभियानम् - उत्तरदायिकृत्रिमबुद्धिरूपरेखा",
}

REQUIREMENT_LABELS = {
    "explainability": "व्याख्येयता", "transparency": "पारदर्शिता",
    "fairness": "निष्पक्षता", "audit_trail": "अंकेक्षणचिह्नम्",
    "grievance_redressal": "अभियोगनिवारणम्", "human_oversight": "मानवपर्यवेक्षणम्",
    "data_privacy": "दत्तगोपनीयता", "model_governance": "प्रतिमानशासनम्",
    "risk_disclosure": "संकटप्रकटीकरणम्", "investor_protection": "निवेशकसंरक्षणम्",
    "accountability": "उत्तरदायित्वम्", "privacy": "गोपनीयता",
    "safety": "सुरक्षा", "inclusivity": "समावेशिता",
}

RECOMMENDATIONS = {
    "all_passed": "सर्वाः अनुपालनपरीक्षाः उत्तीर्णाः। वर्तमाननियन्त्रणानि रक्षन्तु।",
    "schedule_review": "{regulator} इत्यस्य सामयिकपुनरीक्षणापेक्षानुसारं अग्रिमं पुनरीक्षणं निर्धारयन्तु।",
    "revalidate": "शासनसमयसूचीनुसारं प्रतिमानस्य सामयिकं पुनःप्रमाणीकरणं सुनिश्चितं कुर्वन्तु।",
    "retain_logs": "व्याख्याभिलेखान् निर्धारितनियामककालपर्यन्तं रक्षन्तु।",
    "address_failed": "अनुत्तीर्णपरीक्षायाः समाधानं कुर्वन्तु: {check}",
}

UI = {
    "app_title": "एक्स्-ए॰आइ॰ मञ्चः",
    "app_subtitle": "नियमितोद्योगार्थं बहुभाषिकव्याख्येयकृत्रिमबुद्धिः",
    "select_domain": "निर्णयक्षेत्रं चिनोतु", "input_params": "निवेशप्राचलाः",
    "load_sample": "निदर्शदत्तानि पूरयतु", "language_label": "व्याख्याभाषा",
    "generate_btn": "व्याख्यानं जनयतु", "generating": "जन्यते...",
    "decision_label": "निर्णयः", "confidence_label": "विश्वासः",
    "risk_label": "संकटमानम्", "audit_label": "अंकेक्षणसंकेतः",
    "explanation_heading": "कृत्रिमबुद्धिनिर्णयः व्याख्यानं च",
    "contributions_heading": "लक्षणयोगदानम्", "summary_heading": "व्याख्यासारः",
    "report_btn": "अनुपालनप्रतिवेदनं जनयतु",
    "print_btn": "प्रतिवेदनं मुद्रयतु", "report_generating": "प्रतिवेदनं जन्यते...",
    "coverage_label": "अनुवादव्याप्तिः", "needs_review_badge": "मातृभाषिपुनरीक्षणम् आवश्यकम्",
    "footer_note": "अष्टमानुसूच्याः २२ भाषाणां समर्थनम् | अंकेक्षणयोग्यव्याख्यानानि",
    "yes": "आम्", "no": "न",
}
