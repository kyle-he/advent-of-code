import itertools
import functools
from collections import defaultdict, deque, Counter
import math
import re

def p1(f):
    adapters = sorted(map(int, f.readlines()), reverse=True) + [0]
    print(len(adapters))
    print(adapters)

    prev = adapters[0]
    jumps = defaultdict(int)
    for adapter in adapters[1:]:
        jumps[prev - adapter] += 1
        prev = adapter

    print(jumps)

    return jumps[1] * (jumps[3] + 1)

def p2(f):    
    mem = defaultdict(int)
    mem[0] = 1
    adapters = sorted(map(int, f.readlines()))
    for adapter in adapters:
        mem[adapter] = mem[adapter - 1] + mem[adapter - 2] + mem[adapter - 3]

    return mem[max(adapters)]