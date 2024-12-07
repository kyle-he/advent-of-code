import itertools
import functools 
from collections import defaultdict, deque, Counter, OrderedDict
import math
import re

from common.parse import *
from common.list import *
from common.utils import *
from common.grid import *
from common.algos import *

def hash(word):
    a = 0
    for c in word:
        a = (a + ord(c)) * 17 % 256
    return a

def p1(f):
    line = f.read()
    ans = 0
    return sum(map(hash, line.split(",")))

def p2(f):
    line = f.read()
    books = defaultdict(OrderedDict)
    for book in line.split(","):
        name, op, num = re.split("(=|-)", book)
        h = hash(name)
        if op == "-":
            if name in books[h]:
                del books[h][name]
        else:
            books[h][name] = int(num)

    return sum((i + 1) * sum((a + 1) * b for a, b in enumerate(d.values())) for i, d in books.items())