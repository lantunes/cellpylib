from setuptools import setup
import re

INIT_FILE = "cellpylib/__init__.py"

with open(INIT_FILE) as fid:
    file_contents = fid.read()
    match = re.search(r"^__version__\s?=\s?['\"]([^'\"]*)['\"]", file_contents, re.M)
    if match:
        version = match.group(1)
    else:
        raise RuntimeError("Unable to find version string in %s" % INIT_FILE)

setup(name="cellpylib",
      version=version,
      description="CellPyLib, A library for working with Cellular Automata, for Python.",
      long_description="CellPyLib is a library for working with Cellular Automata, for Python. "
                       "Currently, only 1- and 2-dimensional k-color cellular automata with "
                       "periodic boundary conditions are supported. The size of the "
                       "neighbourhood can be adjusted. ",
      license="Apache License 2.0",
      classifiers=[
            'Development Status :: 5 - Production/Stable',
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
