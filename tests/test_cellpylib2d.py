import unittest
import pytest
import matplotlib

import numpy as np
import os

import cellpylib as cpl
import warnings

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
matplotlib.use("Agg")


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

    def test_init_simple2d_coords(self):
        arr = cpl.init_simple2d(rows=3, cols=3, coords=(2, 2))
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 3)
        self.assertEqual(len(arr[0][0]), 3)
        self.assertEqual(len(arr[0][1]), 3)
        self.assertEqual(len(arr[0][2]), 3)
        self.assertEqual(arr[0][0].tolist(), [0, 0, 0])
        self.assertEqual(arr[0][1].tolist(), [0, 0, 0])
        self.assertEqual(arr[0][2].tolist(), [0, 0, 1])

    def test_init_simple2d_coords_invalid_type(self):
        with pytest.raises(Exception):
            cpl.init_simple2d(rows=3, cols=3, coords="a")

    def test_init_simple2d_coords_invalid_length(self):
        with pytest.raises(Exception):
            cpl.init_simple2d(rows=3, cols=3, coords=(0, 1, 2))

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

    def test_tot_rule126_2d_n9_simple_init_memoized(self):
        expected = self._convert_to_numpy_matrix("tot_rule126_2d_n9_simple_init.ca")
        actual = self._create_ca(expected, 126, 'Moore', memoize=True)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_tot_rule126_2d_n9_simple_init_memoize_recursive(self):
        expected = self._convert_to_numpy_matrix("tot_rule126_2d_n9_simple_init.ca")
        actual = self._create_ca(expected, 126, 'Moore', memoize="recursive")
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_tot_rule26_2d_n5_simple_init(self):
        expected = self._convert_to_numpy_matrix("tot_rule26_2d_n5_simple_init.ca")
        actual = self._create_ca(expected, 26, 'von Neumann')
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_tot_rule26_2d_n5_simple_init_memoized(self):
        expected = self._convert_to_numpy_matrix("tot_rule26_2d_n5_simple_init.ca")
        actual = self._create_ca(expected, 26, 'von Neumann', memoize=True)
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_tot_rule26_2d_n5_simple_init_memoize_recursive(self):
        expected = self._convert_to_numpy_matrix("tot_rule26_2d_n5_simple_init.ca")
        actual = self._create_ca(expected, 26, 'von Neumann', memoize="recursive")
        np.testing.assert_equal(expected.tolist(), actual.tolist())

    def test_sequential_rule_2d_update_order(self):
        cellular_automaton = cpl.init_simple2d(3, 3)
        r = cpl.AsynchronousRule(apply_rule=lambda n, c, t: cpl.totalistic_rule(n, k=2, rule=126),
                                 update_order=[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])
        cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=18, neighbourhood='Moore', apply_rule=r)
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

    def test_sequential_rule_2d_num_cells(self):
        np.random.seed(0)
        cellular_automaton = cpl.init_simple2d(3, 3)
        r = cpl.AsynchronousRule(apply_rule=lambda n, c, t: cpl.totalistic_rule(n, k=2, rule=126), num_cells=(3, 3))
        cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=18, neighbourhood='Moore', apply_rule=r)
        expected = [[[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 1, 0]],
                    [[0, 0, 1], [0, 1, 0], [0, 1, 0]], [[0, 1, 1], [0, 1, 0], [0, 1, 0]],
                    [[0, 1, 1], [0, 1, 0], [0, 1, 0]], [[0, 1, 1], [0, 1, 0], [0, 1, 1]],
                    [[0, 1, 1], [0, 1, 0], [1, 1, 1]], [[0, 1, 1], [1, 1, 0], [1, 1, 1]],
                    [[0, 1, 1], [1, 1, 0], [1, 1, 1]], [[0, 1, 1], [1, 1, 0], [1, 1, 1]],
                    [[0, 1, 1], [1, 1, 0], [1, 0, 1]], [[0, 1, 1], [1, 1, 0], [1, 0, 1]],
                    [[0, 1, 1], [1, 1, 0], [1, 0, 1]], [[0, 1, 1], [1, 1, 0], [1, 0, 1]],
                    [[0, 1, 1], [1, 1, 0], [1, 0, 1]], [[0, 1, 1], [1, 1, 0], [1, 0, 1]],
                    [[0, 1, 1], [1, 1, 0], [1, 0, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]]
        np.testing.assert_equal(expected, cellular_automaton.tolist())

    def test_game_of_life_rule(self):
        expected = self._convert_to_numpy_matrix("game_of_life.ca").reshape(60, 60, 60)

        # Glider
        cellular_automaton = cpl.init_simple2d(60, 60)
        cellular_automaton[:, [28, 29, 30, 30], [30, 31, 29, 31]] = 1
        # Blinker
        cellular_automaton[:, [40, 40, 40], [15, 16, 17]] = 1
        # Light Weight Space Ship (LWSS)
        cellular_automaton[:, [18, 18, 19, 20, 21, 21, 21, 21, 20], [45, 48, 44, 44, 44, 45, 46, 47, 48]] = 1

        cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=60, neighbourhood='Moore',
                                          apply_rule=cpl.game_of_life_rule)

        np.testing.assert_equal(expected, cellular_automaton.tolist())

    def test_game_of_life_rule_memoized(self):
        expected = self._convert_to_numpy_matrix("game_of_life.ca").reshape(60, 60, 60)

        # Glider
        cellular_automaton = cpl.init_simple2d(60, 60)
        cellular_automaton[:, [28, 29, 30, 30], [30, 31, 29, 31]] = 1
        # Blinker
        cellular_automaton[:, [40, 40, 40], [15, 16, 17]] = 1
        # Light Weight Space Ship (LWSS)
        cellular_automaton[:, [18, 18, 19, 20, 21, 21, 21, 21, 20], [45, 48, 44, 44, 44, 45, 46, 47, 48]] = 1

        cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=60, neighbourhood='Moore',
                                          apply_rule=cpl.game_of_life_rule, memoize=True)

        np.testing.assert_equal(expected, cellular_automaton.tolist())

    def test_game_of_life_rule_memoize_recursive(self):
        expected = self._convert_to_numpy_matrix("game_of_life.ca").reshape(60, 60, 60)

        # Glider
        cellular_automaton = cpl.init_simple2d(60, 60)
        cellular_automaton[:, [28, 29, 30, 30], [30, 31, 29, 31]] = 1
        # Blinker
        cellular_automaton[:, [40, 40, 40], [15, 16, 17]] = 1
        # Light Weight Space Ship (LWSS)
        cellular_automaton[:, [18, 18, 19, 20, 21, 21, 21, 21, 20], [45, 48, 44, 44, 44, 45, 46, 47, 48]] = 1

        cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=60, neighbourhood='Moore',
                                          apply_rule=cpl.game_of_life_rule, memoize="recursive")

        np.testing.assert_equal(expected, cellular_automaton.tolist())

    def test_langtons_loop(self):
        expected = self._convert_to_numpy_matrix("langtons_loop.ca")

        langtons_loop = cpl.LangtonsLoop()

        cellular_automaton = langtons_loop.init_loops(1, (75, 75), [40], [25])

        cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=10,
                                          apply_rule=langtons_loop)

        np.testing.assert_equal(expected, cellular_automaton.tolist())

    def test_langtons_loop_memoized(self):
        expected = self._convert_to_numpy_matrix("langtons_loop.ca")

        langtons_loop = cpl.LangtonsLoop()

        cellular_automaton = langtons_loop.init_loops(1, (75, 75), [40], [25])

        cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=10,
                                          apply_rule=langtons_loop, memoize=True)

        np.testing.assert_equal(expected, cellular_automaton.tolist())

    def test_langtons_loop_memoize_recursive(self):
        expected = self._convert_to_numpy_matrix("langtons_loop.ca")

        langtons_loop = cpl.LangtonsLoop()

        cellular_automaton = langtons_loop.init_loops(1, (75, 75), [40], [25])

        cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=10,
                                          apply_rule=langtons_loop, memoize="recursive")

        np.testing.assert_equal(expected, cellular_automaton.tolist())

    def test_sdsr_loop(self):
        expected = self._convert_to_numpy_matrix("sdsr_loop.ca")

        sdsr_loop = cpl.SDSRLoop()

        cellular_automaton = sdsr_loop.init_loops(1, (75, 75), [40], [25])

        cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=10,
                                          apply_rule=sdsr_loop)

        np.testing.assert_equal(expected, cellular_automaton.tolist())

    def test_sdsr_loop_memoized(self):
        expected = self._convert_to_numpy_matrix("sdsr_loop.ca")

        sdsr_loop = cpl.SDSRLoop()

        cellular_automaton = sdsr_loop.init_loops(1, (75, 75), [40], [25])

        cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=10,
                                          apply_rule=sdsr_loop, memoize=True)

        np.testing.assert_equal(expected, cellular_automaton.tolist())

    def test_sdsr_loop_memoize_recursive(self):
        expected = self._convert_to_numpy_matrix("sdsr_loop.ca")

        sdsr_loop = cpl.SDSRLoop()

        cellular_automaton = sdsr_loop.init_loops(1, (75, 75), [40], [25])

        cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=10,
                                          apply_rule=sdsr_loop, memoize="recursive")

        np.testing.assert_equal(expected, cellular_automaton.tolist())

    def test_evoloop(self):
        expected = self._convert_to_numpy_matrix("evoloop.ca")

        evoloop = cpl.Evoloop()

        cellular_automaton = evoloop.init_species13_loop((75, 75), 40, 15)

        cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=10,
                                          apply_rule=evoloop)

        np.testing.assert_equal(expected, cellular_automaton.tolist())

    def test_evoloop_memoized(self):
        expected = self._convert_to_numpy_matrix("evoloop.ca")

        evoloop = cpl.Evoloop()

        cellular_automaton = evoloop.init_species13_loop((75, 75), 40, 15)

        cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=10,
                                          apply_rule=evoloop, memoize=True)

        np.testing.assert_equal(expected, cellular_automaton.tolist())

    def test_evoloop_memoize_recursive(self):
        expected = self._convert_to_numpy_matrix("evoloop.ca")

        evoloop = cpl.Evoloop()

        cellular_automaton = evoloop.init_species13_loop((75, 75), 40, 15)

        cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=10,
                                          apply_rule=evoloop, memoize="recursive")

        np.testing.assert_equal(expected, cellular_automaton.tolist())

    def test_block_ca(self):
        expected = self._convert_to_numpy_matrix("block_2d.ca")

        initial_conditions = np.array([[
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]])

        def block2d_rule(n, t):
            n = tuple(tuple(i) for i in n)
            base_rules = {
                ((0, 0), (0, 0)): ((0, 0), (0, 0)),
                ((0, 0), (0, 2)): ((2, 0), (0, 0)),
                ((2, 0), (0, 0)): ((0, 0), (0, 2)),
                ((0, 0), (2, 0)): ((0, 2), (0, 0)),
                ((0, 2), (0, 0)): ((0, 0), (2, 0)),
                ((0, 0), (2, 2)): ((2, 2), (0, 0)),
                ((2, 2), (0, 0)): ((0, 0), (2, 2)),
                ((0, 2), (0, 2)): ((2, 0), (2, 0)),
                ((2, 0), (2, 0)): ((0, 2), (0, 2)),
                ((0, 2), (2, 0)): ((2, 0), (0, 2)),
                ((2, 0), (0, 2)): ((0, 2), (2, 0)),
                ((0, 2), (2, 2)): ((2, 2), (2, 0)),
                ((2, 2), (2, 0)): ((0, 2), (2, 2)),
                ((2, 0), (2, 2)): ((2, 2), (0, 2)),
                ((2, 2), (0, 2)): ((2, 0), (2, 2)),
                ((2, 2), (2, 2)): ((2, 2), (2, 2)),
                # wall rules
                ((0, 0), (1, 1)): ((0, 0), (1, 1)),
                ((0, 1), (1, 1)): ((0, 1), (1, 1)),
                ((0, 2), (1, 1)): ((2, 0), (1, 1)),
                ((2, 0), (1, 1)): ((0, 2), (1, 1)),
                ((2, 1), (1, 1)): ((2, 1), (1, 1)),
                ((2, 2), (1, 1)): ((2, 2), (1, 1)),
                ((1, 1), (1, 1)): ((1, 1), (1, 1)),
            }
            rules = {}
            # add rotations
            for r, v in base_rules.items():
                rules[r] = v
                for _ in range(3):
                    r = ((r[1][0], r[0][0]), (r[1][1], r[0][1]))
                    v = ((v[1][0], v[0][0]), (v[1][1], v[0][1]))
                    if r not in rules:
                        rules[r] = v
            return rules[n]

        ca = cpl.evolve2d_block(initial_conditions, block_size=(2, 2), timesteps=40, apply_rule=block2d_rule)

        np.testing.assert_equal(expected, ca.tolist())

    def test_sandpile(self):
        expected = self._convert_to_numpy_matrix("sandpile.ca")

        n_rows = 10
        n_cols = 10
        sandpile = cpl.Sandpile(n_rows, n_cols)

        np.random.seed(0)
        ca = np.random.randint(5, size=n_rows * n_cols).reshape((1, n_rows, n_cols))
        # we're using a closed boundary, so make the boundary cells 0
        ca[0, 0, :], ca[0, n_rows - 1, :], ca[0, :, 0], ca[0, :, n_cols - 1] = 0, 0, 0, 0

        ca = cpl.evolve2d(ca, timesteps=10, apply_rule=sandpile, neighbourhood="von Neumann")

        np.testing.assert_equal(expected, ca.tolist())

    def test_sandpile_memoized(self):
        expected = self._convert_to_numpy_matrix("sandpile.ca")

        n_rows = 10
        n_cols = 10
        sandpile = cpl.Sandpile(n_rows, n_cols)

        np.random.seed(0)
        ca = np.random.randint(5, size=n_rows * n_cols).reshape((1, n_rows, n_cols))
        # we're using a closed boundary, so make the boundary cells 0
        ca[0, 0, :], ca[0, n_rows - 1, :], ca[0, :, 0], ca[0, :, n_cols - 1] = 0, 0, 0, 0

        ca = cpl.evolve2d(ca, timesteps=10, apply_rule=sandpile, neighbourhood="von Neumann", memoize=True)

        np.testing.assert_equal(expected, ca.tolist())

    def test_sandpile_memoize_recursive(self):
        expected = self._convert_to_numpy_matrix("sandpile.ca")

        n_rows = 10
        n_cols = 10
        sandpile = cpl.Sandpile(n_rows, n_cols)

        np.random.seed(0)
        ca = np.random.randint(5, size=n_rows * n_cols).reshape((1, n_rows, n_cols))
        # we're using a closed boundary, so make the boundary cells 0
        ca[0, 0, :], ca[0, n_rows - 1, :], ca[0, :, 0], ca[0, :, n_cols - 1] = 0, 0, 0, 0

        ca = cpl.evolve2d(ca, timesteps=10, apply_rule=sandpile, neighbourhood="von Neumann", memoize="recursive")

        np.testing.assert_equal(expected, ca.tolist())

    def test_evolve_unknown_neighbourhood_type(self):
        cellular_automaton = np.array([ [[1,1,1], [1,1,1], [1,1,1]] ])
        with pytest.raises(Exception) as e:
            cpl.evolve2d(cellular_automaton, timesteps=2, neighbourhood='foo', apply_rule=cpl.game_of_life_rule)
        self.assertTrue("unknown neighbourhood type: foo" in str(e.value))

    def test_evolve_dynamic_timesteps(self):
        np.random.seed(0)

        n_rows = 10
        n_cols = 10
        sandpile = cpl.Sandpile(n_rows, n_cols)

        initial = np.random.randint(5, size=n_rows * n_cols).reshape((1, n_rows, n_cols))
        # we're using a closed boundary, so make the boundary cells 0
        initial[0, 0, :], initial[0, n_rows - 1, :], initial[0, :, 0], initial[0, :, n_cols - 1] = 0, 0, 0, 0

        ca = cpl.evolve2d(initial, timesteps=cpl.until_fixed_point(),
                          apply_rule=sandpile, neighbourhood="von Neumann")

        self.assertEqual(6, len(ca))

    def test_evolve_dynamic_timesteps_memoized(self):
        np.random.seed(0)

        n_rows = 10
        n_cols = 10
        sandpile = cpl.Sandpile(n_rows, n_cols)

        initial = np.random.randint(5, size=n_rows * n_cols).reshape((1, n_rows, n_cols))
        # we're using a closed boundary, so make the boundary cells 0
        initial[0, 0, :], initial[0, n_rows - 1, :], initial[0, :, 0], initial[0, :, n_cols - 1] = 0, 0, 0, 0

        ca = cpl.evolve2d(initial, timesteps=cpl.until_fixed_point(),
                          apply_rule=sandpile, neighbourhood="von Neumann", memoize=True)

        self.assertEqual(6, len(ca))

    def test_evolve_dynamic_timesteps_memoize_recursive(self):
        np.random.seed(0)

        n_rows = 10
        n_cols = 10
        sandpile = cpl.Sandpile(n_rows, n_cols)

        initial = np.random.randint(5, size=n_rows * n_cols).reshape((1, n_rows, n_cols))
        # we're using a closed boundary, so make the boundary cells 0
        initial[0, 0, :], initial[0, n_rows - 1, :], initial[0, :, 0], initial[0, :, n_cols - 1] = 0, 0, 0, 0

        ca = cpl.evolve2d(initial, timesteps=cpl.until_fixed_point(),
                          apply_rule=sandpile, neighbourhood="von Neumann", memoize="recursive")

        self.assertEqual(6, len(ca))

    def test_sandpile_add_grain(self):
        expected = self._convert_to_numpy_matrix("sandpile_add_grain.ca")

        n_rows = 10
        n_cols = 10
        sandpile = cpl.Sandpile(n_rows, n_cols)
        sandpile.add_grain(cell_index=(3, 3), timestep=1)

        initial = np.loadtxt(os.path.join(THIS_DIR, 'resources', 'sandpile_add_grain.txt'), dtype=int)
        initial = np.array([initial])

        ca = cpl.evolve2d(initial, timesteps=cpl.until_fixed_point(),
                          apply_rule=sandpile, neighbourhood="von Neumann")

        np.testing.assert_equal(expected, ca.tolist())

    def test_sandpile_prior_history(self):
        expected = self._convert_to_numpy_matrix("sandpile_prior_history.ca")

        n = 10
        sandpile = cpl.Sandpile(n, n)
        ca = cpl.init_simple2d(n, n, val=5)

        for i in range(3):
            ca[-1, n // 2, n // 2] += 1
            ca = cpl.evolve2d(ca, apply_rule=sandpile, timesteps=2, neighbourhood='Moore')

        np.testing.assert_equal(expected, ca.tolist())

    def test_plot2d(self):
        # this test ensures that the following code can run successfully without issue
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            cpl.plot2d([
                [[1, 0, 1], [1, 1, 1], [1, 1, 1]]
            ], title="some test")

    def test_plot2d_with_timestep(self):
        # this test ensures that the following code can run successfully without issue
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            cpl.plot2d([
                [[1, 0, 1], [1, 1, 1], [1, 1, 1]],
                [[1, 1, 1], [0, 1, 1], [1, 0, 1]]
            ], timestep=1, title="some test")

    def test_plot2d_slice(self):
        # this test ensures that the following code can run successfully without issue
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            cpl.plot2d_slice(np.array([
                [[1, 0, 1], [1, 1, 1], [1, 1, 1]]
            ]), title="some test")

    def test_plot2d_slice_with_slice(self):
        # this test ensures that the following code can run successfully without issue
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            cpl.plot2d_slice(np.array([
                [[1, 0, 1], [1, 1, 1], [1, 1, 1]],
                [[1, 1, 1], [0, 1, 1], [1, 0, 1]]
            ]), slice=1, title="some test")

    def test_plot2d_spacetime(self):
        # this test ensures that the following code can run successfully without issue
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            cpl.plot2d_spacetime(np.array([
                [[1, 0, 1], [1, 1, 1], [1, 1, 1]],
                [[1, 1, 1], [0, 1, 1], [1, 0, 1]],
                [[1, 1, 1], [0, 1, 1], [1, 0, 1]]
            ]), title="some test")

    def test_plot2d_animate(self):
        # this test ensures that the following code can run successfully without issue
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            cpl.plot2d_animate(np.array([
                [[1, 0, 1], [1, 1, 1], [1, 1, 1]],
                [[1, 1, 1], [0, 1, 1], [1, 0, 1]],
                [[1, 1, 1], [0, 1, 1], [1, 0, 1]]
            ]), title="some test")

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
        return np.array(content, dtype=np.int32)

    def _create_ca(self, expected, rule, neighbourhood, memoize=False):
        steps, _, _ = expected.shape
        cellular_automaton = np.array([expected[0]])
        return cpl.evolve2d(cellular_automaton, timesteps=steps, r=1, neighbourhood=neighbourhood,
                            apply_rule=lambda n, c, t: cpl.totalistic_rule(n, k=2, rule=rule),
                            memoize=memoize)
