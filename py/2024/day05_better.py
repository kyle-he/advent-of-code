import itertools
import functools
from collections import defaultdict, deque, Counter
import math
import re

from common.parse import *
from common.list import *
from common.utils import *
from common.grid import *
from common.algos import *

def p1(f):
    rules, updates = map(split_lines, split_blocks(f.read()))

    rules = [lmap(int, a.split('|')) for a in rules]
    updates = [lmap(int, a.split(',')) for a in updates]

    ans = 0
    for update in updates:
        if any(x in update and y in update and update.index(x) > update.index(y) for x, y in rules):
            continue
        ans += update[len(update) // 2]
    
    return ans

def p2(f):
    rules, updates = map(split_lines, split_blocks(f.read()))

    rules = [lmap(int, a.split('|')) for a in rules]
    updates = [lmap(int, a.split(',')) for a in updates]

    graph = {}
    for x, y in rules:
        graph.setdefault(x, []).append(y)

    ans = 0
    for update in updates:
        if not any(x in update and y in update and update.index(x) > update.index(y) for x, y in rules):
            continue

        s = sorted(update, key=functools.cmp_to_key(lambda x, y: -1 if x in graph and y in graph[x] else 0))
        ans += s[len(s) // 2]

    return ans