import os
from copy import deepcopy
# import download

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    res1 = 0
    res2 = 0
    searched = "XMAS"
    dirx, diry = (-1, 0, 1), (-1, 0, 1)
    lines = f.read().splitlines()
    RL = len(lines)
    CL = len(lines[0])

    for r in range(RL):
        for c in range(CL):
            if lines[r][c] == "X":
                for x in dirx:
                    for y in diry:
                        if x == 0 and y == 0:
                            continue
                        temp = "X"
                        temp_r = deepcopy(r)
                        temp_c = deepcopy(c)
                        while True:
                            temp_r += x
                            if not 0 <= temp_r < RL:
                                break
                            temp_c += y
                            if not 0 <= temp_c < CL:
                                break
                            temp += lines[temp_r][temp_c]
                            if len(temp) == 4:
                                if temp == searched:
                                    res1 += 1
                                break

    for r in range(RL):
        for c in range(CL):
            if lines[r][c] == "A":
                valid = True
                for d in (-1, 1):
                    if not 0 <= r + d < RL or not 0 <= c + d < CL:
                        valid = False
                if valid:
                    dir1 = [(-1, -1), (1, 1)]
                    dir2 = [(1, -1), (-1, 1)]
                    found1 = []
                    found2 = []
                    for d in dir1:
                        found1.append(lines[r+d[0]][c+d[1]])
                    for d in dir2:
                        found2.append(lines[r+d[0]][c+d[1]])
                    if "M" in found1 and "M" in found2 and "S" in found1 and "S" in found2:
                        res2 += 1

    print(f'Result 1 is: {res1}')
    print(f'Result 2 is: {res2}')
