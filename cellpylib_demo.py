import cellpylib as ca

cellular_automaton = ca.init_simple(200)
# cellular_automaton = ca.init_random(200)

# evolve the cellular automaton for n time steps
cellular_automaton = ca.evolve(cellular_automaton, n_steps=100,
                               apply_rule=lambda state: ca.nks_rule(state, 30))

ca.plot(cellular_automaton)
