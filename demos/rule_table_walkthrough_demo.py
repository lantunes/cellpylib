import cellpylib as ca

rule_table, actual_lambda, quiescent_state = ca.random_rule_table(lambda_val=0.0, k=4, r=2,
                                                                  strong_quiescence=True, isotropic=True)

lambda_vals = [0.15, 0.37, 0.75]
ca_list = []
titles = []
for i in range(0, 3):
    # cellular_automaton = ca.init_simple(128, val=1)
    cellular_automaton = ca.init_random(128, k=4)

    rule_table, actual_lambda = ca.table_walk_through(rule_table, lambda_vals[i], k=4, r=2,
                                                      quiescent_state=quiescent_state, strong_quiescence=True)
    print(actual_lambda)

    # evolve the cellular automaton for n time steps
    cellular_automaton = ca.evolve(cellular_automaton, n_steps=200,
                                   apply_rule=lambda state, c: ca.table_rule(state, rule_table), r=2)

    ca_list.append(cellular_automaton)
    avg_cell_entropy = ca.average_cell_entropy(cellular_automaton)
    avg_mutual_information = ca.average_mutual_information(cellular_automaton)
    titles.append(r'$\lambda$ = %s, $\widebar{H}$ = %s, $\widebar{I}$ = %s' %
                  (lambda_vals[i], "{:.4}".format(avg_cell_entropy), "{:.4}".format(avg_mutual_information)))

ca.plot_multiple(ca_list, titles)
