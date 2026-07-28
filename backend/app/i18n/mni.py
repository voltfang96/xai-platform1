"""Manipuri / Meiteilon (মৈতৈলোন্) - Bengali script.

Manipuri is written in both the Bengali script and Meetei Mayek. The Bengali
script is used here because it remains the more widely deployed of the two in
software; a Meetei Mayek variant should be added as a separate catalog if the
audience requires it.

REDUCED catalog - only terms I am reasonably confident about. Longer regulatory
sentences fall back to English rather than being guessed at. See coverage.
"""

META = {
    "code": "mni", "name_native": "মৈতৈলোন্", "name_en": "Manipuri",
    "script": "Bengali", "rtl": False, "scheduled": True,
    "review_status": "needs_native_review",
}

FEATURES = {
    "annual_income": "চহীগী শেন্তম", "credit_history_months": "লোনগী পুৱারী (থা)",
    "existing_loans": "হৌজিক্কী লোনশিং", "loan_amount_requested": "নীজখিবা লোনগী শেন্ফম",
    "employment_years": "থবক তৌবগী মতম (চহী)", "monthly_expenses": "থাগী চাদিং",
    "age": "চহী", "defaults_in_past": "মমাংগী অসোয়বা",
    "bmi": "হকচাংগী অরুম মশক", "smoking_status": "হিদাক থকপগী ফিভম",
    "pre_existing_conditions": "হান্নদগী লৈরিবা লায়না",
    "family_history_score": "ইমুংগী পুৱারী মায়েক", "occupation_risk": "থবক্কী খুদোংথিবা",
    "coverage_amount": "ইনসিওরেন্সগী শেন্ফম", "symptoms_severity": "লায়নাগী মশক কনবা",
    "lab_results_abnormal": "অচুম্বা নত্তবা লেব ফল",
    "medical_history_score": "হকশেলগী পুৱারী মায়েক",
    "vitals_risk_score": "পুন্সিগী খুদোংথিবা মায়েক", "treatment_urgency": "লায়েংবগী অথুবা",
}

DECISIONS = {
    "APPROVED": "য়াবা পীরে", "REJECTED": "য়াদ্রে", "REVIEW_REQUIRED": "অমুক য়েংবা তঙাইফদে",
    "STANDARD_PREMIUM": "মপুং ফাবা প্রিমিয়ম", "LOADED_PREMIUM": "হেনগৎপা প্রিমিয়ম",
    "DECLINED": "য়াদ্রে", "HIGH_RISK_INTERVENTION": "অৱাংবা খুদোংথিবা - শীনফম",
    "MODERATE_RISK_MONITORING": "মরিলমদগী খুদোংথিবা - য়েংশিনবা",
    "LOW_RISK_ROUTINE": "নেম্বা খুদোংথিবা - মহৌশা",
}

STATUS = {
    "COMPLIANT": "ইন্না চৎপা", "REVIEW_NEEDED": "অমুক য়েংবা তঙাইফদে",
    "PASS": "ঙম্লে", "FAIL": "ঙমদ্রে", "REVIEW": "অমুক য়েংবা",
}

DOMAINS = {
    "credit_scoring": "লোন য়েংশিনবা", "insurance_underwriting": "ইনসিওরেন্স অন্দররাইটিং",
    "healthcare": "হকশেলগী খুদোংথিবা য়েংশিনবা",
}

REPORT = {
    "decision": "ৱারেপ", "confidence": "থাজবা", "risk_score": "খুদোংথিবা মায়েক",
    "domain": "লমদম", "regulator": "নিয়ামক",
    "recommendations_heading": "পাউতাক", "checks_heading": "ইন্না চৎপগী য়েংবা",
}

UI = {
    "decision_label": "ৱারেপ", "confidence_label": "থাজবা",
    "risk_label": "খুদোংথিবা মায়েক", "language_label": "শন্দোকপগী লোল",
    "generating": "শেম্লি...", "yes": "হোয়", "no": "নত্তে",
    "needs_review_badge": "মপা লোল ঙাংবগী য়েংবা তঙাইফদে",
}
