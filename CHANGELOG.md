# Change Log
All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

## [2.2.1] - 2022-10-16
- Added this changelog
- Renamed the `callup` package `sasemp`
- Created `__main__.py` as the mainline, making `callup` just `python -m sasemp`

## [2.2.0] - 2022-09-11

- Issue #11: Added `--version` option
- Refactored unit tests to get test coverage to 100%
- Restored old `Perl` version, after extracting text files from `sasemp.db`

## [2.0.1] - 2022-09-11

The main purpose of this version was to improve test coverage.
It went from 88% to 100%.

### Fixed
- Issue #10: Need to find a unique employee name for unit testing
- Issue #9: Need to find a manager of only one employee for unit testing
- Issue #8: Search by userid does not set current employee

## [2.0.0] - 2022-08-30
Major refactoring.  Converted archtecture to
[Model-View-Controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller).

### Added
- `Controller` class and unit tests
- `Model` class and unit tests
- Unit tests for the static methods in `Employee`
- Unit tests for `help`
- Updated help text

## [1.0.2] - 2022-08-25

### Added
- Added context manager `stdout_redirected` to allow unit tests to trap output.
- Added context manager `stdin_redirected` to allow unit tests to provide sample input.

### Changed
Refactored code:
- Arranged methods in alphabetical order
- Added and cleaned up docstrings

### Fixed
- Issue #6: Added `readline` import so that uparrow can access history

## [1.0.0] - 2022-08-25

Major overall of original Perl version.  Now uses an [SQLite](https://sqlite.org/index.html)
database instead of text files.

[Unreleased]: https://github.com/philhanna/callup/compare/2.2.1..HEAD
[2.2.1]: https://github.com/philhanna/callup/compare/2.2.0..2.2.1
[2.2.0]: https://github.com/philhanna/callup/compare/2.0.1..2.2.0
[2.0.1]: https://github.com/philhanna/callup/compare/2.0.0..2.0.1
[2.0.0]: https://github.com/philhanna/callup/compare/1.0.2..2.0.0
[1.0.2]: https://github.com/philhanna/callup/compare/1.0.0..1.0.2
[1.0.0]: https://github.com/philhanna/callup/compare/3418d9..1.0.0
