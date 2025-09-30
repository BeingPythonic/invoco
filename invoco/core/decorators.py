"""Decorators for Invoco tasks."""

from functools import wraps


def log_task(func):
    """Decorator to log before and after a task runs."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[START] {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[END] {func.__name__}")
        return result

    return wrapper
