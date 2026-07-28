"""
XAI Platform Server - Uses Python standard library only.
No external dependencies required.
"""
import json
import sys
import os
import hashlib
import time
import random
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.services.xai_engine import xai_engine
from app.services.translation_service import translation_service
from app.services.compliance_service import compliance_service

explanation_store = {}


class XAIRequestHandler(SimpleHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self._set_cors_headers()
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)
        # Most read endpoints are language-aware; ?lang=xx selects the catalog.
        lang = (query.get("lang") or ["en"])[0]

        if path == "/api/health":
            self._json_response({"status": "healthy", "service": "xai-platform"})
        elif path == "/api/explanations/languages":
            self._json_response(translation_service.get_supported_languages())
        elif path == "/api/i18n/languages":
            # Full catalog metadata: native name, script, direction and the
            # measured translation coverage per language.
            self._json_response(translation_service.get_language_details())
        elif path == "/api/i18n/ui":
            self._json_response({
                "language": lang,
                "rtl": translation_service.is_rtl(lang),
                "strings": translation_service.ui_strings(lang),
            })
        elif path == "/api/models/domains":
            self._json_response(self._get_domains(lang))
        elif path == "/api/models/info":
            self._json_response(self._get_model_info())
        elif path == "/api/reports/frameworks":
            self._json_response(compliance_service.get_all_frameworks(lang))
        elif path.startswith("/api/reports/frameworks/"):
            regulator = path.split("/")[-1]
            info = compliance_service.get_regulatory_info(regulator, lang)
            self._json_response(info if info else {"error": "Not found"}, 200 if info else 404)
        elif path == "/api/explanations":
            self._json_response({"total": len(explanation_store), "explanations": [{"audit_id": k, "domain": v.get("domain"), "decision": v.get("decision")} for k, v in explanation_store.items()]})
        elif path.startswith("/api/explanations/"):
            audit_id = path.split("/")[-1]
            self._json_response(explanation_store.get(audit_id, {"error": "Not found"}), 200 if audit_id in explanation_store else 404)
        else:
            self._serve_frontend(path)

    def do_POST(self):
        path = urlparse(self.path).path
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length).decode("utf-8") if content_length > 0 else "{}"
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            self._json_response({"error": "Invalid JSON"}, 400)
            return
        if path == "/api/explanations/generate":
            self._handle_generate_explanation(data)
        elif path == "/api/reports/generate":
            self._handle_generate_report(data)
        else:
            self._json_response({"error": "Not found"}, 404)

    def _handle_generate_explanation(self, data):
        try:
            domain = data.get("domain", "credit_scoring")
            language = data.get("language", "en")
            regulator = data.get("regulator", "RBI")
            input_data = data.get("input_data", {})

            result = xai_engine.explain(domain, input_data)

            feature_contributions = []
            for contrib in result["contributions"]:
                feature_contributions.append({
                    "feature_name": contrib["feature_name"],
                    # Translated display name, so the chart does not have to
                    # carry its own feature dictionary.
                    "feature_label": translation_service.translate_feature(
                        contrib["feature_name"], language),
                    "feature_value": contrib["feature_value"],
                    "contribution": contrib["contribution"],
                    "contribution_direction": contrib["contribution_direction"],
                    "importance_rank": contrib["importance_rank"],
                    "explanation": translation_service.translate_explanation(contrib["feature_name"], contrib["feature_value"], contrib["contribution"], "en"),
                    "translated_explanation": translation_service.translate_explanation(contrib["feature_name"], contrib["feature_value"], contrib["contribution"], language),
                })

            top_factors = [c["feature_name"] for c in result["contributions"][:3]]
            lang_details = translation_service.get_language_details()
            lang_meta = lang_details["languages"].get(language, {})

            response = {
                # Stable code for logic, translated label for display.
                "decision_code": result["decision"],
                "decision": result["decision"],
                "decision_label": translation_service.translate_decision(result["decision"], language),
                "confidence": result["confidence"],
                "risk_score": result["risk_score"],
                "domain": domain,
                "domain_label": translation_service.translate_domain(domain, language),
                "regulator": regulator,
                "regulator_label": translation_service.translate_regulator(regulator, language),
                "language": language,
                # Direction and coverage travel with the payload so the client
                # can set text direction and warn on partial translation
                # without a second round trip.
                "language_meta": {
                    "code": language,
                    "name_native": lang_meta.get("name_native", language),
                    "name_en": lang_meta.get("name_en", language),
                    "rtl": bool(lang_meta.get("rtl", False)),
                    "coverage_percent": lang_meta.get("coverage_percent", 0.0),
                    "review_status": lang_meta.get("review_status", "needs_native_review"),
                },
                "feature_contributions": feature_contributions,
                "summary_explanation": translation_service.translate_summary(domain, result["decision"], top_factors, "en"),
                "translated_summary": translation_service.translate_summary(domain, result["decision"], top_factors, language),
                "regulatory_compliance": {
                    "regulator": regulator,
                    "compliance_note": translation_service.get_compliance_note(regulator, language),
                    "audit_id": result["audit_id"],
                    "model_metadata": result["model_metadata"],
                },
                "model_version": data.get("model_version", "v1.0"),
                "timestamp": datetime.now().isoformat(),
                "audit_id": result["audit_id"],
            }

            # Persist the version actually supplied, not a hardcoded one - the
            # model_version_tracked compliance check reads this back.
            explanation_store[result["audit_id"]] = {
                **result,
                "domain": domain,
                "regulator": regulator,
                "language": language,
                "model_version": data.get("model_version", "v1.0"),
                "input_data": input_data,
            }
            self._json_response(response)
        except Exception as e:
            self._json_response({"error": str(e)}, 500)

    def _handle_generate_report(self, data):
        try:
            explanation_id = data.get("explanation_id", "")
            if explanation_id not in explanation_store:
                self._json_response({"error": "Explanation not found. Generate one first."}, 404)
                return
            report = compliance_service.generate_compliance_report(
                regulator=data.get("regulator", "RBI"), domain=data.get("domain", "credit_scoring"),
                explanation_data=explanation_store[explanation_id], language=data.get("language", "en"))
            self._json_response(report)
        except Exception as e:
            self._json_response({"error": str(e)}, 500)

    def _serve_frontend(self, path):
        if path == "/" or path == "":
            path = "/index.html"
        frontend_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "frontend")
        filepath = os.path.join(frontend_dir, path.lstrip("/"))
        if os.path.isfile(filepath):
            ct = "text/html; charset=utf-8"
            if filepath.endswith(".js"):
                ct = "application/javascript; charset=utf-8"
            elif filepath.endswith(".css"):
                ct = "text/css; charset=utf-8"
            self._send_file(filepath, ct)
        else:
            index = os.path.join(frontend_dir, "index.html")
            if os.path.isfile(index):
                # SPA fallback.
                self._send_file(index, "text/html; charset=utf-8")
            else:
                self._json_response({"error": "Not found"}, 404)

    def _send_file(self, filepath, content_type):
        with open(filepath, "rb") as handle:
            content = handle.read()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(content)))
        self._set_cors_headers()
        self.end_headers()
        self.wfile.write(content)

    def _json_response(self, data, status=200):
        payload = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        # charset must be declared: responses carry Devanagari, Bengali, Tamil,
        # Ol Chiki and Perso-Arabic text, which mojibakes without it.
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self._set_cors_headers()
        self.end_headers()
        self.wfile.write(payload)

    def _set_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    SAMPLE_INPUTS = {
        "credit_scoring": {
            "regulator": "RBI",
            "sample_input": {
                "annual_income": 800000, "credit_history_months": 60,
                "existing_loans": 2, "loan_amount_requested": 500000,
                "employment_years": 5, "monthly_expenses": 35000,
                "age": 32, "defaults_in_past": 0,
            },
        },
        "insurance_underwriting": {
            "regulator": "IRDAI",
            "sample_input": {
                "age": 45, "bmi": 26.5, "smoking_status": False,
                "pre_existing_conditions": 1, "family_history_score": 0.3,
                "occupation_risk": "medium", "coverage_amount": 5000000,
            },
        },
        "healthcare": {
            "regulator": "IndiaAI",
            "sample_input": {
                "age": 55, "symptoms_severity": 6.5, "lab_results_abnormal": 3,
                "medical_history_score": 0.4, "vitals_risk_score": 0.5,
                "treatment_urgency": "moderate",
            },
        },
    }

    def _get_domains(self, lang="en"):
        """Domains with translated names and per-field translated labels."""
        out = {}
        for code, spec in self.SAMPLE_INPUTS.items():
            out[code] = {
                "name": translation_service.translate_domain(code, lang),
                "regulator": spec["regulator"],
                "regulator_name": translation_service.translate_regulator(
                    spec["regulator"], lang),
                "sample_input": spec["sample_input"],
                # Field labels in the selected language, so the input form is
                # localised too rather than only the output.
                "field_labels": {
                    field: translation_service.translate_feature(field, lang)
                    for field in spec["sample_input"]
                },
            }
        return out

    def _get_model_info(self):
        details = translation_service.get_language_details()
        return {
            "platform": "XAI Platform for Regulated Industries",
            "version": "1.1.0",
            "explanation_method": "SHAP-like Additive Feature Attribution",
            "supported_regulators": ["RBI", "IRDAI", "SEBI", "IndiaAI"],
            # Reported from the catalog rather than asserted as a constant, so
            # the number cannot drift from what is actually installed.
            "scheduled_languages_supported": details["scheduled_languages"],
            "catalogs_installed": details["total_languages"],
            "translation_contract_keys": details["contract_keys"],
        }

    def log_message(self, format, *args):
        pass


def run_server(port=8000):
    server = HTTPServer(("0.0.0.0", port), XAIRequestHandler)
    print(f"\n{'='*60}")
    print(f"  XAI Platform for Regulated Industries")
    print(f"  Server running on http://localhost:{port}")
    print(f"  Open http://localhost:{port} in your browser")
    print(f"{'='*60}\n")
    server.serve_forever()


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    run_server(port)
