import os
from copy import deepcopy
# import download


def checksum(dic):
    position = 0
    res = 0
    for a in dic:
        if dic[a][0]:
            for b in dic[a][0]:
                while b[1] != 0:
                    res += (b[0] * position)
                    b[1] -= 1
                    position += 1
            position += dic[a][1]
    return res


with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    res1 = 0
    res2 = 0
    line = f.readline().strip()
    current_id = len(line) // 2
    d1 = {}
    id_num = 0
    for i, start in enumerate(line):
        if i % 2 == 0:
            if i + 1 < len(line):
                # id of number = number of times, number of spaces after
                d1[id_num] = [[[id_num, int(start)]], int(line[i + 1])]
                id_num += 1
            elif i+1 == len(line):
                d1[id_num] = [[[id_num, int(start)]], 0]

    d2 = deepcopy(d1)
    for i in reversed(d2):
        if i == 0:
            break
        for j in d2:
            if j < i:
                if j in d1:
                    while d1[j][1] != 0:
                        if current_id != d1[j][0][-1][0]:
                            d1[j][0].append([current_id, 1])
                        else:
                            d1[j][0][-1][1] += 1
                        d1[current_id][0][-1][1] -= 1
                        if d1[current_id][0][0][1] == 0:
                            d1.pop(current_id)
                            current_id -= 1
                        d1[j][1] -= 1
                if d2[j][1] >= d2[i][0][0][1]:
                    popped = d2[i][0].pop(0)
                    d2[j][0].append(popped)
                    d2[j][1] -= popped[1]
                    d2[i - 1][1] += popped[1]
                    if not d2[i][0]:
                        k = i - 1
                        while True:
                            if k in d2:
                                d2[k][1] += d2[i][1]
                                d2[i][1] = 0
                                break
                            k -= 1
                    break
            else:
                break

    res1 = checksum(d1)
    res2 = checksum(d2)

    print(f'Result 1 is: {res1}')
    print(f'Result 2 is: {res2}')
