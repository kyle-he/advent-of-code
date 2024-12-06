#region Imports
import collections
import copy
import functools
import heapq
import itertools
import math
import operator
import re
import sys
import typing
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import reduce
from pprint import pprint
#endregion

# Increase recursion limit to handle deep recursion during complex AoC problems.
sys.setrecursionlimit(100000)
T = typing.TypeVar("T")

AIR = "."
WALL = "#"

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

#region List/Vector operations
GRID_DELTA = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # Up, Down, Left, Right
OCT_DELTA = [[1, 1], [-1, -1], [1, -1], [-1, 1]] + GRID_DELTA  # Diagonals + orthogonals

CHAR_TO_DELTA = {
    "U": [-1, 0],
    "R": [0, 1],
    "D": [1, 0],
    "L": [0, -1],
    "N": [-1, 0],
    "E": [0, 1],
    "S": [1, 0],
    "W": [0, -1],
}

DELTA_TO_UDLR = {
    (-1, 0): "U",
    (0, 1): "R",
    (1, 0): "D",
    (0, -1): "L",
}

DELTA_TO_NESW = {
    (-1, 0): "N",
    (0, 1): "E",
    (1, 0): "S",
    (0, -1): "W",
}

def turn_180(drowcol):
    """
    Returns the direction opposite to drowcol.
    For (dx,dy), returns (-dx,-dy).
    """
    drow, dcol = drowcol
    return [-drow, -dcol]

def turn_right(drowcol):
    """
    Rotates a direction 90 degrees to the right.
    """
    drow, dcol = drowcol
    return [dcol, -drow]

def turn_left(drowcol):
    """
    Rotates a direction 90 degrees to the left.
    """
    drow, dcol = drowcol
    return [-dcol, drow]

def dimensions(grid: typing.List) -> typing.List[int]:
    """
    Given a nested list, returns its dimensions.
    Example: dimensions([[1,2],[3,4]]) -> [2,2]
    """
    out = []
    while isinstance(grid, list):
        out.append(len(grid))
        grid = grid[0]
    return out

def neighbours(coord, dims, deltas) -> typing.List[typing.List[int]]:
    """
    Returns valid neighbors around `coord` using the given `deltas` and `dims`.
    dims is a list of maximum sizes in each dimension.
    Only includes neighbors inside the grid.
    """
    out = []
    for delta in deltas:
        new_coord = padd(coord, delta)
        if all(0 <= c < c_max for c, c_max in zip(new_coord, dims)):
            out.append(new_coord)
    return out

def points_to_grid(points, sub_min=True, flip=True):
    """
    Converts a list of (x,y) points into a 2D grid of '.' and '#',
    where '#' marks the points.
    
    sub_min: If True, translate points so min coords start at 0.
    flip: If True, interpret points as (x,y) and flip so indexing grid[y][x].
    """
    if sub_min:
        points = points_sub_min(points)
    if not flip:
        points = [(y, x) for x, y in points]
    grid = make_grid(max(map(snd, points))+1, max(map(fst, points))+1, fill='.')
    for x, y in points:
        grid[y][x] = '#'
    return grid

def print_grid(grid):
    """
    Prints a 2D grid row by row.
    """
    for line in grid:
        print(*line, sep="")

def fst(x):
    """Returns the first element of a tuple."""
    return x[0]

def snd(x):
    """Returns the second element of a tuple."""
    return x[1]

def nth(n):
    """Returns the nth element of a tuple.
       Make a partially applied function to extract nth element from a list of tuples.
    """
    return lambda x: x[n]

def padd(x, y):
    """Component-wise addition of two vectors x and y."""
    return [a+b for a, b in zip(x, y)]

def pneg(v):
    """Component-wise negation of a vector v."""
    return [-i for i in v]

def psub(x, y):
    """Component-wise subtraction x - y."""
    return [a-b for a, b in zip(x, y)]

def pmul(m: int, v):
    """Component-wise multiplication of vector v by scalar m."""
    return [m * i for i in v]

def pdot(x, y):
    """Dot product of two vectors x and y."""
    return sum(a*b for a, b in zip(x, y))

def pdist1(x, y=None):
    """
    Manhattan (L1) distance between x and y or between x and 0 if y is None.
    """
    if y is not None: x = psub(x, y)
    return sum(map(abs, x))

def pdist2sq(x, y=None):
    """
    Squared Euclidean distance between x and y or between x and 0 if y is None.
    """
    if y is not None: x = psub(x, y)
    return sum(i*i for i in x)

def pdist2(v):
    """
    Euclidean distance from v to the origin.
    """
    return math.sqrt(pdist2sq(v))

def signum(n: int) -> int:
    """
    Returns the sign of integer n: 1 if positive, 0 if zero, -1 if negative.
    """
    if n > 0:
        return 1
    elif n == 0:
        return 0
    else:
        return -1
#endregion