import cellpylib as cpl

langtons_loop = cpl.LangtonsLoop()

# the initial conditions consist of a single loop
cellular_automaton = langtons_loop.init_loops(1, (75, 75), [40], [25])

cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=500,
                                  apply_rule=langtons_loop, memoize="recursive")

cpl.plot2d_animate(cellular_automaton)
