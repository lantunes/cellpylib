import unittest
import pytest
import cellpylib as cpl
import numpy as np


class TestCTRBLRule(unittest.TestCase):

    def test_rotations(self):
        ctrbl = cpl.CTRBLRule({
            (0, 1, 2, 3, 4): "a",
            (5, 6, 7, 8, 9): "b"
        })
        self.assertEqual(ctrbl.rule_table, {
            (0, 1, 2, 3, 4): "a",
            (5, 6, 7, 8, 9): "b"
        })

        ctrbl = cpl.CTRBLRule({
            (0, 1, 2, 3, 4): "a",
            (5, 6, 7, 8, 9): "b"
        }, add_rotations=True)
        self.assertEqual(ctrbl.rule_table, {
            (0, 1, 2, 3, 4): "a",
            (0, 4, 1, 2, 3): "a",
            (0, 3, 4, 1, 2): "a",
            (0, 2, 3, 4, 1): "a",
            (5, 6, 7, 8, 9): "b",
            (5, 9, 6, 7, 8): "b",
            (5, 8, 9, 6, 7): "b",
            (5, 7, 8, 9, 6): "b"
        })

    def test_rule(self):
        ctrbl = cpl.CTRBLRule({
            (0, 1, 2, 3, 4): "a",
            (5, 6, 7, 8, 9): "b"
        })

        n = np.array([
            [0, 1, 0],
            [4, 0, 2],
            [0, 3, 0]
        ])
        activity = ctrbl.rule(n, 4, 1)
        self.assertEqual("a", activity)

    def test_activity_rule_does_not_exist(self):
        ctrbl = cpl.CTRBLRule({
            (5, 6, 7, 8, 9): "b"
        })

        with pytest.raises(Exception) as e:
            n = np.array([
                [0, 1, 0],
                [4, 0, 2],
                [0, 3, 0]
            ])
            ctrbl.rule(n, 4, 1)
        self.assertEqual(e.value.args, ("neighbourhood state (0, 1, 2, 3, 4) not in rule table",))
