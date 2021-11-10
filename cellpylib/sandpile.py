from .ca_functions import BaseRule


class Sandpile(BaseRule):
    """
    A rule that operates on von Neumann neighbourhoods with a radius of 1. A sandpile is a 2D cellular automaton and
    dynamical system that displays self-organized criticality. It was introduced by Bak, Tang and Wiesenfeld in 1987.
    """
    def __init__(self, rows, cols, is_closed_boundary=True):
        """
        Creates a Sandpile.

        :param rows: the number of rows in this 2D CA

        :param cols: the number of columns in this 2D CA

        :param is_closed_boundary: whether or not the sandpile's boundary is closed; if it is closed, then all the
               boundary cells will maintain a value of 0 (default is True)
        """
        self._K = 4  # this value is hard-coded because the neighbourhood type, "von Neumann", is fixed
        self._rows = rows
        self._cols = cols
        self._is_closed_boundary = is_closed_boundary
        self._grain_additions = []

    def add_grain(self, cell_index, timestep):
        """
        Drop a grain of sand at the given cell in the given timestep.

        :param cell_index: a 2-tuple representing the row index and column index of the cell that will have
                           a grain of sand added

        :param timestep: the timestep at which the grain addition will occur
        """
        self._grain_additions.append(_GrainAddition(cell_index, timestep))

    def _is_in_boundary(self, c):
        """
        Returns True if the given cell (as a 2-tuple, representing its coordinates) is a boundary cell.

        :param c: a 2-tuple representing the row- and column-index of the cell

        :return: True if the given cell is a boundary cell, False otherwise
        """
        return c[0] == 0 or c[0] == self._rows - 1 or c[1] == 0 or c[1] == self._cols - 1

    def __call__(self, n, c, t):
        """
        The Sandpile rule to apply.

        :param n: the neighbourhood

        :param c: the index of the current cell

        :param t: the current timestep

        :return: the activity of the current cell at the next timestep
        """
        if self._is_closed_boundary and self._is_in_boundary(c):
            return 0  # closed boundary conditions

        for grain_addition in self._grain_additions:
            if t == grain_addition.timestep and c == grain_addition.cell_index:
                return n[1][1] + 1

        # this cell's activity is the value of the center of the von Neumann neighbourhood
        current_activity = n[1][1]
        new_activity = current_activity

        # this assumes a von Neumann neighbourhood of radius 1
        neighbour_activities = [n[0][1], n[1][0], n[1][2], n[2][1]]

        for neighbour_activity in neighbour_activities:

            if neighbour_activity >= self._K:
                new_activity += 1

        if current_activity >= self._K:
            new_activity -= self._K

        return new_activity


class _GrainAddition:
    """
    A representation of the addition of a grain of sand to the sandpile.
    """
    def __init__(self, cell_index, timestep):
        """
        Create an instance of a `_GrainAddition`.

        :param cell_index: the index of the cell that will have a grain of sand added

        :param timestep: the timestep at which the grain addition occurs
        """
        self.cell_index = cell_index
        self.timestep = timestep
