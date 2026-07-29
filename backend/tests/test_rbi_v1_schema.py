"""
Tests for rbi_v1.yaml (Feature 1, task 2).

These are not tests of RBI's rules - the codebase is in no position to assert
those. They test that the schema file says what the compliance owner verified it
should say, and in particular that the two things confirmed NOT to exist stay
absent. A schema is config, and config regresses silently unless something
asserts its content.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.regulatory_grammar import loader  # noqa: E402

SCHEMA_PATH = os.path.join(loader.SCHEMA_DIR, "rbi_v1.yaml")

EXPECTED_FIELDS = {
    "borrower_assessment_basis": ("per_decision", True, "Para 7(i)"),
    "grievance_officer_contact": ("per_entity", True, "Para 11(i)-(ii)"),
    "grievance_escalation_path": ("per_entity", True, "Para 11(iv)"),
    "key_fact_statement_ref": ("per_decision", False, "Para 8(i), Para 8(iv)"),
}


class RbiSchemaTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Loading at all proves it satisfies the meta-schema contract.
        cls.schema = loader.load_file(SCHEMA_PATH)
        cls.fields = {f["key"]: f for f in cls.schema["fields"]}

    # ---- identity and status ------------------------------------------

    def test_declared_in_force_for_rbi_credit_scoring(self):
        self.assertEqual(self.schema["schema_id"], "rbi_v1")
        self.assertEqual(self.schema["regulator"]["code"], "RBI")
        self.assertEqual(self.schema["regulator_status"], "in_force")
        self.assertEqual(self.schema["applies_to"]["domains"], ["credit_scoring"])

    def test_cites_the_2025_directions_not_the_repealed_circular(self):
        sources = self.schema["sources"]
        self.assertEqual(len(sources), 1)
        source = sources[0]
        self.assertIn("2025", source["title"])
        self.assertEqual(source["status"], "in_force")
        self.assertEqual(source["verification"], "primary_verified")
        # The repealed instrument must be recorded as superseded history, not
        # cited as authority.
        self.assertIn("2022", source["supersedes"])

    def test_applies_to_all_decisions_not_just_adverse_ones(self):
        # Omitting `decisions` is meaningful: the duties do not switch off on
        # approval. If someone narrows this to REJECTED, that is a regression.
        self.assertNotIn("decisions", self.schema["applies_to"])

    # ---- the two confirmed absences ------------------------------------

    def test_no_rejection_reason_field(self):
        # RBI's framework has no adverse-action reason requirement. This is the
        # single most likely thing to be wrongly reintroduced from a summary.
        self.assertNotIn("rejection_reason", self.fields)

    # Keys whose values are prose for humans. A threshold may legitimately be
    # *mentioned* here - the file documents that it does not exist - but must
    # never appear in a key, a validation constraint or a rule body, because
    # those are what the engine acts on.
    _PROSE_KEYS = {"note", "notes", "description", "title", "label",
                   "supersedes", "superseded_by", "message", "reviewed_by"}

    def _operative_strings(self, node, path="", found=None):
        """Every string the engine would act on, prose excluded."""
        if found is None:
            found = []
        if isinstance(node, dict):
            for key, value in node.items():
                found.append(("%s.%s(key)" % (path, key), str(key)))
                if key in self._PROSE_KEYS:
                    continue
                self._operative_strings(value, "%s.%s" % (path, key), found)
        elif isinstance(node, list):
            for index, item in enumerate(node):
                self._operative_strings(item, "%s[%d]" % (path, index), found)
        elif node is not None:
            found.append((path, str(node)))
        return found

    def test_no_monetary_threshold_in_operative_config(self):
        # The 2,00,000 conditional does not exist. Guard the parts the engine
        # reads: field keys, validation constraints and rule bodies. Prose that
        # records the absence is fine and is asserted separately below.
        for path, value in self._operative_strings(self.schema):
            for forbidden in ("200000", "2,00,000", "200_000", "2 lakh"):
                self.assertNotIn(
                    forbidden, value,
                    "monetary threshold reappeared as operative config at %s: %r"
                    % (path, value))

    def test_no_threshold_conditional_in_any_rule_body(self):
        # Narrower and blunter: no rule may condition on a loan amount at all.
        for rule in self.schema.get("rules") or []:
            body = {k: v for k, v in rule.items()
                    if k in ("when", "requires", "forbids", "unless",
                             "parameters")}
            for path, value in self._operative_strings(body, rule["id"]):
                self.assertNotIn("amount", value.lower(),
                                 "rule %s conditions on an amount at %s"
                                 % (rule["id"], path))

    def test_omissions_are_documented_in_the_file(self):
        notes = self.schema.get("notes") or ""
        self.assertIn("rejection_reason", notes)
        self.assertIn("2,00,000", notes)

    # ---- fields --------------------------------------------------------

    def test_exactly_the_four_verified_fields(self):
        self.assertEqual(set(self.fields), set(EXPECTED_FIELDS))

    def test_scope_required_and_paragraph_per_field(self):
        for key, (scope, required, locator) in EXPECTED_FIELDS.items():
            field = self.fields[key]
            self.assertEqual(field["scope"], scope, key)
            self.assertEqual(field["required"], required, key)
            self.assertEqual(field["source_locator"], locator, key)

    def test_every_field_is_primary_verified_and_cites_chapter_three(self):
        for key, field in self.fields.items():
            self.assertEqual(field["verification"], "primary_verified", key)
            # Chapter is the durable anchor; it must be recorded separately from
            # the paragraph number so a renumbering does not orphan the field.
            self.assertIn("Chapter III", field["source_section"], key)

    def test_assessment_basis_is_internal_not_a_borrower_disclosure(self):
        # Para 7(i) requires the profile to be captured auditably. It does not
        # require it to be disclosed to the borrower, and the schema must not
        # imply that it does.
        self.assertIs(self.fields["borrower_assessment_basis"]["customer_facing"],
                      False)

    def test_the_three_disclosures_are_customer_facing(self):
        for key in ("grievance_officer_contact", "grievance_escalation_path",
                    "key_fact_statement_ref"):
            self.assertIs(self.fields[key]["customer_facing"], True, key)

    # ---- gap detection preconditions -----------------------------------

    def test_assessment_basis_supports_gap_detection(self):
        # Gap detection lands with the renderer in task 3. This asserts the
        # preconditions it will rely on: the field is mandatory, must be
        # non-empty, and names the three inputs the source names. It replaces
        # rejection_reason as the gap-detection subject.
        field = self.fields["borrower_assessment_basis"]
        self.assertTrue(field["required"])
        self.assertIs(field["validation"]["non_empty"], True)
        self.assertEqual(field["validation"]["must_reference"],
                         ["age", "occupation", "income"])

    # ---- rules ---------------------------------------------------------

    def test_single_conditional_rule_guards_the_kfs(self):
        rules = self.schema["rules"]
        self.assertEqual(len(rules), 1)
        rule = rules[0]
        self.assertEqual(rule["kind"], "conditional_requirement")
        self.assertEqual(rule["severity"], "high")
        self.assertEqual(rule["affects"], ["key_fact_statement_ref"])
        self.assertEqual(rule["when"]["decision_in"], ["APPROVED"])

    def test_inferred_conditionality_is_not_marked_primary_verified(self):
        # The source says "before execution of the contract", not "only on
        # approval". The conditionality is an inference and must be labelled as
        # one, so the compliance view can surface it for confirmation.
        rule = self.schema["rules"][0]
        self.assertEqual(rule["verification"], "secondary_only")
        self.assertIn("FLAG FOR CONFIRMATION", rule["note"])


class RegistryResolutionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.registry = loader.SchemaRegistry().load_all()

    def test_resolves_for_every_credit_decision(self):
        for decision in ("APPROVED", "REJECTED", "REVIEW_REQUIRED"):
            schema = self.registry.resolve("RBI", "credit_scoring", decision)
            self.assertIsNotNone(schema, decision)
            self.assertEqual(schema["schema_id"], "rbi_v1")

    def test_does_not_resolve_for_other_domains_or_regulators(self):
        # None must read as "no schema", never as "compliant".
        self.assertIsNone(self.registry.resolve("RBI", "healthcare", "LOW_RISK_ROUTINE"))
        self.assertIsNone(
            self.registry.resolve("IRDAI", "insurance_underwriting", "DECLINED"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
