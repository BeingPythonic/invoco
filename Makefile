# --- Project Setup ---
.PHONY: install clean dist

install:
	hatch env create

clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache dist build *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +

dist:
	hatch build


# --- Quality Checks (dev env) ---
.PHONY: lint format typecheck check

lint:
	hatch run dev:lint

format:
	hatch run dev:format

typecheck:
	hatch run dev:typecheck

# Run all quality checks together
check: lint format typecheck


# --- Testing (test env) ---
.PHONY: test coverage

test:
	hatch run test:pytest

coverage:
	hatch run test:pytest --cov=invoco --cov-report=term-missing


# --- Docs (docs env) ---
.PHONY: docs docs-serve docs-clean

docs:
	hatch run docs:sphinx-build docs docs/_build/html

# Serve docs locally at http://localhost:8000
docs-serve:
	python -m http.server --directory docs/_build/html 8000

# Clean built docs
docs-clean:
	rm -rf docs/_build


# --- CI Pipeline ---
.PHONY: ci

# CI: clean build, run tests, build docs
ci: clean test docs
