from invoco.core.registry.base import Task
from invoco.core.registry.decorators import register_task, task_metadata


@task_metadata(
    schema={
        "type": "object",
        "properties": {"text": {"type": "string"}},
        "required": ["text"],
    },
    version="1.0",
    tags=["utility", "demo"],
)
@register_task
class EchoTask(Task):
    """Echoes back the text provided in the payload."""

    name = "echo"
    description = "Echo back input text."
    available = True

    def run(self: "EchoTask", payload: dict) -> str:
        return payload.get("text", "")
