import unittest

import numpy as np
import os

import cellpylib as ca

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class TestCellularAutomataFunctions(unittest.TestCase):

    def test_rule0_simple_init(self):
        expected = self._convert_to_numpy_matrix("rule0_simple_init.ca")
        actual = self._create_ca(expected, 0)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_rule0_random_init(self):
        expected = self._convert_to_numpy_matrix("rule0_random_init.ca")
        actual = self._create_ca(expected, 0)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_rule30_simple_init(self):
        expected = self._convert_to_numpy_matrix("rule30_simple_init.ca")
        actual = self._create_ca(expected, 30)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_rule30_random_init(self):
        expected = self._convert_to_numpy_matrix("rule30_random_init.ca")
        actual = self._create_ca(expected, 30)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_rule126_simple_init(self):
        expected = self._convert_to_numpy_matrix("rule126_simple_init.ca")
        actual = self._create_ca(expected, 126)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_rule126_random_init(self):
        expected = self._convert_to_numpy_matrix("rule126_random_init.ca")
        actual = self._create_ca(expected, 126)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_rule225_simple_init(self):
        expected = self._convert_to_numpy_matrix("rule225_simple_init.ca")
        actual = self._create_ca(expected, 225)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_rule225_random_init(self):
        expected = self._convert_to_numpy_matrix("rule225_random_init.ca")
        actual = self._create_ca(expected, 225)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_rule255_simple_init(self):
        expected = self._convert_to_numpy_matrix("rule255_simple_init.ca")
        actual = self._create_ca(expected, 255)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_rule255_random_init(self):
        expected = self._convert_to_numpy_matrix("rule255_random_init.ca")
        actual = self._create_ca(expected, 255)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_totalistic_3color_rule777_simple_init(self):
        expected = self._convert_to_numpy_matrix("tot3_rule777_simple_init.ca")
        actual = self._create_totalistic_ca(expected, 3, 777)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_totalistic_3color_rule777_random_init(self):
        expected = self._convert_to_numpy_matrix("tot3_rule777_random_init.ca")
        actual = self._create_totalistic_ca(expected, 3, 777)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_totalistic_4color_rule107396_simple_init(self):
        expected = self._convert_to_numpy_matrix("tot4_rule107396_simple_init.ca")
        actual = self._create_totalistic_ca(expected, 4, 107396)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_totalistic_4color_rule107396_random_init(self):
        expected = self._convert_to_numpy_matrix("tot4_rule107396_random_init.ca")
        actual = self._create_totalistic_ca(expected, 4, 107396)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_random_rule_table(self):
        table, _, _ = ca.random_rule_table(k=2, r=1)
        self.assertTrue(0 <= table['000'] <= 1)
        self.assertTrue(0 <= table['001'] <= 1)
        self.assertTrue(0 <= table['010'] <= 1)
        self.assertTrue(0 <= table['100'] <= 1)
        self.assertTrue(0 <= table['110'] <= 1)
        self.assertTrue(0 <= table['011'] <= 1)
        self.assertTrue(0 <= table['101'] <= 1)
        self.assertTrue(0 <= table['111'] <= 1)

    def test_random_rule_table_lambda1(self):
        table, actual_lambda, quiescent_val = ca.random_rule_table(k=2, r=1, lambda_val=1.0, quiescent_state=1)
        self.assertEqual(table['000'], 0)
        self.assertEqual(table['001'], 0)
        self.assertEqual(table['010'], 0)
        self.assertEqual(table['100'], 0)
        self.assertEqual(table['110'], 0)
        self.assertEqual(table['011'], 0)
        self.assertEqual(table['101'], 0)
        self.assertEqual(table['111'], 0)
        self.assertEqual(actual_lambda, 1.0)
        self.assertEqual(quiescent_val, 1)

    def test_random_rule_table_lambda0(self):
        table, actual_lambda, quiescent_val = ca.random_rule_table(k=2, r=1, lambda_val=0.0, quiescent_state=1)
        self.assertEqual(table['000'], 1)
        self.assertEqual(table['001'], 1)
        self.assertEqual(table['010'], 1)
        self.assertEqual(table['100'], 1)
        self.assertEqual(table['110'], 1)
        self.assertEqual(table['011'], 1)
        self.assertEqual(table['101'], 1)
        self.assertEqual(table['111'], 1)
        self.assertEqual(actual_lambda, 0.0)
        self.assertEqual(quiescent_val, 1)

    def test_random_rule_table_strong_quiescence(self):
        table, _, _ = ca.random_rule_table(k=4, r=1, strong_quiescence=True)
        self.assertEqual(table['000'], 0)
        self.assertEqual(table['111'], 1)
        self.assertEqual(table['222'], 2)
        self.assertEqual(table['333'], 3)

    def test_random_rule_table_isotropic(self):
        table, _, _ = ca.random_rule_table(k=3, r=1, isotropic=True)
        self.assertTrue(0 <= table['000'] <= 2)
        self.assertTrue(0 <= table['111'] <= 2)
        self.assertTrue(0 <= table['222'] <= 2)
        self.assertTrue(0 <= table['010'] <= 2)
        self.assertTrue(0 <= table['020'] <= 2)
        self.assertTrue(0 <= table['101'] <= 2)
        self.assertTrue(0 <= table['202'] <= 2)
        self.assertTrue(0 <= table['121'] <= 2)
        self.assertTrue(0 <= table['212'] <= 2)
        self.assertEqual(table['001'], table['100'])
        self.assertEqual(table['002'], table['200'])
        self.assertEqual(table['110'], table['011'])
        self.assertEqual(table['220'], table['022'])
        self.assertEqual(table['120'], table['021'])
        self.assertEqual(table['210'], table['012'])
        self.assertEqual(table['211'], table['112'])
        self.assertEqual(table['122'], table['221'])
        self.assertEqual(table['102'], table['201'])

    def test_table_walk_through_increasing(self):
        table, actual_lambda, quiescent_state = ca.random_rule_table(k=3, r=1, lambda_val=0.0)
        table, new_lambda = ca.table_walk_through(table, lambda_val=1.0, k=3, r=1, quiescent_state=quiescent_state)
        self.assertEqual(new_lambda, 1.0)

    def test_table_walk_through_decreasing(self):
        table, actual_lambda, quiescent_state = ca.random_rule_table(k=3, r=1, lambda_val=1.0)
        table, new_lambda = ca.table_walk_through(table, lambda_val=0.0, k=3, r=1, quiescent_state=quiescent_state)
        self.assertEqual(new_lambda, 0.0)

    def test_table_walk_through_increasing_strong_quiescence(self):
        table, actual_lambda, quiescent_state = ca.random_rule_table(k=3, r=1, lambda_val=0.0, strong_quiescence=True)
        table, new_lambda = ca.table_walk_through(table, lambda_val=1.0, k=3, r=1, quiescent_state=quiescent_state,
                                                  strong_quiescence=True)
        np.testing.assert_almost_equal(new_lambda, 0.96, decimal=2)

    def test_table_walk_through_decreasing_strong_quiescence(self):
        table, actual_lambda, quiescent_state = ca.random_rule_table(k=3, r=1, lambda_val=1.0, strong_quiescence=True)
        table, new_lambda = ca.table_walk_through(table, lambda_val=0.0, k=3, r=1, quiescent_state=quiescent_state,
                                                  strong_quiescence=True)
        np.testing.assert_almost_equal(new_lambda, 0.07, decimal=2)

    def test_table_walk_through_increasing_isotropic(self):
        table, actual_lambda, quiescent_state = ca.random_rule_table(k=3, r=1, lambda_val=0.0, isotropic=True)
        table, new_lambda = ca.table_walk_through(table, lambda_val=1.0, k=3, r=1, quiescent_state=quiescent_state,
                                                  isotropic=True)
        self.assertEqual(new_lambda, 1.0)

    def test_table_walk_through_decreasing_isotropic(self):
        table, actual_lambda, quiescent_state = ca.random_rule_table(k=3, r=1, lambda_val=1.0, isotropic=True)
        table, new_lambda = ca.table_walk_through(table, lambda_val=0.0, k=3, r=1, quiescent_state=quiescent_state,
                                                  isotropic=True)
        self.assertEqual(new_lambda, 0.0)

    def test_init_random(self):
        arr = ca.init_random(3, empty_value=9)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 3)
        self.assertTrue(0 <= arr[0][0] <= 1)
        self.assertTrue(0 <= arr[0][1] <= 1)
        self.assertTrue(0 <= arr[0][2] <= 1)

        arr = ca.init_random(3, k=3, empty_value=9)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 3)
        self.assertTrue(0 <= arr[0][0] <= 2)
        self.assertTrue(0 <= arr[0][1] <= 2)
        self.assertTrue(0 <= arr[0][2] <= 2)

        arr = ca.init_random(3, k=3, n_randomized=1, empty_value=9)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 3)
        self.assertEqual(arr[0][0], 9)
        self.assertTrue(0 <= arr[0][1] <= 2)
        self.assertEqual(arr[0][2], 9)

        arr = ca.init_random(3, k=3, n_randomized=0, empty_value=9)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 3)
        self.assertEqual(arr[0][0], 9)
        self.assertEqual(arr[0][1], 9)
        self.assertEqual(arr[0][2], 9)

        arr = ca.init_random(3, k=3, n_randomized=3, empty_value=9)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 3)
        self.assertTrue(0 <= arr[0][0] <= 2)
        self.assertTrue(0 <= arr[0][1] <= 2)
        self.assertTrue(0 <= arr[0][2] <= 2)

        arr = ca.init_random(3, k=3, n_randomized=2, empty_value=9)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 3)
        self.assertTrue(0 <= arr[0][0] <= 2)
        self.assertTrue(0 <= arr[0][1] <= 2)
        self.assertEqual(arr[0][2], 9)

        arr = ca.init_random(1, k=3, n_randomized=1, empty_value=9)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 1)
        self.assertTrue(0 <= arr[0][0] <= 2)

        arr = ca.init_random(1, k=3, n_randomized=0, empty_value=9)
        self.assertEqual(len(arr), 1)
        arr = arr[0]
        self.assertEqual(len(arr), 1)
        self.assertEqual(arr[0], 9)

    def _convert_to_numpy_matrix(self, filename):
        with open(os.path.join(THIS_DIR, filename), 'r') as content_file:
            content = content_file.read()
        content = content.replace('{{', '')
        content = content.replace('}}', '')
        content = content.replace('{', '')
        content = content.replace('},', ';')
        return np.matrix(content, dtype=np.int)

    def _create_ca(self, expected, rule):
        rows, _ = expected.shape
        cellular_automaton = expected[0]
        return ca.evolve(cellular_automaton, n_steps=rows, apply_rule=lambda state, c: ca.nks_rule(state, rule))

    def _create_totalistic_ca(self, expected, k, rule):
        rows, _ = expected.shape
        cellular_automaton = expected[0]
        return ca.evolve(cellular_automaton, n_steps=rows,
                         apply_rule=lambda state, c: ca.totalistic_rule(state, k, rule))

if __name__ == '__main__':
    unittest.main()
