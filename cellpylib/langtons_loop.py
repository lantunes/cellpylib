import numpy as np
from .ctrbl_rule import CTRBLRule


class LangtonsLoop(CTRBLRule):
    """
    An implementation of Langton's Loop, a kind of CTRBL rule. For more information, see:

     .. code-block:: text

        Langton, C. G. (1984). Self-reproduction in Cellular Automata.
        Physica D: Nonlinear Phenomena, 10(1-2), 135-144.

    NOTE: This implementation is meant only for periodic boundary conditions, however, the original Langton's loops
    rules here assume an infinitely sized space. There may be errors due to states missing from the rule table if the
    loops are allowed to overlap. (H. Sayama may have proposed a fix for this in his Ph.D. thesis.)
    """
    def __init__(self):
        """
        Creates a Langton's Loop.
        """
        super().__init__(rule_table={
            (0, 0, 0, 0, 0): 0,
            (0, 0, 0, 0, 1): 2,
            (0, 0, 0, 0, 2): 0,
            (0, 0, 0, 0, 3): 0,
            (0, 0, 0, 0, 5): 0,
            (0, 0, 0, 0, 6): 3,
            (0, 0, 0, 0, 7): 1,
            (0, 0, 0, 1, 1): 2,
            (0, 0, 0, 1, 2): 2,
            (0, 0, 0, 1, 3): 2,
            (0, 0, 0, 2, 1): 2,
            (0, 0, 0, 2, 2): 0,
            (0, 0, 0, 2, 3): 0,
            (0, 0, 0, 2, 6): 2,
            (0, 0, 0, 2, 7): 2,
            (0, 0, 0, 3, 2): 0,
            (0, 0, 0, 5, 2): 5,
            (0, 0, 0, 6, 2): 2,
            (0, 0, 0, 7, 2): 2,
            (0, 0, 1, 0, 2): 2,
            (0, 0, 1, 1, 2): 0,
            (0, 0, 2, 0, 2): 0,
            (0, 0, 2, 0, 3): 0,
            (0, 0, 2, 0, 5): 0,
            (0, 0, 2, 1, 2): 5,
            (0, 0, 2, 2, 2): 0,
            (0, 0, 2, 3, 2): 2,
            (0, 0, 5, 2, 2): 2,
            (0, 1, 2, 3, 2): 1,
            (0, 1, 2, 4, 2): 1,
            (0, 1, 2, 5, 2): 5,
            (0, 1, 2, 6, 2): 1,
            (0, 1, 2, 7, 2): 1,
            (0, 1, 2, 7, 5): 1,
            (0, 1, 4, 2, 2): 1,
            (0, 1, 4, 3, 2): 1,
            (0, 1, 4, 4, 2): 1,
            (0, 1, 4, 7, 2): 1,
            (0, 1, 6, 2, 5): 1,
            (0, 1, 7, 2, 2): 1,
            (0, 1, 7, 2, 5): 5,
            (0, 1, 7, 5, 2): 1,
            (0, 1, 7, 6, 2): 1,
            (0, 1, 7, 7, 2): 1,
            (0, 2, 5, 2, 7): 1,
            (1, 0, 0, 0, 1): 1,
            (1, 0, 0, 0, 6): 1,
            (1, 0, 0, 0, 7): 7,
            (1, 0, 0, 1, 1): 1,
            (1, 0, 0, 1, 2): 1,
            (1, 0, 0, 2, 1): 1,
            (1, 0, 0, 2, 4): 4,
            (1, 0, 0, 2, 7): 7,
            (1, 0, 0, 5, 1): 1,
            (1, 0, 1, 0, 1): 1,
            (1, 0, 1, 1, 1): 1,
            (1, 0, 1, 2, 4): 4,
            (1, 0, 1, 2, 7): 7,
            (1, 0, 2, 0, 2): 6,
            (1, 0, 2, 1, 2): 1,
            (1, 0, 2, 2, 1): 1,
            (1, 0, 2, 2, 4): 4,
            (1, 0, 2, 2, 6): 3,
            (1, 0, 2, 2, 7): 7,
            (1, 0, 2, 3, 2): 7,
            (1, 0, 2, 4, 2): 4,
            (1, 0, 2, 6, 2): 6,
            (1, 0, 2, 6, 4): 4,
            (1, 0, 2, 6, 7): 7,
            (1, 0, 2, 7, 1): 0,
            (1, 0, 2, 7, 2): 7,
            (1, 0, 5, 4, 2): 7,
            (1, 1, 1, 1, 2): 1,
            (1, 1, 1, 2, 2): 1,
            (1, 1, 1, 2, 4): 4,
            (1, 1, 1, 2, 5): 1,
            (1, 1, 1, 2, 6): 1,
            (1, 1, 1, 2, 7): 7,
            (1, 1, 1, 5, 2): 2,
            (1, 1, 2, 1, 2): 1,
            (1, 1, 2, 2, 2): 1,
            (1, 1, 2, 2, 4): 4,
            (1, 1, 2, 2, 5): 1,
            (1, 1, 2, 2, 7): 7,
            (1, 1, 2, 3, 2): 1,
            (1, 1, 2, 4, 2): 4,
            (1, 1, 2, 6, 2): 1,
            (1, 1, 2, 7, 2): 7,
            (1, 1, 3, 2, 2): 1,
            (1, 2, 2, 2, 4): 4,
            (1, 2, 2, 2, 7): 7,
            (1, 2, 2, 4, 3): 4,
            (1, 2, 2, 5, 4): 7,
            (1, 2, 3, 2, 4): 4,
            (1, 2, 3, 2, 7): 7,
            (1, 2, 4, 2, 5): 5,
            (1, 2, 4, 2, 6): 7,
            (1, 2, 5, 2, 7): 5,
            (2, 0, 0, 0, 1): 2,
            (2, 0, 0, 0, 2): 2,
            (2, 0, 0, 0, 4): 2,
            (2, 0, 0, 0, 7): 1,
            (2, 0, 0, 1, 2): 2,
            (2, 0, 0, 1, 5): 2,
            (2, 0, 0, 2, 1): 2,
            (2, 0, 0, 2, 2): 2,
            (2, 0, 0, 2, 3): 2,
            (2, 0, 0, 2, 4): 2,
            (2, 0, 0, 2, 5): 0,
            (2, 0, 0, 2, 6): 2,
            (2, 0, 0, 2, 7): 2,
            (2, 0, 0, 3, 2): 6,
            (2, 0, 0, 4, 2): 3,
            (2, 0, 0, 5, 1): 7,
            (2, 0, 0, 5, 2): 2,
            (2, 0, 0, 5, 7): 5,
            (2, 0, 0, 7, 2): 2,
            (2, 0, 1, 0, 2): 2,
            (2, 0, 1, 1, 2): 2,
            (2, 0, 1, 2, 2): 2,
            (2, 0, 1, 4, 2): 2,
            (2, 0, 1, 7, 2): 2,
            (2, 0, 2, 0, 2): 2,
            (2, 0, 2, 0, 3): 2,
            (2, 0, 2, 0, 5): 2,
            (2, 0, 2, 0, 7): 3,
            (2, 0, 2, 1, 2): 2,
            (2, 0, 2, 1, 5): 2,
            (2, 0, 2, 2, 1): 2,
            (2, 0, 2, 2, 2): 2,
            (2, 0, 2, 2, 7): 2,
            (2, 0, 2, 3, 2): 1,
            (2, 0, 2, 4, 2): 2,
            (2, 0, 2, 4, 5): 2,
            (2, 0, 2, 5, 2): 0,
            (2, 0, 2, 5, 5): 2,
            (2, 0, 2, 6, 2): 2,
            (2, 0, 2, 7, 2): 2,
            (2, 0, 3, 1, 2): 2,
            (2, 0, 3, 2, 1): 6,
            (2, 0, 3, 2, 2): 6,
            (2, 0, 3, 4, 2): 2,
            (2, 0, 4, 2, 2): 2,
            (2, 0, 5, 1, 2): 2,
            (2, 0, 5, 2, 1): 2,
            (2, 0, 5, 2, 2): 2,
            (2, 0, 5, 5, 2): 1,
            (2, 0, 5, 7, 2): 5,
            (2, 0, 6, 2, 2): 2,
            (2, 0, 6, 7, 2): 2,
            (2, 0, 7, 1, 2): 2,
            (2, 0, 7, 2, 2): 2,
            (2, 0, 7, 4, 2): 2,
            (2, 0, 7, 7, 2): 2,
            (2, 1, 1, 2, 2): 2,
            (2, 1, 1, 2, 6): 1,
            (2, 1, 2, 2, 2): 2,
            (2, 1, 2, 2, 4): 2,
            (2, 1, 2, 2, 6): 2,
            (2, 1, 2, 2, 7): 2,
            (2, 1, 4, 2, 2): 2,
            (2, 1, 5, 2, 2): 2,
            (2, 1, 6, 2, 2): 2,
            (2, 1, 7, 2, 2): 2,
            (2, 2, 2, 2, 7): 2,
            (2, 2, 2, 4, 4): 2,
            (2, 2, 2, 4, 6): 2,
            (2, 2, 2, 7, 6): 2,
            (2, 2, 2, 7, 7): 2,
            (3, 0, 0, 0, 1): 3,
            (3, 0, 0, 0, 2): 2,
            (3, 0, 0, 0, 4): 1,
            (3, 0, 0, 0, 7): 6,
            (3, 0, 0, 1, 2): 3,
            (3, 0, 0, 4, 2): 1,
            (3, 0, 0, 6, 2): 2,
            (3, 0, 1, 0, 2): 1,
            (3, 0, 1, 2, 2): 0,
            (3, 0, 2, 5, 1): 1,
            (4, 0, 1, 1, 2): 0,
            (4, 0, 1, 2, 2): 0,
            (4, 0, 1, 2, 5): 0,
            (4, 0, 2, 1, 2): 0,
            (4, 0, 2, 2, 2): 1,
            (4, 0, 2, 3, 2): 6,
            (4, 0, 2, 5, 2): 0,
            (4, 0, 3, 2, 2): 1,
            (5, 0, 0, 0, 2): 2,
            (5, 0, 0, 2, 1): 5,
            (5, 0, 0, 2, 2): 5,
            (5, 0, 0, 2, 3): 2,
            (5, 0, 0, 2, 7): 2,
            (5, 0, 0, 5, 2): 0,
            (5, 0, 2, 0, 2): 2,
            (5, 0, 2, 1, 2): 2,
            (5, 0, 2, 1, 5): 2,
            (5, 0, 2, 2, 2): 0,
            (5, 0, 2, 2, 4): 4,
            (5, 0, 2, 7, 2): 2,
            (5, 1, 2, 1, 2): 2,
            (5, 1, 2, 2, 2): 0,
            (5, 1, 2, 4, 2): 2,
            (5, 1, 2, 7, 2): 2,
            (6, 0, 0, 0, 1): 1,
            (6, 0, 0, 0, 2): 1,
            (6, 0, 2, 1, 2): 0,
            (6, 1, 2, 1, 2): 5,
            (6, 1, 2, 1, 3): 1,
            (6, 1, 2, 2, 2): 5,
            (7, 0, 0, 0, 7): 7,
            (7, 0, 1, 1, 2): 0,
            (7, 0, 1, 2, 2): 0,
            (7, 0, 1, 2, 5): 0,
            (7, 0, 2, 1, 2): 0,
            (7, 0, 2, 2, 2): 1,
            (7, 0, 2, 2, 5): 1,
            (7, 0, 2, 3, 2): 1,
            (7, 0, 2, 5, 2): 5,
            (7, 0, 2, 7, 2): 0
        }, add_rotations=True)

    def init_loops(self, n, dim, row, col):
        """
        Create the initial conditions by specifying the number of loops and their starting positions (as given by the
        coordinates of the first cell of the first row of the loop).

        :param n: the number of loops to create

        :param dim: a 2-tuple representing the dimensions (number of rows and columns) of the CA

        :param row: a list with length n, where the nth item specifies the row number of the nth loop

        :param col: a list with length n, where the nth item specifies the column number of the nth loop

        :return: the initial conditions
        """

        initial_conditions = np.zeros(dim, dtype=np.int)
        for i in range(n):
            row_i = row[i]
            col_i = col[i]
            # 1st row
            initial_conditions[row_i][col_i] = 2
            initial_conditions[row_i][col_i+1] = 2
            initial_conditions[row_i][col_i+2] = 2
            initial_conditions[row_i][col_i+3] = 2
            initial_conditions[row_i][col_i+4] = 2
            initial_conditions[row_i][col_i+5] = 2
            initial_conditions[row_i][col_i+6] = 2
            initial_conditions[row_i][col_i+7] = 2
            # 2nd row
            initial_conditions[row_i+1][col_i-1] = 2
            initial_conditions[row_i+1][col_i] = 1
            initial_conditions[row_i+1][col_i+1] = 7
            initial_conditions[row_i+1][col_i+2] = 0
            initial_conditions[row_i+1][col_i+3] = 1
            initial_conditions[row_i+1][col_i+4] = 4
            initial_conditions[row_i+1][col_i+5] = 0
            initial_conditions[row_i+1][col_i+6] = 1
            initial_conditions[row_i+1][col_i+7] = 4
            initial_conditions[row_i+1][col_i+8] = 2
            # 3rd row
            initial_conditions[row_i+2][col_i-1] = 2
            initial_conditions[row_i+2][col_i] = 0
            initial_conditions[row_i+2][col_i+1] = 2
            initial_conditions[row_i+2][col_i+2] = 2
            initial_conditions[row_i+2][col_i+3] = 2
            initial_conditions[row_i+2][col_i+4] = 2
            initial_conditions[row_i+2][col_i+5] = 2
            initial_conditions[row_i+2][col_i+6] = 2
            initial_conditions[row_i+2][col_i+7] = 0
            initial_conditions[row_i+2][col_i+8] = 2
            # 4th row
            initial_conditions[row_i+3][col_i-1] = 2
            initial_conditions[row_i+3][col_i] = 7
            initial_conditions[row_i+3][col_i+1] = 2
            initial_conditions[row_i+3][col_i+2] = 0
            initial_conditions[row_i+3][col_i+3] = 0
            initial_conditions[row_i+3][col_i+4] = 0
            initial_conditions[row_i+3][col_i+5] = 0
            initial_conditions[row_i+3][col_i+6] = 2
            initial_conditions[row_i+3][col_i+7] = 1
            initial_conditions[row_i+3][col_i+8] = 2
            # 5th row
            initial_conditions[row_i+4][col_i-1] = 2
            initial_conditions[row_i+4][col_i] = 1
            initial_conditions[row_i+4][col_i+1] = 2
            initial_conditions[row_i+4][col_i+2] = 0
            initial_conditions[row_i+4][col_i+3] = 0
            initial_conditions[row_i+4][col_i+4] = 0
            initial_conditions[row_i+4][col_i+5] = 0
            initial_conditions[row_i+4][col_i+6] = 2
            initial_conditions[row_i+4][col_i+7] = 1
            initial_conditions[row_i+4][col_i+8] = 2
            # 6th row
            initial_conditions[row_i+5][col_i-1] = 2
            initial_conditions[row_i+5][col_i] = 0
            initial_conditions[row_i+5][col_i+1] = 2
            initial_conditions[row_i+5][col_i+2] = 0
            initial_conditions[row_i+5][col_i+3] = 0
            initial_conditions[row_i+5][col_i+4] = 0
            initial_conditions[row_i+5][col_i+5] = 0
            initial_conditions[row_i+5][col_i+6] = 2
            initial_conditions[row_i+5][col_i+7] = 1
            initial_conditions[row_i+5][col_i+8] = 2
            # 7th row
            initial_conditions[row_i+6][col_i-1] = 2
            initial_conditions[row_i+6][col_i] = 7
            initial_conditions[row_i+6][col_i+1] = 2
            initial_conditions[row_i+6][col_i+2] = 0
            initial_conditions[row_i+6][col_i+3] = 0
            initial_conditions[row_i+6][col_i+4] = 0
            initial_conditions[row_i+6][col_i+5] = 0
            initial_conditions[row_i+6][col_i+6] = 2
            initial_conditions[row_i+6][col_i+7] = 1
            initial_conditions[row_i+6][col_i+8] = 2
            # 8th row
            initial_conditions[row_i+7][col_i-1] = 2
            initial_conditions[row_i+7][col_i] = 1
            initial_conditions[row_i+7][col_i+1] = 2
            initial_conditions[row_i+7][col_i+2] = 2
            initial_conditions[row_i+7][col_i+3] = 2
            initial_conditions[row_i+7][col_i+4] = 2
            initial_conditions[row_i+7][col_i+5] = 2
            initial_conditions[row_i+7][col_i+6] = 2
            initial_conditions[row_i+7][col_i+7] = 1
            initial_conditions[row_i+7][col_i+8] = 2
            initial_conditions[row_i+7][col_i+9] = 2
            initial_conditions[row_i+7][col_i+10] = 2
            initial_conditions[row_i+7][col_i+11] = 2
            initial_conditions[row_i+7][col_i+12] = 2
            # 9th row
            initial_conditions[row_i+8][col_i-1] = 2
            initial_conditions[row_i+8][col_i] = 0
            initial_conditions[row_i+8][col_i+1] = 7
            initial_conditions[row_i+8][col_i+2] = 1
            initial_conditions[row_i+8][col_i+3] = 0
            initial_conditions[row_i+8][col_i+4] = 7
            initial_conditions[row_i+8][col_i+5] = 1
            initial_conditions[row_i+8][col_i+6] = 0
            initial_conditions[row_i+8][col_i+7] = 7
            initial_conditions[row_i+8][col_i+8] = 1
            initial_conditions[row_i+8][col_i+9] = 1
            initial_conditions[row_i+8][col_i+10] = 1
            initial_conditions[row_i+8][col_i+11] = 1
            initial_conditions[row_i+8][col_i+12] = 1
            initial_conditions[row_i+8][col_i+13] = 2
            # 10th row
            initial_conditions[row_i+9][col_i] = 2
            initial_conditions[row_i+9][col_i+1] = 2
            initial_conditions[row_i+9][col_i+2] = 2
            initial_conditions[row_i+9][col_i+3] = 2
            initial_conditions[row_i+9][col_i+4] = 2
            initial_conditions[row_i+9][col_i+5] = 2
            initial_conditions[row_i+9][col_i+6] = 2
            initial_conditions[row_i+9][col_i+7] = 2
            initial_conditions[row_i+9][col_i+8] = 2
            initial_conditions[row_i+9][col_i+9] = 2
            initial_conditions[row_i+9][col_i+10] = 2
            initial_conditions[row_i+9][col_i+11] = 2
            initial_conditions[row_i+9][col_i+12] = 2

        return np.array([initial_conditions])
