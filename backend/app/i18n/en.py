"""
Canonical English catalog.

This module defines the COMPLETE key contract. Every other language catalog is
measured against the keys declared here to produce a coverage figure, and any
key a language is missing falls back to the English string defined here.

If you add a key here, every language's coverage drops until it is translated.
That is intentional: it keeps gaps visible instead of silently English.
"""

META = {
    "code": "en",
    "name_native": "English",
    "name_en": "English",
    "script": "Latin",
    "rtl": False,
    "scheduled": False,  # not an Eighth Schedule language
    "review_status": "verified",
}

FEATURES = {
    "annual_income": "Annual Income",
    "credit_history_months": "Credit History (months)",
    "existing_loans": "Existing Loans",
    "loan_amount_requested": "Loan Amount Requested",
    "employment_years": "Years of Employment",
    "monthly_expenses": "Monthly Expenses",
    "age": "Age",
    "defaults_in_past": "Past Defaults",
    "bmi": "Body Mass Index",
    "smoking_status": "Smoking Status",
    "pre_existing_conditions": "Pre-existing Conditions",
    "family_history_score": "Family History Score",
    "occupation_risk": "Occupational Risk",
    "coverage_amount": "Coverage Amount",
    "symptoms_severity": "Symptom Severity",
    "lab_results_abnormal": "Abnormal Lab Results",
    "medical_history_score": "Medical History Score",
    "vitals_risk_score": "Vital Signs Risk Score",
    "treatment_urgency": "Treatment Urgency",
}

DECISIONS = {
    "APPROVED": "Approved",
    "REJECTED": "Rejected",
    "REVIEW_REQUIRED": "Review Required",
    "STANDARD_PREMIUM": "Standard Premium",
    "LOADED_PREMIUM": "Loaded Premium",
    "DECLINED": "Declined",
    "HIGH_RISK_INTERVENTION": "High Risk - Intervention",
    "MODERATE_RISK_MONITORING": "Moderate Risk - Monitoring",
    "LOW_RISK_ROUTINE": "Low Risk - Routine",
}

EXPLANATION = {
    "positive_high": "A high value for {feature} ({value}) pushed the decision favourably",
    "positive_low": "{feature} made a small favourable contribution to the decision",
    "negative_high": "The value of {feature} ({value}) pushed the decision unfavourably",
    "negative_low": "{feature} made a small unfavourable contribution to the decision",
}

SUMMARY = {
    "credit_approved": "The loan application was approved. Main factors: {factors}",
    "credit_rejected": "The loan application was rejected. Main reasons: {factors}",
    "credit_review": "The loan application was referred for review. Factors considered: {factors}",
    "insurance_standard": "Standard premium applies. Assessment factors: {factors}",
    "insurance_loaded": "A loaded premium applies. Risk factors: {factors}",
    "insurance_declined": "The insurance application was declined. Risk factors: {factors}",
    "health_high": "High risk - immediate intervention recommended. Factors: {factors}",
    "health_moderate": "Moderate risk - regular monitoring recommended. Factors: {factors}",
    "health_low": "Low risk - routine follow-up. Factors: {factors}",
}


REPORT = {
    "title": "Regulatory Compliance Report",
    "report_id": "Report ID",
    "generated_at": "Generated At",
    "regulator": "Regulator",
    "domain": "Domain",
    "model_version": "Model Version",
    "algorithm": "Algorithm",
    "explanation_method": "Explanation Method",
    "decision": "Decision",
    "confidence": "Confidence",
    "risk_score": "Risk Score",
    "audit_id": "Audit Trail ID",
    "guidelines_heading": "Applicable Guidelines",
    "checks_heading": "Compliance Checks",
    "requirements_heading": "Regulatory Requirements",
    "recommendations_heading": "Recommendations",
    "explainability_heading": "Explainability Report",
    "top_factors": "Top Contributing Factors",
    "features_explained": "Features Explained",
    "explanation_language": "Explanation Language",
    "compliance_note": "This explanation was prepared in accordance with {regulator} guidelines on AI explainability",
    "disclaimer": "This report documents adherence to {framework} guidelines on AI explainability. Final compliance determination rests with the designated compliance officer.",
    "translation_notice": "This report was machine-translated into {language}. The English text is authoritative for regulatory filing.",
}

STATUS = {
    "COMPLIANT": "Compliant",
    "REVIEW_NEEDED": "Review Needed",
    "PASS": "Pass",
    "FAIL": "Fail",
    "REVIEW": "Review",
}

DOMAINS = {
    "credit_scoring": "Credit Scoring",
    "insurance_underwriting": "Insurance Underwriting",
    "healthcare": "Healthcare Risk Assessment",
}

REGULATORS = {
    "RBI": "Reserve Bank of India",
    "IRDAI": "Insurance Regulatory and Development Authority of India",
    "SEBI": "Securities and Exchange Board of India",
    "IndiaAI": "IndiaAI Mission - Responsible AI Framework",
}

REQUIREMENT_LABELS = {
    "explainability": "Explainability",
    "transparency": "Transparency",
    "fairness": "Fairness",
    "audit_trail": "Audit Trail",
    "grievance_redressal": "Grievance Redressal",
    "human_oversight": "Human Oversight",
    "data_privacy": "Data Privacy",
    "model_governance": "Model Governance",
    "risk_disclosure": "Risk Disclosure",
    "investor_protection": "Investor Protection",
    "accountability": "Accountability",
    "privacy": "Privacy",
    "safety": "Safety",
    "inclusivity": "Inclusivity",
}

REQUIREMENT_TEXT = {
    "explainability": "Automated decisions must be accompanied by clear, understandable reasons",
    "transparency": "Affected individuals must be informed when AI is used in a decision",
    "fairness": "Models must be tested for bias across protected categories",
    "audit_trail": "A complete audit trail of decisions must be retained for the prescribed period",
    "grievance_redressal": "A clear mechanism must exist to challenge an automated decision",
    "human_oversight": "Decisions above the defined threshold must receive human review",
    "data_privacy": "Personal data handling must comply with the DPDP Act 2023",
    "model_governance": "Models must undergo periodic validation and revalidation",
    "risk_disclosure": "Risk assessments must disclose model limitations and assumptions",
    "investor_protection": "Retail participants must receive simplified explanations",
    "accountability": "A clear accountability chain for the decision must be documented",
    "privacy": "Data processing must comply with applicable privacy legislation",
    "safety": "The system must be assessed for potential harm to individuals or society",
    "inclusivity": "Explanations must be accessible in the individual's regional language",
}


# Each check has a short display name and a one-line evidence statement.
CHECKS = {
    "feature_explanation_provided": ("Feature Explanation Provided", "Every contributing feature is reported with an importance score"),
    "bias_metrics_documented": ("Bias Metrics Documented", "Bias testing metrics are recorded and within accepted thresholds"),
    "model_version_tracked": ("Model Version Tracked", "Model version and validation state are recorded with the decision"),
    "decision_rationale_clear": ("Decision Rationale Clear", "The rationale is expressed in language a non-specialist can follow"),
    "customer_notification_ready": ("Customer Notification Ready", "A customer-facing explanation is available in the selected language"),
    "audit_trail_complete": ("Audit Trail Complete", "A uniquely identified audit trail is retained for inspection"),
    "underwriting_factors_disclosed": ("Underwriting Factors Disclosed", "All factors affecting the underwriting outcome are disclosed"),
    "premium_rationale_clear": ("Premium Rationale Clear", "The basis for the premium loading is stated explicitly"),
    "no_genetic_discrimination": ("No Genetic Discrimination", "No genetic information was used as a decision input"),
    "data_privacy_compliant": ("Data Privacy Compliant", "Personal data handling follows the DPDP Act 2023"),
    "policyholder_notification": ("Policyholder Notification", "Notice of AI-assisted assessment is prepared for the policyholder"),
    "model_validation_current": ("Model Validation Current", "The model is within its scheduled validation window"),
    "risk_factors_explained": ("Risk Factors Explained", "Each risk factor influencing the assessment is explained"),
    "model_limitations_disclosed": ("Model Limitations Disclosed", "Known model limitations and assumptions are stated"),
    "no_market_manipulation": ("No Market Manipulation", "No manipulative pattern was detected in the decision logic"),
    "stress_test_documented": ("Stress Test Documented", "Behaviour under adverse conditions is documented"),
    "investor_notification": ("Investor Notification", "Notice of AI-assisted assessment is prepared for the investor"),
    "audit_trail_maintained": ("Audit Trail Maintained", "A complete audit trail is maintained for regulatory inspection"),
    "explanation_human_readable": ("Explanation Human Readable", "The explanation is rendered in plain, human-readable form"),
    "multilingual_support": ("Multilingual Support", "The explanation is available in Eighth Schedule languages"),
    "bias_testing_done": ("Bias Testing Done", "Bias testing across protected categories has been completed"),
    "accountability_assigned": ("Accountability Assigned", "An accountable owner is recorded for this decision"),
    "privacy_compliant": ("Privacy Compliant", "Processing is compliant with applicable privacy legislation"),
    "safety_assessed": ("Safety Assessed", "A safety assessment was completed with no harm identified"),
    "inclusive_design": ("Inclusive Design", "Regional language access is provided by design"),
}

RECOMMENDATIONS = {
    "all_passed": "All compliance checks passed. Maintain current controls.",
    "schedule_review": "Schedule the next review in line with {regulator} periodic review requirements.",
    "revalidate": "Ensure periodic model revalidation per the governance schedule.",
    "retain_logs": "Retain explanation logs for the prescribed regulatory retention period.",
    "address_failed": "Address the failed check: {check}",
}

UI = {
    "app_title": "XAI Platform",
    "app_subtitle": "Multilingual Explainable AI for Regulated Industries",
    "select_domain": "Select Decision Domain",
    "input_params": "Input Parameters",
    "load_sample": "Load Sample",
    "language_label": "Explanation Language",
    "generate_btn": "Generate Explanation",
    "generating": "Generating...",
    "decision_label": "Decision",
    "confidence_label": "Confidence",
    "risk_label": "Risk Score",
    "audit_label": "Audit ID",
    "explanation_heading": "AI Decision & Explanation",
    "contributions_heading": "Feature Contributions",
    "summary_heading": "Explanation Summary",
    "report_btn": "Generate Compliance Report",
    "report_generating": "Generating report...",
    "coverage_label": "Translation coverage",
    "needs_review_badge": "Awaiting native-speaker review",
    "footer_note": "Supports the 22 Eighth Schedule languages | Audit-ready explanations",
    "yes": "Yes",
    "no": "No",
}
