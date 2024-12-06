from math import inf

def p1(f):
    ans = 0 
    for line in f.read().splitlines():
        first = [x for x in line if x.isdigit()][0]
        last = [x for x in line if x.isdigit()][-1]
        ans += int(first) * 10 + int(last)
    return ans

digits = "0 zero 1 one 2 two 3 three 4 four 5 five 6 six 7 seven 8 eight 9 nine".split()

def p2(f):
    ans = 0
    for line in f.read().splitlines():
        first = min(digits, key=lambda x: line.index(x) if x in line else inf)
        last = min(digits, key=lambda x: line[::-1].index(x[::-1]) if x in line else inf)
        ans += digits.index(first) // 2 * 10 + digits.index(last) // 2
    return ans