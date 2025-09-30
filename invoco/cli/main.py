"""Thin CLI wrapper for Invoco."""

import argparse
import json

from invoco.core.scheduler import run_tasks


def main():
    parser = argparse.ArgumentParser(description="Run Invoco task lists (debug only)")
    parser.add_argument("file", help="Path to JSON file with tasks")
    args = parser.parse_args()

    with open(args.file) as f:
        task_list = json.load(f)["tasks"]

    for update in run_tasks(task_list):
        print(json.dumps(update, indent=2))


if __name__ == "__main__":
    main()
