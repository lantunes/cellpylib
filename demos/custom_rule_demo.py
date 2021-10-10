import cellpylib as cpl
from collections import defaultdict


class CustomRule(cpl.BaseRule):

    def __init__(self):
        self.count = defaultdict(int)

    def __call__(self, n, c, t):
        self.count[c] += 1
        return self.count[c]


rule = CustomRule()

cellular_automaton = cpl.init_simple(11)

cellular_automaton = cpl.evolve(cellular_automaton, timesteps=10,
                                apply_rule=rule)

cpl.plot(cellular_automaton)
