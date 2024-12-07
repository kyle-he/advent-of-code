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

def find_reflection(grid):  
    for lo, hi in itertools.pairwise(range(grid.cols)):
        errs = 0
        while (0, lo) in grid and (0, hi) in grid:
            if grid.get_cols()[lo] != grid.get_cols()[hi]:
                errs += 1
                break
            lo -= 1
            hi += 1
        
        if errs == 0:
            return (lo + hi) // 2 + 1
    
    return 0

def p1(f):
    blocks = parse_blocks(f.read())
    ans = 0
    for block in blocks:
        grid = Grid(parse_grid(block)) 
        ans += find_reflection(grid)

        grid = grid.transpose()
        ans += 100 * find_reflection(grid)
    
    return ans

def find_reflection2(grid):  
    for lo, hi in itertools.pairwise(range(grid.cols)):
        errs = 0
        while (0, lo) in grid and (0, hi) in grid:
            errs += len(set(enumerate(grid.get_cols()[lo])) - set(enumerate(grid.get_cols()[hi])))
            lo -= 1
            hi += 1
        
        if errs == 1:
            return (lo + hi) // 2 + 1
    
    return 0

def p2(f):
    blocks = parse_blocks(f.read())
    ans = 0
    for block in blocks:
        grid = Grid(parse_grid(block)) 
        ans += find_reflection2(grid)

        grid = grid.transpose()
        ans += 100 * find_reflection2(grid)
    
    return ans