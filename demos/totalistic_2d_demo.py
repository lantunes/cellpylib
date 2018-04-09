import cellpylib as cpl

cellular_automaton = cpl.init_simple2d(60, 60)

# evolve the cellular automaton for 30 time steps
cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=30, neighbourhood='Moore',
                                  apply_rule=lambda n, c, t: cpl.totalistic_rule(n, k=2, rule=126))

cpl.plot2d(cellular_automaton)
