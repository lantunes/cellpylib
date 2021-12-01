import cellpylib as cpl

evoloop = cpl.Evoloop()

# the initial conditions consist of a single loop
cellular_automaton = evoloop.init_species13_loop((100, 100), 40, 15)

cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=700,
                                  apply_rule=evoloop, memoize="recursive")

cpl.plot2d_animate(cellular_automaton)
