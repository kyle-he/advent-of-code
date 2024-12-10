# Day       Time   Rank  Score       Time   Rank  Score
#  10   00:08:30    789      0   00:10:20    610      0

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
    grid = Grid(parse_grid(f.read(), int))
    heads = grid.find(0)
    ans = 0
    for head in heads:
        queue = deque([head])
        visited = set([head])
        while queue:
            node = queue.popleft()
            curr = grid[node]
            if curr == 9:
                ans += 1
                continue
            for delta in GRID_DELTA:
                neighbor = tuple(padd(node, delta))
                if grid[neighbor] == curr + 1 and neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
    return ans

def p2(f):
    grid = Grid(parse_grid(f.read(), int))
    heads = grid.find(0)
    ans = 0
    for head in heads:
        queue = deque([head])
        while queue:
            node = queue.popleft()
            curr = grid[node]
            if curr == 9:
                ans += 1
                continue
            for delta in GRID_DELTA:
                neighbor = tuple(padd(node, delta))
                if grid[neighbor] == curr + 1:
                    queue.append(neighbor)
    return ans