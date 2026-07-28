# XAI Platform - Explainable AI for Regulated Industries

Generates audit-ready explanations for AI decisions in the 22 languages of the
Eighth Schedule of the Constitution of India, mapped onto the RBI, IRDAI, SEBI
and IndiaAI explainability frameworks.

## Quick start

Requires **Python 3.9+** and nothing else. No `pip install`, no `npm install`,
no build step, no network.

```bash
cd backend
python server.py          # Windows: py server.py
```

Then open <http://localhost:8000>.

`run.sh` (macOS/Linux) and `run.bat` (Windows) do the same thing.

## Why there are no dependencies

The backend uses only the Python standard library. The frontend is one
self-contained HTML file with inline CSS and vanilla JavaScript.

This is deliberate. An earlier version loaded React, Babel and Tailwind from
CDNs, which meant the entire UI failed to a blank page whenever the network was
unavailable — the normal condition at a conference venue, and a hard
requirement in an air-gapped compliance environment. Nothing the app needs is
fetched at runtime.

The single optional remote asset is a Google Fonts link for Noto. If it is
blocked the browser falls back to system fonts and the page still works; see
*Font requirements* below.

## Domains

| Domain | Regulator | Decision |
|---|---|---|
| Credit scoring | RBI | Approve / refer / reject a loan application |
| Insurance underwriting | IRDAI | Standard / loaded premium / decline |
| Healthcare risk | IndiaAI | Risk stratification and intervention urgency |

## Languages

All 22 Eighth Schedule languages, plus English as a working language.
Translation is **measured, not asserted** — `en.py` declares a contract of 156
keys and every other catalog is scored against it. Lookups fall back to English
per *key*, so a partially translated language yields partially translated output
rather than being discarded.

| Coverage | Languages |
|---|---|
| 100% | Hindi, Bengali, Tamil, Telugu, Marathi, Gujarati, Kannada, Malayalam, Punjabi, Urdu |
| 75% | Assamese, Odia, Sanskrit, Nepali, Konkani, Dogri, Maithili, Sindhi |
| 30–40% | Kashmiri, Bodo, Manipuri |
| 0% (stub) | Santhali |

Verify at any time:

```bash
curl "http://localhost:8000/api/i18n/languages"
```

Two honesty properties are built in rather than bolted on:

- Every catalog carries a `review_status`. Only the 100% tier is marked
  `verified`; the rest are `needs_native_review`. **Have a native speaker check
  any language before using it in a real regulatory filing.**
- The Santhali catalog is an intentionally empty stub. Ol Chiki is the script I
  could not translate reliably, so rather than fill it with plausible-looking
  but wrong text, it falls back to English and reports 0%. Selecting Santhali
  gives a visibly untranslated result instead of a confidently wrong one.

Nepali was **added** in this version. The previous language list counted English
as one of the 22 and omitted Nepali, so it advertised 22 while shipping 21
Indian languages.

## The compliance report

`POST /api/reports/generate` renders in the requested language: headings, field
labels, statuses, check names, requirement text, recommendations and the
disclaimer all resolve through the catalog.

Two things stay in English on purpose:

- **Guideline citations.** A regulator expects the exact title it published.
- **The authoritative text.** Every non-English report carries a
  `translation_notice` stating that the English text governs the filing. A
  machine translation is not presented as the text of record.

Compliance checks are evidence-based. They read the decision record and can
fail: a missing audit trail id, an empty feature attribution, or a translation
coverage too low to support a multilingual-access claim will all downgrade the
result. They are not decorative pass badges.

## API

| Method | Path | Notes |
|---|---|---|
| GET | `/api/health` | |
| GET | `/api/i18n/languages` | Native names, scripts, direction, coverage |
| GET | `/api/i18n/ui?lang=` | UI string bundle + `rtl` flag |
| GET | `/api/models/domains?lang=` | Domains, sample inputs, translated field labels |
| GET | `/api/models/info` | Counts reported from the catalog, not hardcoded |
| GET | `/api/reports/frameworks?lang=` | |
| GET | `/api/reports/frameworks/{regulator}?lang=` | |
| POST | `/api/explanations/generate` | |
| POST | `/api/reports/generate` | |

```bash
curl -X POST http://localhost:8000/api/explanations/generate \
  -H 'Content-Type: application/json' \
  -d '{"domain":"credit_scoring","language":"hi","regulator":"RBI",
       "input_data":{"annual_income":800000,"credit_history_months":60,
         "existing_loans":2,"loan_amount_requested":500000,"employment_years":5,
         "monthly_expenses":35000,"age":32,"defaults_in_past":0}}'
```

## Layout

```
backend/
  server.py                     stdlib HTTP server, routing, UTF-8 responses
  app/i18n/
    __init__.py                 registry, per-key fallback, coverage scoring
    en.py                       canonical 156-key contract
    hi.py bn.py ta.py ...       one module per language (as_.py / or_.py:
                                'as' and 'or' are Python keywords)
  app/services/
    xai_engine.py               additive feature attribution
    translation_service.py      key-selection policy over the catalog
    compliance_service.py       framework definitions, localised reporting
frontend/index.html             entire UI, no dependencies
```

Adding a language means adding one module under `app/i18n/` and registering its
code. No service or UI change is required.

## Explainability method

Additive feature attribution: each input is normalised, weighted, and summed
against a 0.5 baseline to produce a risk score, then thresholded into a
decision. Contributions are ranked by absolute magnitude and rendered as signed
bars.

This is a transparent stand-in with the same *shape* as SHAP — additive,
per-feature, signed — so the explanation surface and report format are exactly
what a real model would produce. It is **not** SHAP and carries no game-theoretic
guarantees. Swapping in a trained model plus real SHAP values means replacing
`xai_engine.explain()` and nothing else; the response contract is unchanged.

## Font requirements

Indic and Perso-Arabic glyphs need fonts covering those scripts.

- **Windows 10/11** ships Nirmala UI, covering Devanagari, Bengali, Tamil,
  Telugu, Kannada, Malayalam, Gujarati, Gurmukhi and Odia. macOS and most Linux
  desktops with Noto installed are also fine.
- If the Google Fonts link is reachable, Noto is used and coverage is complete.
- If fonts are missing **and** the CDN is blocked, affected text shows as empty
  boxes. The characters are correct — it is a glyph problem, not an encoding
  one. Ol Chiki (Santhali) and Meetei Mayek are the least likely to be present
  on a stock system.

Verified behaviour was confirmed in a headless browser with no Indic fonts
installed: layout, theming, RTL mirroring and all data flows are correct, but
glyph rendering for Indic scripts could not be verified in that environment.

## Interface

Dark theme by default; the toggle persists to `localStorage`. Urdu, Kashmiri and
Sindhi switch the document to `dir="rtl"`, which mirrors the layout including
the direction the contribution bars grow.

## Printing a report

The report carries a **Print report** button, labelled in the selected language.
It uses the browser print dialog, so "Save as PDF" produces the same output.

The print stylesheet drops the app chrome — header, domain cards, input form,
the interactive explanation panel and the buttons themselves — and prints only
the report, on white paper regardless of the on-screen theme. Status and finding
colours are preserved because they carry meaning.

Because browser print headers are often disabled, identity travels inside the
document: a letterhead carries the report ID, audit trail ID, generation
timestamp and origin. Individual findings, requirements and facts are never
split across a page break.

The printed report also includes the feature attribution table. The report
payload always carried `explainability_report.top_factors` but the UI never
displayed it, so a filed report previously omitted the evidence it rested on.

## Licence

MIT. Built as a hackathon demonstration.
