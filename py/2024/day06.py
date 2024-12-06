# Day       Time  Rank  Score       Time  Rank  Score
#   6   00:16:59  2807      0   00:53:54  3546      0

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

def p1(f):
    grid = Grid(parse_grid(f.read()))
    pos = grid.find("^")[0]
    dir = UP

    visited = set()
    visited.add(pos)

    while grid.in_bounds(*pos):
        next_pos = tuple(padd(pos, dir))
        if grid.in_bounds(*next_pos): 
            if grid[next_pos] != "#":
                pos = next_pos
                visited.add(pos)
            else:
                dir = turn_right(dir)
        else: 
            break

    return len(visited)

def p2(f):
    grid = Grid(parse_grid(f.read()))

    def sim():
        pos = grid.find("^")[0]
        dir = UP

        visited = set()

        while grid.in_bounds(*pos):
            if (pos, dir) in visited:
                return True
            visited.add((pos, dir))
        
            next_pos = tuple(padd(pos, dir))
            if grid.in_bounds(*next_pos): 
                if grid[next_pos] != "#":
                    pos = next_pos
                else:
                    dir = tuple(turn_right(dir))
            else: 
                break
        
        return False

    ans = 0
    for x, y in grid.coords():
        if grid.grid[x][y] == ".":
            grid.grid[x][y] = "#"
            if sim():
                ans += 1
            grid.grid[x][y] = "."

    return ans