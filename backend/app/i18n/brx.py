"""Bodo (बड़ो) - Devanagari.

REDUCED catalog. Bodo is a lower-resource language and I could not produce
confident translations for the longer regulatory sentences. Only terms I am
reasonably confident about are included; everything else deliberately falls
back to English rather than guessing, and ``i18n.coverage('brx')`` reports the
resulting gap. Have a native speaker complete this file before any real filing.
"""

META = {
    "code": "brx", "name_native": "बड़ो", "name_en": "Bodo",
    "script": "Devanagari", "rtl": False, "scheduled": True,
    "review_status": "needs_native_review",
}

FEATURES = {
    "annual_income": "बोसोरारि आय", "credit_history_months": "रिन जरासे (दान)",
    "existing_loans": "दानि रिन", "loan_amount_requested": "खावनाय रिन बिबां",
    "employment_years": "खामानि सम (बोसोर)", "monthly_expenses": "दानारि खरसा",
    "age": "बैसो", "defaults_in_past": "आगोलनि गोरोन्थि",
    "bmi": "देहा गिदिं सुजुगरा", "smoking_status": "थामाखु जानाय",
    "pre_existing_conditions": "सिगांनिफ्राय दंनाय बेराम",
    "family_history_score": "नखर जरासे अंख", "occupation_risk": "खामानिनि सोंखानथि",
    "coverage_amount": "बिमा रैखाथि बिबां", "symptoms_severity": "बेरामनि गोब्राब",
    "lab_results_abnormal": "गोयै लेब फिथाइ",
    "medical_history_score": "फरायसालि जरासे अंख",
    "vitals_risk_score": "जिउनि सोंखानथि अंख", "treatment_urgency": "सुस्रुनायनि गोनांथि",
}

DECISIONS = {
    "APPROVED": "आजावबाय", "REJECTED": "नेवसिबाय", "REVIEW_REQUIRED": "फिन नाजिनाय गोनां",
    "STANDARD_PREMIUM": "थाखोमानि प्रिमियाम", "LOADED_PREMIUM": "बांद्राय प्रिमियाम",
    "DECLINED": "नेवसिबाय", "HIGH_RISK_INTERVENTION": "गोजौ सोंखानथि - हांख्रायनाय",
    "MODERATE_RISK_MONITORING": "गेजेर सोंखानथि - नाजिनाय",
    "LOW_RISK_ROUTINE": "खम सोंखानथि - सरासनस्रा",
}

STATUS = {
    "COMPLIANT": "आजावनाय", "REVIEW_NEEDED": "फिन नाजिनाय गोनां",
    "PASS": "जाबाय", "FAIL": "जायाखै", "REVIEW": "फिन नाजिनाय",
}

DOMAINS = {
    "credit_scoring": "रिन बिजिरनाय", "insurance_underwriting": "बिमा आन्डाররाइटिं",
    "healthcare": "देहा सोंखानथि बिजिरनाय",
}

REPORT = {
    "decision": "सानथौ", "confidence": "फोथायनाय", "risk_score": "सोंखानथि अंख",
    "domain": "मंथाइ", "regulator": "नियामक",
    "recommendations_heading": "सल्ला", "checks_heading": "आजावनाय नाजिनाय",
}

UI = {
    "decision_label": "सानथौ", "confidence_label": "फोथायनाय",
    "risk_label": "सोंखानथि अंख", "language_label": "बिबुंथिनि राव",
    "generating": "बानायगासिनो दं...", "yes": "नंगौ", "no": "नङा",
    "needs_review_badge": "आफानि राव नाजिनाय गोनां",
}
