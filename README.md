# 🔍 XAI Platform - Explainable AI for Regulated Industries

> Multilingual Explainable AI platform that integrates with RBI/IRDAI/SEBI/IndiaAI frameworks to generate audit-ready AI decision explanations in 22 Indian languages.

## 🚀 Quick Start (Zero Setup!)

```bash
# Only requires Python 3.9+ (no pip install needed!)
cd xai-platform/backend
python server.py
```

Open **http://localhost:8000** in your browser. That's it!

## 🎯 Problem Statement

RBI, IRDAI, SEBI, and IndiaAI guidelines mandate AI explainability for credit, underwriting, and healthcare decisions — but no tool exists to generate regulator-compliant explanations in Hindi and regional languages.

## 💡 Solution

A multilingual XAI platform that:
- Generates **SHAP-like feature importance** explanations for AI decisions
- Translates explanations into **22 scheduled Indian languages**
- Produces **audit-ready compliance reports** per RBI/IRDAI/SEBI/IndiaAI guidelines
- Maintains complete **audit trails** for regulatory inspection

## 📊 Supported Domains

| Domain | Regulator | Use Case |
|--------|-----------|----------|
| 🏦 Credit Scoring | RBI | Loan application decisions |
| 🛡️ Insurance Underwriting | IRDAI | Premium and coverage decisions |
| 🏥 Healthcare | IndiaAI | Patient risk stratification |

## 🌐 Languages (22 Scheduled Languages)

Hindi, Bengali, Tamil, Telugu, Marathi, Gujarati, Kannada, Malayalam, Punjabi, Urdu, Odia, Assamese, Sanskrit, Kashmiri, Sindhi, Konkani, Dogri, Manipuri, Bodo, Santhali, Maithili + English

## 🏗️ Architecture

```
Frontend (React 18 + Tailwind CSS)
         │ HTTP API
Backend (Python stdlib - zero dependencies)
  ├── XAI Engine (SHAP-like attribution)
  ├── Translation Service (22 languages)
  └── Compliance Service (4 regulators)
```

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/explanations/generate | Generate AI decision explanation |
| POST | /api/reports/generate | Generate compliance report |
| GET | /api/models/domains | List domains with sample data |
| GET | /api/explanations/languages | List supported languages |
| GET | /api/reports/frameworks | List regulatory frameworks |

## 🏆 Key Features

- **Zero dependencies** — Pure Python stdlib backend
- **SHAP-like XAI** — Real additive feature attribution methodology
- **22 Indian languages** — Domain-specific translations
- **4 regulatory frameworks** — Full compliance checks
- **Audit trail** — Unique IDs for every decision
- **Single command startup** — No setup, no config

## 📝 License

MIT
