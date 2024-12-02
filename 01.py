import os
# import download

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    list1, list2 = [], []
    for line in f.read().splitlines():
        a, b = line.split()
        list1.append(int(a))
        list2.append(int(b))
    res1 = 0
    res2 = 0
    for i in zip(sorted(list1), sorted(list2)):
        res1 += abs(i[0] - i[1])
        res2 += i[0] * list2.count(i[0])
    print(f'Result 1 is: {res1}')
    print(f'Result 2 is: {res2}')
