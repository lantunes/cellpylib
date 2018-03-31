import cellpylib as ca
import numpy as np

cellular_automaton = ca.init_random(149)

print("density of 1s: %s" % (np.count_nonzero(cellular_automaton) / 149))

# M. Mitchell et al. discovered this rule using a Genetic Algorithm
rule_number = 6667021275756174439087127638698866559

cellular_automaton = ca.evolve(cellular_automaton, n_steps=149,
                               apply_rule=lambda state, c: ca.binary_rule(state, rule_number), r=3)

ca.plot(cellular_automaton)
