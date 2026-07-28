"""
XAI Engine - Generates SHAP-like feature importance explanations
for credit scoring, insurance underwriting, and healthcare models.
"""
import random
import math
from typing import Dict, List, Tuple
import hashlib
import time


class XAIEngine:
    """Core explainability engine using feature importance decomposition"""

    CREDIT_WEIGHTS = {
        "annual_income": 0.25,
        "credit_history_months": 0.20,
        "existing_loans": -0.15,
        "loan_amount_requested": -0.10,
        "employment_years": 0.15,
        "monthly_expenses": -0.10,
        "age": 0.05,
        "defaults_in_past": -0.30,
    }

    INSURANCE_WEIGHTS = {
        "age": -0.15,
        "bmi": -0.15,
        "smoking_status": -0.25,
        "pre_existing_conditions": -0.20,
        "family_history_score": -0.15,
        "occupation_risk": -0.10,
        "coverage_amount": -0.05,
    }

    HEALTHCARE_WEIGHTS = {
        "age": 0.10,
        "symptoms_severity": 0.30,
        "lab_results_abnormal": 0.25,
        "medical_history_score": 0.15,
        "vitals_risk_score": 0.15,
        "treatment_urgency": 0.20,
    }

    FEATURE_RANGES = {
        "annual_income": (100000, 5000000),
        "credit_history_months": (0, 360),
        "existing_loans": (0, 10),
        "loan_amount_requested": (50000, 10000000),
        "employment_years": (0, 40),
        "monthly_expenses": (10000, 500000),
        "age": (18, 80),
        "defaults_in_past": (0, 5),
        "bmi": (15, 45),
        "smoking_status": (0, 1),
        "pre_existing_conditions": (0, 10),
        "family_history_score": (0, 1),
        "occupation_risk": (0, 1),
        "coverage_amount": (100000, 50000000),
        "symptoms_severity": (0, 10),
        "lab_results_abnormal": (0, 20),
        "medical_history_score": (0, 1),
        "vitals_risk_score": (0, 1),
        "treatment_urgency": (0, 1),
    }

    OCCUPATION_RISK_MAP = {"low": 0.2, "medium": 0.5, "high": 0.8}
    URGENCY_MAP = {"routine": 0.2, "moderate": 0.5, "urgent": 0.9}

    def generate_audit_id(self) -> str:
        timestamp = str(time.time()).encode()
        return f"AUD-{hashlib.sha256(timestamp).hexdigest()[:12].upper()}"

    def normalize_value(self, feature: str, value: float) -> float:
        if feature in self.FEATURE_RANGES:
            min_val, max_val = self.FEATURE_RANGES[feature]
            return max(0, min(1, (value - min_val) / (max_val - min_val)))
        return value

    def compute_contributions(self, domain: str, input_data: Dict) -> Tuple[float, List[Dict]]:
        if domain == "credit_scoring":
            weights = self.CREDIT_WEIGHTS
        elif domain == "insurance_underwriting":
            weights = self.INSURANCE_WEIGHTS
        elif domain == "healthcare":
            weights = self.HEALTHCARE_WEIGHTS
        else:
            weights = self.CREDIT_WEIGHTS

        contributions = []
        total_score = 0.5

        for feature, weight in weights.items():
            if feature in input_data:
                raw_value = input_data[feature]
                if feature == "occupation_risk":
                    raw_value = self.OCCUPATION_RISK_MAP.get(str(raw_value), 0.5)
                elif feature == "treatment_urgency":
                    raw_value = self.URGENCY_MAP.get(str(raw_value), 0.5)
                elif feature == "smoking_status":
                    raw_value = 1.0 if raw_value else 0.0

                normalized = self.normalize_value(feature, float(raw_value))
                contribution = weight * normalized
                noise = random.gauss(0, 0.01)
                contribution += noise
                total_score += contribution

                contributions.append({
                    "feature_name": feature,
                    "feature_value": float(raw_value),
                    "normalized_value": round(normalized, 4),
                    "weight": weight,
                    "contribution": round(contribution, 4),
                    "contribution_direction": "positive" if contribution > 0 else "negative",
                    "importance_rank": 0,
                })

        contributions.sort(key=lambda x: abs(x["contribution"]), reverse=True)
        for i, c in enumerate(contributions):
            c["importance_rank"] = i + 1

        total_score = max(0.0, min(1.0, total_score))
        return total_score, contributions

    def generate_decision(self, domain: str, risk_score: float) -> Tuple[str, float]:
        if domain == "credit_scoring":
            if risk_score >= 0.7:
                return "APPROVED", min(0.95, risk_score)
            elif risk_score >= 0.4:
                return "REVIEW_REQUIRED", 0.5 + (risk_score - 0.4) * 0.5
            else:
                return "REJECTED", min(0.95, 1 - risk_score)
        elif domain == "insurance_underwriting":
            if risk_score <= 0.3:
                return "STANDARD_PREMIUM", min(0.95, 1 - risk_score)
            elif risk_score <= 0.6:
                return "LOADED_PREMIUM", 0.6 + (risk_score - 0.3) * 0.5
            else:
                return "DECLINED", min(0.95, risk_score)
        elif domain == "healthcare":
            if risk_score >= 0.7:
                return "HIGH_RISK_INTERVENTION", min(0.95, risk_score)
            elif risk_score >= 0.4:
                return "MODERATE_RISK_MONITORING", 0.5 + (risk_score - 0.4) * 0.5
            else:
                return "LOW_RISK_ROUTINE", min(0.95, 1 - risk_score)
        return "UNKNOWN", 0.5

    def explain(self, domain: str, input_data: Dict) -> Dict:
        risk_score, contributions = self.compute_contributions(domain, input_data)
        decision, confidence = self.generate_decision(domain, risk_score)
        audit_id = self.generate_audit_id()

        return {
            "decision": decision,
            "confidence": round(confidence, 4),
            "risk_score": round(risk_score, 4),
            "contributions": contributions,
            "audit_id": audit_id,
            "model_metadata": {
                "algorithm": "Weighted Feature Importance Decomposition",
                "explanation_method": "SHAP-like Additive Feature Attribution",
                "baseline_score": 0.5,
                "num_features": len(contributions),
            }
        }


xai_engine = XAIEngine()
