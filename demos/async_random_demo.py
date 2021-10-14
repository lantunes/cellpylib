import cellpylib as cpl


cellular_automaton = cpl.init_simple2d(50, 50, val=0)


# During each timestep, we'll check each cell if it should be the one updated according to the
# update order. At the end of a timestep, the update order index is advanced, but if the
# update order is randomized at the end of each timestep, then this is equivalent to picking
# a cell randomly to update at each timestep.
apply_rule = cpl.AsynchronousRule(apply_rule=lambda n, c, t: 1, num_cells=(50, 50),
                                  randomize_each_cycle=True)

cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=50,
                                  neighbourhood='Moore', apply_rule=apply_rule)

cpl.plot2d_animate(cellular_automaton, interval=200, autoscale=True)
