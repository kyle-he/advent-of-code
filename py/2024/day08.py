# Day       Time   Rank  Score       Time   Rank  Score
#   8   04:31:18  17488      0   04:36:13  15586      0

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
    grid = Grid(parse_grid(f.read()))
    att = defaultdict(list)
    for x, y in grid.coords():
        if grid[x, y] != ".":
            att[grid[x, y]].append((x, y))

    antis = set()
    for a in att.values():
        for a, b in itertools.permutations(a, 2):
            anti = tuple(psub(b, psub(a, b)))
            if anti in grid:
                antis.add(anti)
    
    return len(antis)

def p2(f):
    grid = Grid(parse_grid(f.read()))
    att = defaultdict(list)
    for x, y in grid.coords():
        if grid[x, y] != ".":
            att[grid[x, y]].append((x, y))

    antis = set()
    for a in att.values():
        for a, b in itertools.permutations(a, 2):
            for i in itertools.count():
                anti = tuple(psub(b, pmul(i, psub(a, b))))
                if anti in grid:
                    antis.add(anti)
                else:
                    break
        
    return len(antis)