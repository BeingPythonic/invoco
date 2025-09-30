# 📦 Invoco

[![Tests](https://github.com/beingpythonic/invoco/actions/workflows/tests.yml/badge.svg)](https://github.com/beingpythonic/invoco/actions/workflows/tests.yml)  
[![Docs](https://github.com/beingpythonic/invoco/actions/workflows/docs.yml/badge.svg)](https://beingpythonic.github.io/invoco/)
[![Coverage](https://codecov.io/gh/beingpythonic/invoco/branch/main/graph/badge.svg)](https://codecov.io/gh/beingpythonic/invoco)  
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/invoco)](https://pypi.org/project/invoco/)  
[![License](https://img.shields.io/github/license/beingpythonic/invoco)](LICENSE)  

**Invoco** is a Python library for executing structured task calls, designed for AI-driven agents and orchestration systems.  

---

## ✨ Features (Planned & In Progress)

- 🧩 **Task abstraction** — define reusable `Task` classes.  
- 📜 **Scheduler** — run a sequence of tasks with progress reporting.  
- 🔌 **Task registry** — register and look up tasks dynamically.  
- 🎛 **Decorators** — add logging, retries, or metrics to tasks.  
- 🧪 **Thin CLI** — run task lists from JSON/YAML for debugging.  
- 📚 **Documentation** — built with Sphinx + Furo, auto-published.  
- 🔄 **CI/CD** — GitHub Actions with lint, typecheck, tests, coverage, and docs.  

*(Right now: skeleton and stubs are in place. The real features are being built step by step.)*

---

## 🚀 Quick Start

Install (after release on PyPI):

```bash
pip install invoco
```

For now, clone locally:

```bash
git clone git@github.com:beingpythonic/invoco.git
cd invoco
hatch env create
make test
```

---

## 🛠 Usage Example

```python
from invoco.core.scheduler import run_tasks

task_list = [
    {"name": "dummy", "args": {}}
]

for result in run_tasks(task_list):
    print(result)
```

CLI debugging:

```bash
invoco examples/sample_tasks.json
```

---

## 📖 Documentation

Full docs are published here:  
👉 [Invoco Documentation](https://beingpythonic.github.io/invoco/)

---

## 🤝 Contributing

Want to help? Check out the [Developer Guide](https://beingpythonic.github.io/invoco/dev_guide.html).  

- Run tests: `make test`  
- Lint: `make lint`  
- Typecheck: `make typecheck`  
- Build docs: `make docs`

---

## 📜 License

MIT License © 2025 Christopher Bailey  
