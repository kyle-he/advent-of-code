from collections import deque
import itertools

def p1(f):
    q = deque([])
    for line in f.read().splitlines():
        if len(q) > 25:
            q.popleft()
            # lazy quick implementation
            if not any((a + b == int(line) and a != b) for (a, b) in list(itertools.combinations(q, 2))):
                return int(line)
            
        q.append(int(line))
    
    return 0

def p2(f):
    goal = p1(f)
    f.seek(0)
    input = list(map(int, f.read().splitlines()))
    prev_set = {}
    for i, psum in enumerate(itertools.accumulate(input)):
        prev_set[psum] = i
        if psum - goal in prev_set:
            range = input[prev_set[psum - goal] + 1 : i]
            return max(range) + min(range)
    
    return 0