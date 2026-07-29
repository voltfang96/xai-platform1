# Regulator schema files

One file per regulator per schema version. These are **compliance
configuration**, not code: they change when a circular changes, without a
release.

This directory is intentionally empty of regulator content until each schema's
fields have been checked against primary instrument text.

## Rules for authoring

1. **Every field cites a source declared in the same file.** The validator
   rejects a field whose `source` does not match a declared source `id`. A field
   without a traceable legal basis is an assumption, and assumptions do not
   belong in a filing.

2. **State the verification level honestly.** `primary_verified` means someone
   read the instrument text. `secondary_only` means it came from a summary.
   `unverified` means the citation is asserted but no text was seen. Do not
   upgrade a level without reading the primary document.

3. **`regulator_status` cannot overstate the source.** A schema marked
   `in_force` must cite at least one `in_force` source. A framework still out
   for consultation is `consultation_draft` and must stay that way until the
   final instrument is published — a draft presented as binding is worse than no
   schema at all.

4. **Unknown keys are errors.** A typo such as `requred: true` would otherwise
   silently turn a mandatory disclosure optional, so the validator fails closed.

5. **Put caveats in YAML comments next to the field they qualify.** That is the
   reason these files are YAML and not JSON. If a threshold, date or paragraph
   number is uncertain, say so inline where the next author will see it.

6. **Absent is not the same as satisfied.** If an instrument does not require a
   field, omit the field. Never add a placeholder field to make a scorecard look
   complete.

## Field scope

| Scope | Meaning | Read from |
|---|---|---|
| `per_decision` | Varies with each decision | The explanation record |
| `per_model` | Constant for a model version | Model metadata |
| `per_entity` | Constant for the deploying entity | Deployment config |

Scope matters: without it the renderer would hunt for per-model facts (a model's
accuracy, its purpose) on a single decision record and report gaps that are not
real gaps.

## File layout

```yaml
schema_id: example_v1          # unique; filename should match
schema_version: 1
regulator:
  code: EXAMPLE                # matches the i18n REGULATORS key where one exists
  name: Example Authority
regulator_status: in_force     # in_force | consultation_draft | superseded_source

applies_to:
  domains: [credit_scoring]    # engine domain codes this schema renders for
  decisions: [REJECTED]        # optional; omit to mean every decision

sources:
  - id: example_2025
    title: Example Directions, 2025
    dated: 2025-05-08
    reference: EX/2025-26/01
    status: in_force
    verification: primary_verified
    note: |
      Anything the next author needs to know about how far this was checked.

fields:
  - key: some_disclosure
    label: Some disclosure
    scope: per_decision
    type: text                 # text|reference|enum|boolean|number|date|record_ref
    required: true
    customer_facing: true      # optional; false for internal governance records
    source: example_2025
    source_locator: "para 7.1" # where in the source
    verification: primary_verified
    description: What this field must contain, in the source's own terms.
    validation:
      non_empty: true

rules:                         # optional
  - id: example_block
    kind: blocking             # blocking | conditional_requirement | advisory
    severity: high
    description: What this rule prevents, and why.
    source: example_2025
    source_locator: "para 13"
    affects: [some_disclosure]

review:                        # optional bookkeeping
  last_reviewed: 2026-07-28
  reviewed_by: compliance
  next_review_due: 2027-07-28
```

Rule bodies (`when` / `requires` / `forbids` / `unless` / `parameters`) are
accepted structurally by the validator but their evaluation semantics belong to
the rules engine, which lands with task 3. Do not rely on them executing yet.
