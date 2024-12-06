# Day       Time  Rank  Score       Time  Rank  Score
#   4   00:01:09    68     33   00:40:12  4972      0

import itertools
import functools
from collections import defaultdict, deque, Counter
import math
import re

from common.list import *
from common.grid import *
from common.utils import *
from common.algos import *
from common.dict import *
from common.input import *

def p1(f):
    grid = Grid(parse_grid(f.read()))
    word = "XMAS"
    
    total = 0
    for x, y in grid.coords():
        for dx, dy in OCT_DELTA:
            if all(grid[x + i * dx, y + i * dy] == c for i, c in enumerate(word)):
                total += 1

    return total

def p2(f):
    grid = Grid(parse_grid(f.read()))
    word = "MAS"

    total = 0

    for x, y in grid.coords():
        corners = DIAG_DELTA
        corners = lmap(lambda d: (x + d[0], y + d[1]), corners)
        corners = lmap(grid.get, corners)

        if grid[x, y] == "A":
            if str_rep(corners[0:2]) in ("MS", "SM") and str_rep(corners[2:4]) in ("MS", "SM"):
                total += 1

    return total