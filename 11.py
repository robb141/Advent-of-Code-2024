import os
from collections import defaultdict
import download


def solve(checked, cycle):
    if isinstance(checked, list):
        res = 0
        for elem in checked:
            dic[(elem, cycle)] = solve(elem, cycle)
            if cycle == 0:
                res += dic[(elem, cycle)]
        if cycle == 0:
            return res
    else:
        if cycle == target:
            return 1
        else:
            if checked == "0":
                return dic[("1", cycle + 1)] if ("1", cycle + 1) in dic else solve("1", cycle + 1)
            elif len(checked) % 2 == 0:
                first = checked[0:len(checked)//2]
                second = str(int(checked[len(checked)//2:]))
                if (first, cycle + 1) in dic:
                    g = dic[(first, cycle + 1)]
                else:
                    dic[(first, cycle + 1)] = solve(first, cycle + 1)
                    g = dic[(first, cycle + 1)]
                if (second, cycle + 1) in dic:
                    h = dic[(second, cycle + 1)]
                else:
                    dic[(second, cycle + 1)] = solve(second, cycle + 1)
                    h = solve(second, cycle + 1)
                return g + h
            else:
                if (str(int(checked)*2024), cycle + 1) in dic:
                    return dic[(str(int(checked)*2024), cycle + 1)]
                else:
                    dic[(str(int(checked) * 2024), cycle + 1)] = solve(str(int(checked)*2024), cycle + 1)
                    return dic[(str(int(checked) * 2024), cycle + 1)]


with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    res1 = 0
    res2 = 0
    dic = defaultdict(int)
    line = f.readline().split()
    line[-1].strip()
    target = 25
    res1 = solve(line, 0)
    dic = defaultdict(int)
    target = 75
    res2 = solve(line, 0)
    print(f'Result 1 is: {res1}')
    print(f'Result 2 is: {res2}')
