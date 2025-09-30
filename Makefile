# --- Project Setup ---
.PHONY: install clean dist

install:
	hatch env create

clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache dist build *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +

dist:
	hatch build


# --- Quality Checks ---
.PHONY: lint format typecheck

lint:
	hatch run lint

format:
	hatch run format

typecheck:
	hatch run typecheck


# --- Testing ---
.PHONY: test coverage

test:
	hatch run test

coverage:
	hatch run pytest --cov=invoco --cov-report=term-missing


# --- Docs ---
.PHONY: docs docs-serve

docs:
	hatch run docs

docs-serve:
	python -m http.server --directory docs/_build/html 8000
