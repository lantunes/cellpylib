import cellpylib as ca

cellular_automaton = ca.init_simple2d(60, 60)

# evolve the cellular automaton for 30 time steps
cellular_automaton = ca.evolve2d(cellular_automaton, timesteps=30, neighbourhood='Moore',
                               apply_rule=lambda n, c, t: ca.totalistic_rule(n, k=2, rule=126))

ca.plot2d(cellular_automaton)
