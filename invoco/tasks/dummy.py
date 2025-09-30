"""Dummy task for testing."""

from invoco.core.base import Task
from invoco.core.decorators import log_task


class Dummy(Task):
    """A simple no-op task for testing."""

    @log_task
    def run(self, *args, **kwargs):
        return "Hello from Dummy task"
