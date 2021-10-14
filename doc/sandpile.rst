Sandpiles
---------

A sandpile is a cellular automaton and dynamical system that displays self-organized criticality. It was introduced by
Bak, Tang and Wiesenfeld in 1987.

Below is an example of a sandpile using the built-in :py:class:`~cellpylib.sandpile.Sandpile` class. The boundary of
the 2D CA can be either closed or open. If the boundary is closed, then all boundary cells should have a value of 0.

.. code-block::

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


.. image:: _static/sandpile.gif
    :width: 500

**References:**

*Bak, Per, Chao Tang, and Kurt Wiesenfeld. "Self-organized criticality." Physical review A 38.1 (1988): 364.*

https://en.wikipedia.org/wiki/Abelian_sandpile_model
