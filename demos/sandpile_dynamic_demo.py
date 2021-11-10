import cellpylib as cpl
import numpy as np
np.random.seed(0)


n_rows = 45
n_cols = 45
sandpile = cpl.Sandpile(n_rows, n_cols)

initial = np.random.randint(5, size=n_rows*n_cols).reshape((1, n_rows, n_cols))
# we're using a closed boundary, so make the boundary cells 0
initial[0, 0, :], initial[0, n_rows-1, :], initial[0, :, 0], initial[0, :, n_cols-1] = 0, 0, 0, 0

ca = cpl.evolve2d(initial, timesteps=cpl.until_fixed_point(),
                  apply_rule=sandpile, neighbourhood="von Neumann")

print("Number of timesteps to reach fixed point: %s" % len(ca))
cpl.plot2d_animate(ca)
