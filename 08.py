import os
import download

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    res1 = 0
    res2 = 0
    lines = f.read().splitlines()
    RL = len(lines)
    CL = len(lines[0])

    antennas = []
    pts = []
    for r in range(RL):
        for c in range(CL):
            if lines[r][c] != '.':
                antennas.append((lines[r][c], (r, c)))
                pts.append((r, c))
    antinodes = set()
    more_antinodes = set()
    for i, x in enumerate(antennas):
        lookup, point = x
        for j, y in enumerate(antennas):
            if i < j and y[0] == lookup:
                new_point = y[1]
                more_antinodes.add(point)
                more_antinodes.add(new_point)
                diff_x = new_point[0] - point[0]
                diff_y = new_point[1] - point[1]

                point_ix = point[0] - diff_x
                point_iy = point[1] - diff_y
                c = 0
                while 0 <= point_ix < RL and 0 <= point_iy < CL:
                    if c == 0:
                        antinodes.add((point_ix, point_iy))
                    more_antinodes.add((point_ix, point_iy))
                    point_ix -= diff_x
                    point_iy -= diff_y
                    c += 1

                point_jx = new_point[0]+diff_x
                point_jy = new_point[1]+diff_y
                c = 0
                while 0 <= point_jx < RL and 0 <= point_jy < CL:
                    if c == 0:
                        antinodes.add((point_jx, point_jy))
                    more_antinodes.add((point_jx, point_jy))
                    point_jx += diff_x
                    point_jy += diff_y
                    c += 1
    res1 = len(antinodes)
    res2 = len(more_antinodes)
    print(f'Result 1 is: {res1}')
    print(f'Result 2 is: {res2}')
