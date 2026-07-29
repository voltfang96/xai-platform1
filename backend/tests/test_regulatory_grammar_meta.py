"""
Tests for the schema format, loader and meta-schema validator (Feature 1, task 1).

Fixtures here use a deliberately fictional regulator code (EXAMPLE) so that no
test can be mistaken for authoritative regulatory content.

The emphasis is on what the validator must REJECT. A permissive validator is
worthless for this job: the failure mode that matters is a malformed schema
loading anyway and quietly under-reporting a disclosure obligation.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.regulatory_grammar import loader, meta_schema, yaml_lite  # noqa: E402

VALID = """
# A fictional schema used only to exercise the validator.
schema_id: example_v1
schema_version: 1
regulator:
  code: EXAMPLE
  name: Example Authority
regulator_status: in_force

applies_to:
  domains: [credit_scoring]
  decisions: [REJECTED, REVIEW_REQUIRED]

sources:
  - id: example_2025
    title: Example Directions, 2025
    dated: 2025-05-08
    status: in_force
    verification: primary_verified
    note: |
      Multi-line note.
      Second line.

fields:
  - key: assessment_basis
    label: Assessment basis
    scope: per_decision
    type: text
    required: true
    customer_facing: true
    source: example_2025
    source_locator: "para 7.1"
    verification: primary_verified
    description: >
      Folded description that
      spans lines.
    validation:
      non_empty: true
  - key: model_purpose
    label: Model purpose
    scope: per_model
    type: text
    required: false
    source: example_2025

rules:
  - id: example_block
    kind: blocking
    severity: high
    description: Example blocking rule.
    source: example_2025
    affects: [assessment_basis]
"""


def _mutate(text, old, new):
    assert old in text, "fixture drift: %r not found" % old
    return text.replace(old, new, 1)


class YamlLiteTest(unittest.TestCase):
    """The fallback parser must be correct on our subset and refuse the rest."""

    def test_parses_nested_structures(self):
        data = yaml_lite.loads(VALID, "fixture")
        self.assertEqual(data["schema_id"], "example_v1")
        self.assertEqual(data["schema_version"], 1)
        self.assertEqual(data["regulator"]["code"], "EXAMPLE")
        self.assertEqual(data["applies_to"]["domains"], ["credit_scoring"])
        self.assertEqual(data["applies_to"]["decisions"],
                         ["REJECTED", "REVIEW_REQUIRED"])
        self.assertEqual(len(data["fields"]), 2)
        self.assertEqual(data["fields"][0]["key"], "assessment_basis")
        self.assertIs(data["fields"][0]["required"], True)
        self.assertIs(data["fields"][1]["required"], False)
        self.assertEqual(data["fields"][0]["validation"], {"non_empty": True})
        self.assertEqual(data["rules"][0]["affects"], ["assessment_basis"])

    def test_literal_block_preserves_newlines(self):
        note = yaml_lite.loads(VALID, "fixture")["sources"][0]["note"]
        self.assertIn("Multi-line note.\nSecond line.", note)

    def test_folded_block_joins_lines(self):
        text = yaml_lite.loads(VALID, "fixture")["fields"][0]["description"]
        self.assertIn("Folded description that spans lines.", text)

    def test_quoted_scalar_keeps_leading_zero_and_dots(self):
        data = yaml_lite.loads('a: "para 7.1"\nb: 7\n', "fixture")
        self.assertEqual(data["a"], "para 7.1")
        self.assertEqual(data["b"], 7)

    def test_comment_stripped_but_not_inside_quotes(self):
        data = yaml_lite.loads('a: value # trailing\nb: "has # inside"\n', "f")
        self.assertEqual(data["a"], "value")
        self.assertEqual(data["b"], "has # inside")

    def test_rejects_tab_indentation(self):
        with self.assertRaises(yaml_lite.YamlLiteError):
            yaml_lite.loads("a:\n\tb: 1\n", "fixture")

    def test_rejects_anchors_aliases_tags_and_flow_mappings(self):
        for bad in ("a: &anchor 1\n", "a: *alias\n", "a: !tag x\n",
                    "a: {b: 1}\n"):
            with self.assertRaises(yaml_lite.YamlLiteError, msg=bad):
                yaml_lite.loads(bad, "fixture")

    def test_rejects_duplicate_keys(self):
        # A duplicate key silently overwriting a requirement is exactly the
        # class of error this parser must not absorb.
        with self.assertRaises(yaml_lite.YamlLiteError):
            yaml_lite.loads("a: 1\na: 2\n", "fixture")

    def test_error_carries_line_number(self):
        with self.assertRaises(yaml_lite.YamlLiteError) as caught:
            yaml_lite.loads("a: 1\nb: {c: 2}\n", "fixture.yaml")
        self.assertIn("fixture.yaml:2", str(caught.exception))


class MetaSchemaValidTest(unittest.TestCase):

    def test_valid_schema_has_no_problems(self):
        self.assertEqual(meta_schema.validate(
            yaml_lite.loads(VALID, "fixture"), "fixture"), [])

    def test_loader_annotates_provenance(self):
        schema = loader.load_text(VALID, "example_v1.yaml")
        self.assertEqual(schema["_meta"]["source_file"], "example_v1.yaml")
        self.assertIn(schema["_meta"]["parser"],
                      ("PyYAML", "yaml_lite_fallback"))


class MetaSchemaRejectionTest(unittest.TestCase):
    """Each case is a way a real schema file could be wrong."""

    def _problems(self, text):
        return meta_schema.validate(yaml_lite.loads(text, "f"), "f")

    def _assert_rejected(self, text, needle):
        problems = self._problems(text)
        self.assertTrue(problems, "expected rejection but schema validated")
        self.assertTrue(
            any(needle in problem for problem in problems),
            "expected a problem mentioning %r, got %s" % (needle, problems))

    def test_unknown_key_is_rejected(self):
        # The motivating case: a typo that would downgrade a requirement.
        self._assert_rejected(_mutate(VALID, "    required: true",
                                      "    requred: true"), "unknown key")

    def test_missing_required_top_level_key(self):
        self._assert_rejected(_mutate(VALID, "schema_version: 1\n", ""),
                              "missing required key 'schema_version'")

    def test_field_citing_undeclared_source_is_rejected(self):
        self._assert_rejected(
            _mutate(VALID, "    source: example_2025\n    source_locator",
                    "    source: not_declared\n    source_locator"),
            "does not match any declared source id")

    def test_field_without_source_is_rejected(self):
        self._assert_rejected(
            _mutate(VALID, "    source: example_2025\n    source_locator",
                    "    source_locator"),
            "missing required key 'source'")

    def test_in_force_schema_needs_an_in_force_source(self):
        # Guards against a consultation draft being presented as binding.
        self._assert_rejected(
            _mutate(VALID, "    status: in_force", "    status: consultation_draft"),
            "cannot be more current than its sources")

    def test_consultation_draft_needs_a_consultation_source(self):
        self._assert_rejected(
            _mutate(VALID, "regulator_status: in_force",
                    "regulator_status: consultation_draft"),
            "no cited source is a consultation document")

    def test_bad_scope_is_rejected(self):
        self._assert_rejected(
            _mutate(VALID, "    scope: per_decision", "    scope: per_request"),
            "is not one of")

    def test_bad_verification_level_is_rejected(self):
        self._assert_rejected(
            _mutate(VALID, "    verification: primary_verified\n    description",
                    "    verification: looks_right\n    description"),
            "is not one of")

    def test_required_must_be_explicit_boolean(self):
        self._assert_rejected(_mutate(VALID, "    required: true",
                                      '    required: "yes please"'),
                              "must be true or false")

    def test_enum_without_values_is_rejected(self):
        self._assert_rejected(_mutate(VALID, "    type: text\n    required: true",
                                      "    type: enum\n    required: true"),
                              "requires a non-empty values list")

    def test_values_without_enum_type_is_rejected(self):
        self._assert_rejected(
            _mutate(VALID, "    validation:\n      non_empty: true",
                    "    values: [a, b]"),
            "only meaningful when type is 'enum'")

    def test_duplicate_field_key_is_rejected(self):
        self._assert_rejected(_mutate(VALID, "  - key: model_purpose",
                                      "  - key: assessment_basis"),
                              "duplicate field key")

    def test_empty_sources_list_is_rejected(self):
        text = VALID.split("sources:")[0] + "sources: []\nfields:" + \
            VALID.split("fields:")[1]
        self._assert_rejected(text, "non-empty list")

    def test_rule_affecting_unknown_field_is_rejected(self):
        self._assert_rejected(_mutate(VALID, "    affects: [assessment_basis]",
                                      "    affects: [no_such_field]"),
                              "is not a field declared in this file")

    def test_rule_with_bad_kind_is_rejected(self):
        self._assert_rejected(_mutate(VALID, "    kind: blocking",
                                      "    kind: warning"), "is not one of")

    def test_non_mapping_top_level_is_rejected(self):
        self.assertTrue(meta_schema.validate(["not", "a", "mapping"], "f"))

    def test_loader_raises_with_all_problems(self):
        broken = _mutate(_mutate(VALID, "    required: true", "    requred: true"),
                         "schema_version: 1\n", "")
        with self.assertRaises(loader.SchemaError) as caught:
            loader.load_text(broken, "broken.yaml")
        self.assertGreaterEqual(len(caught.exception.problems), 2)


class RegistryTest(unittest.TestCase):

    def test_schemas_directory_has_no_unvalidated_files(self):
        # The real directory must always load cleanly; a schema file that fails
        # validation would otherwise be skipped and read as "no requirements".
        loaded = loader.SchemaRegistry().load_all()
        self.assertIsInstance(loaded.ids(), list)

    def test_resolve_returns_none_when_nothing_applies(self):
        empty = loader.SchemaRegistry(directory=os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "_no_such_dir"))
        empty.load_all()
        # None must mean "no schema", never "compliant".
        self.assertIsNone(empty.resolve("RBI", "credit_scoring", "REJECTED"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
