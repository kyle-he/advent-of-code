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

# this can def be better

# def print_grid_with_directions(grid, parents, values):
#     directions_map = {UP: "^", DOWN: "V", LEFT: "<", RIGHT: ">", None: "."}
    
#     rows, cols = grid.rows, grid.cols
#     output = []
    
#     for r in range(rows):
#         row = []
#         for c in range(cols):
#             node = (r, c)
#             if node in values:
#                 cost = values[node]
#                 parent = parents.get(node)
#                 direction = None
#                 if parent:
#                     pr, pc = parent[0]
#                     vr, vc = r - pr, c - pc  
#                     direction = (vr, vc)
#                 row.append(f"{directions_map.get(direction, '?')}{cost:2}")
#             else:
#                 row.append(".")  
#         output.append(" ".join(row))
    
#     print("\n".join(output))

def print_grid_with_directions(grid, path, values):
    """
    Prints the grid with directions (velocity) and costs.
    - `grid`: The grid object.
    - `parents`: Dictionary mapping each (position, velocity) node to its parent.
    - `values`: Dictionary mapping each (position, velocity) node to its cost.
    """
    directions_map = {UP: "^", DOWN: "v", LEFT: "<", RIGHT: ">", None: "·"}
    rows, cols = grid.rows, grid.cols
    output = []

    # Extract positions and velocities from the path
    path_positions = {node[0]: node[1] for node in path}

    for r in range(rows):
        row = []
        for c in range(cols):
            node = (r, c)
            if node in path_positions:
                velocity = path_positions[node]
                cost = values.get((node, velocity), "?")  # Get the cost, default to "?" if missing
                direction = directions_map.get(velocity, "?")
                row.append(f"{direction}{cost:2}")
            else:
                row.append(" . ")  # Empty space for non-path nodes
        output.append(" ".join(row))

    print("\n".join(output))


def p1(f):
    grid = Grid(parse_grid(f.read()))

    def expand(node):
        start_node, velocity = node
        for dir in {UP, DOWN, LEFT, RIGHT} - {velocity, tuple(pneg(velocity))}:
            curr_node = start_node
            cost = 0  
            for _ in range(3):  
                next_node = tuple(padd(curr_node, dir))
                if grid.in_bounds(*next_node):
                    curr_node = next_node
                    cost += int(grid[next_node])  
                else:
                    break
            
                yield cost, (curr_node, dir) 
        
    def pred(node):
        node, velocity = node
        return node == (grid.rows - 1, grid.cols - 1)

    # values, parents = dijkstra(((0, 0), (-10, -10)), expand, None, pred)
    # print_grid(points_to_grid(lmap(fst, path_from_parents(parents, next(filter(pred, values.keys()))))))
    # print_grid_with_directions(grid, path_from_parents(parents, next(filter(pred, values.keys()))), values)
    # print(values.keys())
    # return values[next(filter(pred, values.keys()))]

    values, parents = dijkstra(((0, 0), (0, 0)), expand, None, pred)
    return values[min(filter(pred, values.keys()), key=lambda x: values[x])]

def p2(f):
    grid = Grid(parse_grid(f.read()))

    def expand(node):
        start_node, velocity = node
        for dir in {UP, DOWN, LEFT, RIGHT} - {velocity, tuple(pneg(velocity))}:
            curr_node = start_node
            cost = 0  
            for i in range(10):  
                next_node = tuple(padd(curr_node, dir))
                if grid.in_bounds(*next_node):
                    curr_node = next_node
                    cost += int(grid[next_node])  
                else:
                    break

                if i >= 3:
                    yield cost, (curr_node, dir)
        
    def pred(node):
        node, velocity = node
        return node == (grid.rows - 1, grid.cols - 1)

    values, parents = dijkstra(((0, 0), (0, 0)), expand, None, pred)
    return values[min(filter(pred, values.keys()), key=lambda x: values[x])]
