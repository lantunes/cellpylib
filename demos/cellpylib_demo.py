import cellpylib as cpl

cellular_automaton = cpl.init_simple(200)
# cellular_automaton = cpl.init_random(200)

# evolve the cellular automaton for 100 time steps
cellular_automaton = cpl.evolve(cellular_automaton, timesteps=100,
                                apply_rule=lambda n, c, t: cpl.nks_rule(n, 30))

cpl.plot(cellular_automaton)
