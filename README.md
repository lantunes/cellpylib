CellPyLib
=========

CellPyLib is a library for working with Cellular Automata, for Python. Currently, only uniform 1-dimensional _k_-color 
cellular automata with periodic boundary conditions are supported. The size of the neighbourhood can be adjusted. The 
cellular automata produced by this library match the corresponding cellular automata available 
at [atlas.wolfram.com](http://atlas.wolfram.com).

Example usage:
```python
import cellpylib as ca

# initialize a CA with 200 cells (a random initialization is also available) 
cellular_automaton = ca.init_simple(200)

# evolve the CA for 100 time steps, using Rule 30 as defined in NKS
cellular_automaton = ca.evolve(cellular_automaton, n_steps=100, 
                               apply_rule=lambda state, c: ca.nks_rule(state, 30))

# plot the resulting CA evolution
ca.plot(cellular_automaton)

```

<img src="https://raw.githubusercontent.com/lantunes/cellpylib/master/resources/rule30.png" width="50%"/>

Requirements for using this library are Python 3.5, numpy, and matplotlib.

## Varying the Neighbourhood Size

The size of the cell neighbourhood can be varied by setting the parameter _*r*_ when calling the `evolve` function. The
value of _*r*_ represents the number of cells to the left and to the right of the cell under consideration. Thus, to
get a neighbourhood size of 3, _*r*_ should be 1, and to get a neighbourhood size of 7, _*r*_ should be 3.
As an example, consider the work of M. Mitchell et al., carried out in the 1990s, involving the creation (discovery) of
a cellular automaton that solves the density classification problem: if the initial random binary vector contains 
more than 50% of 1s, then a cellular automaton that solves this problem will give rise to a vector that contains only
1s after a fixed number of time steps, and likewise for the case of 0s. A very effective cellular automaton that solves
this problem most of the time was found using a Genetic Algorithm.

```python
import cellpylib as ca

cellular_automaton = ca.init_random(149)

# Mitchell et al. discovered this rule using a Genetic Algorithm
rule_number = 6667021275756174439087127638698866559

# evolve the CA, setting r to 3, for a neighbourhood size of 7
cellular_automaton = ca.evolve(cellular_automaton, n_steps=149,
                               apply_rule=lambda state, c: ca.number_rule(state, rule_number), r=3)

ca.plot(cellular_automaton)
```
<img src="https://raw.githubusercontent.com/lantunes/cellpylib/master/resources/density_classification.png" width="50%"/>

For more information, see:

> Melanie Mitchell, James P. Crutchfield, and Rajarshi Das, "Evolving Cellular Automata with Genetic Algorithms: A Review of Recent Work", In Proceedings of the First International Conference on Evolutionary Computation and Its Applications (EvCA'96), Russian Academy of Sciences (1996).

## Varying the Number of Colors

The number of states that a cell can adopt is given by _k_. For example, a binary cellular automaton, in which a cell can 
assume only values of 0 and 1, has _k_ = 2. CellPyLib supports any value of _k_. A built-in function, `totalistic_rule`,
is an implementation of the [Totalistic cellular automaton rule](http://mathworld.wolfram.com/TotalisticCellularAutomaton.html), 
as described in Wolfram's NKS. The code snippet below illustrates using this rule. A value of _k_ of 3 is used, but
any value between (and including) 2 and 10 is currently supported. The rule number is given in base 10 but is 
interpreted as the rule in base _k_ (thus rule 777 corresponds to '1001210').

```python
import cellpylib as ca

cellular_automaton = ca.init_simple(200)

# evolve the CA, using totalistic rule 777 for a 3-color CA
cellular_automaton = ca.evolve(cellular_automaton, n_steps=100,
                               apply_rule=lambda state, c: ca.totalistic_rule(state, k=3, rule=777))

ca.plot(cellular_automaton)
```

<img src="https://raw.githubusercontent.com/lantunes/cellpylib/master/resources/tot3_rule777.png" width="50%"/>
