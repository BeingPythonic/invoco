from abc import ABC, abstractmethod
from typing import Any, ClassVar


class Task(ABC):
    """
    Abstract base class for all Invoco tasks (tools).
    """

    name: str
    description: str
    available: bool = True

    # Optional metadata attached by @task_metadata
    _metadata: ClassVar[dict[str, object]] = {}

    @abstractmethod
    def run(self: "Task", payload: dict[str, Any]) -> object:
        """
        Execute the task with the provided payload.
        """
        ...
