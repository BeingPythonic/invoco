import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Invoco task lists (debug only)")
    parser.add_argument("file", help="Path to JSON file with tasks")
    args = parser.parse_args()
    print(f"Would run tasks from: {args.file}")
