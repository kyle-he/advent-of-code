#region Imports
import collections
import copy
import functools
import heapq
import itertools
import math
import operator
import re
import sys
import typing
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import reduce
from pprint import pprint
#endregion

# Increase recursion limit to handle deep recursion during complex AoC problems.
sys.setrecursionlimit(100000)
T = typing.TypeVar("T")

#region Strings, lists, dicts
def lmap(func, *iterables):
    """
    Like `map`, but returns a list instead of an iterator.
    Commonly used to quickly apply a function to each element of one or more iterables.
    """
    return list(map(func, *iterables))

def str_rep(iterable):
    """
    Converts all elements in iterables to strings and concatenates them.
    """
    return "".join(map(str, iterable))

def make_grid(*dimensions: typing.List[int], fill=None):
    """
    Creates a multi-dimensional list (grid) of given dimensions, filled with a specified value.
    For example, make_grid(3,4, fill=0) returns a 3x4 grid filled with 0s.
    Useful for 2D or N-D puzzles.
    """
    if len(dimensions) == 1:
        return [fill for _ in range(dimensions[0])]
    next_down = make_grid(*dimensions[1:], fill=fill)
    return [copy.deepcopy(next_down) for _ in range(dimensions[0])]

def min_max(l):
    """
    Returns (minimum, maximum) of a list.
    """
    return min(l), max(l)

def max_minus_min(l):
    """
    Returns the difference between the max and min values in a list.
    """
    return max(l) - min(l)

def partial_sum(l):
    """
    Returns a list of cumulative sums.
    out[i] = sum of l[:i]. The returned list has one extra element at the start (0).
    Example: partial_sum([1,2,3]) -> [0,1,3,6]
    """
    out = [0]
    for i in l:
        out.append(out[-1] + i)
    return out

cum_sum = partial_sum  # Alias for partial_sum

def list_diff(x):
    """
    Returns a list of consecutive differences.
    For input [x0, x1, x2, ...], it returns [x1-x0, x2-x1, ...].
    Useful for analyzing gradients or sequences of changes.
    """
    return [b - a for a, b in zip(x, x[1:])]

def flatten(l):
    """
    Flattens a list of lists into a single list.
    Example: [[1,2],[3,4]] -> [1,2,3,4]
    """
    return [i for x in l for i in x]

def every_n(l,n):
    """
    Groups elements of `l` in chunks of size `n`.
    Example: every_n([1,2,3,4,5,6], 2) -> [(1,2),(3,4),(5,6)]
    """
    return list(zip(*[iter(l)]*n))

def windows(l, n):
    """
    Returns a list of all n-length sliding windows from l.
    Example: windows([1,2,3,4],2) -> [(1,2),(2,3),(3,4)]
    """
    return list(zip(*[l[i:] for i in range(n)]))

def ints(s: str) -> typing.List[int]:
    """
    Extracts all integers (including negative) from a string.
    Example: "x=5, y=-3" -> [5, -3]
    """
    assert isinstance(s, str), f"ints() expected a string, got {type(s)}"
    return lmap(int, re.findall(r"(?:(?<!\d)-)?\d+", s))

def positive_ints(s: str) -> typing.List[int]:
    """
    Extracts all positive integers from a string.
    Example: "There are 10 apples and 20 oranges" -> [10,20]
    """
    assert isinstance(s, str)
    return lmap(int, re.findall(r"\d+", s))

def floats(s: str) -> typing.List[float]:
    """
    Extracts all floats (including negative) from a string.
    Example: "x=-3.2 y=5" -> [-3.2, 5.0]
    """
    assert isinstance(s, str)
    return lmap(float, re.findall(r"-?\d+(?:\.\d+)?", s))

def positive_floats(s: str) -> typing.List[float]:
    """
    Extracts all positive floats from a string.
    Example: "radius=3.14 width=2" -> [3.14, 2.0]
    """
    assert isinstance(s, str)
    return lmap(float, re.findall(r"\d+(?:\.\d+)?", s))

def words(s: str) -> typing.List[str]:
    """
    Extracts alphabetical words from a string.
    Example: "Hello, world 123." -> ["Hello", "world"]
    """
    assert isinstance(s, str)
    return re.findall(r"[a-zA-Z]+", s)

def keyvalues(d):
    """
    Returns a list of (key, value) pairs from a dictionary.
    Equivalent to list(d.items()), but handy if you keep forgetting this.
    """
    return list(d.items())

def make_hashable(l):
    """
    Converts a structure of lists/sets/dicts into a hashable structure (tuple/frozenset).
    Useful for using complex structures as keys in a dictionary or entries in a set.
    """
    if isinstance(l, list):
        return tuple(map(make_hashable, l))
    if isinstance(l, dict):
        l = set(l.items())
    if isinstance(l, set):
        return frozenset(map(make_hashable, l))
    return l

def invert_dict(d, single=True):
    """
    Inverts a dictionary. If single=True, assumes values are unique keys in the inverted dict.
    Otherwise, collects keys into a list for each value.
    Example (single=True): {A:1, B:2} -> {1:A, 2:B}
    Example (single=False): {A:1, B:1} -> {1:[A,B]}
    """
    out = {}
    if single:
        for k, v in d.items():
            v = make_hashable(v)
            if v in out:
                print("[invert_dict] WARNING: duplicate key", v)
            out[v] = k
    else:
        for k, v in d.items():
            v = make_hashable(v)
            out.setdefault(v, []).append(k)
    return out
#endregion

#region Data Structures
class Linked(typing.Generic[T], typing.Iterable[T]):
    """
    Doubly-linked circular list node.
    Useful for puzzles where you need to rotate, remove, or insert items efficiently.
    The class can represent an entire list by using one node as the "head".
    """

    def __init__(self, item: T) -> None:
        self.item = item
        self.forward = self
        self.backward = self
    
    @property
    def val(self): return self.item
    @property
    def after(self): return self.forward
    @property
    def before(self): return self.backward

    def _join(self, other: "Linked[T]") -> None:
        self.forward = other
        other.backward = self
    
    def concat(self, other: "Linked[T]") -> None:
        """
        Concatenate another circular list at the end of this one.
        """
        first_self = self
        last_self = self.backward

        first_other = other
        last_other = other.backward
        last_self._join(first_other)
        last_other._join(first_self)
    
    def concat_immediate(self, other: "Linked[T]") -> None:
        """
        Insert another circular list immediately after this node.
        """
        self.forward.concat(other)
    
    def append(self, val: T) -> None:
        """
        Append a new value before the 'head' node (at the end of the circular list).
        """
        self.concat(Linked(val))
    
    def append_immediate(self, val: T) -> None:
        """
        Insert a new value immediately after this node.
        """
        self.concat_immediate(Linked(val))
    
    def pop(self, n: int = 1) -> None:
        """
        Remove this node and the next n-1 nodes from the parent list, forming a separate list.
        """
        assert n > 0
        first_self = self
        last_self = self.move(n-1)

        first_other = last_self.forward
        last_other = first_self.backward
        
        last_other._join(first_other)
        last_self._join(first_self)
    
    def pop_after(self, after: int, n: int = 1) -> None:
        """
        Pop n nodes starting from the node that is `after` steps away from this one.
        Returns the node where popping starts (the head of the popped-out list).
        """
        to_return = self.move(after)
        to_return.pop(n)
        return to_return

    def delete(self) -> None:
        """
        Delete this node from its list.
        """
        self.pop()
    
    def delete_other(self, n: int) -> None:
        """
        Delete a node n steps away from this one.
        """
        to_delete = self.move(n)
        if to_delete is self:
            raise Exception("can't delete self")
        to_delete.delete()
        del to_delete
    
    def move(self, n: int) -> "Linked[T]":
        """
        Move n steps forward if n > 0 or backward if n < 0, and return that node.
        """
        out = self
        if n >= 0:
            for _ in range(n):
                out = out.forward
        else:
            for _ in range(-n):
                out = out.backward
        return out
    
    def iterate_nodes_inf(self) -> typing.Iterator["Linked[T]"]:
        """
        Infinite iterator cycling through the circular list starting at this node.
        """
        cur = self
        while True:
            yield cur
            cur = cur.forward
    
    def iterate_nodes(self, count=1) -> typing.Iterator["Linked[T]"]:
        """
        Iterate through the circular list `count` times.
        count=1 iterates through the entire list once.
        """
        for node in self.iterate_nodes_inf():
            if node is self:
                count -= 1
                if count < 0:
                    break
            yield node
    
    def iterate_inf(self) -> typing.Iterator[T]:
        """
        Infinite iteration of the item values.
        """
        return map(lambda node: node.item, self.iterate_nodes_inf())
    
    def iterate(self, count=1) -> typing.Iterator[T]:
        """
        Iterate through items in the circular list `count` times.
        """
        return map(lambda node: node.item, self.iterate_nodes(count))
    
    def to_list(self):
        """
        Convert the circular list into a standard Python list (one full cycle).
        """
        return list(self.iterate())
    
    def check_correctness(self) -> None:
        """
        Verifies forward/backward pointers are consistent for this node.
        """
        assert self.forward.backward is self
        assert self.backward.forward is self
    
    def check_correctness_deep(self) -> None:
        """
        Verifies pointers for the entire circular list.
        """
        for node in self.iterate_nodes():
            node.check_correctness()
    
    def __iter__(self) -> typing.Iterator[T]:
        return self.iterate()
    
    def __repr__(self) -> str:
        return "Linked({})".format(self.to_list())

    @classmethod
    def from_list(cls, l: typing.Iterable[T]) -> "Linked[T]":
        """
        Create a circular doubly-linked list from a Python iterable.
        Returns the 'head' node.
        """
        it = iter(l)
        out = cls(next(it))
        for i in it:
            out.concat(cls(i))
        return out


class UnionFind:
    """
    Union-Find (Disjoint Set Union) data structure.
    Efficiently merges sets and finds representatives.
    Useful for connected components in graphs or grouping tasks.
    """

    def __init__(self, n: int) -> None:
        self.n = n
        self.parents = [None] * n
        self.ranks = [1] * n
        self.num_sets = n
    
    def find(self, i: int) -> int:
        """
        Find the representative (root) of the set containing i.
        Uses path compression.
        """
        p = self.parents[i]
        if p is None:
            return i
        p = self.find(p)
        self.parents[i] = p
        return p
    
    def in_same_set(self, i: int, j: int) -> bool:
        """
        Checks if i and j belong to the same set.
        """
        return self.find(i) == self.find(j)
    
    def merge(self, i: int, j: int) -> None:
        """
        Merges the sets containing i and j.
        """
        i = self.find(i)
        j = self.find(j)

        if i == j:
            return
        
        i_rank = self.ranks[i]
        j_rank = self.ranks[j]

        if i_rank < j_rank:
            self.parents[i] = j
        elif i_rank > j_rank:
            self.parents[j] = i
        else:
            self.parents[j] = i
            self.ranks[i] += 1
        self.num_sets -= 1
