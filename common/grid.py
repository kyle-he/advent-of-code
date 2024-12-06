# common grid functions 

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

def parse_grid_dict(input):
    # make a dictionary of (x, y) -> value
    # return rows and cols too

    for y, line in enumerate(input.splitlines()):
        for x, c in enumerate(line.strip()):
            grid[(x, y)] = c
    
    return grid

def parse_grid(input):
    # make a 2d array of values
    # return rows and cols too

    grid = []
    for line in input.splitlines():
        grid.append(list(line))
    
    return grid

class Grid(typing.Generic[T]):
    """
    A simple 2D grid wrapper.
    Provides bounds checking and coordinate iteration.
    """
    def __init__(self, grid: typing.List[typing.List[T]]) -> None:
        self.grid = grid
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
    
    def coords(self) -> typing.List[typing.List[int]]:
        """
        Returns a list of coordinates [[row,col], ...] covering the entire grid.
        """
        return [[r, c] for r in range(self.rows) for c in range(self.cols)]
    
    def get_row(self, row: int):
        """
        Asserts row is in range. Simple sanity check.
        """
        assert 0 <= row < self.rows, f"row {row} is OOB"
    
    def in_bounds(self, row: int, col: int) -> bool:
        """
        Checks if (row,col) is within grid bounds.
        """
        return 0 <= row < self.rows and 0 <= col < self.cols
    
    def __contains__(self, coord: typing.Union[typing.Tuple[int, int], typing.List[int]]) -> bool:
        return self.in_bounds(*coord)
    
    def __getitem__(self, coord: typing.Union[typing.Tuple[int, int], typing.List[int]]) -> T:
        if not self.in_bounds(*coord):
            return None  # RETURN NONE FOR OOB
        
        return self.grid[coord[0]][coord[1]]

    # funny things
    def get(self, coord):
        return self[coord]

    def transpose(self) -> "Grid[T]":
        """
        Transpose the grid (swap rows and columns).
        """
        transposed = [list(row) for row in zip(*self.grid)]
        return Grid(transposed)
    
    def rotate_right(self) -> "Grid[T]":
        """
        Rotate the grid 90 degrees clockwise.
        """
        rotated = [list(row) for row in zip(*self.grid[::-1])]
        return Grid(rotated)
    
    def rotate_left(self) -> "Grid[T]":
        """
        Rotate the grid 90 degrees counterclockwise.
        """
        rotated = [list(row) for row in zip(*self.grid)][::-1]
        return Grid(rotated)
    
    def find(self, value: T) -> typing.Tuple[typing.Tuple[int, int]]:
        """
        Find all coordinates of a value in the grid.
        """
        return [(r, c) for r, c in self.coords() if self[r, c] == value]

#endregion