import cellpylib as ca

rule_table, actual_lambda, quiescent_state = ca.random_rule_table(lambda_val=0.37, k=4, r=2,
                                                                  strong_quiescence=True, isotropic=True)

# cellular_automaton = ca.init_simple(128, val=1)
cellular_automaton = ca.init_random(128, k=4, n_randomized=20)

# evolve the cellular automaton for n time steps
cellular_automaton = ca.evolve(cellular_automaton, n_steps=200,
                               apply_rule=lambda state, c: ca.table_rule(state, rule_table), r=2)

ca.plot(cellular_automaton)
