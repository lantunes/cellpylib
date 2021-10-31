The Collatz Conjecture
----------------------

The Collatz conjecture states that by iteratively applying a particular rule to successive numbers, beginning from any
number, the result will eventually be `1`.

Below is an example of a rule that demonstrates the Collatz conjecture, and also demonstrates the use of a callable for
the ``timesteps`` argument of the :py:func:`~cellpylib.ca_functions.evolve` function, since, in principle, it isn't
known how many iterations are required before the system evolves to a state consisting of the value `1`.

.. code-block::

    import cellpylib as cpl
    import numpy as np

    initial = np.array([[17]], dtype=np.int)

    def activity_rule(n, c, t):
        n = n[1]
        if n % 2 == 0:
            # number is even
            return n / 2
        else:
            return 3*n + 1

    cellular_automaton = cpl.evolve(initial, apply_rule=activity_rule,
                                    timesteps=lambda ca, t: True if ca[-1][0] != 1 else False)

    print([i[0] for i in cellular_automaton])

The program above should print:

.. code-block::

    [17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

**References:**

https://en.wikipedia.org/wiki/Collatz_conjecture
