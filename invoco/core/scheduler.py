"""Task scheduling and execution for Invoco."""


def run_tasks(task_list):
    """Stub scheduler that yields fake results.

    Args:
        task_list (list[dict]): list of tasks with 'name' and 'args'.

    Yields:
        dict: status updates for each task.
    """
    for task in task_list:
        yield {"task": task["name"], "status": "done", "output": None}
