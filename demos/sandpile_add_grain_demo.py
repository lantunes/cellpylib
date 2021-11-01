import cellpylib as cpl
import numpy as np


n_rows = 45
n_cols = 45
sandpile = cpl.Sandpile(n_rows, n_cols)
sandpile.add_grain(cell_index=(23, 23), timestep=1)

initial = np.loadtxt('sandpile_add_grain_demo.txt', dtype=int)
initial = np.array([initial])

ca = cpl.evolve2d(initial, timesteps=cpl.until_fixed_point(),
                  apply_rule=sandpile, neighbourhood="von Neumann")

print("Number of timesteps to reach fixed point: %s" % len(ca))
cpl.plot2d_animate(ca)
