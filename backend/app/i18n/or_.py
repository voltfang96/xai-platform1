"""Odia (ଓଡ଼ିଆ) - Odia script.

Core catalog: explanation output, report labels/statuses and UI are translated.
REQUIREMENT_TEXT and CHECKS evidence lines still fall back to English and are
reported as a coverage gap by ``i18n.coverage('or')``.
"""

META = {
    "code": "or", "name_native": "ଓଡ଼ିଆ", "name_en": "Odia",
    "script": "Odia", "rtl": False, "scheduled": True,
    "review_status": "needs_native_review",
}

FEATURES = {
    "annual_income": "ବାର୍ଷିକ ଆୟ", "credit_history_months": "ଋଣ ଇତିହାସ (ମାସ)",
    "existing_loans": "ବର୍ତ୍ତମାନ ଋଣ", "loan_amount_requested": "ଅନୁରୋଧ କରାଯାଇଥିବା ଋଣ ରାଶି",
    "employment_years": "ନିଯୁକ୍ତି ଅବଧି (ବର୍ଷ)", "monthly_expenses": "ମାସିକ ବ୍ୟୟ",
    "age": "ବୟସ", "defaults_in_past": "ପୂର୍ବ ଖିଲାପ",
    "bmi": "ଶରୀର ଓଜନ ସୂଚକାଙ୍କ", "smoking_status": "ଧୂମପାନ ସ୍ଥିତି",
    "pre_existing_conditions": "ପୂର୍ବରୁ ଥିବା ରୋଗ",
    "family_history_score": "ପାରିବାରିକ ଇତିହାସ ସ୍କୋର", "occupation_risk": "ବୃତ୍ତିଗତ ବିପଦ",
    "coverage_amount": "ବୀମା ସୁରକ୍ଷା ରାଶି", "symptoms_severity": "ଲକ୍ଷଣର ତୀବ୍ରତା",
    "lab_results_abnormal": "ଅସ୍ୱାଭାବିକ ଲାବ ଫଳାଫଳ",
    "medical_history_score": "ଚିକିତ୍ସା ଇତିହାସ ସ୍କୋର",
    "vitals_risk_score": "ଜୀବନ ସଙ୍କେତ ବିପଦ ସ୍କୋର", "treatment_urgency": "ଚିକିତ୍ସାର ଆବଶ୍ୟକତା",
}

DECISIONS = {
    "APPROVED": "ଅନୁମୋଦିତ", "REJECTED": "ପ୍ରତ୍ୟାଖ୍ୟାତ", "REVIEW_REQUIRED": "ସମୀକ୍ଷା ଆବଶ୍ୟକ",
    "STANDARD_PREMIUM": "ମାନକ ପ୍ରିମିୟମ", "LOADED_PREMIUM": "ଅତିରିକ୍ତ ପ୍ରିମିୟମ",
    "DECLINED": "ପ୍ରତ୍ୟାଖ୍ୟାତ", "HIGH_RISK_INTERVENTION": "ଉଚ୍ଚ ବିପଦ - ହସ୍ତକ୍ଷେପ",
    "MODERATE_RISK_MONITORING": "ମଧ୍ୟମ ବିପଦ - ନିରୀକ୍ଷଣ",
    "LOW_RISK_ROUTINE": "କମ ବିପଦ - ସାଧାରଣ",
}

EXPLANATION = {
    "positive_high": "{feature} ର ଉଚ୍ଚ ମୂଲ୍ୟ ({value}) ନିର୍ଣ୍ଣୟକୁ ଅନୁକୂଳ ଦିଶାରେ ନେଇଥିଲା",
    "positive_low": "{feature} ନିର୍ଣ୍ଣୟରେ ଅଲ୍ପ ଅନୁକୂଳ ଯୋଗଦାନ ଦେଇଥିଲା",
    "negative_high": "{feature} ର ମୂଲ୍ୟ ({value}) ନିର୍ଣ୍ଣୟକୁ ପ୍ରତିକୂଳ ଦିଶାରେ ନେଇଥିଲା",
    "negative_low": "{feature} ନିର୍ଣ୍ଣୟରେ ଅଲ୍ପ ପ୍ରତିକୂଳ ଯୋଗଦାନ ଦେଇଥିଲା",
}

SUMMARY = {
    "credit_approved": "ଋଣ ଆବେଦନ ଅନୁମୋଦିତ ହେଲା। ମୁଖ୍ୟ କାରକ: {factors}",
    "credit_rejected": "ଋଣ ଆବେଦନ ପ୍ରତ୍ୟାଖ୍ୟାତ ହେଲା। ମୁଖ୍ୟ କାରଣ: {factors}",
    "credit_review": "ଋଣ ଆବେଦନ ସମୀକ୍ଷା ପାଇଁ ପଠାଯାଇଛି। ବିଚାର କରାଯାଇଥିବା କାରକ: {factors}",
    "insurance_standard": "ମାନକ ପ୍ରିମିୟମ ପ୍ରଯୁଜ୍ୟ। ମୂଲ୍ୟାଙ୍କନ କାରକ: {factors}",
    "insurance_loaded": "ଅତିରିକ୍ତ ପ୍ରିମିୟମ ପ୍ରଯୁଜ୍ୟ। ବିପଦ କାରକ: {factors}",
    "insurance_declined": "ବୀମା ଆବେଦନ ପ୍ରତ୍ୟାଖ୍ୟାତ। ବିପଦ କାରକ: {factors}",
    "health_high": "ଉଚ୍ଚ ବିପଦ - ତତ୍କ୍ଷଣାତ ହସ୍ତକ୍ଷେପ ସୁପାରିଶ। କାରକ: {factors}",
    "health_moderate": "ମଧ୍ୟମ ବିପଦ - ନିୟମିତ ନିରୀକ୍ଷଣ ସୁପାରିଶ। କାରକ: {factors}",
    "health_low": "କମ ବିପଦ - ସାଧାରଣ ଅନୁସରଣ। କାରକ: {factors}",
}

REPORT = {
    "title": "ନିୟାମକ ଅନୁପାଳନ ରିପୋର୍ଟ", "report_id": "ରିପୋର୍ଟ ପରିଚୟ",
    "generated_at": "ପ୍ରସ୍ତୁତ ସମୟ", "regulator": "ନିୟାମକ", "domain": "କ୍ଷେତ୍ର",
    "model_version": "ମଡେଲ ସଂସ୍କରଣ", "algorithm": "ଆଲଗୋରିଦମ",
    "explanation_method": "ବ୍ୟାଖ୍ୟା ପଦ୍ଧତି", "decision": "ନିର୍ଣ୍ଣୟ",
    "confidence": "ବିଶ୍ୱାସ ସ୍ତର", "risk_score": "ବିପଦ ସ୍କୋର",
    "audit_id": "ଅଙ୍କେକ୍ଷଣ ଚିହ୍ନ ପରିଚୟ",
    "guidelines_heading": "ପ୍ରଯୁଜ୍ୟ ମାର୍ଗଦର୍ଶିକା", "checks_heading": "ଅନୁପାଳନ ଯାଞ୍ଚ",
    "requirements_heading": "ନିୟାମକ ଆବଶ୍ୟକତା", "recommendations_heading": "ସୁପାରିଶ",
    "explainability_heading": "ବ୍ୟାଖ୍ୟାଯୋଗ୍ୟତା ରିପୋର୍ଟ",
    "top_factors": "ମୁଖ୍ୟ ଯୋଗଦାନ କାରକ", "features_explained": "ବ୍ୟାଖ୍ୟା କରାଯାଇଥିବା ବୈଶିଷ୍ଟ୍ୟ",
    "explanation_language": "ବ୍ୟାଖ୍ୟାର ଭାଷା",
    "compliance_note": "ଏହି ବ୍ୟାଖ୍ୟା {regulator} ର କୃତ୍ରିମ ବୁଦ୍ଧିମତ୍ତା ବ୍ୟାଖ୍ୟାଯୋଗ୍ୟତା ମାର୍ଗଦର୍ଶିକା ଅନୁସାରେ ପ୍ରସ୍ତୁତ",
    "disclaimer": "ଏହି ରିପୋର୍ଟ {framework} ର ମାର୍ଗଦର୍ଶିକା ପାଳନର ଦଲିଲ। ଅନ୍ତିମ ଅନୁପାଳନ ନିର୍ଣ୍ଣୟ ନିଯୁକ୍ତ ଅନୁପାଳନ ଅଧିକାରୀର ଦାୟିତ୍ୱ।",
    "translation_notice": "ଏହି ରିପୋର୍ଟ {language} ରେ ଯନ୍ତ୍ର-ଅନୁବାଦିତ। ନିୟାମକ ଦାଖଲ ପାଇଁ ଇଂରାଜୀ ପାଠ ପ୍ରାମାଣିକ।",
}

STATUS = {
    "COMPLIANT": "ଅନୁପାଳିତ", "REVIEW_NEEDED": "ସମୀକ୍ଷା ଆବଶ୍ୟକ",
    "PASS": "ଉତ୍ତୀର୍ଣ୍ଣ", "FAIL": "ଅନୁତ୍ତୀର୍ଣ୍ଣ", "REVIEW": "ସମୀକ୍ଷା",
}

DOMAINS = {
    "credit_scoring": "ଋଣ ମୂଲ୍ୟାଙ୍କନ", "insurance_underwriting": "ବୀମା ଅଣ୍ଡରରାଇଟିଂ",
    "healthcare": "ସ୍ୱାସ୍ଥ୍ୟ ବିପଦ ମୂଲ୍ୟାଙ୍କନ",
}

REGULATORS = {
    "RBI": "ଭାରତୀୟ ରିଜର୍ଭ ବ୍ୟାଙ୍କ",
    "IRDAI": "ଭାରତୀୟ ବୀମା ନିୟାମକ ଓ ବିକାଶ ପ୍ରାଧିକରଣ",
    "SEBI": "ଭାରତୀୟ ପ୍ରତିଭୂତି ଓ ବିନିମୟ ବୋର୍ଡ",
    "IndiaAI": "ଇଣ୍ଡିଆଏଆଇ ମିଶନ - ଦାୟିତ୍ୱପୂର୍ଣ୍ଣ କୃତ୍ରିମ ବୁଦ୍ଧିମତ୍ତା ଢାଞ୍ଚା",
}

REQUIREMENT_LABELS = {
    "explainability": "ବ୍ୟାଖ୍ୟାଯୋଗ୍ୟତା", "transparency": "ପାରଦର୍ଶିତା",
    "fairness": "ନିରପେକ୍ଷତା", "audit_trail": "ଅଙ୍କେକ୍ଷଣ ଚିହ୍ନ",
    "grievance_redressal": "ଅଭିଯୋଗ ନିବାରଣ", "human_oversight": "ମାନବ ତତ୍ତ୍ୱାବଧାନ",
    "data_privacy": "ତଥ୍ୟ ଗୋପନୀୟତା", "model_governance": "ମଡେଲ ପରିଚାଳନା",
    "risk_disclosure": "ବିପଦ ପ୍ରକଟୀକରଣ", "investor_protection": "ନିବେଶକ ସୁରକ୍ଷା",
    "accountability": "ଉତ୍ତରଦାୟିତ୍ୱ", "privacy": "ଗୋପନୀୟତା",
    "safety": "ସୁରକ୍ଷା", "inclusivity": "ସମାବେଶୀତା",
}

RECOMMENDATIONS = {
    "all_passed": "ସମସ୍ତ ଅନୁପାଳନ ଯାଞ୍ଚ ଉତ୍ତୀର୍ଣ୍ଣ। ବର୍ତ୍ତମାନ ନିୟନ୍ତ୍ରଣ ବଜାୟ ରଖନ୍ତୁ।",
    "schedule_review": "{regulator} ର ସାମୟିକ ସମୀକ୍ଷା ଆବଶ୍ୟକତା ଅନୁସାରେ ପରବର୍ତ୍ତୀ ସମୀକ୍ଷା ନିର୍ଧାରଣ କରନ୍ତୁ।",
    "revalidate": "ପରିଚାଳନା ସମୟସୂଚୀ ଅନୁସାରେ ମଡେଲର ସାମୟିକ ପୁନଃପ୍ରମାଣୀକରଣ ସୁନିଶ୍ଚିତ କରନ୍ତୁ।",
    "retain_logs": "ବ୍ୟାଖ୍ୟା ଅଭିଲେଖ ନିର୍ଧାରିତ ନିୟାମକ ଅବଧି ପର୍ଯ୍ୟନ୍ତ ସଂରକ୍ଷଣ କରନ୍ତୁ।",
    "address_failed": "ଅନୁତ୍ତୀର୍ଣ୍ଣ ଯାଞ୍ଚର ସମାଧାନ କରନ୍ତୁ: {check}",
}

UI = {
    "app_title": "ଏକ୍ସଏଆଇ ପ୍ଲାଟଫର୍ମ",
    "app_subtitle": "ନିୟନ୍ତ୍ରିତ ଉଦ୍ୟୋଗ ପାଇଁ ବହୁଭାଷୀ ବ୍ୟାଖ୍ୟାଯୋଗ୍ୟ କୃତ୍ରିମ ବୁଦ୍ଧିମତ୍ତା",
    "select_domain": "ନିର୍ଣ୍ଣୟ କ୍ଷେତ୍ର ବାଛନ୍ତୁ", "input_params": "ଇନପୁଟ ପାରାମିଟର",
    "load_sample": "ନମୁନା ତଥ୍ୟ ଭରନ୍ତୁ", "language_label": "ବ୍ୟାଖ୍ୟାର ଭାଷା",
    "generate_btn": "ବ୍ୟାଖ୍ୟା ପ୍ରସ୍ତୁତ କରନ୍ତୁ", "generating": "ପ୍ରସ୍ତୁତ ହେଉଛି...",
    "decision_label": "ନିର୍ଣ୍ଣୟ", "confidence_label": "ବିଶ୍ୱାସ",
    "risk_label": "ବିପଦ ସ୍କୋର", "audit_label": "ଅଙ୍କେକ୍ଷଣ ପରିଚୟ",
    "explanation_heading": "କୃତ୍ରିମ ବୁଦ୍ଧିମତ୍ତା ନିର୍ଣ୍ଣୟ ଓ ବ୍ୟାଖ୍ୟା",
    "contributions_heading": "ବୈଶିଷ୍ଟ୍ୟର ଯୋଗଦାନ", "summary_heading": "ବ୍ୟାଖ୍ୟା ସାରାଂଶ",
    "report_btn": "ଅନୁପାଳନ ରିପୋର୍ଟ ପ୍ରସ୍ତୁତ କରନ୍ତୁ", "report_generating": "ରିପୋର୍ଟ ପ୍ରସ୍ତୁତ ହେଉଛି...",
    "coverage_label": "ଅନୁବାଦ ପରିସର", "needs_review_badge": "ମାତୃଭାଷୀ ସମୀକ୍ଷା ଆବଶ୍ୟକ",
    "footer_note": "ଅଷ୍ଟମ ଅନୁସୂଚୀର ୨୨ ଭାଷାର ସମର୍ଥନ | ଅଙ୍କେକ୍ଷଣଯୋଗ୍ୟ ବ୍ୟାଖ୍ୟା",
    "yes": "ହଁ", "no": "ନା",
}
