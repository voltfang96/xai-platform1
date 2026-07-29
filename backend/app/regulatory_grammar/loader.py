"""
Loading and registry for regulator schema files.

A schema is only returned if it satisfies the meta-schema contract. There is no
"load with warnings" path: a compliance config that half-parses is a liability,
so ``SchemaError`` carries every violation and the caller gets nothing.

Each loaded schema is annotated under ``_meta`` with where it came from and which
YAML parser read it, so a report can state the provenance of its own template
rather than asserting it.
"""
import os
from typing import Any, Dict, List, Optional

from . import meta_schema, yaml_lite

SCHEMA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "schemas")
SCHEMA_SUFFIXES = (".yaml", ".yml")


class SchemaError(ValueError):
    """A schema file is malformed or violates the meta-schema contract."""

    def __init__(self, source: str, problems: List[str]):
        self.source = source
        self.problems = problems
        detail = "\n  - ".join(problems)
        super().__init__("%s failed validation:\n  - %s" % (source, detail))


def load_text(text: str, source_name: str = "<inline>") -> Dict[str, Any]:
    """Parse and validate a schema from a YAML string."""
    try:
        parsed = yaml_lite.loads(text, source=source_name)
    except yaml_lite.YamlLiteError as exc:
        raise SchemaError(source_name, [str(exc)])

    problems = meta_schema.validate(parsed, source_name)
    if problems:
        raise SchemaError(source_name, problems)

    parsed["_meta"] = {
        "source_file": source_name,
        "parser": "PyYAML" if yaml_lite.using_pyyaml() else "yaml_lite_fallback",
    }
    return parsed


def load_file(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as handle:
        text = handle.read()
    return load_text(text, os.path.basename(path))


class SchemaRegistry:
    """
    All schema files in a directory, indexed by schema_id and regulator code.

    Loading is strict and eager: ``load_all`` raises on the first invalid file
    rather than skipping it, because a silently absent schema would render as
    "no requirements for this regulator", which is the most dangerous possible
    failure mode for this product.
    """

    def __init__(self, directory: Optional[str] = None):
        self.directory = directory or SCHEMA_DIR
        self._by_id: Dict[str, Dict[str, Any]] = {}

    def load_all(self) -> "SchemaRegistry":
        self._by_id = {}
        if not os.path.isdir(self.directory):
            return self
        for name in sorted(os.listdir(self.directory)):
            if not name.endswith(SCHEMA_SUFFIXES):
                continue
            schema = load_file(os.path.join(self.directory, name))
            schema_id = schema["schema_id"]
            if schema_id in self._by_id:
                raise SchemaError(name, [
                    "schema_id %r is already defined by %s" % (
                        schema_id, self._by_id[schema_id]["_meta"]["source_file"])])
            self._by_id[schema_id] = schema
        return self

    # ---- lookup -------------------------------------------------------

    def ids(self) -> List[str]:
        return sorted(self._by_id)

    def get(self, schema_id: str) -> Optional[Dict[str, Any]]:
        return self._by_id.get(schema_id)

    def for_regulator(self, code: str) -> List[Dict[str, Any]]:
        """Every schema declared for a regulator, newest schema_version first."""
        matches = [s for s in self._by_id.values()
                   if s["regulator"].get("code") == code]
        return sorted(matches, key=lambda s: s["schema_version"], reverse=True)

    def resolve(self, regulator: str, domain: str,
                decision: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """
        Pick the schema for a regulator/domain/decision, or None.

        Returning None is a legitimate answer: not every decision a model makes
        has a regulator-specific disclosure schema attached. Callers must treat
        None as "render the generic report", never as "compliant".
        """
        for schema in self.for_regulator(regulator):
            applies = schema.get("applies_to") or {}
            if domain not in (applies.get("domains") or []):
                continue
            decisions = applies.get("decisions")
            if decision is not None and decisions and decision not in decisions:
                continue
            return schema
        return None

    def summary(self) -> Dict[str, Any]:
        """Inventory for the compliance view: status and verification spread."""
        out = {}
        for schema_id, schema in self._by_id.items():
            fields = schema.get("fields") or []
            sources = schema.get("sources") or []
            out[schema_id] = {
                "regulator": schema["regulator"].get("code"),
                "regulator_status": schema["regulator_status"],
                "schema_version": schema["schema_version"],
                "domains": (schema.get("applies_to") or {}).get("domains") or [],
                "field_count": len(fields),
                "required_field_count": sum(
                    1 for f in fields if f.get("required")),
                "rule_count": len(schema.get("rules") or []),
                "scopes": _tally(f.get("scope") for f in fields),
                # Surfaced so a schema resting on unverified citations is
                # visible rather than implied by its absence.
                "source_verification": _tally(
                    s.get("verification") for s in sources),
                "parser": schema["_meta"]["parser"],
            }
        return out


def _tally(values) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for value in values:
        if value is None:
            continue
        counts[value] = counts.get(value, 0) + 1
    return counts


registry = SchemaRegistry()
