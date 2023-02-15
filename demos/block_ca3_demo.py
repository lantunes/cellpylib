import cellpylib as cpl
import numpy as np

"""
Block CA from 
https://writings.stephenwolfram.com/2023/02/computational-foundations-for-the-second-law-of-thermodynamics/
"""

initial_conditions = np.array([[0]*25 + [2]*17 + [0]*24])


def block_rule(n, t):
    if   n == (1, 1): return 2, 2
    elif n == (1, 0): return 1, 0
    elif n == (0, 1): return 0, 1
    elif n == (0, 0): return 0, 0
    elif n == (2, 2): return 1, 1
    elif n == (2, 0): return 0, 2
    elif n == (0, 2): return 2, 0
    elif n == (2, 1): return 2, 1
    elif n == (1, 2): return 1, 2


ca = cpl.evolve_block(initial_conditions, block_size=2, timesteps=200, apply_rule=block_rule)

cpl.plot(ca)
