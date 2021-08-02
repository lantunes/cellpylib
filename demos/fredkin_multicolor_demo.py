import cellpylib as cpl
import numpy as np

cellular_automaton = cpl.init_simple2d(60, 60)
# the letter "E"
cellular_automaton[0][28][28] = 0
cellular_automaton[0][28][29] = 1
cellular_automaton[0][28][30] = 2
cellular_automaton[0][29][28] = 3
cellular_automaton[0][30][28] = 4
cellular_automaton[0][30][29] = 5
cellular_automaton[0][30][30] = 6
cellular_automaton[0][31][28] = 7
cellular_automaton[0][32][28] = 8
cellular_automaton[0][32][29] = 9
cellular_automaton[0][32][30] = 10

def activity_rule(n, c, t):
    current_activity = n[1][1]
    return (np.sum(n) - current_activity) % 11

cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=23,
                                  apply_rule=activity_rule, neighbourhood="von Neumann")

cpl.plot2d_animate(cellular_automaton, interval=350, colormap='viridis')
