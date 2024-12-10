import os
# import download


def solve(rr, cc, res):
    curr = lines[rr][cc]
    if curr == 9:
        distinct_paths[0] += 1
        if (rr, cc) in trailheads:
            return
        trailheads.add((rr, cc))
        return
    for d in dirs:
        x = rr + d[0]
        y = cc + d[1]
        if 0 <= x < RL and 0 <= y < CL and (lines[x][y] - curr) == 1:
            solve(x, y, res)
    return


with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    res1 = 0
    res2 = 0
    dirs = [(-1, 0), (0,  1), (1, 0), (0, -1)]
    lines = f.read().splitlines()
    RL = len(lines)
    CL = len(lines[0])
    a = 0

    for i in range(RL):
        lines[i] = [int(j) for j in lines[i]]

    for r in range(RL):
        for c in range(CL):
            if lines[r][c] == 0:
                trailheads = set()
                distinct_paths = [0]
                solve(r, c, res=0)
                res1 += len(trailheads)
                res2 += distinct_paths[0]

    print(f'Result 1 is: {res1}')
    print(f'Result 2 is: {res2}')
