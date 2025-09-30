"""Base task definitions for Invoco."""


class Task:
    """Base class for all Invoco tasks."""

    def run(self, *args, **kwargs):
        """Execute the task. Must be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement run()")
