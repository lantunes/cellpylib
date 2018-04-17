import numpy as np

import cellpylib as cpl

# NKS page 437 - Rule 214R

# run the CA forward for 32 steps to get the initial condition for the next evolution
cellular_automaton = cpl.init_simple(63)
r = cpl.ReversibleRule(cellular_automaton[0], 214)
cellular_automaton = cpl.evolve(cellular_automaton, timesteps=32,
                                apply_rule=r.apply_rule)

# use the last state of the CA as the initial, previous state for this evolution
r = cpl.ReversibleRule(cellular_automaton[-1], 214)
cellular_automaton = np.array([cellular_automaton[-2]])
cellular_automaton = cpl.evolve(cellular_automaton, timesteps=62,
                                apply_rule=r.apply_rule)

cpl.plot(cellular_automaton)
