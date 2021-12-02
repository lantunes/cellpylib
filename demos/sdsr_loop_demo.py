import cellpylib as cpl

sdsr_loop = cpl.SDSRLoop()

# the initial conditions consist of a single loop
cellular_automaton = sdsr_loop.init_loops(1, (100, 100), [40], [40])

cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=700,
                                  apply_rule=sdsr_loop, memoize="recursive")

cpl.plot2d_animate(cellular_automaton)
