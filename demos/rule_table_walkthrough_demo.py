import cellpylib as cpl

rule_table, actual_lambda, quiescent_state = cpl.random_rule_table(lambda_val=0.0, k=4, r=2,
                                                                   strong_quiescence=True, isotropic=True)

lambda_vals = [0.15, 0.37, 0.75]
ca_list = []
titles = []
for i in range(0, 3):
    # cellular_automaton = cpl.init_simple(128, val=1)
    cellular_automaton = cpl.init_random(128, k=4)

    rule_table, actual_lambda = cpl.table_walk_through(rule_table, lambda_vals[i], k=4, r=2,
                                                       quiescent_state=quiescent_state, strong_quiescence=True)
    print(actual_lambda)

    # evolve the cellular automaton for 200 time steps
    cellular_automaton = cpl.evolve(cellular_automaton, timesteps=200,
                                    apply_rule=lambda n, c, t: cpl.table_rule(n, rule_table), r=2)

    ca_list.append(cellular_automaton)
    avg_cell_entropy = cpl.average_cell_entropy(cellular_automaton)
    avg_mutual_information = cpl.average_mutual_information(cellular_automaton)
    titles.append(r'$\lambda$ = %s, $\widebar{H}$ = %s, $\widebar{I}$ = %s' %
                  (lambda_vals[i], "{:.4}".format(avg_cell_entropy), "{:.4}".format(avg_mutual_information)))

cpl.plot_multiple(ca_list, titles)
