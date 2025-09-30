from collections.abc import Generator
from typing import Any


def run_tasks(task_list: list[dict[str, Any]]) -> Generator[dict[str, Any], None, None]:
    """Stub scheduler that yields structured task execution results."""
    for task in task_list:
        yield {
            "task": task["name"],
            "args": task["args"],
            "status": "done",  # required by tests
            "result": f"Executed {task['name']} with args {task['args']}",
        }
