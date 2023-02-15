import cellpylib as cpl
import numpy as np

"""
Block CA at the bottom of NKS page 462
"""

initial_conditions = np.array([[0]*30 + [2]*30 + [0]*30])


def block_rule(n, t):
    if   n == (1, 1): return 1, 1
    elif n == (1, 0): return 0, 2
    elif n == (0, 1): return 2, 0
    elif n == (0, 0): return 0, 0
    elif n == (2, 2): return 2, 2
    elif n == (2, 0): return 1, 0
    elif n == (0, 2): return 0, 1
    elif n == (2, 1): return 2, 1
    elif n == (1, 2): return 1, 2


ca = cpl.evolve_block(initial_conditions, block_size=2, timesteps=4500, apply_rule=block_rule)

cpl.plot(ca[-500:])
