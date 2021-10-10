from .ca_functions import BaseRule


class CTRBLRule(BaseRule):
    """
    A rule that operates on von Neumann neighbourhoods, taking into account the states of a cell's
    neighbours at the top, right, bottom and left positions. Only supports 2D automata with periodic boundaries and a
    radius of 1.
    """
    def __init__(self, rule_table, add_rotations=False):
        """
        Creates a CTRBLRule.

        :param rule_table: a dictionary with keys being a 5-tuple representing the states of the CTRBL cells, and values
                           being a single value representing the image state (i.e. the state of the Center cell in
                           the next timestep); all combinations of states must exist, otherwise, if the combination of
                           states does not exist in the rule table, an exception will be raised

        :param add_rotations: whether rotations in the rule table are implied, and should be included (default is False)
        """
        self._rule_table = self._init_rule_table(rule_table, add_rotations)

    def __call__(self, n, c, t):
        """
        The CTRBL rule to apply.

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
            raise Exception("neighbourhood state (%s, %s, %s, %s, %s) not in rule table" % key)
        return self._rule_table[key]

    @property
    def rule_table(self):
        """
        The rule table for this CTRBL rule.

        :return: the rule table
        """
        return self._rule_table

    @staticmethod
    def _init_rule_table(rule_table, add_rotations):
        new_rule_table = {}
        for rule, image in rule_table.items():
            new_rule_table[rule] = image
            if add_rotations:
                r = list(rule)
                for _ in range(3):
                    r.insert(1, r.pop(4))
                    new_rule_table[tuple(r)] = image
        return new_rule_table
