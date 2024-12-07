# Day       Time  Rank  Score       Time  Rank  Score
#   7   00:02:22   126      0   00:25:29  3070      0

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
    lines = f.read().splitlines()
    ans = 0
    for line in lines:
        a, *b = ints(line)
        for ops in itertools.product(list("+*"), repeat=len(b) - 1):
            r = b[0]
            for op, n in zip(ops, b[1:]):
                if op == "+":
                    r += n
                else:
                    r *= n
            if r == a:
                ans += a
                break
    return ans

def eval_expression(nums, ops):
    r = nums[0]
    for op, n in zip(ops, nums[1:]):
        if op == "+":
            r += n
        elif op == "|":
            r = int(str(r) + str(n)) 
        else:  
            r *= n
    return r

def p2(f):
    lines = f.read().splitlines()
    ans = 0
    for line in lines:
        a, *b = ints(line)
        for ops in itertools.product(list("+*|"), repeat=len(b) - 1):
            if a == eval_expression(b, ops):
                ans += a
                break
    return ans