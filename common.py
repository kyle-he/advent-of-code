
def split_blocks(lines):
    """Splits input into blocks separated by empty lines."""
    return [block.split('\n') for block in '\n'.join(lines).split('\n\n')]

# Math Utilities
def lcm(a, b):
    """Returns the least common multiple of a and b."""
    return abs(a * b) // math.gcd(a, b)

def gcd_multiple(numbers):
    """Returns the greatest common divisor of a list of numbers."""
    return functools.reduce(math.gcd, numbers)

def lcm_multiple(numbers):
    """Returns the least common multiple of a list of numbers."""
    return functools.reduce(lcm, numbers)

# Permutations and Combinations
def all_permutations(iterable):
    """Returns all permutations of the given iterable."""
    return list(itertools.permutations(iterable))

def all_combinations(iterable, r):
    """Returns all combinations of length r."""
    return list(itertools.combinations(iterable, r))

def all_combinations_with_replacement(iterable, r):
    """Returns combinations with replacement of length r."""
    return list(itertools.combinations_with_replacement(iterable, r))

# Grids
def neighbors_4(x, y):
    """Returns the 4-neighbors of (x, y)."""
    return [(x + dx, y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]

def neighbors_8(x, y):
    """Returns the 8-neighbors of (x, y)."""
    return [(x + dx, y + dy) for dx, dy in itertools.product([-1, 0, 1], repeat=2) if (dx, dy) != (0, 0)]

def parse_grid(lines):
    """Parses a grid into a dict with (x, y) keys and values from the grid."""
    return {(x, y): value for y, row in enumerate(lines) for x, value in enumerate(row)}

def manhattan_distance(p1, p2):
    """Calculates the Manhattan distance between two points."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# Searching
def bfs(start, neighbors_fn, goal_fn):
    """Performs breadth-first search."""
    queue = deque([start])
    visited = set()
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        if goal_fn(current):
            return current
        queue.extend(neighbors_fn(current))
    return None

def dfs(start, neighbors_fn, goal_fn):
    """Performs depth-first search."""
    stack = [start]
    visited = set()
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        if goal_fn(current):
            return current
        stack.extend(neighbors_fn(current))
    return None

# Parsing and Manipulation
def extract_ints(s):
    """Extracts integers from a string."""
    return list(map(int, re.findall(r"-?\d+", s)))

def extract_words(s):
    """Extracts words from a string."""
    return re.findall(r"[a-zA-Z]+", s)

def binary_to_int(binary_str):
    """Converts a binary string to an integer."""
    return int(binary_str, 2)

def int_to_binary(n, bits=0):
    """Converts an integer to a binary string of fixed length."""
    return format(n, f"0{bits}b")

# Functional Programming
def map_list(func, iterable):
    """Applies a function to all elements of a list."""
    return list(map(func, iterable))

def filter_list(func, iterable):
    """Filters elements of a list based on a function."""
    return list(filter(func, iterable))

def reduce_list(func, iterable):
    """Reduces a list to a single value using a function."""
    return functools.reduce(func, iterable)

def rotate(directions, clockwise=True):
    """
    Yields directional changes in a clockwise or counterclockwise order.

    Args:
        directions: A list of 2D direction tuples (e.g., [(0, 1), (-1, 0), ...]).
        clockwise: If True, iterate in clockwise order; otherwise, counterclockwise.

    Yields:
        Tuples representing direction vectors.
    """
    idx = 0
    n = len(directions)
    while True:
        yield directions[idx]
        idx = (idx + 1) % n if clockwise else (idx - 1 + n) % n

directions_4 = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # East, South, West, North

# Define all 8 possible directions in a 2D grid using NESW notation
directions_8 = [
    (0, 1),   # North
    (1, 1),   # North-East
    (1, 0),   # East
    (1, -1),  # South-East
    (0, -1),  # South
    (-1, -1), # South-West
    (-1, 0),  # West
    (-1, 1)   # North-West
]
