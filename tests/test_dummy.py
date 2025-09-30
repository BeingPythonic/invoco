from invoco.tasks.dummy import DummyTask


def test_dummy_task_runs() -> None:
    task = DummyTask()
    output = task.run()
    assert output == "Hello from Dummy task"
