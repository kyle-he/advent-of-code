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
        line = ints(line)        
        while not all(a == 0 for a in line):
            ans += line[-1]
            line = list(b - a for a, b in itertools.pairwise(line))
    
    return ans
                

def p1(f):
    lines = f.read().splitlines()
    ans = 0
    for line in lines:
        line = reversed(ints(line))        
        while not all(a == 0 for a in line):
            ans += line[-1]
            line = list(b - a for a, b in itertools.pairwise(line))
    
    return ans