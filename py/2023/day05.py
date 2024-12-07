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
    seeds, *rules = parse_blocks(f.read())

    seeds = ints(seeds)

    maps = defaultdict(list)
    for i, rule in enumerate(rules):
        _, *rule = rule.splitlines()
        
        for a, b, c in map(ints, rule):
            maps[i].append((a, b, c))

    ans = float("inf")
    for seed in seeds:
        curr = seed
        for i in range(7):
            for a, b, c in maps[i]:
                if b <= curr < b + c:
                    curr = a + curr - b
                    break
        
        ans = min(ans, curr)

    return ans
        
# todo
def p2(f):
    # seeds, *rules = parse_blocks(f.read())

    # seeds = ints(seeds)

    # maps = defaultdict(list)
    # for i, rule in enumerate(rules):
    #     _, *rule = rule.splitlines()
        
    #     for a, b, c in map(ints, rule):
    #         maps[i].append((a, b, c))

    # ans = float("inf")
    # ranges = deque([range(seed, seed + offset) for seed, offset in every_n(seeds, 2)])
    # for i in range(7):
    #     mapping = maps[i]
    #     print(ranges)
    #     for _ in range(len(ranges)):
    #         r = ranges.popleft()
    #         for a, b, c in mapping:
    #             overlap = range_overlap(r, range(b, b + c))
    #             if overlap:
    #                 ranges.append(range(a + overlap.start - b, a + overlap.stop - b))
    
    # ans = min(ans, min(map(min, ranges)))

    # for seed, offset in every_n(seeds, 2):
    #     lo = seed
    #     hi = seed + offset

    #     ranges = defaultdict(list, {0: [range(lo, hi)]})
    #     for i in range(7):
    #         # a = destination start
    #         # b = source start
    #         # c = offset
    #         while ranges[i]:
    #             r = ranges[i].pop()
    #             for a, b, c in maps[i]:
    #                 overlap = range_overlap(r, range(b, b + c))
    #                 if overlap:
    #                     ranges[i + 1].append(range(a + overlap.start - b, a + overlap.stop - b))

    #     if ranges[7]:
    #         print(ans)
    #         ans = min(ans, min(map(min, ranges[7])))

    # return ans
    return 0