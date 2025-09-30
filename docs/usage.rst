Usage Guide
===========

Basic Example
-------------

Run a list of tasks directly in Python:

.. code-block:: python

   from invoco.core.scheduler import run_tasks

   task_list = [{"name": "dummy", "args": {}}]
   for result in run_tasks(task_list):
       print(result)

Command-Line Interface
----------------------

For debugging, you can run tasks from a JSON file:

.. code-block:: bash

   invoco examples/sample_tasks.json

