# Day       Time  Rank  Score       Time  Rank  Score
#   4   00:01:09    68     33   00:40:12  4972      0

import itertools
import functools
from collections import defaultdict, deque, Counter
import math
import re

directions_8 = [
    (0, 1),   # North
    (1, 1),   # North-East
    (1, 0),   # East
    (1, -1),  # South-East
    (0, -1),  # South
    (-1, -1), # South-West
    (-1, 0),  # West
    (-1, 1)   # North-West
]

class Grid:
    def __init__(self, file):
        self.grid = self.make_grid(file)
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

    def make_grid(self, file):
        lines = file.read().splitlines()
        return [list(line) for line in lines]

    def get(self, x, y):
        if 0 <= x < self.rows and 0 <= y < self.cols:
            return self.grid[x][y]
        return None

def p1(f):
    grid = Grid(f)
    word = "XMAS"
    
    def count_occurrences(start_x, start_y, dx, dy):
        x, y = start_x, start_y
        for letter in word:
            if grid.get(x, y) != letter:
                return 0
            x += dx
            y += dy
        return 1

    total = 0
    for x in range(grid.rows):
        for y in range(grid.cols):
            for dx, dy in directions_8:
                total += count_occurrences(x, y, dx, dy)
    return total

def p2(f):
    grid = Grid(f)

    def get_diagonals(x, y):
        try:
            main_diag =  "".join((grid.get(x - 1, y - 1), grid.get(x, y), grid.get(x + 1, y + 1)))
            anti_diag =  "".join((grid.get(x - 1, y + 1), grid.get(x, y), grid.get(x + 1, y - 1))) 
            return main_diag, anti_diag
        except:
            return None, None

    total = 0
    for x in range(grid.rows):
        for y in range(grid.cols):
            if grid.get(x, y) == 'A':  
                main_diag, anti_diag = get_diagonals(x, y)
                if main_diag in ("MAS", "SAM") and anti_diag in ("MAS", "SAM"):
                    total += 1

    return total
