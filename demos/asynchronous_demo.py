import cellpylib as cpl

# implements the rule 60 sequential automaton from the NKS Notes on
#   Chapter 9, section 10: "Sequential cellular automata"
#   http://www.wolframscience.com/nks/notes-9-10--sequential-cellular-automata/
cellular_automaton = cpl.init_simple(21)

r = cpl.AsynchronousRule(apply_rule=lambda n, c, t: cpl.nks_rule(n, 60), update_order=range(1, 20))

cellular_automaton = cpl.evolve(cellular_automaton, timesteps=19*20,
                                apply_rule=r.apply_rule)

# get every 19th row, including the first, as a cycle is completed every 19 rows
cpl.plot(cellular_automaton[::19])
