import cellpylib as cpl

rule_table, actual_lambda, quiescent_state = cpl.random_rule_table(lambda_val=0.37, k=4, r=2,
                                                                   strong_quiescence=True, isotropic=True)

# cellular_automaton = cpl.init_simple(128, val=1)
cellular_automaton = cpl.init_random(128, k=4, n_randomized=20)

# evolve the cellular automaton for 200 time steps
cellular_automaton = cpl.evolve(cellular_automaton, timesteps=200,
                                apply_rule=lambda n, c, t: cpl.table_rule(n, rule_table), r=2)

cpl.plot(cellular_automaton)
