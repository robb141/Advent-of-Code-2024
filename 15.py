import os
import download


def print_storage_map():
    for i in range(len(STORAGE_MAP)):
        line = ''
        for j in range(2*len(STORAGE_MAP[0])):
            found = False
            for g in BOXES:
                if [i, j] in g:
                    if [i, j] == g[0]:
                        line += "["
                    else:
                        line += "]"
                    found = True
                    break
            if found:
                continue
            if [i, j] in WALLS:
                line += "#"
            elif robot == [i, j]:
                line += "@"
            else:
                line += "."
        print(line)


def solve():
    global next_moves, BOXES
    SEEN = []
    SEEN2 = []
    SEEN += [bb for bb in BOXES if [robot[0] + r, robot[1] + c] in bb][0]
    while True:
        SEEN2.clear()
        for elem in SEEN:
            if [elem[0] + r, elem[1] + c] in WALLS:
                return False
            if [bb for bb in BOXES if [elem[0] + r, elem[1] + c] in bb]:
                for e in [bb for bb in BOXES if [elem[0] + r, elem[1] + c] in bb][0]:
                    SEEN2.append(e)
        SEEN.clear()
        for s in SEEN2:
            for bb in BOXES:
                if s in bb and s not in SEEN:
                    SEEN.append(s)
                    next_moves.append(s)
        if not SEEN:
            return True


with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    res1 = 0
    res2 = 0
    DIRECTIONS = {"^": (-1, 0), ">":  (0, 1), "v": (1, 0), "<": (0, -1)}
    STORAGE_MAP, MOVES = f.read().split('\n\n')
    STORAGE_MAP = STORAGE_MAP.split('\n')
    MOVES = MOVES.replace("\n", "")
    WALLS = []
    BOXES = []
    for i in range(len(STORAGE_MAP)):
        for j in range(len(STORAGE_MAP[0])):
            if STORAGE_MAP[i][j] == "#":
                WALLS.append([i, j])
            elif STORAGE_MAP[i][j] == "O":
                BOXES.append([i, j])
            elif STORAGE_MAP[i][j] == "@":
                robot = [i, j]
    for move in MOVES:
        r, c = DIRECTIONS[move]
        new_position = [r + robot[0], c + robot[1]]
        new_r, new_c = new_position
        if new_position in WALLS:
            continue
        elif new_position in BOXES:
            while STORAGE_MAP[new_r][new_c] != "#":
                if [new_r, new_c] not in WALLS + BOXES:
                    index = BOXES.index([r + robot[0], c + robot[1]])
                    BOXES[index] = [new_r, new_c]
                    robot = [r + robot[0], c + robot[1]]
                    break
                new_r, new_c = new_r + r, new_c + c
        else:
            robot = [new_r, new_c]
    for b in BOXES:
        res1 += (100 * b[0] + b[1])

    WALLS = []
    BOXES = []
    for i in range(len(STORAGE_MAP)):
        for j in range(len(STORAGE_MAP[0])):
            if STORAGE_MAP[i][j] == "#":
                WALLS.append([i, 2 * j])
                WALLS.append([i, 2 * j + 1])
            elif STORAGE_MAP[i][j] == "O":
                BOXES.append([[i, 2 * j], [i, 2 * j + 1]])
            elif STORAGE_MAP[i][j] == "@":
                robot = [i, 2*j]

    for move in MOVES:
        r, c = DIRECTIONS[move]
        new_position = [r + robot[0], c + robot[1]]
        new_r, new_c = new_position
        found = False
        flag_finish = False
        for box in BOXES:
            if [new_r, new_c] in box:
                found = True
                if move in [">", "<"]:
                    while [new_r, new_c] not in WALLS:
                        if all([new_r, new_c] not in bb for bb in BOXES):
                            c_modif = abs(robot[1] - new_c) - 1
                            for i in range(1, c_modif, 2):
                                searched = [bb for bb in BOXES if [new_r, new_c - i * c] in bb][0]
                                index = BOXES.index(searched)
                                BOXES[index][0] = [BOXES[index][0][0], BOXES[index][0][1] + c]
                                BOXES[index][1] = [BOXES[index][1][0], BOXES[index][1][1] + c]
                            robot = new_position
                            break
                        new_r, new_c = new_r + r, new_c + c
                else:
                    next_moves = []
                    next_moves += [bb for bb in BOXES if [new_r, new_c] in bb][0]
                    result = solve()
                    if result:
                        for m in range(len(next_moves) - 1, -1, -2):
                            index = BOXES.index([next_moves[m - 1], next_moves[m]])
                            BOXES[index][0] = [BOXES[index][0][0] + r, BOXES[index][0][1]]
                            BOXES[index][1] = [BOXES[index][1][0] + r, BOXES[index][1][1]]
                        robot = new_position
                break
        if found:
            continue
        if new_position in WALLS:
            continue
        else:
            robot = [new_r, new_c]

    for b in BOXES:
        res2 += (100 * b[0][0] + b[0][1])

    print(f'Result 1 is: {res1}')
    print(f'Result 2 is: {res2}')
