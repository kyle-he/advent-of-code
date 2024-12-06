def parse_grid_dict(input):
    # make a dictionary of (x, y) -> value
    # return rows and cols too

    for y, line in enumerate(input.splitlines()):
        for x, c in enumerate(line.strip()):
            grid[(x, y)] = c
    
    return grid

def parse_grid(input):
    # make a 2d array of values
    # return rows and cols too

    grid = []
    for line in input.splitlines():
        grid.append(list(line))
    
    return grid

def parse_blocks(input):
    return input.split("\n\n")