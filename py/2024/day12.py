# Day       Time   Rank  Score       Time   Rank  Score
#  12   00:08:29    546      0   01:33:32   3340      0

import itertools
import functools
from collections import defaultdict, deque, Counter
import math
import re

from common.parse import *
from common.list import *
from common.utils import *
from common.grid import *

def p1(f):
    grid = Grid(parse_grid(f.read()))
    total_cost = 0
    visited = set()

    def bfs(plant, grid, start):
        queue = deque([start])
        blob = set()
        perim = list()

        while queue:
            node = queue.popleft()
            if node in blob:
                continue
            blob.add(node)

            for delta in GRID_DELTA:
                neighbor = tuple(padd(node, delta))
                if grid[neighbor] != plant:
                    perim.append(neighbor)
                elif neighbor not in blob:
                    queue.append(neighbor)
        
        nonlocal visited
        visited.update(blob)

        return len(blob), len(perim)

    for node in grid.coords():
        node = tuple(node)
        if node not in visited:
            a, b = bfs(grid[node], grid, node)
            total_cost += a * b

    return total_cost

def p2(f):
    grid = Grid(parse_grid(f.read()))
    total_cost = 0
    visited = set()

    def bfs(plant, grid, start):
        queue = deque([start])
        blob = set()
        perim = defaultdict(set)

        while queue:
            node = queue.popleft()
            if node in blob:
                continue
            blob.add(node)

            for delta in GRID_DELTA:
                delta = tuple(delta)
                neighbor = tuple(padd(node, delta))
                if grid[neighbor] != plant:
                    perim[delta].add(neighbor)
                elif neighbor not in blob:
                    queue.append(neighbor)
        
        nonlocal visited
        visited.update(blob)

        sides = 0
        HORI = (RIGHT, LEFT)
        VERT = (UP, DOWN)
        for delta, merge in [(UP, HORI), (DOWN, HORI), (LEFT, VERT), (RIGHT, VERT)]:
            uf = UnionFind()
            for node in perim[delta]:
                uf.find(tuple(node))

            for node in perim[delta]:
                a = tuple(padd(node, merge[0]))
                b = tuple(padd(node, merge[1]))

                if a in perim[delta]:
                    uf.union(node, a)
                
                if b in perim[delta]:
                    uf.union(node, b)
            
            sides += uf.num_sets()

        return len(blob), sides

    for node in grid.coords():
        node = tuple(node)
        if node not in visited:
            a, b = bfs(grid[node], grid, node)
            total_cost += a * b

    return total_cost
