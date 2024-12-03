import itertools
import functools
from collections import defaultdict, deque, Counter
import math
import re

def p1(f):
    lines = f.read().splitlines()
    safe = 0
    for line in lines:
        line = list(map(int, line.split()))
        diffs = [line[i+1] - line[i] for i in range(len(line) - 1)]
        if all(1 <= diff <= 3 for diff in diffs) or all(-3 <= diff <= -1 for diff in diffs):
            safe += 1
    
    return safe

def p2(f):
    lines = f.read().splitlines()
    safe = 0
    for line in lines:
        line = list(map(int, line.split()))
        diffs = [line[i+1] - line[i] for i in range(len(line) - 1)]
        if all(1 <= diff <= 3 for diff in diffs) or all(-3 <= diff <= -1 for diff in diffs):
            safe += 1
            continue

        for i in range(len(line)):
            temp = line[:i] + line[i+1:]
            diffs = [temp[i+1] - temp[i] for i in range(len(temp) - 1)]
            if all(1 <= diff <= 3 for diff in diffs) or all(-3 <= diff <= -1 for diff in diffs):
                safe += 1
                break
    
    return safe