# Invoco

[![Tests](https://github.com/beingpythonic/invoco/actions/workflows/tests.yml/badge.svg)](https://github.com/beingpythonic/invoco/actions/workflows/tests.yml)
[![Docs](https://github.com/beingpythonic/invoco/actions/workflows/docs.yml/badge.svg)](https://beingpythonic.github.io/invoco/)
[![Coverage](https://codecov.io/gh/beingpythonic/invoco/branch/main/graph/badge.svg)](https://codecov.io/gh/beingpythonic/invoco)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/invoco)](https://pypi.org/project/invoco/)
[![License](https://img.shields.io/github/license/beingpythonic/invoco?cacheBust=1)](LICENSE)

**Invoco** is a Python project focused on executing structured task calls.  
It is intended to serve as a bridge between AI-driven agents and local execution environments.

The project is in its early stages. Current code consists of stubs and scaffolding, with full functionality under active development.

---

## Project Goals

Invoco is being developed to provide:

- **Task abstraction**: reusable task definitions with clear input/output schemas.  
- **Task registry**: dynamic discovery and safe execution of tools.  
- **Execution control**: timeouts, error handling, retries, and logging.  
- **CLI interface**: run JSON/YAML task definitions for local debugging.  
- **Integration options**: usable as a Python library, command-line tool, or lightweight service.  
- **Safety features**: permission controls and sandboxing to prevent misuse.  

---

## Installation

PyPI release will be available once core features are stable.

For development:

```bash
git clone git@github.com:beingpythonic/invoco.git
cd invoco
hatch env create
make test
```

---

## Example (Early Prototype)

```python
from invoco.core.scheduler import run_tasks

task_list = [
    {"name": "dummy", "args": {}}
]

for result in run_tasks(task_list):
    print(result)
```

Command-line usage (stub):

```bash
invoco examples/sample_tasks.json
```

---

## Documentation

Documentation (in progress) is published at:  
[https://beingpythonic.github.io/invoco/](https://beingpythonic.github.io/invoco/)

---

## Contributing

Contributions are welcome. Please see the [Developer Guide](https://beingpythonic.github.io/invoco/dev_guide.html) for details.  

Common development commands:

```bash
make test
make lint
make typecheck
make docs
```

---

## License

MIT License © 2025 Christopher Bailey

