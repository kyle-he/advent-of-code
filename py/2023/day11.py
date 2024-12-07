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
    galaxies = grid.find("#")

    rows = set(range(grid.rows))
    cols = set(range(grid.cols))
    for r, c in galaxies:
        cols.discard(c)
        rows.discard(r)
    
    ans = 0
    for a, b in itertools.combinations(galaxies, 2):
        r1, c1 = a
        r2, c2 = b
        ans += pdist1(a, b) + len(rows & set(range(*min_max([r1, r2])))) + len(cols & set(range(*min_max([c1, c2]))))
        
    return ans

    # too slow

    # def expand(node):
    #     for v in GRID_DELTA:
    #         cost = 1
    #         neighbor = tuple(padd(node, v))
    #         r, c = neighbor
    #         if tuple(v) in (UP, DOWN):
    #             if r in rows:
    #                 cost = 2
    #         else:
    #             if c in cols:
    #                 cost = 2
                
    #         if grid.in_bounds(*neighbor):
    #             yield cost, neighbor
    
    # ans = 0
    # for a, b in itertools.combinations(galaxies, 2):
    #     costs, _ = dijkstra(a, expand, b, lambda node: pdist1(node, b))
    #     ans += costs[b]
    
    # return ans

def p2(f):
    grid = Grid(parse_grid(f.read()))
    galaxies = grid.find("#")

    rows = set(range(grid.rows))
    cols = set(range(grid.cols))
    for r, c in galaxies:
        cols.discard(c)
        rows.discard(r)
    
    ans = 0
    for a, b in itertools.combinations(galaxies, 2):
        r1, c1 = a
        r2, c2 = b
        ans += pdist1(a, b) + 999999 * len(rows & set(range(*min_max([r1, r2])))) + 999999 * len(cols & set(range(*min_max([c1, c2]))))
        
    return ans