from typing import NoReturn


class Task:
    """Base class for all Invoco tasks."""

    def run(self, *args: object, **kwargs: object) -> NoReturn:
        """Execute the task. Must be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement run()")
