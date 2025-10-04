from invoco.core.registry.base import Task
from invoco.core.registry.exceptions import (
    TaskAlreadyRegisteredError,
    TaskNotFoundError,
)


class TaskRegistry:
    """
    Central registry for Invoco tasks.

    Stores registered tasks and provides lookup and manifest generation.
    """

    def __init__(self: "TaskRegistry") -> None:
        self._tasks: dict[str, Task] = {}
        self._metadata: dict[str, dict[str, object]] = {}

    def register(
        self: "TaskRegistry", task: Task, metadata: dict[str, object] | None = None
    ) -> None:
        if task.name in self._tasks:
            raise TaskAlreadyRegisteredError(f"Task '{task.name}' already exists.")
        self._tasks[task.name] = task
        if metadata:
            self._metadata[task.name] = metadata

    def get(self: "TaskRegistry", name: str) -> Task:
        if name not in self._tasks:
            raise TaskNotFoundError(f"Task '{name}' not found.")
        task = self._tasks[name]
        if not getattr(task, "available", True):
            raise TaskNotFoundError(f"Task '{name}' is registered but disabled.")
        return task

    def list_tasks(
        self: "TaskRegistry", include_unavailable: bool = False
    ) -> dict[str, Task]:
        if include_unavailable:
            return dict(self._tasks)
        return {n: t for n, t in self._tasks.items() if getattr(t, "available", True)}

    def manifest(
        self: "TaskRegistry", include_unavailable: bool = False
    ) -> dict[str, dict[str, object]]:
        """
        Produce a manifest of tasks and their metadata.

        Returns:
            Mapping of task name -> metadata dict
        """
        manifest: dict[str, dict[str, object]] = {}
        for name, task in self._tasks.items():
            if not include_unavailable and not getattr(task, "available", True):
                continue
            base_info = {
                "name": task.name,
                "description": task.description,
                "available": task.available,
            }
            manifest[name] = {**base_info, **self._metadata.get(name, {})}
        return manifest


# Global instance
registry = TaskRegistry()
