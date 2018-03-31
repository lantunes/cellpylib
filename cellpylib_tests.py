import unittest
import cellpylib as ca
import numpy as np


class TestCellularAutomataFunctions(unittest.TestCase):

    def test_rule0_simple_init(self):
        expected = self._convert_to_numpy_matrix("tests/rule0_simple_init.ca")
        actual = self._create_ca(expected, 0)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_rule0_random_init(self):
        expected = self._convert_to_numpy_matrix("tests/rule0_random_init.ca")
        actual = self._create_ca(expected, 0)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_rule30_simple_init(self):
        expected = self._convert_to_numpy_matrix("tests/rule30_simple_init.ca")
        actual = self._create_ca(expected, 30)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_rule30_random_init(self):
        expected = self._convert_to_numpy_matrix("tests/rule30_random_init.ca")
        actual = self._create_ca(expected, 30)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_rule126_simple_init(self):
        expected = self._convert_to_numpy_matrix("tests/rule126_simple_init.ca")
        actual = self._create_ca(expected, 126)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_rule126_random_init(self):
        expected = self._convert_to_numpy_matrix("tests/rule126_random_init.ca")
        actual = self._create_ca(expected, 126)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_rule225_simple_init(self):
        expected = self._convert_to_numpy_matrix("tests/rule225_simple_init.ca")
        actual = self._create_ca(expected, 225)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_rule225_random_init(self):
        expected = self._convert_to_numpy_matrix("tests/rule225_random_init.ca")
        actual = self._create_ca(expected, 225)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_rule255_simple_init(self):
        expected = self._convert_to_numpy_matrix("tests/rule255_simple_init.ca")
        actual = self._create_ca(expected, 255)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_rule255_random_init(self):
        expected = self._convert_to_numpy_matrix("tests/rule255_random_init.ca")
        actual = self._create_ca(expected, 255)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_totalistic_3color_rule777_simple_init(self):
        expected = self._convert_to_numpy_matrix("tests/tot3_rule777_simple_init.ca")
        actual = self._create_totalistic_ca(expected, 3, 777)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_totalistic_3color_rule777_random_init(self):
        expected = self._convert_to_numpy_matrix("tests/tot3_rule777_random_init.ca")
        actual = self._create_totalistic_ca(expected, 3, 777)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_totalistic_4color_rule107396_simple_init(self):
        expected = self._convert_to_numpy_matrix("tests/tot4_rule107396_simple_init.ca")
        actual = self._create_totalistic_ca(expected, 4, 107396)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_totalistic_4color_rule107396_random_init(self):
        expected = self._convert_to_numpy_matrix("tests/tot4_rule107396_random_init.ca")
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

    def _convert_to_numpy_matrix(self, filename):
        with open(filename, 'r') as content_file:
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
