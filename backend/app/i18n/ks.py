"""Kashmiri (کٲشُر) - Perso-Arabic, right-to-left.

REDUCED catalog - core terms only. The longer regulatory sentences fall back to
English rather than being guessed at. See ``i18n.coverage('ks')``.
"""

META = {
    "code": "ks", "name_native": "کٲشُر", "name_en": "Kashmiri",
    "script": "Perso-Arabic", "rtl": True, "scheduled": True,
    "review_status": "needs_native_review",
}

FEATURES = {
    "annual_income": "سالانہ آمدنی", "credit_history_months": "قرضہ تٲریٖخ (ریٚتھ)",
    "existing_loans": "موجوٗد قرضہ", "loan_amount_requested": "طلب کرنہ آمُت قرضہ رقم",
    "employment_years": "نوکری مدت (ؤری)", "monthly_expenses": "ماہانہ خرچ",
    "age": "عُمر", "defaults_in_past": "پیٚٹھ کنہٕ ناکامی",
    "bmi": "جسمٲنی وزن اشاریہ", "smoking_status": "تمٲکھ نوٗشی حالت",
    "pre_existing_conditions": "بُنیٚادی بیمٲری",
    "family_history_score": "خانٛدٲنی تٲریٖخ سکور", "occupation_risk": "پیشہ ورانہ خطرٕ",
    "coverage_amount": "بیمہ کوریج رقم", "symptoms_severity": "علامات شدت",
    "lab_results_abnormal": "غیٚر معموٗلی لیب نتیجہ",
    "medical_history_score": "طِبی تٲریٖخ سکور",
    "vitals_risk_score": "حیٲتی علامات خطرٕ سکور", "treatment_urgency": "علاج ضرورت",
}

DECISIONS = {
    "APPROVED": "منظوٗر", "REJECTED": "نامنظوٗر", "REVIEW_REQUIRED": "جٲیزٕ ضروٗری",
    "STANDARD_PREMIUM": "معیٲری پریمیم", "LOADED_PREMIUM": "زیادٕ پریمیم",
    "DECLINED": "اِنکار", "HIGH_RISK_INTERVENTION": "زیادٕ خطرٕ - مداخلت",
    "MODERATE_RISK_MONITORING": "درمیٲنہ خطرٕ - نِگرٲنی",
    "LOW_RISK_ROUTINE": "کم خطرٕ - عام",
}

STATUS = {
    "COMPLIANT": "تعمیٖل شُدٕ", "REVIEW_NEEDED": "جٲیزٕ ضروٗری",
    "PASS": "کامیاب", "FAIL": "ناکام", "REVIEW": "جٲیزٕ",
}

DOMAINS = {
    "credit_scoring": "قرضہ جٲنٛچ", "insurance_underwriting": "بیمہ انڈر رٲیٹنٛگ",
    "healthcare": "صِحت خطرٕ جٲنٛچ",
}

REPORT = {
    "decision": "فیصلہ", "confidence": "اِعتِماد", "risk_score": "خطرٕ سکور",
    "domain": "شُعبہ", "regulator": "ضابطہ کار", "report_id": "رپورٹ شِناخت",
    "recommendations_heading": "سِفارِشات", "checks_heading": "تعمیٖل جٲنٛچ",
    "requirements_heading": "ضابطہ جٲتی تقاضٕ", "guidelines_heading": "قٲبِل اِطلاق ہِدایات",
}

REQUIREMENT_LABELS = {
    "explainability": "وضاحت پزیٖری", "transparency": "شفٲفیت",
    "fairness": "غیٚر جانٛبداری", "audit_trail": "آڈٹ ٹریٚل",
    "accountability": "جوابدِہی", "privacy": "رازداری", "safety": "سلامتی",
}

UI = {
    "decision_label": "فیصلہ", "confidence_label": "اِعتِماد",
    "risk_label": "خطرٕ سکور", "language_label": "وضاحت زبان",
    "generating": "بنان چھُ...", "yes": "آ", "no": "نہ",
    "needs_review_badge": "مادری زبان جٲیزٕ ضروٗری",
}
