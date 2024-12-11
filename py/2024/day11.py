# Day       Time   Rank  Score       Time   Rank  Score
#  11   00:01:52    118      0   00:05:47     84     17

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
    stones = ints(f.read())
    def mult(stones):
        for stone in stones:
            if stone == 0:
                yield 1
            elif len(str(stone)) % 2 == 0:
                half = len(str(stone)) // 2
                yield int(str(stone)[:half])
                yield int(str(stone)[half:])
            else:
                yield stone * 2024
    
    for _ in range(25):
        stones = list(mult(stones))
    
    return len(stones)

def p2(f):
    stones = ints(f.read())
    counts = Counter(stones)
    def mult_e(counts):
        new_counts = Counter()
        for stone, count in counts.items():
            if stone == 0:
                new_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                half = len(str(stone)) // 2
                new_counts[int(str(stone)[:half])] += count
                new_counts[int(str(stone)[half:])] += count
            else:
                new_counts[stone * 2024] += count
        return new_counts
    
    for _ in range(75):
        counts = mult_e(counts)
    
    return sum(counts.values())