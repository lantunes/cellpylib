import cellpylib as cpl
import numpy as np


n_rows = 45
n_cols = 45
sandpile = cpl.Sandpile(n_rows, n_cols)

ca = np.random.randint(5, size=n_rows*n_cols).reshape((1, n_rows, n_cols))
# we're using a closed boundary, so make the boundary cells 0
ca[0, 0, :], ca[0, n_rows-1, :], ca[0, :, 0], ca[0, :, n_cols-1] = 0, 0, 0, 0

ca = cpl.evolve2d(ca, timesteps=50, apply_rule=sandpile, neighbourhood="von Neumann")

cpl.plot2d_animate(ca)
