import cellpylib as ca

# Glider
cellular_automaton = ca.init_simple2d(60, 60)
cellular_automaton[0][28][30] = 1
cellular_automaton[0][29][31] = 1
cellular_automaton[0][30][29] = 1
cellular_automaton[0][30][31] = 1

# Blinker
cellular_automaton[0][40][15] = 1
cellular_automaton[0][40][16] = 1
cellular_automaton[0][40][17] = 1

# Light Weight Space Ship (LWSS)
cellular_automaton[0][18][45] = 1
cellular_automaton[0][18][48] = 1
cellular_automaton[0][19][44] = 1
cellular_automaton[0][20][44] = 1
cellular_automaton[0][21][44] = 1
cellular_automaton[0][21][45] = 1
cellular_automaton[0][21][46] = 1
cellular_automaton[0][21][47] = 1
cellular_automaton[0][20][48] = 1

# evolve the cellular automaton for 60 time steps
cellular_automaton = ca.evolve2d(cellular_automaton, timesteps=60, neighbourhood='Moore',
                                 apply_rule=ca.game_of_life_rule)

ca.plot2d_animate(cellular_automaton)
