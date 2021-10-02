# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added 

- Added more test coverage
- Added `CHANGELOG.md`
- Added docs and tests for `bits_to_int` and `int_to_bits` functions
- Added more documentation to functions in `entropy.py` and `bien.py`, and to `plot2d_slice` and `plot2d_spacetime` 

### Changed

- Addressing test warnings by making subtle adjustments to the code, such as using `np.int32` instead of `np.int`
- Replaced copyright notice in `README.md` with link to Apache License 2.0 

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
