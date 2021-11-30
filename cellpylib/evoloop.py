import numpy as np
from .ctrbl_rule import CTRBLRule


class Evoloop(CTRBLRule):
    """
    An implementation of H. Sayama's Evoloop. For more information, see:

    .. code-block:: text

       Sayama, H. (1998). Constructing evolutionary systems on a simple deterministic cellular automata space.
       PhD, University of Tokyo, Department of Information Science.
    """
    def __init__(self):
        """
        Create an Evoloop.
        """
        super().__init__(rule_table={
            (0, 0, 0, 0, 1): 2,
            (1, 0, 2, 0, 2): 1,
            (1, 1, 2, 7, 2): 7,
            (2, 0, 1, 7, 2): 2,
            (2, 1, 3, 2, 2): 2,
            (4, 0, 1, 2, 5): 0,
            (0, 0, 0, 0, 4): 3,
            (1, 0, 2, 1, 1): 1,
            (1, 1, 2, 7, 3): 5,
            (2, 0, 2, 0, 2): 2,
            (2, 1, 4, 2, 2): 2,
            (4, 0, 1, 6, 2): 0,
            (0, 0, 0, 1, 2): 2,
            (1, 0, 2, 1, 2): 1,
            (1, 1, 3, 2, 2): 1,
            (2, 0, 2, 0, 3): 2,
            (2, 1, 6, 2, 2): 2,
            (4, 0, 2, 1, 2): 0,
            (0, 0, 0, 1, 5): 2,
            (1, 0, 2, 1, 3): 1,
            (1, 1, 3, 3, 2): 1,
            (2, 0, 2, 0, 5): 2,
            (2, 1, 7, 2, 2): 2,
            (4, 0, 2, 1, 5): 0,
            (0, 0, 0, 2, 1): 2,
            (1, 0, 2, 2, 1): 1,
            (1, 1, 5, 4, 2): 4,
            (2, 0, 2, 0, 6): 5,
            (2, 2, 2, 2, 4): 2,
            (4, 0, 2, 2, 2): 1,
            (0, 0, 0, 2, 4): 2,
            (1, 0, 2, 2, 4): 4,
            (1, 1, 5, 7, 2): 7,
            (2, 0, 2, 0, 7): 3,
            (2, 2, 2, 2, 7): 2,
            (4, 0, 2, 3, 2): 1,
            (0, 0, 0, 4, 2): 2,
            (1, 0, 2, 2, 7): 7,
            (1, 1, 6, 2, 4): 4,
            (2, 0, 2, 1, 2): 2,
            (2, 2, 2, 3, 4): 2,
            (4, 0, 2, 6, 2): 6,
            (0, 0, 0, 4, 5): 2,
            (1, 0, 2, 3, 2): 4,
            (1, 1, 6, 2, 7): 7,
            (2, 0, 2, 1, 5): 2,
            (2, 2, 2, 3, 7): 2,
            (4, 0, 3, 1, 2): 0,
            (0, 0, 0, 7, 5): 2,
            (1, 0, 2, 4, 1): 4,
            (1, 2, 2, 2, 4): 4,
            (2, 0, 2, 2, 1): 2,
            (2, 2, 2, 4, 3): 2,
            (4, 0, 3, 2, 2): 1,
            (0, 0, 1, 0, 2): 2,
            (1, 0, 2, 4, 2): 4,
            (1, 2, 2, 2, 7): 7,
            (2, 0, 2, 2, 2): 2,
            (2, 2, 2, 4, 4): 2,
            (5, 0, 0, 0, 2): 5,
            (0, 0, 2, 1, 4): 1,
            (1, 0, 2, 4, 3): 4,
            (1, 2, 2, 4, 3): 4,
            (2, 0, 2, 2, 3): 2,
            (2, 2, 2, 7, 3): 2,
            (5, 0, 0, 1, 2): 5,
            (0, 0, 2, 1, 7): 1,
            (1, 0, 2, 5, 1): 1,
            (1, 2, 2, 7, 3): 7,
            (2, 0, 2, 3, 2): 3,
            (2, 2, 2, 7, 7): 2,
            (5, 0, 0, 2, 1): 5,
            (0, 0, 2, 3, 2): 2,
            (1, 0, 2, 5, 2): 7,
            (1, 2, 3, 2, 4): 4,
            (2, 0, 2, 4, 2): 2,
            (2, 2, 3, 2, 4): 3,
            (5, 0, 0, 2, 3): 2,
            (0, 1, 1, 2, 2): 1,
            (1, 0, 2, 5, 4): 3,
            (1, 2, 3, 2, 7): 7,
            (2, 0, 2, 4, 5): 2,
            (2, 2, 3, 2, 7): 3,
            (5, 0, 0, 2, 4): 5,
            (0, 1, 2, 1, 2): 1,
            (1, 0, 2, 5, 7): 7,
            (1, 2, 4, 2, 6): 6,
            (2, 0, 2, 5, 2): 5,
            (3, 0, 0, 0, 1): 3,
            (5, 0, 0, 2, 7): 5,
            (0, 1, 2, 3, 2): 1,
            (1, 0, 2, 7, 1): 7,
            (1, 2, 4, 3, 3): 3,
            (2, 0, 2, 6, 2): 0,
            (3, 0, 0, 0, 2): 2,
            (5, 0, 0, 4, 2): 5,
            (0, 1, 2, 4, 2): 1,
            (1, 0, 2, 7, 2): 7,
            (1, 2, 6, 2, 7): 6,
            (2, 0, 2, 6, 5): 0,
            (3, 0, 0, 0, 3): 2,
            (5, 0, 0, 7, 2): 5,
            (0, 1, 2, 4, 5): 1,
            (1, 0, 2, 7, 3): 5,
            (2, 0, 0, 0, 1): 2,
            (2, 0, 2, 7, 2): 2,
            (3, 0, 0, 0, 4): 3,
            (5, 0, 2, 0, 2): 2,
            (0, 1, 2, 5, 2): 6,
            (1, 0, 5, 1, 2): 1,
            (2, 0, 0, 0, 2): 2,
            (2, 0, 2, 7, 5): 2,
            (3, 0, 0, 0, 7): 4,
            (5, 0, 2, 0, 5): 2,
            (0, 1, 2, 6, 2): 6,
            (1, 0, 5, 4, 2): 4,
            (2, 0, 0, 0, 4): 2,
            (2, 0, 3, 1, 2): 2,
            (3, 0, 0, 1, 2): 3,
            (5, 0, 2, 1, 2): 5,
            (0, 1, 2, 7, 2): 1,
            (1, 0, 5, 7, 2): 7,
            (2, 0, 0, 0, 5): 2,
            (2, 0, 3, 2, 2): 2,
            (3, 0, 0, 3, 2): 2,
            (5, 0, 2, 1, 5): 2,
            (0, 1, 2, 7, 5): 1,
            (1, 0, 6, 2, 1): 1,
            (2, 0, 0, 0, 6): 0,
            (2, 0, 3, 4, 2): 2,
            (3, 0, 0, 4, 2): 1,
            (5, 0, 2, 4, 2): 5,
            (0, 1, 3, 4, 2): 1,
            (1, 0, 6, 2, 4): 4,
            (2, 0, 0, 0, 7): 1,
            (2, 0, 3, 4, 5): 2,
            (3, 0, 1, 0, 2): 1,
            (5, 0, 2, 7, 2): 5,
            (0, 1, 3, 7, 2): 1,
            (1, 0, 6, 2, 7): 7,
            (2, 0, 0, 1, 2): 2,
            (2, 0, 3, 7, 2): 2,
            (3, 0, 1, 2, 5): 0,
            (5, 0, 3, 1, 2): 0,
            (0, 1, 4, 2, 2): 1,
            (1, 1, 1, 1, 2): 1,
            (2, 0, 0, 1, 5): 2,
            (2, 0, 4, 1, 2): 2,
            (3, 0, 2, 1, 2): 3,
            (6, 0, 2, 0, 2): 2,
            (0, 1, 4, 2, 5): 1,
            (1, 1, 1, 2, 2): 1,
            (2, 0, 0, 2, 1): 2,
            (2, 0, 4, 2, 2): 2,
            (3, 0, 2, 4, 2): 3,
            (6, 0, 2, 1, 2): 2,
            (0, 1, 4, 3, 2): 1,
            (1, 1, 1, 2, 4): 4,
            (2, 0, 0, 2, 2): 2,
            (2, 0, 4, 4, 2): 2,
            (3, 0, 2, 5, 2): 1,
            (6, 0, 2, 2, 2): 0,
            (0, 1, 4, 3, 5): 1,
            (1, 1, 1, 2, 5): 1,
            (2, 0, 0, 2, 3): 2,
            (2, 0, 5, 1, 2): 2,
            (3, 0, 2, 7, 2): 3,
            (6, 0, 2, 4, 2): 2,
            (0, 1, 4, 4, 2): 1,
            (1, 1, 1, 2, 7): 7,
            (2, 0, 0, 2, 4): 2,
            (2, 0, 5, 4, 2): 5,
            (3, 0, 3, 3, 2): 1,
            (6, 0, 2, 7, 2): 2,
            (0, 1, 4, 6, 2): 1,
            (1, 1, 1, 6, 2): 1,
            (2, 0, 0, 2, 6): 0,
            (2, 0, 5, 7, 2): 5,
            (3, 1, 2, 1, 2): 3,
            (6, 1, 2, 2, 2): 0,
            (0, 1, 7, 2, 2): 1,
            (1, 1, 2, 1, 2): 1,
            (2, 0, 0, 2, 7): 2,
            (2, 0, 6, 1, 2): 5,
            (3, 1, 2, 4, 2): 3,
            (6, 2, 2, 2, 4): 0,
            (0, 1, 7, 2, 5): 1,
            (1, 1, 2, 1, 3): 1,
            (2, 0, 0, 3, 2): 4,
            (2, 0, 6, 2, 1): 2,
            (3, 1, 2, 5, 2): 1,
            (6, 2, 2, 2, 7): 0,
            (0, 1, 7, 5, 6): 1,
            (1, 1, 2, 1, 5): 1,
            (2, 0, 0, 4, 2): 3,
            (2, 0, 6, 4, 2): 5,
            (3, 1, 2, 7, 2): 3,
            (7, 0, 1, 0, 2): 0,
            (0, 1, 7, 6, 2): 1,
            (1, 1, 2, 2, 2): 1,
            (2, 0, 0, 4, 5): 2,
            (2, 0, 6, 7, 2): 5,
            (3, 2, 4, 2, 4): 3,
            (7, 0, 1, 1, 2): 0,
            (0, 1, 7, 7, 2): 1,
            (1, 1, 2, 2, 4): 4,
            (2, 0, 0, 5, 4): 5,
            (2, 0, 7, 1, 2): 2,
            (3, 2, 4, 2, 5): 1,
            (7, 0, 1, 2, 2): 0,
            (1, 0, 0, 0, 1): 1,
            (1, 1, 2, 2, 7): 7,
            (2, 0, 0, 5, 7): 5,
            (2, 0, 7, 2, 2): 2,
            (3, 2, 4, 2, 7): 3,
            (7, 0, 1, 2, 5): 0,
            (1, 0, 0, 1, 2): 1,
            (1, 1, 2, 3, 2): 1,
            (2, 0, 0, 6, 2): 0,
            (2, 0, 7, 7, 2): 2,
            (3, 2, 5, 2, 7): 1,
            (7, 0, 1, 6, 2): 0,
            (1, 0, 0, 2, 1): 1,
            (1, 1, 2, 4, 2): 4,
            (2, 0, 0, 7, 2): 2,
            (2, 1, 1, 2, 2): 2,
            (3, 2, 7, 2, 7): 3,
            (7, 0, 2, 1, 2): 0,
            (1, 0, 0, 2, 4): 4,
            (1, 1, 2, 4, 3): 4,
            (2, 0, 0, 7, 5): 2,
            (2, 1, 2, 2, 2): 2,
            (4, 0, 0, 0, 0): 1,
            (7, 0, 2, 1, 5): 0,
            (1, 0, 0, 2, 7): 7,
            (1, 1, 2, 5, 2): 7,
            (2, 0, 1, 0, 2): 2,
            (2, 1, 2, 2, 3): 2,
            (4, 0, 0, 0, 2): 1,
            (7, 0, 2, 2, 2): 1,
            (1, 0, 1, 2, 1): 1,
            (1, 1, 2, 5, 4): 3,
            (2, 0, 1, 1, 2): 2,
            (2, 1, 2, 2, 4): 2,
            (4, 0, 1, 0, 2): 0,
            (7, 0, 2, 3, 2): 0,
            (1, 0, 1, 2, 4): 4,
            (1, 1, 2, 5, 7): 7,
            (2, 0, 1, 2, 2): 2,
            (2, 1, 2, 2, 7): 2,
            (4, 0, 1, 1, 2): 0,
            (7, 0, 2, 6, 2): 6,
            (1, 0, 1, 2, 7): 7,
            (1, 1, 2, 6, 2): 6,
            (2, 0, 1, 4, 2): 2,
            (2, 1, 2, 3, 2): 3,
            (4, 0, 1, 2, 2): 0,
            (7, 0, 3, 1, 2): 0,
        }, add_rotations=True)

    def __call__(self, n, c, t):
        """
        From:
        Sayama, H. (1998). Constructing evolutionary systems on a simple deterministic cellular automata space.
        PhD, University of Tokyo, Department of Information Science.

        :param n: the neighbourhood

        :param c: the index of the current cell

        :param t: the current timestep

        :return: the activity of the current cell at the next timestep
        """
        current_activity = n[1][1]
        top = n[0][1]
        right = n[1][2]
        bottom = n[2][1]
        left = n[1][0]
        key = (current_activity, top, right, bottom, left)

        if key not in self._rule_table:
            trbl = (top, right, bottom, left)
            new_activity = None

            # Let 8->0 with no condition.
            if current_activity == 8:
                new_activity = 0

            # To all the undefined situations in whose four neighbourhood (TRBL) there is at least one site in state 8,
            # apply the following:
            if 8 in trbl:
                # Let 0,1->8 if there is at least one site in state 2,3,...,7 in its four neighbourhood (TRBL),
                # otherwise let 0->0 and 1->1
                if current_activity == 0 or current_activity == 1:
                    if np.any([i in trbl for i in (2, 3, 4, 5, 6, 7)]):
                        new_activity = 8
                    elif current_activity == 0:
                        new_activity = 0
                    elif current_activity == 1:
                        new_activity = 1

                # Let 2,3,5->0.
                if current_activity in (2, 3, 5):
                    new_activity = 0

                # Let 4,6,7->1.
                if current_activity in (4, 6, 7):
                    new_activity = 1

            # Clear up all the undefined situations by letting 0->0 and 1,2,...,7->8.
            if new_activity is None and current_activity == 0:
                new_activity = 0
            if new_activity is None and current_activity in (1, 2, 3, 4, 5, 6, 7):
                new_activity = 8

            return new_activity

        return self._rule_table[key]

    @staticmethod
    def init_species13_loop(dim, row, col):
        """
        Create the initial conditions by specifying the a loop of species 13 and its starting position (as given by the
        coordinates of the first cell of the first row of the loop).

        :param dim: a 2-tuple representing the dimensions (number of rows and columns) of the CA

        :param row: the row number of the loop

        :param col: the column number of the loop

        :return: the initial conditions
        """

        initial_conditions = np.zeros(dim, dtype=np.int32)

        # 1st row
        initial_conditions[row][col] = 2
        initial_conditions[row][col+1] = 2
        initial_conditions[row][col+2] = 2
        initial_conditions[row][col+3] = 2
        initial_conditions[row][col+4] = 2
        initial_conditions[row][col+5] = 2
        initial_conditions[row][col+6] = 2
        initial_conditions[row][col+7] = 2
        initial_conditions[row][col+8] = 2
        initial_conditions[row][col+9] = 2
        initial_conditions[row][col+10] = 2
        initial_conditions[row][col+11] = 2
        initial_conditions[row][col+12] = 2
        initial_conditions[row][col+13] = 2
        initial_conditions[row][col+14] = 2

        # 2nd row
        initial_conditions[row+1][col-1] = 2
        initial_conditions[row+1][col] = 0
        initial_conditions[row+1][col+1] = 1
        initial_conditions[row+1][col+2] = 7
        initial_conditions[row+1][col+3] = 0
        initial_conditions[row+1][col+4] = 1
        initial_conditions[row+1][col+5] = 7
        initial_conditions[row+1][col+6] = 0
        initial_conditions[row+1][col+7] = 1
        initial_conditions[row+1][col+8] = 7
        initial_conditions[row+1][col+9] = 0
        initial_conditions[row+1][col+10] = 1
        initial_conditions[row+1][col+11] = 4
        initial_conditions[row+1][col+12] = 0
        initial_conditions[row+1][col+13] = 1
        initial_conditions[row+1][col+14] = 4
        initial_conditions[row+1][col+15] = 2

        # 3rd row
        initial_conditions[row+2][col-1] = 2
        initial_conditions[row+2][col] = 7
        initial_conditions[row+2][col+1] = 2
        initial_conditions[row+2][col+2] = 2
        initial_conditions[row+2][col+3] = 2
        initial_conditions[row+2][col+4] = 2
        initial_conditions[row+2][col+5] = 2
        initial_conditions[row+2][col+6] = 2
        initial_conditions[row+2][col+7] = 2
        initial_conditions[row+2][col+8] = 2
        initial_conditions[row+2][col+9] = 2
        initial_conditions[row+2][col+10] = 2
        initial_conditions[row+2][col+11] = 2
        initial_conditions[row+2][col+12] = 2
        initial_conditions[row+2][col+13] = 2
        initial_conditions[row+2][col+14] = 0
        initial_conditions[row+2][col+15] = 2

        # 4th row
        initial_conditions[row+3][col-1] = 2
        initial_conditions[row+3][col] = 1
        initial_conditions[row+3][col+1] = 2
        initial_conditions[row+3][col+13] = 2
        initial_conditions[row+3][col+14] = 1
        initial_conditions[row+3][col+15] = 2

        # 5th row
        initial_conditions[row+4][col-1] = 2
        initial_conditions[row+4][col] = 0
        initial_conditions[row+4][col+1] = 2
        initial_conditions[row+4][col+13] = 2
        initial_conditions[row+4][col+14] = 1
        initial_conditions[row+4][col+15] = 2

        # 6th row
        initial_conditions[row+5][col-1] = 2
        initial_conditions[row+5][col] = 7
        initial_conditions[row+5][col+1] = 2
        initial_conditions[row+5][col+13] = 2
        initial_conditions[row+5][col+14] = 1
        initial_conditions[row+5][col+15] = 2

        # 7th row
        initial_conditions[row + 6][col - 1] = 2
        initial_conditions[row + 6][col] = 1
        initial_conditions[row + 6][col + 1] = 2
        initial_conditions[row + 6][col + 13] = 2
        initial_conditions[row + 6][col + 14] = 1
        initial_conditions[row + 6][col + 15] = 2

        # 8th row
        initial_conditions[row + 7][col - 1] = 2
        initial_conditions[row + 7][col] = 0
        initial_conditions[row + 7][col + 1] = 2
        initial_conditions[row + 7][col + 13] = 2
        initial_conditions[row + 7][col + 14] = 1
        initial_conditions[row + 7][col + 15] = 2

        # 9th row
        initial_conditions[row + 8][col - 1] = 2
        initial_conditions[row + 8][col] = 7
        initial_conditions[row + 8][col + 1] = 2
        initial_conditions[row + 8][col + 13] = 2
        initial_conditions[row + 8][col + 14] = 1
        initial_conditions[row + 8][col + 15] = 2

        # 10th row
        initial_conditions[row + 9][col - 1] = 2
        initial_conditions[row + 9][col] = 1
        initial_conditions[row + 9][col + 1] = 2
        initial_conditions[row + 9][col + 13] = 2
        initial_conditions[row + 9][col + 14] = 1
        initial_conditions[row + 9][col + 15] = 2

        # 11th row
        initial_conditions[row + 10][col - 1] = 2
        initial_conditions[row + 10][col] = 0
        initial_conditions[row + 10][col + 1] = 2
        initial_conditions[row + 10][col + 13] = 2
        initial_conditions[row + 10][col + 14] = 1
        initial_conditions[row + 10][col + 15] = 2

        # 12th row
        initial_conditions[row + 11][col - 1] = 2
        initial_conditions[row + 11][col] = 7
        initial_conditions[row + 11][col + 1] = 2
        initial_conditions[row + 11][col + 13] = 2
        initial_conditions[row + 11][col + 14] = 1
        initial_conditions[row + 11][col + 15] = 2

        # 13th row
        initial_conditions[row + 12][col - 1] = 2
        initial_conditions[row + 12][col] = 1
        initial_conditions[row + 12][col + 1] = 2
        initial_conditions[row + 12][col + 13] = 2
        initial_conditions[row + 12][col + 14] = 1
        initial_conditions[row + 12][col + 15] = 2

        # 14th row
        initial_conditions[row + 13][col - 1] = 2
        initial_conditions[row + 13][col] = 0
        initial_conditions[row + 13][col + 1] = 2
        initial_conditions[row + 13][col + 13] = 2
        initial_conditions[row + 13][col + 14] = 1
        initial_conditions[row + 13][col + 15] = 2

        # 15th row
        initial_conditions[row + 14][col - 1] = 2
        initial_conditions[row + 14][col] = 7
        initial_conditions[row + 14][col + 1] = 2
        initial_conditions[row + 14][col + 2] = 2
        initial_conditions[row + 14][col + 3] = 2
        initial_conditions[row + 14][col + 4] = 2
        initial_conditions[row + 14][col + 5] = 2
        initial_conditions[row + 14][col + 6] = 2
        initial_conditions[row + 14][col + 7] = 2
        initial_conditions[row + 14][col + 8] = 2
        initial_conditions[row + 14][col + 9] = 2
        initial_conditions[row + 14][col + 10] = 2
        initial_conditions[row + 14][col + 11] = 2
        initial_conditions[row + 14][col + 12] = 2
        initial_conditions[row + 14][col + 13] = 2
        initial_conditions[row + 14][col + 14] = 1
        initial_conditions[row + 14][col + 15] = 2
        initial_conditions[row + 14][col + 16] = 2
        initial_conditions[row + 14][col + 17] = 2
        initial_conditions[row + 14][col + 18] = 2
        initial_conditions[row + 14][col + 19] = 2
        initial_conditions[row + 14][col + 20] = 2
        initial_conditions[row + 14][col + 21] = 2
        initial_conditions[row + 14][col + 22] = 2
        initial_conditions[row + 14][col + 23] = 2
        initial_conditions[row + 14][col + 24] = 2
        initial_conditions[row + 14][col + 25] = 2
        initial_conditions[row + 14][col + 26] = 2
        initial_conditions[row + 14][col + 27] = 2
        initial_conditions[row + 14][col + 28] = 2

        # 16th row
        initial_conditions[row + 15][col - 1] = 2
        initial_conditions[row + 15][col] = 1
        initial_conditions[row + 15][col + 1] = 0
        initial_conditions[row + 15][col + 2] = 7
        initial_conditions[row + 15][col + 3] = 1
        initial_conditions[row + 15][col + 4] = 0
        initial_conditions[row + 15][col + 5] = 7
        initial_conditions[row + 15][col + 6] = 1
        initial_conditions[row + 15][col + 7] = 0
        initial_conditions[row + 15][col + 8] = 7
        initial_conditions[row + 15][col + 9] = 1
        initial_conditions[row + 15][col + 10] = 0
        initial_conditions[row + 15][col + 11] = 7
        initial_conditions[row + 15][col + 12] = 1
        initial_conditions[row + 15][col + 13] = 0
        initial_conditions[row + 15][col + 14] = 7
        initial_conditions[row + 15][col + 15] = 1
        initial_conditions[row + 15][col + 16] = 1
        initial_conditions[row + 15][col + 17] = 1
        initial_conditions[row + 15][col + 18] = 1
        initial_conditions[row + 15][col + 19] = 1
        initial_conditions[row + 15][col + 20] = 1
        initial_conditions[row + 15][col + 21] = 1
        initial_conditions[row + 15][col + 22] = 1
        initial_conditions[row + 15][col + 23] = 1
        initial_conditions[row + 15][col + 24] = 1
        initial_conditions[row + 15][col + 25] = 1
        initial_conditions[row + 15][col + 26] = 1
        initial_conditions[row + 15][col + 27] = 1
        initial_conditions[row + 15][col + 28] = 1
        initial_conditions[row + 15][col + 29] = 2

        # 17th row
        initial_conditions[row + 16][col] = 2
        initial_conditions[row + 16][col + 1] = 2
        initial_conditions[row + 16][col + 2] = 2
        initial_conditions[row + 16][col + 3] = 2
        initial_conditions[row + 16][col + 4] = 2
        initial_conditions[row + 16][col + 5] = 2
        initial_conditions[row + 16][col + 6] = 2
        initial_conditions[row + 16][col + 7] = 2
        initial_conditions[row + 16][col + 8] = 2
        initial_conditions[row + 16][col + 9] = 2
        initial_conditions[row + 16][col + 10] = 2
        initial_conditions[row + 16][col + 11] = 2
        initial_conditions[row + 16][col + 12] = 2
        initial_conditions[row + 16][col + 13] = 2
        initial_conditions[row + 16][col + 14] = 2
        initial_conditions[row + 16][col + 15] = 2
        initial_conditions[row + 16][col + 16] = 2
        initial_conditions[row + 16][col + 17] = 2
        initial_conditions[row + 16][col + 18] = 2
        initial_conditions[row + 16][col + 19] = 2
        initial_conditions[row + 16][col + 20] = 2
        initial_conditions[row + 16][col + 21] = 2
        initial_conditions[row + 16][col + 22] = 2
        initial_conditions[row + 16][col + 23] = 2
        initial_conditions[row + 16][col + 24] = 2
        initial_conditions[row + 16][col + 25] = 2
        initial_conditions[row + 16][col + 26] = 2
        initial_conditions[row + 16][col + 27] = 2
        initial_conditions[row + 16][col + 28] = 2

        return np.array([initial_conditions])
