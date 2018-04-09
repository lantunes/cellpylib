import cellpylib as cpl
import numpy as np

cellular_automaton = cpl.init_random(149)

print("density of 1s: %s" % (np.count_nonzero(cellular_automaton) / 149))

# M. Mitchell et al. discovered this rule using a Genetic Algorithm
rule_number = 6667021275756174439087127638698866559

cellular_automaton = cpl.evolve(cellular_automaton, timesteps=149,
                                apply_rule=lambda n, c, t: cpl.binary_rule(n, rule_number), r=3)

cpl.plot(cellular_automaton)
