"""Gujarati (ગુજરાતી) - Gujarati script."""

META = {
    "code": "gu", "name_native": "ગુજરાતી", "name_en": "Gujarati",
    "script": "Gujarati", "rtl": False, "scheduled": True,
    "review_status": "verified",
}

FEATURES = {
    "annual_income": "વાર્ષિક આવક", "credit_history_months": "ધિરાણ ઇતિહાસ (મહિના)",
    "existing_loans": "વર્તમાન ધિરાણ", "loan_amount_requested": "માંગેલી ધિરાણ રકમ",
    "employment_years": "નોકરીનો સમય (વર્ષ)", "monthly_expenses": "માસિક ખર્ચ",
    "age": "ઉંમર", "defaults_in_past": "ભૂતકાળની ચૂક",
    "bmi": "શરીર દ્રવ્યમાન સૂચકાંક", "smoking_status": "ધૂમ્રપાનની સ્થિતિ",
    "pre_existing_conditions": "પૂર્વ-વિદ્યમાન રોગો",
    "family_history_score": "કૌટુંબિક ઇતિહાસ ગુણ", "occupation_risk": "વ્યાવસાયિક જોખમ",
    "coverage_amount": "વીમા કવચ રકમ", "symptoms_severity": "લક્ષણોની તીવ્રતા",
    "lab_results_abnormal": "અસામાન્ય પ્રયોગશાળા પરિણામ",
    "medical_history_score": "તબીબી ઇતિહાસ ગુણ",
    "vitals_risk_score": "જીવનસંકેત જોખમ ગુણ", "treatment_urgency": "સારવારની તાત્કાલિકતા",
}

DECISIONS = {
    "APPROVED": "મંજૂર", "REJECTED": "નામંજૂર", "REVIEW_REQUIRED": "સમીક્ષા આવશ્યક",
    "STANDARD_PREMIUM": "પ્રમાણિત પ્રીમિયમ", "LOADED_PREMIUM": "વધારાનું પ્રીમિયમ",
    "DECLINED": "નકારેલ", "HIGH_RISK_INTERVENTION": "ઉચ્ચ જોખમ - હસ્તક્ષેપ",
    "MODERATE_RISK_MONITORING": "મધ્યમ જોખમ - દેખરેખ",
    "LOW_RISK_ROUTINE": "નીચું જોખમ - નિયમિત",
}

EXPLANATION = {
    "positive_high": "{feature} નું ઊંચું મૂલ્ય ({value}) નિર્ણયને અનુકૂળ દિશામાં લઈ ગયું",
    "positive_low": "{feature} એ નિર્ણયમાં અલ્પ અનુકૂળ યોગદાન આપ્યું",
    "negative_high": "{feature} નું મૂલ્ય ({value}) નિર્ણયને પ્રતિકૂળ દિશામાં લઈ ગયું",
    "negative_low": "{feature} એ નિર્ણયમાં અલ્પ પ્રતિકૂળ યોગદાન આપ્યું",
}

SUMMARY = {
    "credit_approved": "ધિરાણ અરજી મંજૂર થઈ. મુખ્ય પરિબળો: {factors}",
    "credit_rejected": "ધિરાણ અરજી નામંજૂર થઈ. મુખ્ય કારણો: {factors}",
    "credit_review": "ધિરાણ અરજી સમીક્ષા માટે મોકલી. વિચારેલા પરિબળો: {factors}",
    "insurance_standard": "પ્રમાણિત પ્રીમિયમ લાગુ. મૂલ્યાંકન પરિબળો: {factors}",
    "insurance_loaded": "વધારાનું પ્રીમિયમ લાગુ. જોખમ પરિબળો: {factors}",
    "insurance_declined": "વીમા અરજી નકારેલ. જોખમ પરિબળો: {factors}",
    "health_high": "ઉચ્ચ જોખમ - તાત્કાલિક હસ્તક્ષેપ સૂચિત. પરિબળો: {factors}",
    "health_moderate": "મધ્યમ જોખમ - નિયમિત દેખરેખ સૂચિત. પરિબળો: {factors}",
    "health_low": "નીચું જોખમ - નિયમિત અનુવર્તન. પરિબળો: {factors}",
}

REPORT = {
    "title": "નિયામક અનુપાલન અહેવાલ", "report_id": "અહેવાલ ક્રમાંક",
    "generated_at": "તૈયાર કર્યાનો સમય", "regulator": "નિયામક", "domain": "ક્ષેત્ર",
    "model_version": "મોડેલ સંસ્કરણ", "algorithm": "અલ્ગોરિદમ",
    "explanation_method": "સ્પષ્ટીકરણ પદ્ધતિ", "decision": "નિર્ણય",
    "confidence": "વિશ્વાસ સ્તર", "risk_score": "જોખમ ગુણ",
    "audit_id": "ઓડિટ ટ્રેલ ક્રમાંક",
    "guidelines_heading": "લાગુ માર્ગદર્શિકા", "checks_heading": "અનુપાલન તપાસ",
    "requirements_heading": "નિયામક આવશ્યકતાઓ", "recommendations_heading": "ભલામણો",
    "explainability_heading": "સ્પષ્ટીકરણક્ષમતા અહેવાલ",
    "top_factors": "મુખ્ય યોગદાન પરિબળો", "features_explained": "સ્પષ્ટ કરેલી વિશેષતાઓ",
    "explanation_language": "સ્પષ્ટીકરણની ભાષા",
    "compliance_note": "આ સ્પષ્ટીકરણ {regulator} ની કૃત્રિમ બુદ્ધિ સ્પષ્ટીકરણક્ષમતા માર્ગદર્શિકા અનુસાર તૈયાર કરેલ છે",
    "disclaimer": "આ અહેવાલ {framework} ની માર્ગદર્શિકાના પાલનનો દસ્તાવેજ છે. અંતિમ અનુપાલન નિર્ધારણ નિયુક્ત અનુપાલન અધિકારીની જવાબદારી છે.",
    "translation_notice": "આ અહેવાલ {language} માં યંત્ર-અનુવાદિત છે. નિયામક રજૂઆત માટે અંગ્રેજી લખાણ પ્રમાણભૂત છે.",
}

STATUS = {
    "COMPLIANT": "અનુપાલિત", "REVIEW_NEEDED": "સમીક્ષા આવશ્યક",
    "PASS": "ઉત્તીર્ણ", "FAIL": "અનુત્તીર્ણ", "REVIEW": "સમીક્ષા",
}

DOMAINS = {
    "credit_scoring": "ધિરાણ મૂલ્યાંકન", "insurance_underwriting": "વીમા અંડરરાઇટિંગ",
    "healthcare": "આરોગ્ય જોખમ મૂલ્યાંકન",
}

REGULATORS = {
    "RBI": "ભારતીય રિઝર્વ બેંક",
    "IRDAI": "ભારતીય વીમા નિયામક અને વિકાસ પ્રાધિકરણ",
    "SEBI": "ભારતીય પ્રતિભૂતિ અને વિનિમય બોર્ડ",
    "IndiaAI": "ઇન્ડિયાએઆઈ મિશન - જવાબદાર કૃત્રિમ બુદ્ધિ ઢાંચો",
}

REQUIREMENT_LABELS = {
    "explainability": "સ્પષ્ટીકરણક્ષમતા", "transparency": "પારદર્શકતા",
    "fairness": "નિષ્પક્ષતા", "audit_trail": "ઓડિટ ટ્રેલ",
    "grievance_redressal": "ફરિયાદ નિવારણ", "human_oversight": "માનવ દેખરેખ",
    "data_privacy": "ડેટા ગોપનીયતા", "model_governance": "મોડેલ સુશાસન",
    "risk_disclosure": "જોખમ પ્રકટીકરણ", "investor_protection": "રોકાણકાર સંરક્ષણ",
    "accountability": "જવાબદેહી", "privacy": "ગોપનીયતા",
    "safety": "સુરક્ષા", "inclusivity": "સમાવેશકતા",
}

REQUIREMENT_TEXT = {
    "explainability": "સ્વયંસંચાલિત નિર્ણયો સાથે સ્પષ્ટ અને સમજી શકાય તેવા કારણો હોવા જોઈએ",
    "transparency": "નિર્ણયમાં કૃત્રિમ બુદ્ધિના ઉપયોગની જાણ સંબંધિત વ્યક્તિને કરવી જોઈએ",
    "fairness": "સંરક્ષિત વર્ગોના સંદર્ભમાં મોડેલની પૂર્વગ્રહ ચકાસણી થવી જોઈએ",
    "audit_trail": "નિર્ણયોનો સંપૂર્ણ ઓડિટ ટ્રેલ નિર્ધારિત સમય સુધી જાળવવો જોઈએ",
    "grievance_redressal": "સ્વયંસંચાલિત નિર્ણયને પડકારવાની સ્પષ્ટ વ્યવસ્થા હોવી જોઈએ",
    "human_oversight": "નિર્ધારિત મર્યાદાથી ઉપરના નિર્ણયોની માનવ સમીક્ષા આવશ્યક છે",
    "data_privacy": "વ્યક્તિગત ડેટા સંચાલન ડીપીડીપી અધિનિયમ ૨૦૨૩ અનુસાર હોવું જોઈએ",
    "model_governance": "મોડેલોની સમયાંતરે ચકાસણી અને પુનઃચકાસણી થવી જોઈએ",
    "risk_disclosure": "જોખમ મૂલ્યાંકનમાં મોડેલની મર્યાદાઓ અને ધારણાઓ પ્રકટ થવી જોઈએ",
    "investor_protection": "છૂટક રોકાણકારોને સરળ સ્પષ્ટીકરણ મળવું જોઈએ",
    "accountability": "નિર્ણય માટે સ્પષ્ટ જવાબદેહી શ્રૃંખલા નોંધાયેલી હોવી જોઈએ",
    "privacy": "ડેટા પ્રક્રિયા લાગુ ગોપનીયતા કાયદા અનુસાર હોવી જોઈએ",
    "safety": "વ્યક્તિ કે સમાજને સંભવિત નુકસાનનું મૂલ્યાંકન થવું જોઈએ",
    "inclusivity": "સ્પષ્ટીકરણ વ્યક્તિની પ્રાદેશિક ભાષામાં ઉપલબ્ધ હોવું જોઈએ",
}

CHECKS = {
    "feature_explanation_provided": ("વિશેષતા સ્પષ્ટીકરણ પ્રદાન", "યોગદાન આપતી પ્રત્યેક વિશેષતા મહત્ત્વ ગુણ સાથે નોંધાયેલી છે"),
    "bias_metrics_documented": ("પૂર્વગ્રહ માપદંડ નોંધાયેલ", "પૂર્વગ્રહ ચકાસણી માપદંડ નોંધાયેલા અને સ્વીકાર્ય મર્યાદામાં છે"),
    "model_version_tracked": ("મોડેલ સંસ્કરણ નોંધાયેલ", "નિર્ણય સાથે મોડેલ સંસ્કરણ અને ચકાસણી સ્થિતિ નોંધાયેલી છે"),
    "decision_rationale_clear": ("નિર્ણયનો તર્ક સ્પષ્ટ", "તર્ક બિન-નિષ્ણાત પણ સમજી શકે તેવી ભાષામાં છે"),
    "customer_notification_ready": ("ગ્રાહક સૂચના તૈયાર", "પસંદ કરેલી ભાષામાં ગ્રાહક માટે સ્પષ્ટીકરણ ઉપલબ્ધ છે"),
    "audit_trail_complete": ("ઓડિટ ટ્રેલ પૂર્ણ", "વિશિષ્ટ ઓળખ ધરાવતો ટ્રેલ નિરીક્ષણ માટે જાળવેલ છે"),
    "underwriting_factors_disclosed": ("અંડરરાઇટિંગ પરિબળો પ્રકટ", "અંડરરાઇટિંગ પરિણામને પ્રભાવિત કરતા સર્વ પરિબળો પ્રકટ છે"),
    "premium_rationale_clear": ("પ્રીમિયમનો આધાર સ્પષ્ટ", "પ્રીમિયમ વધારાનો આધાર સ્પષ્ટપણે દર્શાવેલ છે"),
    "no_genetic_discrimination": ("આનુવંશિક ભેદભાવ નથી", "નિર્ણયમાં કોઈ આનુવંશિક માહિતી વપરાયેલી નથી"),
    "data_privacy_compliant": ("ડેટા ગોપનીયતા અનુપાલિત", "વ્યક્તિગત ડેટા સંચાલન ડીપીડીપી અધિનિયમ ૨૦૨૩ અનુસાર છે"),
    "policyholder_notification": ("પોલિસીધારક સૂચના", "કૃત્રિમ બુદ્ધિ સહાયિત મૂલ્યાંકનની સૂચના તૈયાર છે"),
    "model_validation_current": ("મોડેલ ચકાસણી વર્તમાન", "મોડેલ તેની નિર્ધારિત ચકાસણી અવધિમાં છે"),
    "risk_factors_explained": ("જોખમ પરિબળો સ્પષ્ટ", "મૂલ્યાંકનને પ્રભાવિત કરતું પ્રત્યેક જોખમ પરિબળ સ્પષ્ટ છે"),
    "model_limitations_disclosed": ("મોડેલ મર્યાદાઓ પ્રકટ", "મોડેલની જ્ઞાત મર્યાદાઓ અને ધારણાઓ દર્શાવેલી છે"),
    "no_market_manipulation": ("બજાર ચાલાકી નથી", "નિર્ણય તર્કમાં કોઈ ચાલાકીભરી પ્રવૃત્તિ મળી નથી"),
    "stress_test_documented": ("તાણ પરીક્ષણ નોંધાયેલ", "પ્રતિકૂળ પરિસ્થિતિમાં વર્તન નોંધાયેલ છે"),
    "investor_notification": ("રોકાણકાર સૂચના", "કૃત્રિમ બુદ્ધિ સહાયિત મૂલ્યાંકનની સૂચના તૈયાર છે"),
    "audit_trail_maintained": ("ઓડિટ ટ્રેલ જાળવેલ", "નિયામક નિરીક્ષણ માટે સંપૂર્ણ ટ્રેલ જાળવેલ છે"),
    "explanation_human_readable": ("સ્પષ્ટીકરણ માનવ-વાચનીય", "સ્પષ્ટીકરણ સરળ, માનવ-વાચનીય સ્વરૂપે છે"),
    "multilingual_support": ("બહુભાષી સમર્થન", "સ્પષ્ટીકરણ આઠમી અનુસૂચિની ભાષાઓમાં ઉપલબ્ધ છે"),
    "bias_testing_done": ("પૂર્વગ્રહ ચકાસણી પૂર્ણ", "સંરક્ષિત વર્ગોમાં પૂર્વગ્રહ ચકાસણી પૂર્ણ થઈ છે"),
    "accountability_assigned": ("જવાબદેહી નિર્ધારિત", "આ નિર્ણય માટે જવાબદાર વ્યક્તિ નોંધાયેલી છે"),
    "privacy_compliant": ("ગોપનીયતા અનુપાલિત", "પ્રક્રિયા લાગુ ગોપનીયતા કાયદા અનુસાર છે"),
    "safety_assessed": ("સુરક્ષા મૂલ્યાંકિત", "સુરક્ષા મૂલ્યાંકન પૂર્ણ, કોઈ નુકસાન ઓળખાયું નથી"),
    "inclusive_design": ("સમાવેશક રચના", "પ્રાદેશિક ભાષા પ્રવેશ રચનામાં જ પ્રદાન કરેલ છે"),
}

RECOMMENDATIONS = {
    "all_passed": "સર્વ અનુપાલન તપાસ ઉત્તીર્ણ. વર્તમાન નિયંત્રણો જાળવો.",
    "schedule_review": "{regulator} ની સમયાંતરે સમીક્ષા આવશ્યકતા અનુસાર આગામી સમીક્ષા નિર્ધારિત કરો.",
    "revalidate": "સુશાસન સમયપત્રક અનુસાર મોડેલની સમયાંતરે પુનઃચકાસણી સુનિશ્ચિત કરો.",
    "retain_logs": "સ્પષ્ટીકરણ નોંધો નિર્ધારિત નિયામક અવધિ સુધી જાળવો.",
    "address_failed": "અનુત્તીર્ણ તપાસનું નિવારણ કરો: {check}",
}

UI = {
    "app_title": "એક્સએઆઈ પ્લેટફોર્મ",
    "app_subtitle": "નિયમિત ઉદ્યોગો માટે બહુભાષી સ્પષ્ટીકરણક્ષમ કૃત્રિમ બુદ્ધિ",
    "select_domain": "નિર્ણય ક્ષેત્ર પસંદ કરો", "input_params": "ઇનપુટ પરિમાણ",
    "load_sample": "નમૂના ડેટા ભરો", "language_label": "સ્પષ્ટીકરણની ભાષા",
    "generate_btn": "સ્પષ્ટીકરણ બનાવો", "generating": "બની રહ્યું છે...",
    "decision_label": "નિર્ણય", "confidence_label": "વિશ્વાસ",
    "risk_label": "જોખમ ગુણ", "audit_label": "ઓડિટ ક્રમાંક",
    "explanation_heading": "કૃત્રિમ બુદ્ધિ નિર્ણય અને સ્પષ્ટીકરણ",
    "contributions_heading": "વિશેષતાઓનું યોગદાન", "summary_heading": "સ્પષ્ટીકરણ સારાંશ",
    "report_btn": "અનુપાલન અહેવાલ બનાવો",
    "print_btn": "અહેવાલ છાપો", "report_generating": "અહેવાલ બની રહ્યો છે...",
    "coverage_label": "અનુવાદ વ્યાપ", "needs_review_badge": "માતૃભાષી સમીક્ષા આવશ્યક",
    "footer_note": "આઠમી અનુસૂચિની ૨૨ ભાષાઓનું સમર્થન | ઓડિટ-યોગ્ય સ્પષ્ટીકરણ",
    "yes": "હા", "no": "ના",
}
