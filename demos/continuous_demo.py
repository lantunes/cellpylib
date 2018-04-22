import math
from pprint import pprint

import numpy as np

import cellpylib as cpl

cellular_automaton = cpl.init_simple(200, dtype=np.float32)


# NKS page 157
def apply_rule(n, c, t):
    result = (sum(n) / len(n)) * (3 / 2)
    frac, whole = math.modf(result)
    return frac

cellular_automaton = cpl.evolve(cellular_automaton, timesteps=100,
                                apply_rule=apply_rule)

pprint(cellular_automaton[:6, 95:106].tolist(), width=100)

cpl.plot(cellular_automaton)
