import unittest
import cellpylib as cpl
import numpy as np
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class TestHopfieldNet(unittest.TestCase):

    def test_hopfield_net(self):
        np.random.seed(0)

        # patterns for training
        zero = [
            0, 1, 1, 1, 0,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            0, 1, 1, 1, 0,
            0, 0, 0, 0, 0]
        one = [
            0, 1, 1, 0, 0,
            0, 0, 1, 0, 0,
            0, 0, 1, 0, 0,
            0, 0, 1, 0, 0,
            0, 0, 1, 0, 0,
            0, 0, 1, 0, 0,
            0, 0, 0, 0, 0]
        two = [
            1, 1, 1, 0, 0,
            0, 0, 0, 1, 0,
            0, 0, 0, 1, 0,
            0, 1, 1, 0, 0,
            1, 0, 0, 0, 0,
            1, 1, 1, 1, 1,
            0, 0, 0, 0, 0]
        # replace the zeroes with -1 to make these vectors bipolar instead of binary
        one = [-1 if x == 0 else x for x in one]
        two = [-1 if x == 0 else x for x in two]
        zero = [-1 if x == 0 else x for x in zero]
        P = [zero, one, two]

        hopfield_net = cpl.HopfieldNet(num_cells=35)
        hopfield_net.train(P)

        expected_weights = self._convert_to_ndarray("hopfield_net_weights.txt")
        np.testing.assert_equal(expected_weights, hopfield_net.W)

        expected_activities = self._convert_to_ndarray("hopfield_net.ca")

        half_two = [
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 1, 1, 0, 0,
            1, 0, 0, 0, 0,
            1, 1, 1, 1, 1,
            0, 0, 0, 0, 0]
        half_two = [-1 if x == 0 else x for x in half_two]

        cellular_automaton = np.array([half_two])

        cellular_automaton = cpl.evolve(cellular_automaton, timesteps=155,
                                        apply_rule=hopfield_net.apply_rule, r=hopfield_net.r)

        np.testing.assert_equal(expected_activities, cellular_automaton)

    def _convert_to_ndarray(self, filename, dtype=int):
        with open(os.path.join(THIS_DIR, 'resources', filename), 'r') as content_file:
            content = content_file.read()
        content = content.replace('[[', '')
        content = content.replace(']]', '')
        content = content.replace('[', '')
        content = content.replace('],', ';')
        content = [[dtype(i) for i in x.split(',')] for x in content.split(';')]
        return np.array(content)