import cellpylib as ca

rule_table = ca.create_lambda_table(lambda_val=0.45, k=4, r=2)

cellular_automaton = ca.init_simple(128, val=1)
# cellular_automaton = ca.init_random(128, k=4)

# evolve the cellular automaton for n time steps
cellular_automaton = ca.evolve(cellular_automaton, n_steps=200,
                               apply_rule=lambda state, c: ca.table_rule(state, rule_table), r=2)

ca.plot(cellular_automaton)