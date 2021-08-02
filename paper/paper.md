---
title: 'CellPyLib: A Python Library for working with Cellular Automata'
tags:
  - Python
  - Cellular Automata
  - complex systems
  - non-linear dynamics
  - discrete dynamical systems
authors:
  - name: Luis M. Antunes
    affiliation: 1
affiliations:
 - name: Department of Chemistry, University of Reading, Whiteknights, Reading RG6 6DX, United Kingdom
   index: 1
date: 28 July 2021
bibliography: paper.bib
---

# Summary

Cellular Automata (CA) are discrete dynamical systems with a rich history [@ilachinski2001cellular]. Introduced by John 
von Neumann and Stanislaw Ulam in the 1940s [@von1951general], CA have continued to fascinate, as their conceptual 
simplicity serves as a powerful microscope that allows us to explore the nature of computation and complexity, and the 
origins of emergence. Far from being an antiquated computational model, investigators are utilizing CA in novel and 
creative ways, such as the incorporation with Deep Learning [@nichele2017deep] [@mordvintsev2020growing]. Popularized 
and investigated by Stephen Wolfram in his book `A New Kind of Science` [@wolfram2002new], CA remain premier reminders 
of a common theme in the study of the physical world: that simple systems and rules can give rise to remarkable 
complexity. They are a laboratory for the study of the origins of the complexity we see in the world around us.

`CellPyLib` is a Python library for working with CA. It provides a concise and simple interface for defining and 
analyzing 1- and 2-dimensional CA. The CA can consist of discrete or continuous states. Neighbourhood radii are 
adjustable, and in the 2-dimensional case, both Moore and von Neumann neighbourhoods are supported. With `CellPyLib`, it 
is trivial to create Elementary CA, and CA with totalistic rules, as these rules are provided as part of the library. 
Additionally, the library provides a means for creating asynchronous and reversible CA. Finally, an implementation 
of C. G. Langton's approach for creating CA rules using the lambda value is provided, allowing for the exploration of 
complex systems, phase transitions and emergent computation. [@langton1990computation]

Utility functions for plotting and viewing the evolved CA are also provided. These tools make it easy to visualize the
results of CA evolution, and include the option of creating animations of the evolution itself. Moreover, utility 
functions for computing the information-theoretic properties of CA, such as the Shannon entropy and mutual information, 
are included.

# Statement of need

The Python software ecosystem is lacking when it comes to Cellular Automata. A web search reveals that while there are 
some projects dedicated to the simulation of CA, most are not general-purpose, focusing only on certain CA systems, and 
are generally missing a substantial test suite, hindering their future extensibility and maintainability. In short, 
there appears to be a dearth of robust and flexible libraries for working with CA in Python. 

Currently, many scientists choose Python as their main tool for computational tasks. Though researchers can choose to 
implement CA themselves, this is error-prone, as there are some subtleties when it comes to correctly handling issues 
such as boundary conditions on periodic lattices, or constructing von Neumann neighbourhoods with radius greater than 1, 
for example. Researchers may be dissuaded from incorporating CA into their research if they are forced to work with 
unfamiliar languages and technologies, or are required to devote considerable effort to the implementation and testing 
of non-trivial algorithms. The availability of a user-friendly Python library for CA will likely encourage more 
researchers to consider these fascinating dynamical and computational systems. Moreover, having a standard 
implementation of CA in the Python environment helps to ensure that scientific results are reproducible.

# Example Usage

`CellPyLib` can be readily installed using `pip`:

```
$ pip install cellpylib
```

It has minimal dependencies, depending only on the commonly used libraries NumPy [@harris2020array] and Matplotlib 
[@Hunter:2007].

The following example illustrates the evolution of the Rule 30 CA, described in `A New Kind of Science` 
[@wolfram2002new], as implemented with `CellPyLib`:

```python
import cellpylib as cpl

cellular_automaton = cpl.init_simple(200)

cellular_automaton = cpl.evolve(cellular_automaton, timesteps=100, 
                                apply_rule=lambda n, c, t: cpl.nks_rule(n, 30))
```

First, the initial conditions are instantiated using the function `init_simple`, which, in this example, creates a 
200-dimensional vector consisting of zeroes, except for the component in the center of the vector, which is initialized
with a value of 1. Next, the system is subjected to evolution by calling the `evolve` function. The system evolves under 
the rule specified through the `apply_rule` parameter. Any function that accepts the three arguments `n`, `c` and `t` 
can be supplied as a rule, but in this case the built-in function `nks_rule` is invoked to provide Rule 30. The CA is 
evolved for 100 `timesteps`, or 100 applications of the rule to the initial and subsequent conditions.

During each timestep, the function supplied to `apply_rule` is invoked for each cell. The `n` argument refers to the 
neighbourhood of the current cell, and consists of an array (in the 1-dimensional CA case) of the activities (i.e. 
states) of the cells comprising the current cell's neighbourhood (an array with length 3, in the case of a 1-dimensional 
CA with radius of 1). The `c` argument refers to index of the cell under consideration. It serves as a label identifying 
the current cell. The `t` argument is an integer specifying the current timestep.

Finally, to visualize the results, the `plot` function can be utilized:

```python
cpl.plot(cellular_automaton)
```

![Rule 30, as rendered with CellPyLib.\label{fig:rule30}](rule30.png){ width=60% }

The result is rendered, as depicted in \autoref{fig:rule30}.

# References