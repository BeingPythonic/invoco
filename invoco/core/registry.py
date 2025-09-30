from typing import Any

TASK_REGISTRY: dict[str, type[Any]] = {}


def register_task(name: str, cls: type[Any]) -> None:
    """Register a task class in the global registry."""
    TASK_REGISTRY[name] = cls


def get_task(name: str) -> type[Any] | None:
    """Retrieve a task class by name."""
    return TASK_REGISTRY.get(name)
