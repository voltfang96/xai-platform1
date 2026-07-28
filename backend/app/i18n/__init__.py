"""
Language catalog registry.

Design notes
------------
* ``en`` is the canonical catalog and defines the full key contract.
* Lookups fall back to English *per key*, not per language. A catalog that
  translates 80% of keys yields 80% translated output rather than being
  discarded wholesale.
* ``coverage()`` reports, per language, how much of the contract is actually
  translated. This is deliberately exposed over the API so that a partially
  translated language cannot masquerade as complete.
* ``review_status`` distinguishes catalogs that a native speaker has confirmed
  from those that still need review. For a regulated deployment the provenance
  of a translation matters, so it is treated as first-class metadata.
"""

from importlib import import_module
from typing import Any, Dict, List, Optional

from . import en as _en

# Eighth Schedule of the Constitution of India: 22 languages.
# `en` is offered additionally as a working language but is NOT one of the 22.
_MODULES = {
    "en": "en",
    "as": "as_",
    "bn": "bn",
    "brx": "brx",
    "doi": "doi",
    "gu": "gu",
    "hi": "hi",
    "kn": "kn",
    "ks": "ks",
    "kok": "kok",
    "mai": "mai",
    "ml": "ml",
    "mni": "mni",
    "mr": "mr",
    "ne": "ne",
    "or": "or_",
    "pa": "pa",
    "sa": "sa",
    "sat": "sat",
    "sd": "sd",
    "ta": "ta",
    "te": "te",
    "ur": "ur",
}

# Sections that are flat ``key -> string`` maps.
_FLAT_SECTIONS = (
    "FEATURES", "DECISIONS", "EXPLANATION", "SUMMARY", "REPORT",
    "REPORT_REASONS", "STATUS", "DOMAINS", "REGULATORS",
    "REQUIREMENT_LABELS", "REQUIREMENT_TEXT", "RECOMMENDATIONS", "UI",
)
# CHECKS maps key -> (name, details) tuples and is handled separately.

_cache: Dict[str, Any] = {}


def _load(code: str):
    if code in _cache:
        return _cache[code]
    module_name = _MODULES.get(code)
    if module_name is None:
        return None
    try:
        module = import_module(f"{__name__}.{module_name}")
    except ModuleNotFoundError:
        return None
    _cache[code] = module
    return module


def available() -> List[str]:
    """Language codes that have a loadable catalog."""
    return [code for code in _MODULES if _load(code) is not None]


def scheduled_languages() -> List[str]:
    """The Eighth Schedule languages that have a catalog (excludes English)."""
    out = []
    for code in available():
        module = _load(code)
        if getattr(module, "META", {}).get("scheduled", True):
            out.append(code)
    return out



def meta(code: str) -> Dict[str, Any]:
    module = _load(code) or _en
    base = dict(getattr(_en, "META", {}))
    base.update(getattr(module, "META", {}))
    return base


def is_rtl(code: str) -> bool:
    return bool(meta(code).get("rtl", False))


def text(code: str, section: str, key: str, default: Optional[str] = None) -> str:
    """
    Resolve a single string, falling back to English for that key alone.

    Returns ``default`` (or the key itself) only if English also lacks the key.
    """
    module = _load(code)
    if module is not None:
        table = getattr(module, section, None)
        if isinstance(table, dict):
            value = table.get(key)
            if isinstance(value, str) and value.strip():
                return value
    table = getattr(_en, section, None)
    if isinstance(table, dict):
        value = table.get(key)
        if isinstance(value, str) and value.strip():
            return value
    return default if default is not None else key


def check(code: str, check_id: str) -> Dict[str, str]:
    """Resolve a compliance check's display name and evidence line."""
    def _lookup(module):
        table = getattr(module, "CHECKS", None)
        if isinstance(table, dict):
            entry = table.get(check_id)
            if isinstance(entry, (tuple, list)) and len(entry) >= 2:
                return str(entry[0]), str(entry[1])
        return None

    module = _load(code)
    resolved = _lookup(module) if module is not None else None
    fallback = _lookup(_en)

    if resolved is None and fallback is None:
        pretty = check_id.replace("_", " ").title()
        return {"name": pretty, "details": pretty}
    if resolved is None:
        return {"name": fallback[0], "details": fallback[1]}
    return {"name": resolved[0], "details": resolved[1]}


def section(code: str, name: str) -> Dict[str, str]:
    """Whole section with English filling any gaps."""
    merged = dict(getattr(_en, name, {}) or {})
    module = _load(code)
    if module is not None:
        local = getattr(module, name, None)
        if isinstance(local, dict):
            for key, value in local.items():
                if isinstance(value, str) and value.strip():
                    merged[key] = value
    return merged



def _contract_keys() -> List[tuple]:
    """Every (section, key) pair the English catalog declares."""
    keys: List[tuple] = []
    for name in _FLAT_SECTIONS:
        table = getattr(_en, name, None)
        if isinstance(table, dict):
            keys.extend((name, key) for key in table)
    checks = getattr(_en, "CHECKS", None)
    if isinstance(checks, dict):
        keys.extend(("CHECKS", key) for key in checks)
    return keys


def coverage(code: str) -> Dict[str, Any]:
    """
    Measure how much of the English key contract this language translates.

    A key counts as translated only when the language supplies a non-empty
    string of its own; inherited English does not count.
    """
    module = _load(code)
    contract = _contract_keys()
    total = len(contract)

    if module is None:
        return {
            "code": code, "translated": 0, "total": total,
            "percent": 0.0, "missing_sections": sorted({s for s, _ in contract}),
        }

    translated = 0
    missing_by_section: Dict[str, int] = {}

    for sec, key in contract:
        table = getattr(module, sec, None)
        ok = False
        if isinstance(table, dict):
            value = table.get(key)
            if sec == "CHECKS":
                ok = (isinstance(value, (tuple, list)) and len(value) >= 2
                      and str(value[0]).strip() and str(value[1]).strip())
            else:
                ok = isinstance(value, str) and bool(value.strip())
        if ok:
            translated += 1
        else:
            missing_by_section[sec] = missing_by_section.get(sec, 0) + 1

    return {
        "code": code,
        "translated": translated,
        "total": total,
        "percent": round(translated / total * 100, 1) if total else 0.0,
        "missing_by_section": missing_by_section,
    }


def catalog_summary() -> Dict[str, Any]:
    """Language list with native names, script, direction and coverage."""
    languages = {}
    for code in available():
        info = meta(code)
        cov = coverage(code)
        languages[code] = {
            "name_native": info.get("name_native", code),
            "name_en": info.get("name_en", code),
            "script": info.get("script", ""),
            "rtl": bool(info.get("rtl", False)),
            "scheduled": bool(info.get("scheduled", True)),
            "review_status": info.get("review_status", "needs_native_review"),
            "coverage_percent": cov["percent"],
        }
    return {
        "languages": languages,
        "total_languages": len(languages),
        "scheduled_languages": len(scheduled_languages()),
        "contract_keys": len(_contract_keys()),
    }
