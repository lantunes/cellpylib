import unittest

import numpy as np
import os

import cellpylib as cpl

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class TestCellularAutomataFunctions2D(unittest.TestCase):

    def test_init_simple2d_1x1(self):
        arr = cpl.init_simple2d(rows=1, cols=1)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 1)
        self.assertEqual(len(arr[0][0]), 1)
        self.assertEqual(arr[0][0][0], 1)

    def test_init_simple2d_1x1_val2(self):
        arr = cpl.init_simple2d(rows=1, cols=1, val=2)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 1)
        self.assertEqual(len(arr[0][0]), 1)
        self.assertEqual(arr[0][0][0], 2)

    def test_init_simple2d_2x2(self):
        arr = cpl.init_simple2d(rows=2, cols=2)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 2)
        self.assertEqual(len(arr[0][0]), 2)
        self.assertEqual(len(arr[0][1]), 2)
        self.assertEqual(arr[0][0].tolist(), [0, 0])
        self.assertEqual(arr[0][1].tolist(), [0, 1])

    def test_init_simple2d_3x3(self):
        arr = cpl.init_simple2d(rows=3, cols=3)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 3)
        self.assertEqual(len(arr[0][0]), 3)
        self.assertEqual(len(arr[0][1]), 3)
        self.assertEqual(len(arr[0][2]), 3)
        self.assertEqual(arr[0][0].tolist(), [0, 0, 0])
        self.assertEqual(arr[0][1].tolist(), [0, 1, 0])
        self.assertEqual(arr[0][2].tolist(), [0, 0, 0])

    def test_init_simple2d_2x3(self):
        arr = cpl.init_simple2d(rows=2, cols=3)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 2)
        self.assertEqual(len(arr[0][0]), 3)
        self.assertEqual(len(arr[0][1]), 3)
        self.assertEqual(arr[0][0].tolist(), [0, 0, 0])
        self.assertEqual(arr[0][1].tolist(), [0, 1, 0])

    def test_init_random2d_1x1(self):
        arr = cpl.init_random2d(1, 1)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 1)
        self.assertEqual(len(arr[0][0]), 1)
        self.assertTrue(0 <= arr[0][0][0] <= 1)

    def test_init_random2d_1x1_k2(self):
        arr = cpl.init_random2d(rows=1, cols=1, k=2)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 1)
        self.assertEqual(len(arr[0][0]), 1)
        self.assertTrue(0 <= arr[0][0][0] <= 2)

    def test_init_random2d_2x2(self):
        arr = cpl.init_random2d(rows=2, cols=2)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 2)
        self.assertEqual(len(arr[0][0]), 2)
        self.assertEqual(len(arr[0][1]), 2)
        self.assertTrue(0 <= arr[0][0][0] <= 1)
        self.assertTrue(0 <= arr[0][0][1] <= 1)
        self.assertTrue(0 <= arr[0][1][0] <= 1)
        self.assertTrue(0 <= arr[0][1][1] <= 1)

    def test_init_random2d_3x3_k2(self):
        arr = cpl.init_random2d(rows=3, cols=3, k=2)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 3)
        self.assertEqual(len(arr[0][0]), 3)
        self.assertEqual(len(arr[0][1]), 3)
        self.assertEqual(len(arr[0][2]), 3)
        self.assertTrue(0 <= arr[0][0][0] <= 2)
        self.assertTrue(0 <= arr[0][0][1] <= 2)
        self.assertTrue(0 <= arr[0][0][2] <= 2)
        self.assertTrue(0 <= arr[0][1][0] <= 2)
        self.assertTrue(0 <= arr[0][1][1] <= 2)
        self.assertTrue(0 <= arr[0][1][2] <= 2)
        self.assertTrue(0 <= arr[0][2][0] <= 2)
        self.assertTrue(0 <= arr[0][2][1] <= 2)
        self.assertTrue(0 <= arr[0][2][2] <= 2)

    def test_init_random2d_2x3(self):
        arr = cpl.init_random2d(rows=2, cols=3)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 2)
        self.assertEqual(len(arr[0][0]), 3)
        self.assertEqual(len(arr[0][1]), 3)
        self.assertTrue(0 <= arr[0][0][0] <= 1)
        self.assertTrue(0 <= arr[0][0][1] <= 1)
        self.assertTrue(0 <= arr[0][0][2] <= 1)
        self.assertTrue(0 <= arr[0][1][0] <= 1)
        self.assertTrue(0 <= arr[0][1][1] <= 1)
        self.assertTrue(0 <= arr[0][1][2] <= 1)

    def test_init_random2d_dtype(self):
        arr = cpl.init_random2d(rows=2, cols=2, dtype=np.float32)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 2)
        self.assertEqual(len(arr[0][0]), 2)
        self.assertEqual(len(arr[0][1]), 2)
        self.assertTrue(0.0 <= arr[0][0][0] < 1.0)
        self.assertTrue(0.0 <= arr[0][0][1] < 1.0)
        self.assertTrue(0.0 <= arr[0][1][0] < 1.0)
        self.assertTrue(0.0 <= arr[0][1][1] < 1.0)

    def test_tot_rule126_2d_n9_simple_init(self):
        expected = self._convert_to_numpy_matrix("tot_rule126_2d_n9_simple_init.ca")
        actual = self._create_ca(expected, 126, 'Moore')
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_tot_rule26_2d_n5_simple_init(self):
        expected = self._convert_to_numpy_matrix("tot_rule26_2d_n5_simple_init.ca")
        actual = self._create_ca(expected, 26, 'von Neumann')
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_sequential_rule_2d(self):
        cellular_automaton = cpl.init_simple2d(3, 3)
        r = cpl.AsynchronousRule(apply_rule=lambda n, c, t: cpl.totalistic_rule(n, k=2, rule=126),
                                 update_order=range(0, 9))
        cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=18, neighbourhood='Moore',
                                          apply_rule=r.apply_rule)
        expected = [[[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[1, 0, 0], [0, 1, 0], [0, 0, 0]],
                    [[1, 1, 0], [0, 1, 0], [0, 0, 0]], [[1, 1, 1], [0, 1, 0], [0, 0, 0]],
                    [[1, 1, 1], [1, 1, 0], [0, 0, 0]], [[1, 1, 1], [1, 1, 0], [0, 0, 0]],
                    [[1, 1, 1], [1, 1, 1], [0, 0, 0]], [[1, 1, 1], [1, 1, 1], [1, 0, 0]],
                    [[1, 1, 1], [1, 1, 1], [1, 0, 0]], [[1, 1, 1], [1, 1, 1], [1, 0, 0]],
                    [[0, 1, 1], [1, 1, 1], [1, 0, 0]], [[0, 1, 1], [1, 1, 1], [1, 0, 0]],
                    [[0, 1, 1], [1, 1, 1], [1, 0, 0]], [[0, 1, 1], [1, 1, 1], [1, 0, 0]],
                    [[0, 1, 1], [1, 1, 1], [1, 0, 0]], [[0, 1, 1], [1, 1, 1], [1, 0, 0]],
                    [[0, 1, 1], [1, 1, 1], [1, 0, 0]], [[0, 1, 1], [1, 1, 1], [1, 1, 0]]]
        np.testing.assert_equal(expected, cellular_automaton.tolist())

    def _convert_to_numpy_matrix(self, filename):
        with open(os.path.join(THIS_DIR, 'resources', filename), 'r') as content_file:
            content = content_file.read()
            content = content.replace('{{{', '')
        content = content.replace('}}}', '')
        content = content.replace('{{', '')
        content = content.replace('{', '')
        content = [x.split('},') for x in content.split('}},')]
        content = [[h.split(',') for h in x] for x in content]
        content = [[[int(i) for i in h] for h in x] for x in content]
        return np.array(content, dtype=np.int)

    def _create_ca(self, expected, rule, neighbourhood):
        steps, _, _ = expected.shape
        cellular_automaton = np.array([expected[0]])
        return cpl.evolve2d(cellular_automaton, timesteps=steps, r=1, neighbourhood=neighbourhood,
                            apply_rule=lambda n, c, t: cpl.totalistic_rule(n, k=2, rule=rule))
