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

def bisect(f, lo=0, hi=None, eps=1e-9):
    """
    Floating-point binary search that tries to find a value x for which f(x) changes truth value.
    f is a boolean predicate.
    Assumes f(lo) != f(hi) once hi is determined.
    Useful for searching a threshold or boundary in continuous problems.
    """
    lo_bool = f(lo)
    if hi is None:
        offset = 1
        while f(lo+offset) == lo_bool:
            offset *= 2
        hi = lo + offset
    else:
        assert f(hi) != lo_bool
    while hi - lo > eps:
        mid = (hi + lo) / 2
        if f(mid) == lo_bool:
            lo = mid
        else:
            hi = mid
    return lo if lo_bool else hi

def binary_search(f, lo=0, hi=None):
    """
    Integer binary search to find the boundary where f(x) flips its truth value.
    f is a boolean predicate.
    Assumes that eventually f(x) changes from True to False or vice versa.
    """
    lo_bool = f(lo)
    if hi is None:
        offset = 1
        while f(lo+offset) == lo_bool:
            offset *= 2
        hi = lo + offset
    else:
        assert f(hi) != lo_bool
    best_so_far = lo if lo_bool else hi
    while lo <= hi:
        mid = (hi + lo) // 2
        result = f(mid)
        if result:
            best_so_far = mid
        if result == lo_bool:
            lo = mid + 1
        else:
            hi = mid - 1
    return best_so_far

def topsort(out_edges: typing.Dict[T, typing.List[T]]) -> typing.List[T]:
    """
    Topologically sorts a directed acyclic graph (DAG).
    out_edges: A dictionary from node to list of successor nodes.
    Returns a list of nodes in topological order.
    Raises Exception if the graph is not a DAG.
    """
    temp = set()
    seen = set()
    out = []

    def dfs(n):
        if n in seen:
            return
        if n in temp:
            raise Exception("not a DAG")
        temp.add(n)
        if n in out_edges:
            for other in out_edges[n]:
                dfs(other)
        temp.remove(n)
        seen.add(n)
        out.append(n)
    
    for n in out_edges:
        dfs(n)
    out.reverse()
    return out

def path_from_parents(parents: typing.Dict[T, T], end: T) -> typing.List[T]:
    """
    Given a dictionary of {child: parent} entries and an end node,
    reconstructs the path from the start to the end node.
    """
    out = [end]
    while out[-1] in parents:
        out.append(parents[out[-1]])
    out.reverse()
    return out

def dijkstra(
    from_node: T,
    expand: typing.Callable[[T], typing.Iterable[typing.Tuple[int, T]]],
    to_node: typing.Optional[T] = None,
    heuristic: typing.Optional[typing.Callable[[T], int]] = None,
) -> typing.Tuple[typing.Dict[T, int], typing.Dict[T, T]]:
    """
    Dijkstra's / A* algorithm for shortest paths.
    expand(node) -> Iterable[(cost, successor_node)]
    If heuristic is provided, runs A* search.
    If to_node is provided, can stop early when that node is reached.
    Returns (distances, parents) dictionaries.
    Use path_from_parents to reconstruct the path.
    """
    if heuristic is None:
        heuristic = lambda _: 0
    seen = set()
    g_values = {from_node: 0}
    parents = {}

    todo = [(0 + heuristic(from_node), 0, from_node)]

    while todo:
        f, g, node = heapq.heappop(todo)
        if node in seen:
            continue
        seen.add(node)
        if to_node is not None and node == to_node:
            break

        for cost, new_node in expand(node):
            new_g = g + cost
            if new_node not in g_values or new_g < g_values[new_node]:
                parents[new_node] = node
                g_values[new_node] = new_g
                heapq.heappush(todo, (new_g + heuristic(new_node), new_g, new_node))
    
    return (g_values, parents)

import heapq
import typing
from typing import Callable, Dict, Iterable, List, Optional, Tuple, TypeVar

def rust_dijkstra(
    from_nodes,  # List of (initial_cost, starting_node)
    expand: Callable[[T], Iterable[Tuple[int, T]]],
    predicate: Optional[Callable[[T], bool]] = None,
    heuristic: Optional[Callable[[T], int]] = None,
) -> Tuple[Dict[T, int], Dict[T, T], Optional[T]]:
    """
    Modified Dijkstra's / A* algorithm to find the best path fulfilling a predicate,
    with support for multiple starting nodes.
    expand(node) -> Iterable[(cost, successor_node)]
    If heuristic is provided, runs A* search.
    Returns (distances, parents, best_node) where best_node is the node that satisfies the predicate with the least cost.
    Use path_from_parents to reconstruct the path.
    """
    if heuristic is None:
        heuristic = lambda _: 0

    seen = set()
    g_values = {}
    parents = {}

    todo = []
    for start_node in from_nodes:
        g_values[start_node] = 0
        heapq.heappush(todo, (heuristic(start_node), 0, start_node))
    
    best_node = None
    best_cost = float('inf')

    while todo:
        f, g, node = heapq.heappop(todo)
        if node in seen:
            continue
        seen.add(node)

        # Check the predicate for the current node
        if predicate is not None and predicate(node):
            if g < best_cost:
                best_node = node
                best_cost = g

        for cost, new_node in expand(node):
            new_g = g + cost
            if new_node not in g_values or new_g < g_values[new_node]:
                parents[new_node] = node
                g_values[new_node] = new_g
                heapq.heappush(todo, (new_g + heuristic(new_node), new_g, new_node))
    
    return (g_values, parents, best_node)

def a_star(
    from_node: T,
    expand: typing.Callable[[T], typing.Iterable[typing.Tuple[int, T]]],
    to_node: T,
    heuristic: typing.Optional[typing.Callable[[T], int]] = None,
) -> typing.Tuple[int, typing.List[T]]:
    """
    A* search algorithm.
    expand(node) -> (cost, successor_node) pairs.
    Returns (distance, path) for the shortest path from from_node to to_node.
    Raises Exception if to_node is unreachable.
    """
    g_values, parents = dijkstra(from_node, to_node=to_node, expand=expand, heuristic=heuristic)
    if to_node not in g_values:
        raise Exception("couldn't reach to_node")
    return (g_values[to_node], path_from_parents(parents, to_node))

def bfs(
    from_node: T,
    expand: typing.Callable[[T], typing.Iterable[T]],
    to_node: typing.Optional[T] = None
) -> typing.Tuple[typing.Dict[T,int], typing.Dict[T,T]]:
    """
    Breadth-first search.
    expand(node) -> successor_nodes
    Returns (distances, parents).
    If to_node is provided, stops when found.
    """
    g_values = {from_node: 0}
    parents = {}
    todo = [from_node]
    dist = 0

    while todo:
        new_todo = []
        dist += 1
        for node in todo:
            for new_node in expand(node):
                if new_node not in g_values:
                    parents[new_node] = node
                    g_values[new_node] = dist
                    new_todo.append(new_node)
        todo = new_todo
        if to_node is not None and to_node in g_values:
            break
    return (g_values, parents)

def bfs_single(
    from_node: T,
    expand: typing.Callable[[T], typing.Iterable[T]],
    to_node: T,
) -> typing.Tuple[int, typing.List[T]]:
    """
    BFS for a single shortest path to a specific node.
    Returns (distance, path).
    Raises Exception if unreachable.
    """
    g_values, parents = bfs(from_node, to_node=to_node, expand=expand)
    if to_node not in g_values:
        raise Exception("couldn't reach to_node")
    return (g_values[to_node], path_from_parents(parents, to_node))

BLANK = object()

def hamming_distance(a, b) -> int:
    """
    Hamming distance between two sequences: counts positions where they differ.
    If lengths differ, positions beyond the shorter are considered mismatched.
    """
    return sum(i is BLANK or j is BLANK or i != j for i, j in itertools.zip_longest(a, b, fillvalue=BLANK))

def edit_distance(a, b) -> int:
    """
    Compute the Levenshtein (edit) distance between two sequences a and b.
    Measures the minimum number of single-character edits (insertions, deletions, substitutions).
    Uses DP for efficiency.
    """
    n = len(a)
    m = len(b)
    dp = [[None] * (m+1) for _ in range(n+1)]
    dp[n][m] = 0
    def aux(i, j):
        if dp[i][j] is not None:
            return dp[i][j]
        if i == n:
            dp[i][j] = 1 + aux(i, j+1)
        elif j == m:
            dp[i][j] = 1 + aux(i+1, j)
        else:
            dp[i][j] = min((a[i]!=b[j]) + aux(i+1, j+1), 1 + aux(i+1, j), 1 + aux(i, j+1))
        return dp[i][j]
    return aux(0,0)
#endregion