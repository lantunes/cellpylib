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

if __name__ == '__main__':
    unittest.main()
