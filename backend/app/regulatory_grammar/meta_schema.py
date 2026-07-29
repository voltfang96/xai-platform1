"""
The contract every regulator schema file must satisfy, and its validator.

This is a "meta-schema": it does not describe a regulatory disclosure, it
describes the shape of the files that do. ``jsonschema`` is unavailable in this
deployment (and PyPI is unreachable), so the contract is expressed as data below
and checked by ``validate``.

Design rules, all of which exist because this is compliance config
-----------------------------------------------------------------
1. FAIL CLOSED ON UNKNOWN KEYS. A typo like ``requred: true`` would otherwise
   silently downgrade a mandatory disclosure to optional. Unknown keys are
   errors, not warnings.

2. NO UNCITED FIELD. Every field must name a source declared in the same file,
   and every source must carry a status and a verification level. A field whose
   legal basis cannot be traced is not a field, it is an assumption.

3. STATUS CANNOT BE OVERSTATED. A schema claiming ``in_force`` must cite at
   least one in-force source; one claiming ``consultation_draft`` must cite a
   consultation source. This is what stops a draft framework being presented as
   settled law.

4. SCOPE IS EXPLICIT. Fields declare whether they are a property of the
   decision, the model, or the entity. Without this the renderer would look for
   per-model facts on a per-decision record and report false gaps.

``validate`` returns every problem it finds rather than raising on the first, so
an author fixing a schema sees the whole list in one pass.
"""
from typing import Any, Dict, List, Optional, Set

# ---------------------------------------------------------------- vocabularies

# Whether the instrument behind a schema is currently law.
REGULATOR_STATUSES = (
    "in_force",           # cited instrument is current and binding
    "consultation_draft",  # proposed only; must not be presented as binding
    "superseded_source",   # instrument has been repealed or replaced
)

# What the field is a property of. Determines where the renderer looks.
FIELD_SCOPES = (
    "per_decision",  # varies per decision; read from the explanation record
    "per_model",     # constant for a model version; read from model metadata
    "per_entity",    # constant for the deploying entity; read from config
)

# How well the wording behind a field or source has been checked.
VERIFICATION_LEVELS = (
    "primary_verified",  # read against the primary instrument text
    "secondary_only",    # taken from a summary; not yet checked against primary
    "unverified",        # citation asserted but no text seen
)

FIELD_TYPES = (
    "text",        # free text; use with validation.non_empty for mandatory prose
    "reference",   # pointer to another document, clause or system record
    "enum",        # closed set; requires `values`
    "boolean",
    "number",
    "date",
    "record_ref",  # structured reference: who/when/record id
)

RULE_KINDS = (
    "blocking",                # decision must not be issued while triggered
    "conditional_requirement",  # a field becomes required under a condition
    "advisory",                # surfaced to the officer, does not block
)

RULE_SEVERITIES = ("high", "medium", "low")

# Rule bodies are validated structurally here; their evaluation semantics are
# defined by the rules engine (task 3). Keys are allowed but not interpreted.
_RULE_BODY_KEYS = {"when", "requires", "forbids", "unless", "parameters"}

# ---------------------------------------------------------------- key contracts

_TOP_LEVEL_REQUIRED = {"schema_id", "schema_version", "regulator",
                       "regulator_status", "applies_to", "sources", "fields"}
_TOP_LEVEL_OPTIONAL = {"rules", "notes", "review"}

_REGULATOR_REQUIRED = {"code"}
_REGULATOR_OPTIONAL = {"name", "name_i18n_key"}

_APPLIES_TO_REQUIRED = {"domains"}
_APPLIES_TO_OPTIONAL = {"decisions", "note"}

_SOURCE_REQUIRED = {"id", "title", "status", "verification"}
_SOURCE_OPTIONAL = {"dated", "reference", "url", "note", "supersedes", "superseded_by"}

_FIELD_REQUIRED = {"key", "label", "scope", "type", "required", "source"}
_FIELD_OPTIONAL = {"source_locator", "verification", "description",
                   "label_i18n_key", "values", "validation", "note",
                   "customer_facing"}

_VALIDATION_OPTIONAL = {"non_empty", "min_length", "must_reference", "max_length"}

_RULE_REQUIRED = {"id", "kind", "severity", "description", "source"}
_RULE_OPTIONAL = {"affects", "source_locator", "verification", "note",
                  "message"} | _RULE_BODY_KEYS

_REVIEW_OPTIONAL = {"last_reviewed", "reviewed_by", "next_review_due", "note"}


def _check_keys(obj: Dict[str, Any], required: Set[str], optional: Set[str],
                path: str, errors: List[str]) -> None:
    missing = sorted(required - set(obj))
    for key in missing:
        errors.append("%s: missing required key %r" % (path, key))
    unknown = sorted(set(obj) - required - optional)
    for key in unknown:
        errors.append(
            "%s: unknown key %r (unknown keys are rejected so a typo cannot "
            "silently change meaning)" % (path, key))


def _check_choice(value: Any, allowed: tuple, path: str,
                  errors: List[str]) -> None:
    if value not in allowed:
        errors.append("%s: %r is not one of %s" % (path, value, list(allowed)))


def _require_text(value: Any, path: str, errors: List[str]) -> None:
    if not isinstance(value, str) or not value.strip():
        errors.append("%s: must be a non-empty string" % path)


def validate(schema: Any, source_name: str = "<schema>") -> List[str]:
    """Return a list of contract violations; empty means the schema is valid."""
    errors: List[str] = []

    if not isinstance(schema, dict):
        return ["%s: top level must be a mapping" % source_name]

    _check_keys(schema, _TOP_LEVEL_REQUIRED, _TOP_LEVEL_OPTIONAL,
                source_name, errors)

    _require_text(schema.get("schema_id"), "%s.schema_id" % source_name, errors)
    if not isinstance(schema.get("schema_version"), int):
        errors.append("%s.schema_version: must be an integer" % source_name)

    status = schema.get("regulator_status")
    _check_choice(status, REGULATOR_STATUSES,
                  "%s.regulator_status" % source_name, errors)

    _validate_regulator(schema.get("regulator"), source_name, errors)
    _validate_applies_to(schema.get("applies_to"), source_name, errors)
    source_ids = _validate_sources(schema.get("sources"), source_name, errors)
    _validate_status_consistency(status, schema.get("sources"), source_name, errors)
    field_keys = _validate_fields(schema.get("fields"), source_ids,
                                  source_name, errors)
    _validate_rules(schema.get("rules"), source_ids, field_keys,
                    source_name, errors)

    review = schema.get("review")
    if review is not None:
        if isinstance(review, dict):
            _check_keys(review, set(), _REVIEW_OPTIONAL,
                        "%s.review" % source_name, errors)
        else:
            errors.append("%s.review: must be a mapping" % source_name)

    return errors


def _validate_regulator(regulator: Any, source_name: str,
                        errors: List[str]) -> None:
    path = "%s.regulator" % source_name
    if not isinstance(regulator, dict):
        errors.append("%s: must be a mapping" % path)
        return
    _check_keys(regulator, _REGULATOR_REQUIRED, _REGULATOR_OPTIONAL, path, errors)
    _require_text(regulator.get("code"), "%s.code" % path, errors)


def _validate_applies_to(applies_to: Any, source_name: str,
                         errors: List[str]) -> None:
    path = "%s.applies_to" % source_name
    if not isinstance(applies_to, dict):
        errors.append("%s: must be a mapping" % path)
        return
    _check_keys(applies_to, _APPLIES_TO_REQUIRED, _APPLIES_TO_OPTIONAL,
                path, errors)

    domains = applies_to.get("domains")
    if not isinstance(domains, list) or not domains:
        errors.append("%s.domains: must be a non-empty list" % path)
    else:
        for position, domain in enumerate(domains):
            _require_text(domain, "%s.domains[%d]" % (path, position), errors)

    decisions = applies_to.get("decisions")
    if decisions is not None:
        if not isinstance(decisions, list):
            errors.append(
                "%s.decisions: must be a list (omit the key to mean 'all "
                "decisions')" % path)
        else:
            for position, decision in enumerate(decisions):
                _require_text(decision, "%s.decisions[%d]" % (path, position),
                              errors)


def _validate_sources(sources: Any, source_name: str,
                      errors: List[str]) -> Set[str]:
    path = "%s.sources" % source_name
    ids: Set[str] = set()
    if not isinstance(sources, list) or not sources:
        errors.append(
            "%s: must be a non-empty list; a schema with no cited source "
            "cannot be traced to a legal basis" % path)
        return ids

    for position, entry in enumerate(sources):
        entry_path = "%s[%d]" % (path, position)
        if not isinstance(entry, dict):
            errors.append("%s: must be a mapping" % entry_path)
            continue
        _check_keys(entry, _SOURCE_REQUIRED, _SOURCE_OPTIONAL, entry_path, errors)

        identifier = entry.get("id")
        _require_text(identifier, "%s.id" % entry_path, errors)
        if isinstance(identifier, str):
            if identifier in ids:
                errors.append("%s.id: duplicate source id %r"
                              % (entry_path, identifier))
            ids.add(identifier)

        _require_text(entry.get("title"), "%s.title" % entry_path, errors)
        _check_choice(entry.get("status"), REGULATOR_STATUSES,
                      "%s.status" % entry_path, errors)
        _check_choice(entry.get("verification"), VERIFICATION_LEVELS,
                      "%s.verification" % entry_path, errors)
    return ids


def _validate_status_consistency(status: Any, sources: Any, source_name: str,
                                 errors: List[str]) -> None:
    """A schema must not claim more authority than its sources carry."""
    if not isinstance(sources, list):
        return
    statuses = {entry.get("status") for entry in sources
                if isinstance(entry, dict)}
    if status == "in_force" and "in_force" not in statuses:
        errors.append(
            "%s.regulator_status: declared 'in_force' but no cited source has "
            "status 'in_force'; a schema cannot be more current than its "
            "sources" % source_name)
    if status == "consultation_draft" and "consultation_draft" not in statuses:
        errors.append(
            "%s.regulator_status: declared 'consultation_draft' but no cited "
            "source is a consultation document" % source_name)


def _validate_fields(fields: Any, source_ids: Set[str], source_name: str,
                     errors: List[str]) -> Set[str]:
    path = "%s.fields" % source_name
    keys: Set[str] = set()
    if not isinstance(fields, list) or not fields:
        errors.append("%s: must be a non-empty list" % path)
        return keys

    for position, field in enumerate(fields):
        field_path = "%s[%d]" % (path, position)
        if not isinstance(field, dict):
            errors.append("%s: must be a mapping" % field_path)
            continue
        _check_keys(field, _FIELD_REQUIRED, _FIELD_OPTIONAL, field_path, errors)

        key = field.get("key")
        _require_text(key, "%s.key" % field_path, errors)
        if isinstance(key, str):
            if key in keys:
                errors.append("%s.key: duplicate field key %r"
                              % (field_path, key))
            keys.add(key)
            field_path = "%s(%s)" % (field_path, key)

        _require_text(field.get("label"), "%s.label" % field_path, errors)
        _check_choice(field.get("scope"), FIELD_SCOPES,
                      "%s.scope" % field_path, errors)
        _check_choice(field.get("type"), FIELD_TYPES,
                      "%s.type" % field_path, errors)

        if not isinstance(field.get("required"), bool):
            errors.append(
                "%s.required: must be true or false, written explicitly"
                % field_path)

        _check_source_ref(field.get("source"), source_ids,
                          "%s.source" % field_path, errors)

        if field.get("verification") is not None:
            _check_choice(field.get("verification"), VERIFICATION_LEVELS,
                          "%s.verification" % field_path, errors)

        if field.get("type") == "enum":
            values = field.get("values")
            if not isinstance(values, list) or not values:
                errors.append(
                    "%s.values: type 'enum' requires a non-empty values list"
                    % field_path)
        elif "values" in field:
            errors.append(
                "%s.values: only meaningful when type is 'enum'" % field_path)

        validation = field.get("validation")
        if validation is not None:
            if isinstance(validation, dict):
                _check_keys(validation, set(), _VALIDATION_OPTIONAL,
                            "%s.validation" % field_path, errors)
            else:
                errors.append("%s.validation: must be a mapping" % field_path)

        if field.get("customer_facing") is not None and not isinstance(
                field.get("customer_facing"), bool):
            errors.append("%s.customer_facing: must be true or false"
                          % field_path)
    return keys


def _check_source_ref(value: Any, source_ids: Set[str], path: str,
                      errors: List[str]) -> None:
    if not isinstance(value, str) or not value.strip():
        errors.append(
            "%s: must name a source declared in this file; an uncited field "
            "is an assumption, not a requirement" % path)
        return
    if source_ids and value not in source_ids:
        errors.append("%s: %r does not match any declared source id (%s)"
                      % (path, value, ", ".join(sorted(source_ids)) or "none"))


def _validate_rules(rules: Any, source_ids: Set[str], field_keys: Set[str],
                    source_name: str, errors: List[str]) -> None:
    if rules is None:
        return
    path = "%s.rules" % source_name
    if not isinstance(rules, list):
        errors.append("%s: must be a list" % path)
        return

    seen: Set[str] = set()
    for position, rule in enumerate(rules):
        rule_path = "%s[%d]" % (path, position)
        if not isinstance(rule, dict):
            errors.append("%s: must be a mapping" % rule_path)
            continue
        _check_keys(rule, _RULE_REQUIRED, _RULE_OPTIONAL, rule_path, errors)

        identifier = rule.get("id")
        _require_text(identifier, "%s.id" % rule_path, errors)
        if isinstance(identifier, str):
            if identifier in seen:
                errors.append("%s.id: duplicate rule id %r"
                              % (rule_path, identifier))
            seen.add(identifier)
            rule_path = "%s(%s)" % (rule_path, identifier)

        _check_choice(rule.get("kind"), RULE_KINDS, "%s.kind" % rule_path, errors)
        _check_choice(rule.get("severity"), RULE_SEVERITIES,
                      "%s.severity" % rule_path, errors)
        _require_text(rule.get("description"), "%s.description" % rule_path,
                      errors)
        _check_source_ref(rule.get("source"), source_ids,
                          "%s.source" % rule_path, errors)

        if rule.get("verification") is not None:
            _check_choice(rule.get("verification"), VERIFICATION_LEVELS,
                          "%s.verification" % rule_path, errors)

        affects = rule.get("affects")
        if affects is not None:
            if not isinstance(affects, list):
                errors.append("%s.affects: must be a list of field keys"
                              % rule_path)
            else:
                for entry in affects:
                    if not isinstance(entry, str):
                        errors.append("%s.affects: entries must be field keys"
                                      % rule_path)
                    elif field_keys and entry not in field_keys:
                        errors.append(
                            "%s.affects: %r is not a field declared in this "
                            "file" % (rule_path, entry))
