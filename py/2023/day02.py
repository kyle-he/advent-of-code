def p1(f):
    ans = 0 

    for line in f.read().splitlines():
        game, groups = line.split(": ")
        _, game_id = game.split()
        
        valid = True
        for num, color in [tuple(x.split()) for x in groups.replace(";", ",").split(",")]:
            num = int(num)
            if color == "red" and num > 12:
                valid = False
            elif color == "green" and num > 13:
                valid = False
            elif color == "blue" and num > 14:
                valid = False
        
        if valid:
            ans += int(game_id)
    
    return ans


def p2(f):
    ans = 0

    for line in f.read().splitlines():
        game, groups = line.split(": ")
        _, game_id = game.split()
        
        max_r = 0
        max_g = 0
        max_b = 0
        for num, color in [tuple(x.split()) for x in groups.replace(";", ",").split(",")]:
            num = int(num)
            if color == "red":
                max_r = max(max_r, num)
            elif color == "green":
                max_g = max(max_g, num)
            elif color == "blue":
                max_b = max(max_b, num)
        
        ans += max_r * max_g * max_b
    
    return ans