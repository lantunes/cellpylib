import cellpylib as cpl
import numpy as np

cellular_automaton = cpl.init_simple2d(60, 60)
# the letter "E"
cellular_automaton[0][28][28] = 1
cellular_automaton[0][28][29] = 1
cellular_automaton[0][28][30] = 1
cellular_automaton[0][29][28] = 1
cellular_automaton[0][30][28] = 1
cellular_automaton[0][30][29] = 1
cellular_automaton[0][30][30] = 1
cellular_automaton[0][31][28] = 1
cellular_automaton[0][32][28] = 1
cellular_automaton[0][32][29] = 1
cellular_automaton[0][32][30] = 1

def activity_rule(n, c, t):
    current_activity = n[1][1]
    return (np.sum(n) - current_activity) % 2

cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=20,
                                  apply_rule=activity_rule, neighbourhood="Moore")

cpl.plot2d_animate(cellular_automaton, interval=350)
