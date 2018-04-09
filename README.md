CellPyLib
=========

CellPyLib is a library for working with Cellular Automata, for Python. Currently, only 1- and 2-dimensional _k_-color 
cellular automata with periodic boundary conditions are supported. The size of the neighbourhood can be adjusted. The 
cellular automata produced by this library match the corresponding cellular automata available 
at [atlas.wolfram.com](http://atlas.wolfram.com).

Example usage:
```python
import cellpylib as cpl

# initialize a CA with 200 cells (a random initialization is also available) 
cellular_automaton = cpl.init_simple(200)

# evolve the CA for 100 time steps, using Rule 30 as defined in NKS
cellular_automaton = cpl.evolve(cellular_automaton, timesteps=100, 
                                apply_rule=lambda n, c, t: cpl.nks_rule(n, 30))

# plot the resulting CA evolution
cpl.plot(cellular_automaton)

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
import cellpylib as cpl

cellular_automaton = cpl.init_random(149)

# Mitchell et al. discovered this rule using a Genetic Algorithm
rule_number = 6667021275756174439087127638698866559

# evolve the CA, setting r to 3, for a neighbourhood size of 7
cellular_automaton = cpl.evolve(cellular_automaton, timesteps=149,
                                apply_rule=lambda n, c, t: cpl.binary_rule(n, rule_number), r=3)

cpl.plot(cellular_automaton)
```
<img src="https://raw.githubusercontent.com/lantunes/cellpylib/master/resources/density_classification.png" width="50%"/>

For more information, see:

> Melanie Mitchell, James P. Crutchfield, and Rajarshi Das, "Evolving Cellular Automata with Genetic Algorithms: A Review of Recent Work", In Proceedings of the First International Conference on Evolutionary Computation and Its Applications (EvCA'96), Russian Academy of Sciences (1996).

## Varying the Number of Colors

The number of states, or colors, that a cell can adopt is given by _k_. For example, a binary cellular automaton, in which a cell can 
assume only values of 0 and 1, has _k_ = 2. CellPyLib supports any value of _k_. A built-in function, `totalistic_rule`,
is an implementation of the [Totalistic cellular automaton rule](http://mathworld.wolfram.com/TotalisticCellularAutomaton.html), 
as described in [Wolfram's NKS](https://www.wolframscience.com/nks/). The code snippet below illustrates using this rule. 
A value of _k_ of 3 is used, but any value between (and including) 2 and 36 is currently supported. The rule number is 
given in base 10 but is interpreted as the rule in base _k_ (thus rule 777 corresponds to '1001210' when _k_ = 3).

```python
import cellpylib as cpl

cellular_automaton = cpl.init_simple(200)

# evolve the CA, using totalistic rule 777 for a 3-color CA
cellular_automaton = cpl.evolve(cellular_automaton, timesteps=100,
                                apply_rule=lambda n, c, t: cpl.totalistic_rule(n, k=3, rule=777))

cpl.plot(cellular_automaton)
```

<img src="https://raw.githubusercontent.com/lantunes/cellpylib/master/resources/tot3_rule777.png" width="50%"/>

## Rule Tables

One way to specify cellular automata rules is with rule tables. Rule tables are enumerations of all possible 
neighbourhood states together with their cell state mappings. For any given neighbourhood state, a rule table provides 
the associated cell state value. CellPyLib provides a built-in function for creating random rule tables. The following
snippet demonstrates its usage:
```python
import cellpylib as cpl

rule_table, actual_lambda, quiescent_state = cpl.random_rule_table(lambda_val=0.45, k=4, r=2,
                                                                   strong_quiescence=True, isotropic=True)

cellular_automaton = cpl.init_random(128, k=4)

# use the built-in table_rule to use the generated rule table
cellular_automaton = cpl.evolve(cellular_automaton, timesteps=200,
                                apply_rule=lambda n, c, t: cpl.table_rule(n, rule_table), r=2)
```
The following plots demonstrate the effect of varying the lambda parameter:

<img src="https://raw.githubusercontent.com/lantunes/cellpylib/master/resources/phase_transition.png" width="100%"/>

C. G. Langton describes the lambda parameter, and the transition from order to criticality to chaos in cellular 
automata while varying the lambda parameter, in the paper:

> Langton, C. G. (1990). Computation at the edge of chaos: phase transitions and emergent computation. Physica D: Nonlinear Phenomena, 42(1-3), 12-37.

## Measures of Complexity

CellPyLib provides various built-in functions which can act as measures of complexity in the cellular automata being
examined.

### Average Cell Entropy

Average cell entropy can reveal something about the presence of information within cellular automata dynamics. The 
built-in function `average_cell_entropy` provides the average Shannon entropy per single cell in a given cellular 
automaton. The following snippet demonstrates the calculation of the average cell entropy:

```python
import cellpylib as cpl

cellular_automaton = cpl.init_random(200)

cellular_automaton = cpl.evolve(cellular_automaton, timesteps=1000,
                                apply_rule=lambda n, c, t: cpl.nks_rule(n, 30))

# calculate the average cell entropy; the value will be ~0.999 in this case
avg_cell_entropy = cpl.average_cell_entropy(cellular_automaton)
```

The following plots illustrate how average cell entropy changes as a function of lambda:

<img src="https://raw.githubusercontent.com/lantunes/cellpylib/master/resources/avg_cell_entropy.png" width="100%"/>

### Average Mutual Information

The degree to which a cell state is correlated to its state in the next time step can be described using mutual 
information. Ideal levels of correlation are required for effective processing of information. The built-in function 
`average_mutual_information` provides the average mutual information between a cell and itself in the next time step 
(the temporal distance can be adjusted). The following snippet demonstrates the calculation of the average mutual 
information:

```python
import cellpylib as cpl

cellular_automaton = cpl.init_random(200)

cellular_automaton = cpl.evolve(cellular_automaton, timesteps=1000,
                                apply_rule=lambda n, c, t: cpl.nks_rule(n, 30))

# calculate the average mutual information between a cell and itself in the next time step
avg_mutual_information = cpl.average_mutual_information(cellular_automaton)
```

The following plots illustrate how average mutual information changes as a function of lambda:

<img src="https://raw.githubusercontent.com/lantunes/cellpylib/master/resources/avg_mutual_information.png" width="100%"/>

## 2D Cellular Automata

CellPyLib supports 2-dimensional cellular automata with periodic boundary conditions. The number of states, _k_, can be
any whole number. The neighbourhood radius, _r_, can also be any whole number, and both Moore and von Neumann 
neighbourhood types are supported. The following snippet demonstrates creating a 2D totalistic cellular automaton:

```python
import cellpylib as cpl

# initialize a 60x60 2D cellular automaton 
cellular_automaton = cpl.init_simple2d(60, 60)

# evolve the cellular automaton for 30 time steps, 
#  applying totalistic rule 126 to each cell with a Moore neighbourhood
cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=30, neighbourhood='Moore',
                                  apply_rule=lambda n, c, t: cpl.totalistic_rule(n, k=2, rule=126))

cpl.plot2d(cellular_automaton)
```

The `plot2D` function plots the state of the cellular automaton at the final time step:

<img src="https://raw.githubusercontent.com/lantunes/cellpylib/master/resources/tot_rule126_2d_moore.png" width="30%"/>

### Conway's Game of Life

There are a number of built-in plotting functions for 2D cellular automata. For example, `plot2d_animate` will animate 
the evolution of the cellular automaton. This is illustrated in the following snippet, which demonstrates the built-in 
Game of Life rule:

```python
import cellpylib as cpl

# Glider
cellular_automaton = cpl.init_simple2d(60, 60)
cellular_automaton[:, [28,29,30,30], [30,31,29,31]] = 1

# Blinker
cellular_automaton[:, [40,40,40], [15,16,17]] = 1

# Light Weight Space Ship (LWSS)
cellular_automaton[:, [18,18,19,20,21,21,21,21,20], [45,48,44,44,44,45,46,47,48]] = 1

# evolve the cellular automaton for 60 time steps
cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=60, neighbourhood='Moore',
                                  apply_rule=cpl.game_of_life_rule)

cpl.plot2d_animate(cellular_automaton)
```

<img src="https://raw.githubusercontent.com/lantunes/cellpylib/master/resources/game_of_life.gif" width="65%"/>

For more information about Conway's Game of Life, see:

> Conway, J. (1970). The game of life. Scientific American, 223(4), 4.