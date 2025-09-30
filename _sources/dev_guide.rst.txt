Developer Guide
===============

Setting Up
----------

Clone the repo and create the environment:

.. code-block:: bash

   hatch env create

Common Tasks
------------

- **Run tests**: ``make test``
- **Lint code**: ``make lint``
- **Format code**: ``make format``
- **Type check**: ``make typecheck``
- **Build docs**: ``make docs``
- **Check coverage**: ``make coverage``

Tools Used
----------

- **Hatch** for builds and environments
- **Ruff** for linting
- **Black** for formatting
- **Mypy** for type checking
- **Pytest** for testing
- **Coverage.py** for coverage reports
- **Sphinx + Furo** for documentation

Coverage Reports
----------------

Generate a coverage report with:

.. code-block:: bash

   make coverage

This will run the test suite with coverage enabled and print a summary
to the terminal.


