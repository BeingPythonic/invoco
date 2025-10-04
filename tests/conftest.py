import importlib
import pkgutil
import sys
from collections.abc import Generator

import pytest

import invoco.tasks
from invoco.core.registry.registry import registry


def _reload_all_tasks() -> None:
    """Force reload of all modules under invoco.tasks so decorators run again."""
    for _, module_name, _ in pkgutil.iter_modules(invoco.tasks.__path__):
        full_name = f"invoco.tasks.{module_name}"
        if full_name in sys.modules:
            importlib.reload(sys.modules[full_name])
        else:
            importlib.import_module(full_name)


@pytest.fixture(autouse=True)
def reset_registry() -> Generator[None, None, None]:
    registry._tasks.clear()
    registry._metadata.clear()

    _reload_all_tasks()  # ensure tasks like EchoTask re-register

    yield

    registry._tasks.clear()
    registry._metadata.clear()
