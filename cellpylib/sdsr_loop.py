import numpy as np
from .langtons_loop import LangtonsLoop


class SDSRLoop(LangtonsLoop):
    """
    An implementation of H. Sayama's SDSR loop. For more information, see:

    .. code-block:: text

       Sayama, H. (1998). Constructing evolutionary systems on a simple deterministic cellular automata space.
       PhD, University of Tokyo, Department of Information Science.
    """
    def __init__(self):
        """
        Create an SDSR Loop.
        """
        super().__init__()

        # Define rule '11152->8' and its rotationally symmetric ones.
        self._rule_table[(1, 1, 1, 5, 2)] = 8
        self._rule_table[(1, 2, 1, 1, 5)] = 8
        self._rule_table[(1, 5, 2, 1, 1)] = 8
        self._rule_table[(1, 1, 5, 2, 1)] = 8

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
            in_tube = self._is_in_tube(top, right, bottom, left)
            new_activity = None

            # Let 0->1 if it is in the tube and next to 1. Let all other 0s remain as is.
            if current_activity == 0:
                if in_tube and 1 in trbl:
                    new_activity = 1
                else:
                    new_activity = 0

            # Let 1->7 if it is in the tube and next to 7. Else, let 1->6 if it is in the tube and next to 6.
            # Else, let 1->4 if it is in the tube and next to 4.
            if current_activity == 1 and in_tube:
                if 7 in trbl:
                    new_activity = 7
                elif 6 in trbl:
                    new_activity = 6
                elif 4 in trbl:
                    new_activity = 4

            # Let 4,6,7->0 if it is in the tube and next to 0.
            if current_activity in (4, 6, 7) and in_tube and 0 in trbl:
                new_activity = 0

            # Let 2->1 if it is next to 3. Else, let 2 remain as is if it is next to another 2.
            if current_activity == 2 and 3 in trbl:
                new_activity = 1
            elif current_activity == 2 and 2 in trbl:
                new_activity = 2

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

    def _is_in_tube(self, top, right, bottom, left):
        k = 0
        for site in [top, right, bottom, left]:
            if site in (1, 2, 4, 6, 7):
                k += 1
        return k >= 2
