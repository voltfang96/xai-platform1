"""
Regulator-specific explanation grammar.

This package sits between the model output and the rendered explanation. The
same computation object can be presented against different regulators'
disclosure requirements by selecting a different schema; the schemas are data
files, not code, so a circular update is a config change.

Task 1 scope (this commit): the schema file format, a strict loader, and the
meta-schema validator that rejects malformed config. No regulator schema files
are included yet - those arrive in tasks 2 and 5, and only with citations
verified against primary instrument text.

  meta_schema.py  the contract every schema file must satisfy, and its checker
  yaml_lite.py    YAML loading; prefers PyYAML, falls back to a strict subset
  loader.py       load + validate + registry lookup
  schemas/        the schema files themselves

Deliberately absent: any regulatory field, threshold or citation invented by
this codebase. Every field in every schema must name a source declared in the
same file, and the validator enforces it.
"""
from .loader import (  # noqa: F401
    SCHEMA_DIR,
    SchemaError,
    SchemaRegistry,
    load_file,
    load_text,
    registry,
)
from .meta_schema import (  # noqa: F401
    FIELD_SCOPES,
    FIELD_TYPES,
    REGULATOR_STATUSES,
    RULE_KINDS,
    RULE_SEVERITIES,
    VERIFICATION_LEVELS,
    validate,
)

__all__ = [
    "SCHEMA_DIR", "SchemaError", "SchemaRegistry", "load_file", "load_text",
    "registry", "validate", "REGULATOR_STATUSES", "FIELD_SCOPES",
    "VERIFICATION_LEVELS", "FIELD_TYPES", "RULE_KINDS", "RULE_SEVERITIES",
]
