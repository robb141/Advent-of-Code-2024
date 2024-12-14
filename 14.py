import os
import re
import download


with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    res1 = 0
    res2 = 0
    Q1, Q2, Q3, Q4 = 0, 0, 0, 0
    robots = set()
    space = [101, 103]
    lines = f.read().splitlines()
    positions = []
    for line in lines:
        numbers = re.findall(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
        positions.append([int(numbers[0][0]), int(numbers[0][1]), int(numbers[0][2]), int(numbers[0][3])])
    for n in [100, 6644]:
        robots.clear()
        for line in positions:
            new_position = [line[0] + line[2]*n, line[1] + line[3]*n]
            for i in range(len(new_position)):
                if new_position[i] < 0:
                    while new_position[i] < 0:
                        new_position[i] += space[i]
                else:
                    while new_position[i] >= space[i]:
                        new_position[i] -= space[i]
            if n == 100:
                if new_position[0] < space[0] // 2 and new_position[1] < space[1] // 2:
                    Q1 += 1
                elif new_position[0] > space[0] // 2 and new_position[1] > space[1] // 2:
                    Q4 += 1
                elif new_position[0] < space[0] // 2 and new_position[1] > space[1] // 2:
                    Q2 += 1
                elif new_position[0] > space[0] // 2 and new_position[1] < space[1] // 2:
                    Q3 += 1
            robots.add((new_position[0], new_position[1]))
        half = space[0]//2
        symmetrical = 0
        for x in robots:
            if x[0] < half and (half+half-x[0], x[1]) in robots:
                symmetrical += 2
        if symmetrical > len(robots)//5:
            print(f"================================={n}=================================")
            for i in range(space[1]):
                a = ""
                for j in range(space[0]):
                    if j == half:
                        a += "|"
                    elif (j, i) in robots:
                        a += "0"
                    else:
                        a += " "
                print(a)
    res1 = Q1 * Q2 * Q3 * Q4
    print(f'Result 1 is: {res1}')
