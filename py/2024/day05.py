# Day       Time  Rank  Score       Time  Rank  Score
#   5   00:01:33    75     26   00:03:32    90     11

import itertools
import functools
from collections import defaultdict, deque, Counter
import math
import re

def p1(f):
    rules, updates = map(str.splitlines, f.read().strip().split("\n\n"))

    rules = [list(map(int, a.split('|'))) for a in rules]
    updates = [list(map(int, a.split(','))) for a in updates]

    ans = 0
    for update in updates:
        if any(x in update and y in update and update.index(x) > update.index(y) for x, y in rules):
            continue
        ans += update[len(update) // 2]
    
    return ans

from graphlib import TopologicalSorter

def p2(f):
    rules, updates = map(str.splitlines, f.read().strip().split("\n\n"))

    rules = [list(map(int, a.split('|'))) for a in rules]
    updates = [list(map(int, a.split(','))) for a in updates]

    ans = 0
    for update in updates:
        if not any(x in update and y in update and update.index(x) > update.index(y) for x, y in rules):
            continue

        graph = defaultdict(list)
        for x, y in rules:
            if x in update and y in update:
                graph[x].append(y)
        ts = TopologicalSorter(graph)
        r = list(ts.static_order())

        s = sorted(update, key=lambda node: r.index(node))
        ans += s[len(s) // 2]

    return ans
