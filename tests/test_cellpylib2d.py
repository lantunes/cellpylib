import unittest

import os

import cellpylib as ca

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class TestCellularAutomataFunctions2D(unittest.TestCase):

    def test_init_simple_1x1(self):
        arr = ca.init_simple2d(rows=1, cols=1)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 1)
        self.assertEqual(len(arr[0][0]), 1)
        self.assertEqual(arr[0][0][0], 1)

    def test_init_simple_1x1_val2(self):
        arr = ca.init_simple2d(rows=1, cols=1, val=2)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 1)
        self.assertEqual(len(arr[0][0]), 1)
        self.assertEqual(arr[0][0][0], 2)

    def test_init_simple_2x2(self):
        arr = ca.init_simple2d(rows=2, cols=2)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 2)
        self.assertEqual(len(arr[0][0]), 2)
        self.assertEqual(len(arr[0][1]), 2)
        self.assertEqual(arr[0][0].tolist(), [0, 0])
        self.assertEqual(arr[0][1].tolist(), [0, 1])

    def test_init_simple_3x3(self):
        arr = ca.init_simple2d(rows=3, cols=3)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 3)
        self.assertEqual(len(arr[0][0]), 3)
        self.assertEqual(len(arr[0][1]), 3)
        self.assertEqual(len(arr[0][2]), 3)
        self.assertEqual(arr[0][0].tolist(), [0, 0, 0])
        self.assertEqual(arr[0][1].tolist(), [0, 1, 0])
        self.assertEqual(arr[0][2].tolist(), [0, 0, 0])

    def test_init_simple_2x3(self):
        arr = ca.init_simple2d(rows=2, cols=3)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 2)
        self.assertEqual(len(arr[0][0]), 3)
        self.assertEqual(len(arr[0][1]), 3)
        self.assertEqual(arr[0][0].tolist(), [0, 0, 0])
        self.assertEqual(arr[0][1].tolist(), [0, 1, 0])

    def test_init_random_1x1(self):
        arr = ca.init_random2d(1, 1)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 1)
        self.assertEqual(len(arr[0][0]), 1)
        self.assertTrue(0 <= arr[0][0][0] <= 1)

    def test_init_random_1x1_k2(self):
        arr = ca.init_random2d(rows=1, cols=1, k=2)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 1)
        self.assertEqual(len(arr[0][0]), 1)
        self.assertTrue(0 <= arr[0][0][0] <= 2)

    def test_init_random_2x2(self):
        arr = ca.init_random2d(rows=2, cols=2)
        self.assertEqual(len(arr), 1)
        self.assertEqual(len(arr[0]), 2)
        self.assertEqual(len(arr[0][0]), 2)
        self.assertEqual(len(arr[0][1]), 2)
        self.assertTrue(0 <= arr[0][0][0] <= 1)
        self.assertTrue(0 <= arr[0][0][1] <= 1)
        self.assertTrue(0 <= arr[0][1][0] <= 1)
        self.assertTrue(0 <= arr[0][1][1] <= 1)

    def test_init_random_3x3_k2(self):
        arr = ca.init_random2d(rows=3, cols=3, k=2)
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

    def test_init_random_2x3(self):
        arr = ca.init_random2d(rows=2, cols=3)
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