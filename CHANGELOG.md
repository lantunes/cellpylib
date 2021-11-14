# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## Added

- Added more Sandpile demos and more content to the Sandpile tutorial in the docs

## Changed

- Changed interpretation of the `cellular_automaton` argument in `evolve` and `evolve2d` such that a history of states can be provided

## [2.0.0] - 2021-11-10

### Added 

- Added more test coverage
- Added `CHANGELOG.md`
- Added docs and tests for `bits_to_int` and `int_to_bits` functions
- Added more documentation to functions in `entropy.py` and `bien.py`, and to `plot2d_slice` and `plot2d_spacetime`
- Added the `BaseRule` class, which provides a base for custom callable rules
- Added built-in `Sandpile` implementation
- Added `show=True` argument to plotting function signatures
- Added `show_grid`, `show_margin` and `scale` arguments to `plot2d` and `plot2d_slice` functions

### Changed

- Addressing test warnings by making subtle adjustments to the code, such as using `np.int32` instead of `np.int`
- Replaced copyright notice in `README.md` with link to Apache License 2.0
- Importing modules explicitly in `__init__.py` to avoid polluting namespace
- Changed `AsynchronousRule`, `ReversibleRule`, and `CTRBLRule` so that they extend `BaseRule` and implement `__call__`
- Changed plotting function signatures so that they accept `imshow` keyword args
- Changed the `evolve` and `evolve2d` functions so that the `timesteps` parameter can alternatively be a callable,
  so that models where the number of timesteps is not known in advance are supported

## [1.1.0] - 2021-08-02

### Added

- Added support for CTRBL rules
- Added Langton's Loop implementation
- Added Wireworld demo code
- Added more optional arguments to `plot2d_animate` function signature

## [1.0.0] - 2021-07-29

### Added

- Initial stable release
- Added more documentation to code
