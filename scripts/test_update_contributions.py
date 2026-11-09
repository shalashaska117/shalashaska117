import json
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET

import update_contributions as cards


class ContributionTests(unittest.TestCase):
    @patch.object(cards.subprocess, "run")
    def test_total_count_is_not_limited_to_returned_items(self, run):
        run.return_value.stdout = json.dumps({
            "total_count": 1500, "incomplete_results": False, "items": [{}],
        })
        self.assertEqual(cards.search_count("is:pr"), 1500)

    @patch.object(cards.subprocess, "run")
    def test_incomplete_search_is_rejected(self, run):
        run.return_value.stdout = json.dumps({"total_count": 5, "incomplete_results": True})
        with self.assertRaises(ValueError):
            cards.search_count("is:pr")

    @patch.object(cards, "search_count", side_effect=[47, 24, 1, 3, 8])
    def test_every_query_excludes_private_and_owned_repositories(self, search):
        data = cards.collect()
        self.assertEqual(data["total"], 47)
        self.assertEqual(data["projects"][0]["repository"], "vprover/vampire")
        for call in search.call_args_list:
            query = call.args[0].split()
            self.assertIn("is:public", query)
            self.assertIn("is:merged", query)
            self.assertIn("author:shalashaska117", query)
            self.assertIn("-user:shalashaska117", query)

    @patch.object(cards, "search_count", side_effect=[1, 24, 1, 3, 8])
    def test_inconsistent_snapshot_is_rejected(self, search):
        with self.assertRaises(ValueError):
            cards.collect()

    @patch.object(cards, "collect", side_effect=RuntimeError("API unavailable"))
    @patch.object(cards.Path, "write_text")
    def test_api_failure_preserves_existing_files(self, write, collect):
        with self.assertRaises(RuntimeError):
            cards.main()
        write.assert_not_called()

    def test_zero_counts_and_xml_escaping(self):
        data = {"total": 0, "updated": "2026-11-09", "projects": [
            {"name": "A & B <test>", "merged": 0},
        ]}
        for theme in cards.THEMES:
            root = ET.fromstring(cards.render(data, theme))
            self.assertIn("A & B <test>", "".join(root.itertext()))


if __name__ == "__main__":
    unittest.main()
