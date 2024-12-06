from itertools import cycle
import math

def p1(f):
    graph = {}
    path = ""
    for line in f.read().splitlines():
        if not path:
            path = line
        elif line:
            line = line.replace(")", "").replace("(", "")
            node, children = line.split(" = ")
            child0, child1 = children.split(", ")
            graph[node] = [child0, child1]
    
    curr_node = "AAA"
    steps = 0
    for direction in cycle(path):
        if curr_node == "ZZZ":
            return steps
        match direction:
            case "L":
                curr_node = graph[curr_node][0]
            case "R":
                curr_node = graph[curr_node][1]
        steps += 1
    return steps

def p2(f):
    path, maps = f.read().split("\n\n")
    maps = [x.split(" = ") for x in maps.splitlines()]
    maps = {a: b[1:-1].split(", ") for a, b in maps}

    ans = []

    for curr in maps:
        if not curr.endswith("A"):
            continue
        visited = set()
        for count, (idx, d) in enumerate(cycle(enumerate(path)), start=1):
            prev, curr = curr, maps[curr][d == "R"]
            visited.add((curr, idx))
            if prev.endswith("Z") and (curr, idx) in visited:
                ans.append(count - 1)
                break

    return math.lcm(*ans)