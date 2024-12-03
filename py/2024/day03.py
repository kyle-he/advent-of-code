import itertools
import functools
from collections import defaultdict, deque, Counter
import math
import re

def p1(f):
    lines = f.read()
    regex = "mul\((\d+),(\d+)\)"
    return sum(int(x) * int(y) for x, y in re.findall(regex, lines))

def p2(f):
    lines = f.read()
    regex = re.compile(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)")

    total = 0
    enabled = True
    for match in regex.finditer(lines):
        if match.group(0) == "do()":
            enabled = True
        elif match.group(0) == "don't()":
            enabled = False
        else:
            if enabled:
                x, y = int(match.group(1)), int(match.group(2))
                total += x * y

    return total
