from collections.abc import Generator
from typing import Any


def run_tasks(task_list: list[dict[str, Any]]) -> Generator[str, None, None]:
    """Stub scheduler that yields fake results."""
    for task in task_list:
        yield f"Executed {task['name']} with args {task['args']}"
