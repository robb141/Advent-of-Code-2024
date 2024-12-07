import os
from copy import deepcopy
import download

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    res1 = 0
    res2 = 0
    searched = []
    turn_count = 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    lines = f.read().splitlines()
    RL = len(lines)
    CL = len(lines[0])
    flag_done = False
    for r in range(RL):
        for c in range(CL):
            if lines[r][c] in ["^"]:
                new_r = deepcopy(r)
                new_c = deepcopy(c)
                searched.append((r, c))
                while True:
                    curr_dir = directions[turn_count % len(directions)]
                    temp_r = curr_dir[0]+new_r
                    temp_c = curr_dir[1]+new_c
                    if temp_r < 0 or temp_r >= RL or temp_c < 0 or temp_c >= CL:
                        flag_done = True
                        break
                    elif lines[temp_r][temp_c] == "#":
                        turn_count += 1
                    else:
                        if (temp_r, temp_c) in searched:
                            indices = [i for i, x in enumerate(searched) if x == (temp_r, temp_c)]
                            for i in indices:
                                if i == 0:
                                    continue
                                else:
                                    if searched[-1] == searched[i-1]:
                                        flag_done = True
                        new_r += curr_dir[0]
                        new_c += curr_dir[1]
                        searched.append((new_r, new_c))
                    if flag_done:
                        break

                loop_count = 0
                loops = []
                for obstacle in set(searched):
                    searched2 = []
                    turn_count = 0
                    new_r = deepcopy(r)
                    new_c = deepcopy(c)
                    flag_done = False
                    while True:
                        curr_dir = directions[turn_count % len(directions)]
                        temp_r = curr_dir[0] + new_r
                        temp_c = curr_dir[1] + new_c
                        if temp_r < 0 or temp_r >= RL or temp_c < 0 or temp_c >= CL:
                            flag_done = True
                            break
                        elif lines[temp_r][temp_c] == "#" or (temp_r, temp_c) == obstacle:
                            turn_count += 1
                        else:
                            if (temp_r, temp_c) in searched2:
                                indices = [i for i, x in enumerate(searched2) if x == (temp_r, temp_c)]
                                for i in indices:
                                    if i == 0:
                                        continue
                                    else:
                                        if searched2[-1] == searched2[i - 1]:
                                            loop_count += 1
                                            loops.append(obstacle)
                                            flag_done = True
                            new_r += curr_dir[0]
                            new_c += curr_dir[1]
                            searched2.append((new_r, new_c))
                        if flag_done:
                            break

    res1 = len(set(searched))
    print(loops)
    print(f'Result 1 is: {res1}')
    print(f'Result 2 is: {loop_count}')
