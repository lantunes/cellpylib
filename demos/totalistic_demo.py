import cellpylib as ca

cellular_automaton = ca.init_simple(200)
# cellular_automaton = ca.init_random(200, k=3)

# evolve the cellular automaton for 100 time steps
cellular_automaton = ca.evolve(cellular_automaton, timesteps=100,
                               apply_rule=lambda n, c, t: ca.totalistic_rule(n, k=3, rule=777))

ca.plot(cellular_automaton)
