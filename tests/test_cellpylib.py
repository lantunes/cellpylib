import unittest

import numpy as np
import os
import ast

import cellpylib as cpl

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
        table, _, _ = cpl.random_rule_table(k=2, r=1)
        self.assertTrue(0 <= table['000'] <= 1)
        self.assertTrue(0 <= table['001'] <= 1)
        self.assertTrue(0 <= table['010'] <= 1)
        self.assertTrue(0 <= table['100'] <= 1)
        self.assertTrue(0 <= table['110'] <= 1)
        self.assertTrue(0 <= table['011'] <= 1)
        self.assertTrue(0 <= table['101'] <= 1)
        self.assertTrue(0 <= table['111'] <= 1)

    def test_random_rule_table_lambda1(self):
        table, actual_lambda, quiescent_val = cpl.random_rule_table(k=2, r=1, lambda_val=1.0, quiescent_state=1)
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
        table, actual_lambda, quiescent_val = cpl.random_rule_table(k=2, r=1, lambda_val=0.0, quiescent_state=1)
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
        table, _, _ = cpl.random_rule_table(k=4, r=1, strong_quiescence=True)
        self.assertEqual(table['000'], 0)
        self.assertEqual(table['111'], 1)
        self.assertEqual(table['222'], 2)
        self.assertEqual(table['333'], 3)

    def test_random_rule_table_isotropic(self):
        table, _, _ = cpl.random_rule_table(k=3, r=1, isotropic=True)
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
        table, actual_lambda, quiescent_state = cpl.random_rule_table(k=3, r=1, lambda_val=0.0)
        table, new_lambda = cpl.table_walk_through(table, lambda_val=1.0, k=3, r=1, quiescent_state=quiescent_state)
        self.assertEqual(new_lambda, 1.0)

    def test_table_walk_through_decreasing(self):
        table, actual_lambda, quiescent_state = cpl.random_rule_table(k=3, r=1, lambda_val=1.0)
        table, new_lambda = cpl.table_walk_through(table, lambda_val=0.0, k=3, r=1, quiescent_state=quiescent_state)
        self.assertEqual(new_lambda, 0.0)

    def test_table_walk_through_increasing_strong_quiescence(self):
        table, actual_lambda, quiescent_state = cpl.random_rule_table(k=3, r=1, lambda_val=0.0, strong_quiescence=True)
        table, new_lambda = cpl.table_walk_through(table, lambda_val=1.0, k=3, r=1, quiescent_state=quiescent_state,
                                                   strong_quiescence=True)
        np.testing.assert_almost_equal(new_lambda, 0.96, decimal=2)

    def test_table_walk_through_decreasing_strong_quiescence(self):
        table, actual_lambda, quiescent_state = cpl.random_rule_table(k=3, r=1, lambda_val=1.0, strong_quiescence=True)
        table, new_lambda = cpl.table_walk_through(table, lambda_val=0.0, k=3, r=1, quiescent_state=quiescent_state,
                                                   strong_quiescence=True)
        np.testing.assert_almost_equal(new_lambda, 0.07, decimal=2)

    def test_table_walk_through_increasing_isotropic(self):
        table, actual_lambda, quiescent_state = cpl.random_rule_table(k=3, r=1, lambda_val=0.0, isotropic=True)
        table, new_lambda = cpl.table_walk_through(table, lambda_val=1.0, k=3, r=1, quiescent_state=quiescent_state,
                                                   isotropic=True)
        self.assertEqual(new_lambda, 1.0)

    def test_table_walk_through_decreasing_isotropic(self):
        table, actual_lambda, quiescent_state = cpl.random_rule_table(k=3, r=1, lambda_val=1.0, isotropic=True)
        table, new_lambda = cpl.table_walk_through(table, lambda_val=0.0, k=3, r=1, quiescent_state=quiescent_state,
                                                   isotropic=True)
        self.assertEqual(new_lambda, 0.0)

    def test_init_simple_1(self):
        arr = cpl.init_simple(1)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 1)
        self.assertEqual(arr[0][0], 1)

    def test_init_simple_1_val2(self):
        arr = cpl.init_simple(1, val=2)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 1)
        self.assertEqual(arr[0][0], 2)

    def test_init_simple_3(self):
        arr = cpl.init_simple(3)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 3)
        self.assertEqual(arr[0][0], 0)
        self.assertEqual(arr[0][1], 1)
        self.assertEqual(arr[0][2], 0)

    def test_init_random_3(self):
        arr = cpl.init_random(3, empty_value=9)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 3)
        self.assertTrue(0 <= arr[0][0] <= 1)
        self.assertTrue(0 <= arr[0][1] <= 1)
        self.assertTrue(0 <= arr[0][2] <= 1)

    def test_init_random_3_k3(self):
        arr = cpl.init_random(3, k=3, empty_value=9)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 3)
        self.assertTrue(0 <= arr[0][0] <= 2)
        self.assertTrue(0 <= arr[0][1] <= 2)
        self.assertTrue(0 <= arr[0][2] <= 2)

    def test_init_random_3_k3_n1(self):
        arr = cpl.init_random(3, k=3, n_randomized=1, empty_value=9)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 3)
        self.assertEqual(arr[0][0], 9)
        self.assertTrue(0 <= arr[0][1] <= 2)
        self.assertEqual(arr[0][2], 9)

    def test_init_random_3_k3_n0(self):
        arr = cpl.init_random(3, k=3, n_randomized=0, empty_value=9)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 3)
        self.assertEqual(arr[0][0], 9)
        self.assertEqual(arr[0][1], 9)
        self.assertEqual(arr[0][2], 9)

    def test_init_random_3_k3_n3(self):
        arr = cpl.init_random(3, k=3, n_randomized=3, empty_value=9)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 3)
        self.assertTrue(0 <= arr[0][0] <= 2)
        self.assertTrue(0 <= arr[0][1] <= 2)
        self.assertTrue(0 <= arr[0][2] <= 2)

    def test_init_random_3_k3_n2(self):
        arr = cpl.init_random(3, k=3, n_randomized=2, empty_value=9)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 3)
        self.assertTrue(0 <= arr[0][0] <= 2)
        self.assertTrue(0 <= arr[0][1] <= 2)
        self.assertEqual(arr[0][2], 9)

    def test_init_random_1_k3_n1(self):
        arr = cpl.init_random(1, k=3, n_randomized=1, empty_value=9)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 1)
        self.assertTrue(0 <= arr[0][0] <= 2)

    def test_init_random_1_k3_n0(self):
        arr = cpl.init_random(1, k=3, n_randomized=0, empty_value=9)
        self.assertEqual(len(arr), 1)
        arr = arr[0]
        self.assertEqual(len(arr), 1)
        self.assertEqual(arr[0], 9)

    def test_shannon_entropy(self):
        entropy = cpl.shannon_entropy('1111111')
        self.assertEqual(entropy, 0)
        entropy = cpl.shannon_entropy('0000000')
        self.assertEqual(entropy, 0)
        entropy = cpl.shannon_entropy('01010101')
        self.assertEqual(entropy, 1.0)
        entropy = cpl.shannon_entropy('00010001')
        np.testing.assert_almost_equal(entropy, 0.8113, decimal=4)
        entropy = cpl.shannon_entropy('1234')
        self.assertEqual(entropy, 2.0)

    def test_average_cell_entropy(self):
        cellular_automaton = self._convert_to_numpy_matrix("rule30_random_init.ca")
        avg_cell_entropy = cpl.average_cell_entropy(cellular_automaton)
        np.testing.assert_almost_equal(avg_cell_entropy, 0.9946, decimal=4)

    def test_joint_shannon_entropy(self):
        joint_entropy = cpl.joint_shannon_entropy('0010101', '3232223')
        np.testing.assert_almost_equal(joint_entropy, 1.842, decimal=3)

    def test_mutual_information(self):
        mutual_information = cpl.mutual_information('0010101', '3232223')
        np.testing.assert_almost_equal(mutual_information, 0.1281, decimal=4)
        mutual_information = cpl.mutual_information('0010101', '1101010')
        np.testing.assert_almost_equal(mutual_information, 0.9852, decimal=4)
        mutual_information = cpl.mutual_information('0010101', '0010101')
        np.testing.assert_almost_equal(mutual_information, 0.9852, decimal=4)
        mutual_information = cpl.mutual_information('0010101', '0001001')
        np.testing.assert_almost_equal(mutual_information, 0.0060, decimal=4)

    def test_average_mutual_information(self):
        cellular_automaton = self._convert_to_numpy_matrix("rule30_random_init.ca")
        avg_mutual_information = cpl.average_mutual_information(cellular_automaton)
        np.testing.assert_almost_equal(avg_mutual_information, 0.0047, decimal=4)
        avg_mutual_information = cpl.average_mutual_information(cellular_automaton, temporal_distance=2)
        np.testing.assert_almost_equal(avg_mutual_information, 0.0050, decimal=4)
        avg_mutual_information = cpl.average_mutual_information(cellular_automaton, temporal_distance=3)
        np.testing.assert_almost_equal(avg_mutual_information, 0.0051, decimal=4)

    def test_evolve_apply_rule_1_step(self):
        cellular_automaton = np.array([[1, 2, 3, 4, 5]])
        cellular_automaton = cpl.evolve(cellular_automaton, timesteps=1, apply_rule=lambda n, c, t: 1)
        np.testing.assert_equal(cellular_automaton.tolist(), [[1, 2, 3, 4, 5]])

    def test_evolve_apply_rule_3_steps(self):
        cellular_automaton = np.array([[1, 2, 3, 4, 5]])
        neighbourhoods = []
        cell_identities = []
        timesteps = []
        def apply_rule(n, c, t):
            neighbourhoods.append(n.tolist())
            cell_identities.append(c)
            timesteps.append(t)
            return n[1]
        cpl.evolve(cellular_automaton, timesteps=3, apply_rule=apply_rule)
        np.testing.assert_equal(neighbourhoods, [[5, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 1],
                                                 [5, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 1]])
        np.testing.assert_equal(cell_identities, [0, 1, 2, 3, 4, 0, 1, 2, 3, 4])
        np.testing.assert_equal(timesteps, [1, 1, 1, 1, 1, 2, 2, 2, 2, 2])

    def test_rule150R_simple_init(self):
        expected = self._convert_to_numpy_matrix("rule150R_simple_init.ca")
        actual = self._create_reversible_ca(expected, 150)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_dtype(self):
        cellular_automaton = cpl.init_simple(11, dtype=np.float32)
        cellular_automaton = cpl.evolve(cellular_automaton, timesteps=6,
                                        apply_rule=lambda n, c, t: sum(n) / len(n))
        np.testing.assert_almost_equal(cellular_automaton.tolist(), [
            [0.0,   0.0,   0.0,   0.0,   0.0,   1.0,   0.0,   0.0,   0.0,   0.0,    0.0],
            [0.0,   0.0,   0.0,   0.0,   0.333, 0.333, 0.333, 0.0,   0.0,   0.0,    0.0],
            [0.0,   0.0,   0.0,   0.111, 0.222, 0.333, 0.222, 0.111, 0.0,   0.0,    0.0],
            [0.0,   0.0,   0.037, 0.111, 0.222, 0.259, 0.222, 0.111, 0.037, 0.0,    0.0],
            [0.0,   0.012, 0.049, 0.123, 0.198, 0.235, 0.198, 0.123, 0.049, 0.0123, 0.0],
            [0.004, 0.021, 0.062, 0.123, 0.185, 0.210, 0.185, 0.123, 0.062, 0.021,  0.004]], decimal=3)

    def test_sequential_left_to_right(self):
        expected = self._convert_to_numpy_matrix("rule60_sequential_simple_init.ca")
        cellular_automaton = cpl.init_simple(21)
        r = cpl.AsynchronousRule(apply_rule=lambda n, c, t: cpl.nks_rule(n, 60), update_order=range(1, 20))
        cellular_automaton = cpl.evolve(cellular_automaton, timesteps=19*20,
                                        apply_rule=r.apply_rule)
        np.testing.assert_equal(expected.tolist(), cellular_automaton[::19].tolist())

    def test_sequential_random(self):
        expected = self._convert_to_numpy_matrix("rule90_sequential_simple_init.ca")
        cellular_automaton = cpl.init_simple(21)
        update_order = [19, 11, 4, 9, 6, 16, 10, 2, 17, 1, 12, 15, 5, 3, 8, 18, 7, 13, 14]
        r = cpl.AsynchronousRule(apply_rule=lambda n, c, t: cpl.nks_rule(n, 90), update_order=update_order)
        cellular_automaton = cpl.evolve(cellular_automaton, timesteps=19*20,
                                        apply_rule=r.apply_rule)
        np.testing.assert_equal(expected.tolist(), cellular_automaton[::19].tolist())

    def test_init_random_dtype(self):
        arr = cpl.init_random(3, dtype=np.float32)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 3)
        self.assertTrue(0.0 <= arr[0][0] < 1.0)
        self.assertTrue(0.0 <= arr[0][1] < 1.0)
        self.assertTrue(0.0 <= arr[0][2] < 1.0)

    def _convert_to_numpy_matrix(self, filename):
        with open(os.path.join(THIS_DIR, 'resources', filename), 'r') as content_file:
            content = content_file.read()
        return np.array(ast.literal_eval(content.replace("{", "[").replace("}", "]")), dtype=np.int32)

    def _create_ca(self, expected, rule):
        rows, _ = expected.shape
        cellular_automaton = expected[0].reshape(1, -1)
        return cpl.evolve(cellular_automaton, timesteps=rows, apply_rule=lambda n, c, t: cpl.nks_rule(n, rule))

    def _create_totalistic_ca(self, expected, k, rule):
        rows, _ = expected.shape
        cellular_automaton = expected[0].reshape(1, -1)
        return cpl.evolve(cellular_automaton, timesteps=rows,
                          apply_rule=lambda n, c, t: cpl.totalistic_rule(n, k, rule))

    def _create_reversible_ca(self, expected, rule):
        rows, _ = expected.shape
        cellular_automaton = expected[0].reshape(1, -1)
        r = cpl.ReversibleRule(cellular_automaton.tolist()[0], rule)
        return cpl.evolve(cellular_automaton, timesteps=rows, apply_rule=r.apply_rule)

    def test_binary_rule(self):
        rule_number = 6667021275756174439087127638698866559
        radius = 3
        timesteps = 12
        init = np.array([[1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1]])

        actual = cpl.evolve(init, timesteps=timesteps,
                            apply_rule=lambda n, c, t: cpl.binary_rule(n, rule_number), r=radius)

        expected = np.array([[1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
                             [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1],
                             [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
                             [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
                             [0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
                             [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
                             [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
                             [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                             [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                             [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_binary_rule_powers_of_two_nks(self):
        rule_number = 30
        radius = 1
        size = 149
        timesteps = 149

        expected = cpl.evolve(cpl.init_simple(size=size), timesteps=timesteps,
                              apply_rule=lambda n, c, t: cpl.binary_rule(n, rule_number, scheme="nks"), r=radius)

        powers_of_two = 2 ** np.arange(radius * 2 + 1)[::-1]
        rule = list(map(int, bin(rule_number)[2:]))
        rule_bin_array = np.pad(rule, ((2 ** (radius * 2 + 1)) - len(rule), 0), 'constant').tolist()
        actual = cpl.evolve(cpl.init_simple(size=size), timesteps=timesteps,
                            apply_rule=lambda n, c, t: cpl.binary_rule(n, rule_bin_array, scheme="nks",
                                                                       powers_of_two=powers_of_two),
                            r=radius)

        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_binary_rule_powers_of_two_default(self):
        rule_number = 6667021275756174439087127638698866559
        radius = 3
        timesteps = 49
        init = np.array([[1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0,
                          1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1]])

        expected = cpl.evolve(init, timesteps=timesteps,
                              apply_rule=lambda n, c, t: cpl.binary_rule(n, rule_number), r=radius)

        powers_of_two = 2 ** np.arange(radius * 2 + 1)[::-1]
        rule = list(map(int, bin(rule_number)[2:]))
        rule_bin_array = np.pad(rule, ((2 ** (radius * 2 + 1)) - len(rule), 0), 'constant')
        actual = cpl.evolve(init, timesteps=timesteps,
                            apply_rule=lambda n, c, t: cpl.binary_rule(n, rule_bin_array, powers_of_two=powers_of_two),
                            r=radius)

        np.testing.assert_equal(expected.tolist(), actual.tolist())


if __name__ == '__main__':
    unittest.main()
