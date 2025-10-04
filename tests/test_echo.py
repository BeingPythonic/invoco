from invoco.core.registry.registry import registry


def test_echo_task_runs() -> None:
    from invoco.tasks.echo import EchoTask  # import inside test

    task = EchoTask()
    output = task.run({"text": "hello"})
    assert output == "hello"


def test_echo_task_registered() -> None:
    from invoco.tasks import echo  # import module after reload

    task = registry.get("echo")
    assert isinstance(task, echo.EchoTask)
    assert task.run({"text": "world"}) == "world"


def test_echo_task_missing_text() -> None:
    from invoco.tasks.echo import EchoTask

    task = EchoTask()
    output = task.run({})
    assert output == ""
