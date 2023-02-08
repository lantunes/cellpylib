import cellpylib as cpl
import numpy as np

"""
Block CA at the top of NKS page 460
"""

initial_conditions = np.array([[0]*13 + [1]*2 + [0]*201])


def block_rule(n, t):
    if n == (1, 1): return 1, 1
    elif n == (1, 0): return 1, 0
    elif n == (0, 1): return 0, 0
    elif n == (0, 0): return 0, 1


ca = cpl.evolve_block(initial_conditions, block_size=2, timesteps=200, apply_rule=block_rule)

cpl.plot(ca)
