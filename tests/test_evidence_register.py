import unittest
from examples.evidence_register import summarize

class EvidenceTests(unittest.TestCase):
    def row(self, **kwargs):
        return dict(asset_id="a", status="planned", area_m2="2.5", source_id="S", locator="row 1") | kwargs

    def test_plans_are_not_confirmed(self):
        r = summarize([self.row()], {"S"})
        self.assertEqual(r["by_status"]["planned"]["area_m2"], "2.5")
        self.assertEqual(r["by_status"]["field_confirmed"]["count"], 0)

    def test_unauthorized_source(self):
        r = summarize([self.row()], {"T"})
        self.assertEqual(len(r["unresolved"]), 1)
        self.assertEqual(r["by_status"]["planned"]["count"], 0)

    def test_invalid_area(self):
        self.assertEqual(len(summarize([self.row(area_m2="NaN")], {"S"})["unresolved"]), 1)

    def test_duplicate(self):
        with self.assertRaises(ValueError):
            summarize([self.row(), self.row()], {"S"})
