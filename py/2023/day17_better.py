# import itertools
# import functools 
# from collections import defaultdict, deque, Counter
# import math
# import re

# from common.parse import *
# from common.list import *
# from common.utils import *
# from common.grid import *
# from common.algos import *

# def p1(f):
#     grid = Grid(parse_grid(f.read()))

#     def expand(node):
#         start_node, velocity = node
#         for dir in {UP, DOWN, LEFT, RIGHT} - {velocity, tuple(pneg(velocity))}:
#             curr_node = start_node
#             cost = 0  
#             for _ in range(3):  
#                 next_node = tuple(padd(curr_node, dir))
#                 if grid.in_bounds(*next_node):
#                     curr_node = next_node
#                     cost += int(grid[next_node])  
#                 else:
#                     break
            
#                 yield cost, (curr_node, dir) 

#     values, parents, best_node = rust_dijkstra(
#         [((0, 0), LEFT)], 
#         expand, 
#         lambda x: x[0] == (grid.rows - 1, grid.cols - 1)
#     )
#     return values[best_node]

# def p2(f):
#     grid = Grid(parse_grid(f.read()))

#     def expand(node):
#         start_node, velocity = node
#         for dir in {UP, DOWN, LEFT, RIGHT} - {velocity, tuple(pneg(velocity))}:
#             curr_node = start_node
#             cost = 0  
#             for i in range(10):  
#                 next_node = tuple(padd(curr_node, dir))
#                 if grid.in_bounds(*next_node):
#                     curr_node = next_node
#                     cost += int(grid[next_node])  
#                 else:
#                     break

#                 if i >= 3:
#                     yield cost, (curr_node, dir)

#     values, parents, best_node = rust_dijkstra(
#         [((0, 0), LEFT)], 
#         expand, 
#         lambda x: x[0] == (grid.rows - 1, grid.cols - 1)
#     )
#     return values[best_node]
