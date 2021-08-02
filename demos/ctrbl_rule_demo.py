import cellpylib as cpl

ctrbl = cpl.CTRBLRule(rule_table={
    (0, 1, 0, 0, 0): 1,
    (1, 1, 0, 0, 0): 0,
    (0, 0, 0, 0, 0): 0,
    (1, 0, 0, 0, 0): 1,
    (0, 0, 1, 1, 0): 0,
    (1, 1, 1, 1, 1): 1,
    (0, 1, 0, 1, 0): 0,
    (1, 1, 1, 0, 1): 1,
    (1, 0, 1, 0, 1): 1,
    (0, 1, 1, 1, 1): 1,
    (0, 0, 1, 1, 1): 0,
    (1, 1, 0, 0, 1): 1
}, add_rotations=True)

cellular_automaton = cpl.init_simple2d(rows=10, cols=10)

cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=60,
                                  apply_rule=ctrbl.rule, neighbourhood="von Neumann")

cpl.plot2d_animate(cellular_automaton)
