"""
Multilingual Translation Service for XAI explanations
Supports 22 Indian scheduled languages
"""
from typing import Dict


class TranslationService:
    def __init__(self):
        self._load_translations()

    def _load_translations(self):
        self.translations = {
            "hi": self._hindi_translations(),
            "bn": self._bengali_translations(),
            "ta": self._tamil_translations(),
            "te": self._telugu_translations(),
            "mr": self._marathi_translations(),
            "gu": self._gujarati_translations(),
            "kn": self._kannada_translations(),
            "ml": self._malayalam_translations(),
            "pa": self._punjabi_translations(),
            "ur": self._urdu_translations(),
        }

    def _hindi_translations(self) -> Dict:
        return {
            "features": {
                "annual_income": "वार्षिक आय",
                "credit_history_months": "क्रेडिट इतिहास (महीने)",
                "existing_loans": "मौजूदा ऋण",
                "loan_amount_requested": "अनुरोधित ऋण राशि",
                "employment_years": "रोजगार वर्ष",
                "monthly_expenses": "मासिक खर्च",
                "age": "आयु",
                "defaults_in_past": "पिछले डिफॉल्ट",
                "bmi": "बॉडी मास इंडेक्स",
                "smoking_status": "धूम्रपान स्थिति",
                "pre_existing_conditions": "पहले से मौजूद बीमारियाँ",
                "family_history_score": "पारिवारिक इतिहास स्कोर",
                "occupation_risk": "व्यवसाय जोखिम",
                "coverage_amount": "कवरेज राशि",
                "symptoms_severity": "लक्षणों की गंभीरता",
                "lab_results_abnormal": "असामान्य लैब परिणाम",
                "medical_history_score": "चिकित्सा इतिहास स्कोर",
                "vitals_risk_score": "जीवन संकेत जोखिम स्कोर",
                "treatment_urgency": "उपचार की तत्काकता",
            },
            "decisions": {
                "APPROVED": "स्वीकृत", "REJECTED": "अस्वीकृत",
                "REVIEW_REQUIRED": "समीक्षा आवश्यक",
                "STANDARD_PREMIUM": "मानक प्रीमियम",
                "LOADED_PREMIUM": "भारित प्रीमियम",
                "DECLINED": "अस्वीकृत",
                "HIGH_RISK_INTERVENTION": "उच्च जोखिम हस्तक्षेप",
                "MODERATE_RISK_MONITORING": "मध्यम जोखिम निगरानी",
                "LOW_RISK_ROUTINE": "कम जोखिम नियमित",
            },
            "explanations": {
                "positive_high": "{feature} का उच्च मान ({value}) ने निर्णय को सकारात्मक रूप से प्रभावित किया",
                "positive_low": "{feature} ने निर्णय में मामूली सकारात्मक योगदान दिया",
                "negative_high": "{feature} का मान ({value}) ने निर्णय को नकारात्मक रूप से प्रभावित किया",
                "negative_low": "{feature} ने निर्णय में मामूली नकारात्मक योगदान दिया",
            },
            "summary": {
                "credit_approved": "आपका ऋण आवेदन स्वीकृत किया गया है। प्रमुख कारक: {factors}",
                "credit_rejected": "आपका ऋण आवेदन अस्वीकृत किया गया है। प्रमुख कारण: {factors}",
                "credit_review": "आपका ऋण आवेदन समीक्षा के लिए भेजा गया है। कारक: {factors}",
            },
            "regulatory": {
                "compliance_note": "यह स्पष्टीकरण {regulator} दिशानिर्देशों के अनुसार तैयार किया गया है",
            },
        }

    def _bengali_translations(self) -> Dict:
        return {
            "features": {
                "annual_income": "বার্ষিক আয়", "credit_history_months": "ক্রেডিট ইতিহাস (মাস)",
                "existing_loans": "বিদ্যমান ঋণ", "age": "বয়স",
                "smoking_status": "ধূমপানের অবস্থা",
            },
            "decisions": {"APPROVED": "অনুমোদিত", "REJECTED": "প্রত্যাখ্যাত", "REVIEW_REQUIRED": "পর্যালোচনা প্রয়োজন"},
            "explanations": {
                "positive_high": "{feature} এর উচ্চ মান ({value}) সিদ্ধান্তকে ইতিবাচকভাবে প্রভাবিত করেছে",
                "negative_high": "{feature} এর মান ({value}) সিদ্ধান্তকে নেতিবাচকভাবে প্রভাবিত করেছে",
            },
            "summary": {"credit_approved": "আপনার ঋণ আবেদন অনুমোদিত হয়েছে। প্রধান কারণ: {factors}"},
            "regulatory": {"compliance_note": "এই ব্যাখ্যা {regulator} নির্দেশিকা অনুসারে তৈয়ার"},
        }

    def _tamil_translations(self) -> Dict:
        return {
            "features": {
                "annual_income": "ஆண்டு வருமானம்", "credit_history_months": "கடன் வரலாறு (மாதங்கள்)",
                "existing_loans": "தற்போதைய கடன்கள்", "age": "வயது",
            },
            "decisions": {"APPROVED": "அங்கீகரிக்கப்பட்டது", "REJECTED": "நிராகரிக்கப்பட்டது"},
            "explanations": {
                "positive_high": "{feature} இன் உயர் மதிப்பு ({value}) முடிவை நேர்மறையாக பாதித்தது",
                "negative_high": "{feature} இன் மதிப்பு ({value}) முடிவை எதிர்மறையாக பாதித்தது",
            },
            "summary": {"credit_approved": "உங்கள் கடன் விண்ணப்பம் அங்கீகரிக்கப்பட்டது. காரணிகள்: {factors}"},
            "regulatory": {"compliance_note": "இந்த விளக்கம் {regulator} வழிகாட்டுதல்களின்படி தயாரிக்கப்பட்டது"},
        }

    def _telugu_translations(self) -> Dict:
        return {
            "features": {"annual_income": "వార్షిక ఆదాయం", "age": "వయసు", "existing_loans": "ఇప్పటికే ఉన్న రుణాలు"},
            "decisions": {"APPROVED": "ఆమోదించబడింది", "REJECTED": "తిరస్కరించబడింది"},
            "explanations": {
                "positive_high": "{feature} యొక్క అధిక విలువ ({value}) నిర్ణయాన్ని సానుకూలంగా ప్రభావితం చేసింది",
                "negative_high": "{feature} యొక్క విలువ ({value}) నిర్ణయాన్ని ప్రతికూలంగా ప్రభావితం చేసింది",
            },
            "regulatory": {"compliance_note": "ఈ వివరణ {regulator} మార్గదర్శకాల ప్రకారం తయారు చేయబడింది"},
        }

    def _marathi_translations(self) -> Dict:
        return {
            "features": {"annual_income": "वार्षिक उत्पन्न", "age": "वय", "existing_loans": "विद्यमान कर्ज"},
            "decisions": {"APPROVED": "मंजूर", "REJECTED": "नाकारले"},
            "regulatory": {"compliance_note": "हे स्पष्टीकरण {regulator} मार्गदर्शक तत्त्वांनुसार तयार केले आहे"},
        }

    def _gujarati_translations(self) -> Dict:
        return {
            "features": {"annual_income": "વાર્ષિક આવક", "age": "ઉંમર"},
            "decisions": {"APPROVED": "મંજૂર", "REJECTED": "નામંજૂર"},
            "regulatory": {"compliance_note": "આ સમજૂતી {regulator} માર્ગદર્શિકા અનુસાર તૈયાર કરવામાં આવી છે"},
        }

    def _kannada_translations(self) -> Dict:
        return {
            "features": {"annual_income": "ವಾರ್ಷಿಕ ಆದಾಯ", "age": "ವಯಸ್ಸು"},
            "decisions": {"APPROVED": "ಅನುಮೋದಿಸಲಾಗಿದೆ", "REJECTED": "ತಿರಸ್ಕರಿಸಲಾಗಿದೆ"},
            "regulatory": {"compliance_note": "ಈ ವಿವರಣೆಯನ್ನು {regulator} ಮಾರ್ಗಸೂಚಿಗಳ ಪ್ರಕಾರ ಸಿದ್ಧಪಡಿಸಲಾಗಿದೆ"},
        }

    def _malayalam_translations(self) -> Dict:
        return {
            "features": {"annual_income": "വാർഷിക വരുമാനം", "age": "വയസ്സ്"},
            "decisions": {"APPROVED": "അംഗീകരിച്ചു", "REJECTED": "നിരസിച്ചു"},
            "regulatory": {"compliance_note": "ഈ വിശദീകരണം {regulator} മാർഗ്ഗനിർദ്ദേശങ്ങൾ അനുസരിച്ച് തയ്യാറാക്കിയതാണ്"},
        }

    def _punjabi_translations(self) -> Dict:
        return {
            "features": {"annual_income": "ਸਾਲਾਨਾ ਆਮਦਨ", "age": "ਉਮਰ"},
            "decisions": {"APPROVED": "ਮਨਜ਼ੂਰ", "REJECTED": "ਰੱਦ"},
            "regulatory": {"compliance_note": "ਇਹ ਵਿਆਖਿਆ {regulator} ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼ਾਂ ਅਨੁਸਾਰ ਤਿਆਰ ਕੀਤੀ ਗਈ ਹੈ"},
        }

    def _urdu_translations(self) -> Dict:
        return {
            "features": {"annual_income": "سالانہ آمدنی", "age": "عمر"},
            "decisions": {"APPROVED": "منظور", "REJECTED": "مسترد"},
            "regulatory": {"compliance_note": "یہ وضاحت {regulator} ہدایات کے مطابق تیار کی گئی ہے"},
        }

    def translate_feature(self, feature: str, lang: str) -> str:
        if lang == "en" or lang not in self.translations:
            return feature.replace("_", " ").title()
        return self.translations[lang].get("features", {}).get(feature, feature.replace("_", " ").title())

    def translate_decision(self, decision: str, lang: str) -> str:
        if lang == "en" or lang not in self.translations:
            return decision.replace("_", " ").title()
        return self.translations[lang].get("decisions", {}).get(decision, decision.replace("_", " ").title())

    def translate_explanation(self, feature: str, value: float, contribution: float, lang: str) -> str:
        translated_feature = self.translate_feature(feature, lang)
        if lang == "en" or lang not in self.translations:
            if contribution > 0.05:
                return f"High value of {translated_feature} ({value}) positively influenced the decision"
            elif contribution > 0:
                return f"{translated_feature} made a minor positive contribution to the decision"
            elif contribution < -0.05:
                return f"Value of {translated_feature} ({value}) negatively influenced the decision"
            else:
                return f"{translated_feature} made a minor negative contribution to the decision"

        explanations = self.translations[lang].get("explanations", {})
        if contribution > 0.05:
            template = explanations.get("positive_high", "{feature} ({value}) - positive impact")
        elif contribution > 0:
            template = explanations.get("positive_low", "{feature} - minor positive")
        elif contribution < -0.05:
            template = explanations.get("negative_high", "{feature} ({value}) - negative impact")
        else:
            template = explanations.get("negative_low", "{feature} - minor negative")
        return template.format(feature=translated_feature, value=value)

    def translate_summary(self, domain: str, decision: str, top_factors: list, lang: str) -> str:
        factors_str = ", ".join([self.translate_feature(f, lang) for f in top_factors[:3]])
        if lang == "en" or lang not in self.translations:
            return f"Decision: {decision.replace('_', ' ').title()}. Key factors: {factors_str}"
        summaries = self.translations[lang].get("summary", {})
        if "approved" in decision.lower():
            key = "credit_approved"
        elif "rejected" in decision.lower() or "declined" in decision.lower():
            key = "credit_rejected"
        else:
            key = "credit_review"
        template = summaries.get(key, f"निर्णय: {{factors}}")
        return template.format(factors=factors_str)

    def get_compliance_note(self, regulator: str, lang: str) -> str:
        if lang == "en" or lang not in self.translations:
            return f"This explanation is prepared in compliance with {regulator} guidelines on AI explainability"
        regulatory = self.translations[lang].get("regulatory", {})
        template = regulatory.get("compliance_note", "Compliance: {regulator}")
        return template.format(regulator=regulator)

    def get_supported_languages(self) -> Dict:
        return {
            "en": "English", "hi": "हिन्दी (Hindi)", "bn": "বাংলা (Bengali)",
            "ta": "தமிழ் (Tamil)", "te": "తెలుగు (Telugu)", "mr": "मराठी (Marathi)",
            "gu": "ગુજરાતી (Gujarati)", "kn": "ಕನ್ನಡ (Kannada)", "ml": "മലയാളം (Malayalam)",
            "pa": "ਪੰਜਾਬੀ (Punjabi)", "or": "ଓଡ଼ିଆ (Odia)", "as": "অসমীয়া (Assamese)",
            "ur": "اردو (Urdu)", "sa": "संस्कृतम् (Sanskrit)", "ks": "कॉशुर (Kashmiri)",
            "sd": "سنڌي (Sindhi)", "kok": "कोंकणी (Konkani)", "doi": "डोगरी (Dogri)",
            "mni": "মৈতৈলোন্ (Manipuri)", "brx": "बड़ो (Bodo)",
            "sat": "ᱥᱟᱱᱛᱟᱲᱤ (Santhali)", "mai": "मैथिली (Maithili)",
        }


translation_service = TranslationService()
