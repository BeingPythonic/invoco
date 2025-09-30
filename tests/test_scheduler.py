from invoco.core.scheduler import run_tasks


def test_scheduler_runs_task_list():
    task_list = [{"name": "dummy", "args": {}}]
    results = list(run_tasks(task_list))
    assert results, "Scheduler should yield results"
    assert results[0]["task"] == "dummy"
    assert results[0]["status"] == "done"
