from invoco.core.decorators import log_task


class DummyTask:
    """A simple demo task."""

    @log_task
    def run(self: "DummyTask", *args: object, **kwargs: object) -> str:
        return "Hello from Dummy task"
