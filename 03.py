import os
import re
# import download

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    res1 = 0
    res2 = 0
    do = True
    for line in f.read().splitlines():
        multiplications = re.findall(r"mul\((\d+),(\d+)\)", line)
        for elem in multiplications:
            res1 += int(elem[0])*int(elem[1])

        multiplications_with_commands = re.findall(r"mul\((\d+),(\d+)\)|(do(n't)?\(\))", line)
        for elem in multiplications_with_commands:
            if "do()" in elem:
                do = True
            elif "don't()" in elem:
                do = False
            else:
                if do:
                    res2 += int(elem[0]) * int(elem[1])

    print(f'Result 1 is: {res1}')
    print(f'Result 2 is: {res2}')
