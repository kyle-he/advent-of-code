def parse_grid_dict(input, func=lambda x: x):
    grid = {}
    for y, line in enumerate(input.splitlines()):
        for x, c in enumerate(line.strip()):
            grid[(x, y)] = func(c)
    return grid

def parse_grid(input, func=lambda x: x):
    grid = []
    for line in input.splitlines():
        grid.append([func(c) for c in line.strip()])
    return grid

def parse_blocks(input):
    return input.split("\n\n")