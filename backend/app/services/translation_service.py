"""
Translation service.

Thin facade over ``app.i18n``. All strings live in the per-language catalogs;
this module only decides *which* key to look up for a given decision or
contribution. Keeping the policy here and the data there is what let the
language count grow from 10 partial dictionaries to 22 measured catalogs
without touching call sites.
"""
from typing import Dict, List

from app import i18n


class TranslationService:

    # ---- feature / decision naming -------------------------------------

    def translate_feature(self, feature: str, lang: str) -> str:
        return i18n.text(lang, "FEATURES", feature,
                         default=feature.replace("_", " ").title())

    def translate_decision(self, decision: str, lang: str) -> str:
        return i18n.text(lang, "DECISIONS", decision,
                         default=decision.replace("_", " ").title())

    def translate_domain(self, domain: str, lang: str) -> str:
        return i18n.text(lang, "DOMAINS", domain,
                         default=domain.replace("_", " ").title())

    def translate_regulator(self, regulator: str, lang: str) -> str:
        return i18n.text(lang, "REGULATORS", regulator, default=regulator)

    def translate_status(self, status: str, lang: str) -> str:
        return i18n.text(lang, "STATUS", status,
                         default=status.replace("_", " ").title())

    # ---- per-feature contribution explanations -------------------------

    @staticmethod
    def _explanation_key(contribution: float) -> str:
        """Pick the sentence template that matches sign and magnitude."""
        if contribution > 0.05:
            return "positive_high"
        if contribution > 0:
            return "positive_low"
        if contribution < -0.05:
            return "negative_high"
        return "negative_low"

    def translate_explanation(self, feature: str, value: float,
                              contribution: float, lang: str) -> str:
        template = i18n.text(lang, "EXPLANATION", self._explanation_key(contribution))
        return template.format(feature=self.translate_feature(feature, lang),
                               value=value)

    # ---- overall decision summary --------------------------------------

    # Maps (domain, decision) onto a summary template key. Explicit rather
    # than substring-matching on the decision string, which previously caused
    # insurance and healthcare decisions to fall through to credit wording.
    _SUMMARY_KEYS = {
        ("credit_scoring", "APPROVED"): "credit_approved",
        ("credit_scoring", "REJECTED"): "credit_rejected",
        ("credit_scoring", "REVIEW_REQUIRED"): "credit_review",
        ("insurance_underwriting", "STANDARD_PREMIUM"): "insurance_standard",
        ("insurance_underwriting", "LOADED_PREMIUM"): "insurance_loaded",
        ("insurance_underwriting", "DECLINED"): "insurance_declined",
        ("healthcare", "HIGH_RISK_INTERVENTION"): "health_high",
        ("healthcare", "MODERATE_RISK_MONITORING"): "health_moderate",
        ("healthcare", "LOW_RISK_ROUTINE"): "health_low",
    }

    def translate_summary(self, domain: str, decision: str,
                          top_factors: List[str], lang: str) -> str:
        factors = ", ".join(self.translate_feature(f, lang) for f in top_factors[:3])
        key = self._SUMMARY_KEYS.get((domain, decision))
        if key is None:
            # Unknown pairing: state the decision plainly rather than
            # mislabelling it with another domain's wording.
            return f"{self.translate_decision(decision, lang)}: {factors}"
        return i18n.text(lang, "SUMMARY", key).format(factors=factors)

    # ---- regulatory notes ----------------------------------------------

    def get_compliance_note(self, regulator: str, lang: str) -> str:
        return i18n.text(lang, "REPORT", "compliance_note").format(
            regulator=self.translate_regulator(regulator, lang))

    # ---- language metadata ---------------------------------------------

    def get_supported_languages(self) -> Dict[str, str]:
        """
        Code -> display label, for populating a picker.

        Labels combine the native name with the English name so a user who
        cannot read the target script can still find their language.
        """
        out = {}
        for code in i18n.available():
            meta = i18n.meta(code)
            native, english = meta.get("name_native", code), meta.get("name_en", code)
            out[code] = native if native == english else f"{native} ({english})"
        return out

    def get_language_details(self) -> Dict:
        """Full metadata including script, direction and translation coverage."""
        return i18n.catalog_summary()

    def is_rtl(self, lang: str) -> bool:
        return i18n.is_rtl(lang)

    def ui_strings(self, lang: str) -> Dict[str, str]:
        """UI label bundle for the frontend, English-filled where untranslated."""
        return i18n.section(lang, "UI")


translation_service = TranslationService()
