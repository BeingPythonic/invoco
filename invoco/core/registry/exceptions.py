class RegistryError(Exception):
    """Base exception for all registry-related errors."""


class TaskNotFoundError(RegistryError):
    """Raised when a requested task is not found or unavailable."""


class TaskAlreadyRegisteredError(RegistryError):
    """Raised when attempting to register a duplicate task name."""
