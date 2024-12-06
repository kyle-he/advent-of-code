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

part = defaultdict(list, {
    "S": (UP, DOWN, LEFT, RIGHT),
    "-": (LEFT, RIGHT),
    "|": (UP, DOWN),
    "F": (DOWN, RIGHT),
    "7": (DOWN, LEFT),
    "L": (UP, RIGHT),
    "J": (UP, LEFT)
})

def p1(f):
    grid = Grid(parse_grid(f.read()))
    start = grid.find("S")[0]
    pos = COORD(start)

    def get_neighbors(pos):
        neighbors = []
        for neighbor in [pos + vel for vel in part[grid.get(pos)]]:
            if pos in set(neighbor + vel if vel else None for vel in part[grid.get(neighbor)]):
                neighbors.append(neighbor)

        return neighbors

    distances, nodes = bfs(pos, get_neighbors)
    return max(distances.values())

# this can be cleaner, but idk how
def p2(f):
    grid = Grid(parse_grid(f.read()))
    start = grid.find("S")[0]
    pos = COORD(start)

    # get pipes
    def get_neighbors(pos):
        neighbors = []
        for neighbor in [pos + vel for vel in part[grid.get(pos)]]:
            if pos in set(neighbor + vel if vel else None for vel in part[grid.get(neighbor)]):
                neighbors.append(neighbor)
        return list(set(neighbors))

    distances, _ = bfs(pos, get_neighbors)

    # sort the pipes in clockwise / counterclockwise order
    pipes = deque(distances.keys())
    path = [pipes.popleft(), pipes.popleft()]
    pipes = set(pipes) - set(path)
    while pipes:
        for neighbor in get_neighbors(path[-1]):
            if neighbor not in path:
                path.append(neighbor)
                pipes.remove(neighbor)
    
    path.append(path[0])

    # shoelace formula
    area = 0.5 * abs(
        functools.reduce(
            lambda acc, i: acc + (path[i][0] * path[i + 1][1] - path[i][1] * path[i + 1][0]),
            range(len(path) - 1),
            0
        )
    )
    return int(area) - (len(path) // 2) + 1
