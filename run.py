import argparse
import os.path
import time
import traceback
from datetime import datetime, timedelta, timezone
from importlib import import_module, reload

# run.py taken from https://github.com/oliver-ni/advent-of-code/tree/master

def run(func, filename="filename"):
    try:
        with open(filename) as f:
            try:
                start = time.monotonic_ns()
                print(func(f), end="\t")
                end = time.monotonic_ns()
                print(f"[{(end-start) / 10**6:.3f} ms]")
            except:
                traceback.print_exc()
    except FileNotFoundError:
        print()


if __name__ == "__main__":
    now = datetime.now(timezone(timedelta(hours=-5)))
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions.")
    parser.add_argument("--year", "-y", type=int, help="The year to run.", default=now.year)
    parser.add_argument("--day", "-d", type=int, help="The day to run.", default=now.day)
    parser.add_argument("--test", "-t", help="Run the test cases.", action="store_true")
    parser.add_argument("--extra", "-e", help="Choose a different solution to run.")
    args = parser.parse_args()

    input_paths = {
        "sample": f"input/{args.year}/day{args.day:02}_sample.txt",
        "input": f"input/{args.year}/day{args.day:02}.txt",
    }

    if not os.path.exists(input_paths["input"]):
        print("loading input from aocd")
        try:
            from aocd import AocdError, get_data
        except ImportError:
            pass
        else:
            try:
                data = get_data(day=args.day, year=args.year)
            except AocdError as e:
                print(e)
            else:
                with open(input_paths["input"], "w") as f:
                    f.write(data)

    module_name = f"py.{args.year}.day{args.day:02}"
    if args.extra:
        module_name += f"_{args.extra}"

    print(f"{module_name}")

    module = import_module(module_name)

    for i in ("p1", "p2"):
        if not hasattr(module, i):
            continue
        print(f"--- {i} ---")
        print("sample:", end="\t")
        run(getattr(module, i), f"input/{args.year}/day{args.day:02}_sample.txt")
        reload(module)

        if not args.test:
            print("input:", end="\t")
            run(getattr(module, i), f"input/{args.year}/day{args.day:02}.txt")