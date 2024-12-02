import os
from copy import deepcopy
# import download

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    res1 = 0
    res2 = 0
    for line in f.read().splitlines():
        line = [int(i) for i in line.split()]
        diffs = []
        for i in range(len(line) - 1):
            diffs.append(line[i + 1] - line[i])
        diff_len = len(diffs)
        decr = len([x for x in diffs[1:] if x in [-1, -2, -3]])
        incr = len([x for x in diffs[1:] if x in [1, 2, 3]])
        if decr > 1:
            decreasing = True
            if diff_len - len([x for x in diffs if x in [-1, -2, -3]]) == 0:
                res1 += 1
                res2 += 1
                continue
            elif diff_len - decr == 0:
                res2 += 1
                continue
        else:
            decreasing = False
            if diff_len - len([x for x in diffs if x in [1, 2, 3]]) == 0:
                res1 += 1
                res2 += 1
                continue
            elif diff_len - incr == 0:
                res2 += 1
                continue

        for i in range(len(line)):
            copied_line = deepcopy(line)
            copied_line.pop(i)
            new_diffs = []
            for j in range(len(copied_line) - 1):
                new_diffs.append(copied_line[j + 1] - copied_line[j])
            diff_len = len(new_diffs)
            if decreasing:
                if diff_len - len([x for x in new_diffs if x in [-1, -2, -3]]) == 0:
                    res2 += 1
                    break
            else:
                if diff_len - len([x for x in new_diffs if x in [1, 2, 3]]) == 0:
                    res2 += 1
                    break
    print(f'Result 1 is: {res1}')
    print(f'Result 2 is: {res2}')
