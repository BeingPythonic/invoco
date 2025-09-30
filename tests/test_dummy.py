from invoco.tasks.dummy import Dummy


def test_dummy_task_runs():
    task = Dummy()
    output = task.run()
    assert output == "Hello from Dummy task"
