.. _contents:

CellPyLib
=========

CellPyLib is a Python library for working with Cellular Automata (CA). It provides a concise and simple interface for
defining and analyzing 1- and 2-dimensional CA. The CA can consist of discrete or continuous states. Neighbourhood
radii are adjustable, and in the 2-dimensional case, both Moore and von Neumann neighbourhoods are supported.

With CellPyLib, it is trivial to create Elementary CA, and CA with totalistic rules. These rules are provided as part
of the library. Additionally, the library provides a means for creating asynchronous CA, and reversible CA. Finally, an
implementation of C. G. Langton's approach for creating CA rules using the lambda value is provided, allowing for the
exploration of complex systems, phase transitions and emergent computation.

Utility functions for plotting and viewing the evolved CA are provided. These tools make it easy to visualize the
results of CA evolution. Moreover, utility functions for computing the information-theoretic properties of CA, such as
the Shannon entropy and mutual information, are provided.

.. toctree::
  :caption: Using CellPyLib
  :maxdepth: 5

  installation
  working
  additional

.. toctree::
  :caption: Tutorials
  :maxdepth: 5

  eca
  neighbourhood
  colors
  complexity
  continuous
  totalistic
  twodim
  gol
  wireworld
  fredkin
  hopfield
  langtons_loop

.. toctree::
  :caption: API Docs and License
  :maxdepth: 5

  reference
  Source <https://github.com/lantunes/cellpylib>
  license

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`