from collections.abc import Callable
from functools import wraps
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def log_task(func: Callable[P, R]) -> Callable[P, R]:
    """Decorator to log before and after a task runs."""

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"[START] {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[END] {func.__name__}")
        return result

    return wrapper
