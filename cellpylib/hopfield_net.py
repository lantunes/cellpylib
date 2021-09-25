from .ca_functions import *


class HopfieldNet:
    """
    An implementation of the Hopfield network. Due to limitations of this implementation, only an odd number of cells
    is supported.

    For more information on Hopfield networks, see:

    .. code-block:: text

        Hopfield, J. J. (1982). Neural networks and physical systems with emergent collective
        computational abilities. Proceedings of the national academy of sciences, 79(8), 2554-2558.
    """
    def __init__(self, num_cells):
        """
        Create an instance of the Hopfield network.

        :param num_cells: the number of cells in this Hopfield network; only an odd number of cells are supported in
                          this implementation
        """
        self.apply_rule = AsynchronousRule(apply_rule=self._rule, num_cells=num_cells).apply_rule
        self._r = num_cells // 2

    def train(self, P):
        """
        The training set consists of patterns to be learned by this net. The patterns should be composed of 
        bipolar ({-1,1}), and not binary ({0,1}), values.

        :param P: the set of training patterns
        """
        self._W = np.zeros((len(P[0]), len(P[0])), dtype=np.int32)
        for p in P:
            for i in range(len(p)):
                for j in range(len(p)):
                    if i ==j:
                        self._W[i, j] = 0
                    else:
                        self._W[i, j] += p[i]*p[j]

    def _rule(self, n, c, t):
        left_neighbours = n[0 : len(n)//2]
        right_neighbours = n[len(n)//2 + 1 :]
        V = 0
        for j, left_V in enumerate(left_neighbours):
            V += self._W[c - self._r + j, c] * left_V
        for j, right_V in enumerate(right_neighbours):
            V += self._W[(c + j + 1) % len(n), c] * right_V
        return 1 if V >= 0 else -1

    @property
    def W(self):
        """
        Returns the learned weight matrix.

        :return: the learned weight matrix
        """
        return self._W

    @property
    def r(self):
        """
        The radius of this automaton.

        :return: the radius
        """
        return self._r
