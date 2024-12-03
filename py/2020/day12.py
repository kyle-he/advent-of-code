import itertools
import functools
from collections import defaultdict, deque, Counter
import math
import re

directions_4 = [(1, 0), (0, -1), (-1, 0), (0, 1)]  

def p1(f):
    x, y = 0, 0  
    direction = 0  

    for command in f.read().splitlines():
        action, value = command[0], int(command[1:])
        if action == 'F':  
            dx, dy = directions_4[direction]
            x += dx * value
            y += dy * value
        elif action == 'L':  
            direction = (direction - value // 90) % 4
        elif action == 'R':  
            direction = (direction + value // 90) % 4
        elif action == 'N':  
            y += value
        elif action == 'S':  
            y -= value
        elif action == 'E':  
            x += value
        elif action == 'W':  
            x -= value

    
    return abs(x) + abs(y)

def p2(f):
    x, y = 0, 0  
    wx, wy = 10, 1  

    for command in f.read().splitlines():
        action, value = command[0], int(command[1:])
        if action == 'F':  
            x += wx * value
            y += wy * value
        elif action == 'N':  
            wy += value
        elif action == 'S':  
            wy -= value
        elif action == 'E':  
            wx += value
        elif action == 'W':  
            wx -= value
        elif action in {'L', 'R'}:  
            
            rotations = value // 90
            if action == 'R':  
                rotations = -rotations  
            
            for _ in range(rotations % 4):  
                wx, wy = -wy, wx  

    
    return abs(x) + abs(y)