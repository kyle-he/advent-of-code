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
    field = defaultdict(set)

    stack = [((0, -1), RIGHT)]
    while stack:
        pos, dir = map(tuple, stack.pop())
        if dir in field[pos]:
            continue
        field[pos].add(dir)

        next_pos = tuple(padd(pos, dir))
        if grid.in_bounds(*next_pos):
            match grid[next_pos]:
                case "/":
                    if dir in (UP, DOWN):
                        stack.append((next_pos, turn_right(dir)))
                    else:
                        stack.append((next_pos, turn_left(dir)))
                case "\\":
                    if dir in (UP, DOWN):
                        stack.append((next_pos, turn_left(dir)))
                    else:
                        stack.append((next_pos, turn_right(dir)))
                case "|":
                    if dir in (UP, DOWN):
                        stack.append((next_pos, dir))
                    else:
                        stack.append((next_pos, UP))
                        stack.append((next_pos, DOWN))
                case "-":
                    if dir in (RIGHT, LEFT):
                        stack.append((next_pos, dir))
                    else:
                        stack.append((next_pos, RIGHT))
                        stack.append((next_pos, LEFT))
                case _:
                    stack.append((next_pos, dir))
    
    return len(field) - 1


def p2(f):
    grid = Grid(parse_grid(f.read()))

    starts = [((r, -1), RIGHT) for r in range(grid.rows)] + [((-1, c), DOWN) for c in range(grid.cols)] + [((grid.rows, c), UP) for c in range(grid.cols)] + [((r, grid.cols), LEFT) for r in range(grid.rows)]
    ans = 0
    for start in starts:
        field = defaultdict(set)
        stack = [start]
        while stack:
            pos, dir = map(tuple, stack.pop())
            if dir in field[pos]:
                continue
            field[pos].add(dir)

            next_pos = tuple(padd(pos, dir))
            if grid.in_bounds(*next_pos):
                match grid[next_pos]:
                    case "/":
                        if dir in (UP, DOWN):
                            stack.append((next_pos, turn_right(dir)))
                        else:
                            stack.append((next_pos, turn_left(dir)))
                    case "\\":
                        if dir in (UP, DOWN):
                            stack.append((next_pos, turn_left(dir)))
                        else:
                            stack.append((next_pos, turn_right(dir)))
                    case "|":
                        if dir in (UP, DOWN):
                            stack.append((next_pos, dir))
                        else:
                            stack.append((next_pos, UP))
                            stack.append((next_pos, DOWN))
                    case "-":
                        if dir in (RIGHT, LEFT):
                            stack.append((next_pos, dir))
                        else:
                            stack.append((next_pos, RIGHT))
                            stack.append((next_pos, LEFT))
                    case _:
                        stack.append((next_pos, dir))
    
        ans = max(ans, len(field) - 1)
    
    return ans