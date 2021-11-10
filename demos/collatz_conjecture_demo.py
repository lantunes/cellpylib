import cellpylib as cpl
import numpy as np


initial = np.array([[17]], dtype=np.int)


def activity_rule(n, c, t):
    n = n[1]
    if n % 2 == 0:
        # number is even
        return n / 2
    else:
        return 3*n + 1


cellular_automaton = cpl.evolve(initial, apply_rule=activity_rule,
                                timesteps=lambda ca, t: True if ca[-1][0] != 1 else False)

print([i[0] for i in cellular_automaton])
