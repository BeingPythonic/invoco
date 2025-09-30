class Task:
    """Base class for all Invoco tasks."""

    def run(self: "Task", *args: object, **kwargs: object) -> None:
        """Execute the task. Must be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement run()")
