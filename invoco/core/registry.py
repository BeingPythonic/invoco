"""Task registry for Invoco."""

TASK_REGISTRY = {}


def register_task(name, cls):
    """Register a task class in the global registry."""
    TASK_REGISTRY[name] = cls


def get_task(name):
    """Retrieve a task class by name."""
    return TASK_REGISTRY.get(name)
