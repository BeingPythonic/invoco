"""
Discovery utilities for auto-loading tasks from entry points or modules.
"""

import importlib.metadata


def discover_tasks(group: str = "invoco.tasks") -> None:
    """
    Discover and load tasks from entry points.

    Args:
        group: Entry point group name (default: "invoco.tasks").
    """
    for entry_point in importlib.metadata.entry_points().get(group, []):
        task_cls = entry_point.load()
        task_cls()  # registration happens via decorator
