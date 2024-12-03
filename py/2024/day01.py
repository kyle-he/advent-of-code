# Day       Time  Rank  Score       Time  Rank  Score
#   1   00:02:28   522      0   00:07:29  1761      0

import itertools
import functools
from collections import defaultdict, deque, Counter
import math
import re

def p1(f):
    lines = f.read().splitlines()
    l = [tuple(map(int, line.split())) for line in lines]
    l1, l2 = zip(*l)
    l1, l2 = sorted(l1), sorted(l2)
   
    return sum(abs(a - b) for a, b in zip(l1, l2))

def p2(f):
    lines = f.read().splitlines()
    l = [tuple(map(int, line.split())) for line in lines]
    l1, l2 = zip(*l)
   
    return sum(a * l2.count(a) for a, b in zip(l1, l2))