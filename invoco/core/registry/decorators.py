from typing import Callable, TypeVar

from invoco.core.registry.base import Task
from invoco.core.registry.registry import registry

T = TypeVar("T", bound=type[Task])


def task_metadata(**metadata: object) -> Callable[[T], T]:
    """
    Attach metadata (schema, version, tags, etc.) to a Task class.

    Example:
        @task_metadata(schema=..., version="1.0", tags=["utility"])
        @register_task
        class EchoTask(Task): ...
    """

    def wrapper(cls: T) -> T:
        cls._metadata = metadata  # attach metadata at class level
        return cls

    return wrapper


def register_task(cls: T) -> T:
    """
    Register a Task automatically in the global registry.

    Example:
        @task_metadata(schema=..., version="1.0")
        @register_task
        class EchoTask(Task):
            ...
    """
    instance = cls()
    # Pick up metadata if it was set by @task_metadata
    metadata = getattr(cls, "_metadata", None)
    registry.register(instance, metadata)
    return cls
