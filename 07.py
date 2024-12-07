import os
import download


def solve(n, nums):
    if len(nums) == 0:
        if n == value:
            return True
        return False
    elif n > value:
        return False
    if solve(n + nums[0], nums[1:]):
        return True
    return solve(n * nums[0], nums[1:])


def solve2(n, nums):
    if len(nums) == 0:
        if n == value:
            return True
        return False
    elif n > value:
        return False
    if solve2(n + nums[0], nums[1:]):
        return True
    elif solve2(n * nums[0], nums[1:]):
        return True
    return solve2(int(f"{n}{nums[0]}"), nums[1:])


with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    res1 = 0
    res2 = 0
    for line in f.read().splitlines():
        value, numbers = line.split(":")
        value = int(value.strip())
        numbers = [int(i) for i in numbers.split()]
        if solve(numbers[0], numbers[1:]):
            res1 += value
            res2 += value
        else:
            if solve2(numbers[0], numbers[1:]):
                res2 += value
    print(f'Result 1 is: {res1}')
    print(f'Result 2 is: {res2}')
