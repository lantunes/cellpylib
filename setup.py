from setuptools import setup

setup(name="cellpylib",
      version="0.2.0",
      description="CellPyLib, A library for working with Cellular Automata, for Python.",
      long_description="CellPyLib is a library for working with Cellular Automata, for Python. "
                       "Currently, only 1- and 2-dimensional k-color cellular automata with "
                       "periodic boundary conditions are supported. The size of the "
                       "neighbourhood can be adjusted. ",
      license="Apache License 2.0",
      classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Topic :: Scientific/Engineering :: Artificial Intelligence',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python :: 3.6',
      ],
      url='http://github.com/lantunes/cellpylib',
      author="Luis M. Antunes",
      author_email="lantunes@gmail.com",
      packages=["cellpylib"],
      keywords=["cellular automata", "complexity", "complex systems", "computation", "non-linear dynamics"],
      python_requires='>3.6',
      install_requires=["numpy >= 1.15.4", "matplotlib >= 3.0.2"])
