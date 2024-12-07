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

def tilt(grid):
    grid = copy.deepcopy(grid)
    for c in range(grid.cols):
        lo = 0
        for r in range(grid.rows):
            char = grid[r, c]
            if char == "#":
                lo = r + 1
            if char == "O":
                grid.grid[r][c] = "."
                grid.grid[lo][c] = "O"
                lo += 1
    return grid

def p1(f):
    grid = Grid(parse_grid(f.read()))
    grid = tilt(grid)
    
    ans = 0
    for r, c in grid.coords():
        if grid[r, c] == "O":
            ans += grid.rows - r
    
    return ans

    # ans = 0
    # for col in grid.get_cols():
    #     rocks = [0] + [i + 1 for i, c in enumerate(col) if c == "#"] + [grid.rows]
    #     for lo, hi in itertools.pairwise(rocks):
    #         ans += sum(range(grid.rows - lo - col[lo:hi].count("O") + 1, grid.rows - lo + 1))

    # return ans

def p2(f):
    def generator():
        grid = Grid(parse_grid(f.read()))
        while True:
            for _ in range(4): 
                grid = tilt(grid) 
                grid = grid.rotate_right()
            yield grid

    seq = RepeatingSequence(generator(), lambda x: make_hashable(x.grid))
    grid = seq[1000000000 - 1]

    ans = 0
    for r, c in grid.coords():
        if grid[r, c] == "O":
            ans += grid.rows - r

    return ans