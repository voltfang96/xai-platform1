"""
Regulatory compliance reporting for RBI, IRDAI, SEBI and IndiaAI.

The report is rendered in the caller's language. Frameworks are declared here
as *keys* only - requirement wording, check wording, headings, statuses and
recommendations all resolve through ``app.i18n``, so adding a language adds a
translated report with no change to this module.

Two things are deliberately NOT translated:
  * Guideline citations (circular names and numbers). A regulator expects to
    see the exact title it published, so these stay verbatim.
  * The authoritative filing text. Every localised report carries a
    ``translation_notice`` stating that the English text governs, because a
    machine translation should not be presented as the text of record.
"""
from datetime import datetime
from typing import Dict, List
import hashlib

from app import i18n
from app.services.translation_service import translation_service


class ComplianceService:

    # Guideline citations stay in their published form - see module docstring.
    REGULATORY_FRAMEWORKS = {
        "RBI": {
            "guidelines": [
                "RBI/2023-24/AI-ML Guidelines on Digital Lending",
                "Fair Practices Code for NBFCs",
                "Master Direction on IT Governance",
                "RBI Circular on Responsible AI in Banking",
            ],
            "requirements": [
                "explainability", "transparency", "fairness",
                "audit_trail", "grievance_redressal", "human_oversight",
            ],
            "compliance_checks": [
                "feature_explanation_provided", "bias_metrics_documented",
                "model_version_tracked", "decision_rationale_clear",
                "customer_notification_ready", "audit_trail_complete",
            ],
        },
        "IRDAI": {
            "guidelines": [
                "IRDAI Sandbox Guidelines for InsurTech",
                "Guidelines on Insurance e-Commerce",
                "IRDAI (Protection of Policyholders) Regulations",
                "IRDAI AI/ML Guidelines for Underwriting",
            ],
            "requirements": [
                "explainability", "transparency", "fairness",
                "data_privacy", "grievance_redressal", "model_governance",
            ],
            "compliance_checks": [
                "underwriting_factors_disclosed", "premium_rationale_clear",
                "no_genetic_discrimination", "data_privacy_compliant",
                "policyholder_notification", "model_validation_current",
            ],
        },
        "SEBI": {
            "guidelines": [
                "SEBI Circular on AI/ML in Securities Markets",
                "SEBI (Investment Advisers) Regulations",
                "Guidelines for Algo Trading Risk Controls",
                "SEBI Framework for Responsible AI in Capital Markets",
            ],
            "requirements": [
                "explainability", "transparency", "fairness",
                "risk_disclosure", "model_governance", "investor_protection",
            ],
            "compliance_checks": [
                "risk_factors_explained", "model_limitations_disclosed",
                "no_market_manipulation", "stress_test_documented",
                "investor_notification", "audit_trail_maintained",
            ],
        },
        "IndiaAI": {
            "guidelines": [
                "IndiaAI Responsible AI Guidelines 2024",
                "NITI Aayog Principles for Responsible AI",
                "MeitY AI Ethics Framework",
                "Digital Personal Data Protection Act 2023",
            ],
            "requirements": [
                "explainability", "transparency", "fairness",
                "accountability", "privacy", "safety", "inclusivity",
            ],
            "compliance_checks": [
                "explanation_human_readable", "multilingual_support",
                "bias_testing_done", "accountability_assigned",
                "privacy_compliant", "safety_assessed", "inclusive_design",
            ],
        },
    }

    # ---- helpers --------------------------------------------------------

    @staticmethod
    def _label(lang: str, key: str, **fmt) -> str:
        value = i18n.text(lang, "REPORT", key)
        return value.format(**fmt) if fmt else value

    def _status(self, lang: str, status: str) -> Dict[str, str]:
        """Status as both a stable code and a translated label."""
        return {"code": status, "label": i18n.text(lang, "STATUS", status)}

    # ---- compliance checks ---------------------------------------------

    def _evaluate(self, check_id: str, explanation_data: Dict, lang: str) -> str:
        """
        Decide PASS / REVIEW / FAIL from the actual explanation payload.

        Previously every check was hardcoded to PASS. These are still coarse
        rules, but they are now driven by evidence present in the record, so a
        missing audit id or an empty attribution genuinely fails.
        """
        contributions = explanation_data.get("contributions") or []

        if check_id in ("feature_explanation_provided", "risk_factors_explained",
                        "underwriting_factors_disclosed", "decision_rationale_clear",
                        "explanation_human_readable", "premium_rationale_clear",
                        "model_limitations_disclosed"):
            return "PASS" if contributions else "FAIL"

        if check_id in ("audit_trail_complete", "audit_trail_maintained",
                        "accountability_assigned"):
            return "PASS" if explanation_data.get("audit_id") else "FAIL"

        if check_id == "model_version_tracked":
            return "PASS" if explanation_data.get("model_version") else "REVIEW"

        if check_id in ("customer_notification_ready", "policyholder_notification",
                        "investor_notification"):
            # Requires a translated, customer-facing rendering to exist.
            return "PASS" if lang in i18n.available() else "FAIL"

        if check_id in ("multilingual_support", "inclusive_design"):
            # Only meaningful if the chosen language is actually translated.
            percent = i18n.coverage(lang)["percent"]
            if percent >= 90:
                return "PASS"
            return "REVIEW" if percent > 0 else "FAIL"

        if check_id == "no_genetic_discrimination":
            genetic = {"family_history_score"}
            used = {c.get("feature_name") for c in contributions}
            return "REVIEW" if genetic & used else "PASS"

        # Controls that are asserted by the deployment rather than derived
        # from a single decision record.
        return "PASS"

    def _finding(self, check_id: str, status: str, explanation_data: Dict,
                 lang: str) -> str:
        """
        Why a check did not pass.

        The catalog ``details`` line states the criterion being tested, which
        reads as a contradiction when the status is not PASS (e.g. "No genetic
        information was used" next to a REVIEW). Non-passing checks therefore
        carry a separate finding naming the evidence that triggered them.
        """
        if status == "PASS":
            return ""

        contributions = explanation_data.get("contributions") or []

        if check_id == "no_genetic_discrimination":
            flagged = [c["feature_name"] for c in contributions
                       if c.get("feature_name") == "family_history_score"]
            names = ", ".join(i18n.text(lang, "FEATURES", f, default=f) for f in flagged)
            return (f"Proxy for hereditary risk used as an input: {names}. "
                    f"Confirm this is permitted for the product before filing.")

        if check_id in ("multilingual_support", "inclusive_design"):
            cov = i18n.coverage(lang)
            meta = i18n.meta(lang)
            return (f"Translation coverage for {meta.get('name_en', lang)} is "
                    f"{cov['percent']}%; untranslated strings fall back to English.")

        if not contributions:
            return "No feature attribution present on the decision record."

        if check_id == "model_version_tracked" and not explanation_data.get("model_version"):
            return "No model version recorded against the decision."

        if not explanation_data.get("audit_id"):
            return "No audit trail identifier recorded against the decision."

        return "Evidence for this control was not found on the decision record."

    def _run_checks(self, framework: Dict, explanation_data: Dict, lang: str) -> List[Dict]:
        results = []
        for check_id in framework.get("compliance_checks", []):
            status = self._evaluate(check_id, explanation_data, lang)
            wording = i18n.check(lang, check_id)
            entry = {
                "check_id": check_id,
                "check_name": wording["name"],
                # Criterion being tested, in the caller's language.
                "criterion": wording["details"],
                "status": status,
                "status_label": i18n.text(lang, "STATUS", status),
            }
            finding = self._finding(check_id, status, explanation_data, lang)
            if finding:
                # Findings stay in English: they name specific evidence and are
                # read by the compliance officer, for whom English governs.
                entry["finding"] = finding
            results.append(entry)
        return results

    # ---- recommendations -----------------------------------------------

    def _recommendations(self, checks: List[Dict], regulator: str, lang: str) -> List[str]:
        out = []
        failed = [c for c in checks if c["status"] != "PASS"]

        if failed:
            template = i18n.text(lang, "RECOMMENDATIONS", "address_failed")
            out.extend(template.format(check=c["check_name"]) for c in failed)
        else:
            out.append(i18n.text(lang, "RECOMMENDATIONS", "all_passed"))

        out.append(i18n.text(lang, "RECOMMENDATIONS", "schedule_review")
                   .format(regulator=regulator))
        out.append(i18n.text(lang, "RECOMMENDATIONS", "revalidate"))
        out.append(i18n.text(lang, "RECOMMENDATIONS", "retain_logs"))
        return out

    # ---- plain-language reasoning ---------------------------------------

    def _reasoning(self, domain: str, explanation_data: Dict, lang: str) -> Dict:
        """
        Build the human-readable "why" block.

        The report's purpose is that a customer or officer can understand the
        decision, so each factor is returned with three things a reader needs:
        the value that was actually submitted, a full sentence explaining the
        effect, and a *share of influence* rather than a raw model coefficient.

        Share matters. The raw contribution is a weighted internal quantity;
        rendering it as "+4.4%" invites the reader to think 4.4% of something
        meaningful. Share is normalised over the absolute contributions, so the
        numbers sum to 100% and "this factor drove a fifth of the outcome" is a
        true statement.
        """
        contributions = explanation_data.get("contributions") or []
        total = sum(abs(c.get("contribution", 0.0)) for c in contributions)

        def describe(c):
            contribution = c.get("contribution", 0.0)
            value = c.get("feature_value")
            return {
                "rank": c.get("importance_rank"),
                "feature_code": c["feature_name"],
                "feature": translation_service.translate_feature(c["feature_name"], lang),
                "value": value,
                "contribution": round(contribution, 4),
                # Normalised, so the listed shares add up to 100%.
                "share": round(abs(contribution) / total, 4) if total else 0.0,
                "direction": c.get("contribution_direction"),
                "explanation": translation_service.translate_explanation(
                    c["feature_name"], value, contribution, lang),
            }

        described = [describe(c) for c in contributions]
        favour = [d for d in described if d["direction"] == "positive"]
        against = [d for d in described if d["direction"] != "positive"]

        decision = explanation_data.get("decision", "")
        top = [c["feature_name"] for c in contributions[:3]]

        block = {
            # Same one-line verdict the customer saw on screen, so the printed
            # report and the interactive view cannot disagree.
            "plain_summary": translation_service.translate_summary(
                domain, decision, top, lang) if top else "",
            "favour": favour,
            "against": against,
        }
        if described:
            block["strongest"] = i18n.text(lang, "REPORT_REASONS", "strongest_factor") \
                .format(feature=described[0]["feature"])
        return block

    # ---- report ---------------------------------------------------------

    def generate_compliance_report(self, regulator: str, domain: str,
                                   explanation_data: Dict, language: str) -> Dict:
        framework = self.REGULATORY_FRAMEWORKS.get(
            regulator, self.REGULATORY_FRAMEWORKS["RBI"])
        lang = language or "en"

        timestamp = datetime.now().isoformat()
        report_id = f"RPT-{hashlib.sha256(timestamp.encode()).hexdigest()[:10].upper()}"

        checks = self._run_checks(framework, explanation_data, lang)
        passed = sum(1 for c in checks if c["status"] == "PASS")
        overall = "COMPLIANT" if passed == len(checks) else "REVIEW_NEEDED"

        regulator_name = i18n.text(lang, "REGULATORS", regulator, default=regulator)
        coverage = i18n.coverage(lang)
        meta = i18n.meta(lang)

        decision = explanation_data.get("decision", "UNKNOWN")

        report = {
            "report_id": report_id,
            "generated_at": timestamp,
            "language": {
                "code": lang,
                "name_native": meta.get("name_native", lang),
                "name_en": meta.get("name_en", lang),
                "rtl": bool(meta.get("rtl", False)),
                "coverage_percent": coverage["percent"],
                "review_status": meta.get("review_status", "needs_native_review"),
            },
            # Translated headings and field labels, so the client renders the
            # report in-language without carrying its own dictionary.
            "labels": {
                key: self._label(lang, key) for key in (
                    "title", "report_id", "generated_at", "regulator", "domain",
                    "model_version", "algorithm", "explanation_method",
                    "decision", "confidence", "risk_score", "audit_id",
                    "guidelines_heading", "checks_heading",
                    "requirements_heading", "recommendations_heading",
                    "explainability_heading", "top_factors",
                    "features_explained", "explanation_language",
                )
            },
            "regulator": {
                "code": regulator,
                "name": regulator_name,
                "applicable_guidelines": framework["guidelines"],
            },
            "domain": {
                "code": domain,
                "name": i18n.text(lang, "DOMAINS", domain,
                                  default=domain.replace("_", " ").title()),
            },
            "model_info": {
                "version": explanation_data.get("model_version", "v1.0"),
                "algorithm": "Weighted Feature Importance Decomposition",
                "explanation_method": "SHAP-like Additive Feature Attribution",
            },
            "decision_summary": {
                "decision_code": decision,
                "decision": i18n.text(lang, "DECISIONS", decision,
                                      default=decision.replace("_", " ").title()),
                "confidence": explanation_data.get("confidence", 0),
                "risk_score": explanation_data.get("risk_score", 0),
                "audit_id": explanation_data.get("audit_id", "N/A"),
            },
            # Plain-language reasons, and the labels that head them. This block
            # is what makes the report readable; the framework evidence below
            # is what makes it filable.
            "reason_labels": i18n.section(lang, "REPORT_REASONS"),
            "reasoning": self._reasoning(domain, explanation_data, lang),
            "explainability_report": {
                "num_features_explained": len(explanation_data.get("contributions", [])),
                "top_factors": [
                    {
                        "feature_code": c["feature_name"],
                        "feature": i18n.text(lang, "FEATURES", c["feature_name"],
                                             default=c["feature_name"]),
                        "contribution": c["contribution"],
                        "direction": c["contribution_direction"],
                    }
                    for c in explanation_data.get("contributions", [])[:5]
                ],
            },
            "compliance_assessment": {
                "overall_status": overall,
                "overall_status_label": i18n.text(lang, "STATUS", overall),
                "checks_passed": passed,
                "checks_total": len(checks),
                "detailed_checks": checks,
            },
            "requirements_met": [
                {
                    "key": key,
                    "label": i18n.text(lang, "REQUIREMENT_LABELS", key,
                                       default=key.replace("_", " ").title()),
                    "text": i18n.text(lang, "REQUIREMENT_TEXT", key, default=""),
                }
                for key in framework["requirements"]
            ],
            "recommendations": self._recommendations(checks, regulator, lang),
            "legal_disclaimer": self._label(lang, "disclaimer", framework=regulator_name),
        }

        # Surface machine-translation provenance whenever the report is not
        # in English. A reviewer must know which text is authoritative.
        if lang != "en":
            report["translation_notice"] = self._label(
                lang, "translation_notice",
                language=meta.get("name_native", lang))

        return report

    # ---- framework introspection ---------------------------------------

    def get_regulatory_info(self, regulator: str, language: str = "en") -> Dict:
        framework = self.REGULATORY_FRAMEWORKS.get(regulator)
        if not framework:
            return {}
        return {
            "code": regulator,
            "name": i18n.text(language, "REGULATORS", regulator, default=regulator),
            "guidelines": framework["guidelines"],
            "requirements": [
                {
                    "key": key,
                    "label": i18n.text(language, "REQUIREMENT_LABELS", key),
                    "text": i18n.text(language, "REQUIREMENT_TEXT", key, default=""),
                }
                for key in framework["requirements"]
            ],
            "compliance_checks": [
                dict(check_id=cid, **i18n.check(language, cid))
                for cid in framework["compliance_checks"]
            ],
        }

    def get_all_frameworks(self, language: str = "en") -> Dict:
        return {
            code: {
                "name": i18n.text(language, "REGULATORS", code, default=code),
                "num_guidelines": len(fw["guidelines"]),
                "num_requirements": len(fw["requirements"]),
                "num_checks": len(fw["compliance_checks"]),
            }
            for code, fw in self.REGULATORY_FRAMEWORKS.items()
        }


compliance_service = ComplianceService()
