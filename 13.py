import os
import re
import download


def solve_equation():
    if (a[1] * prizes[0] - prizes[1] * a[0]) % (b[0] * a[1] - b[1] * a[0]) != 0:
        return False
    y = (a[1] * prizes[0] - prizes[1] * a[0]) // (b[0] * a[1] - b[1] * a[0])
    if (prizes[0] - b[0] * y) % a[0] != 0:
        return False
    x = (prizes[0] - b[0] * y) // a[0]
    return x, y


with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    res1 = 0
    res2 = 0
    SEEN = []
    turn_count = 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    lines = f.read().split('\n\n')
    lines = [line.split('\n') for line in lines]
    for line in lines:
        a = [int(x) for x in re.findall(r'\+(\d+)', line[0])]
        b = [int(x) for x in re.findall(r'\+(\d+)', line[1])]
        prizes = [int(x) for x in re.findall(r'=(\d+)', line[2])]

        temp_solve = solve_equation()
        if temp_solve:
            res1 += temp_solve[0]*3 + temp_solve[1]

        prizes = [x+10000000000000 for x in prizes]
        temp_solve = solve_equation()
        if temp_solve:
            res2 += temp_solve[0]*3 + temp_solve[1]

    print(f'Result 1 is: {res1}')
    print(f'Result 2 is: {res2}')
