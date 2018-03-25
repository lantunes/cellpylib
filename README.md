CellPyLib
=========

CellPyLib is a library for working with Cellular Automata, for Python. Currently, only uniform 1-dimensional binary 
cellular automata are supported. The cellular automata produced by this library match the corresponding cellular 
automata available at [atlas.wolfram.com](http://atlas.wolfram.com).

Example usage:
```python
import cellpylib as ca

# initialize a CA with 200 cells (a random initialization is also available) 
cellular_automaton = ca.init_simple(200)

# evolve the CA for 100 time steps, using Rule 30 as defined in NKS
cellular_automaton = ca.evolve(cellular_automaton, n_steps=100, 
                               apply_rule=lambda state: ca.nks_rule(state, 30))

# plot the resulting CA evolution
ca.plot(cellular_automaton)

```

<img src="https://raw.githubusercontent.com/lantunes/cellpylib/master/resources/rule30.png" width="50%"/>

Requirements for using this library are Python 3.5, numpy, and matplotlib.