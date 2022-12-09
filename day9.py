import parser_util

inp = parser_util.readList("inputs/9.txt", "string", True, False)


def part_one():
    head = {'x': 0, 'y': 0}
    tail = {'x': 0, 'y': 0}

    tailPositions = [(0, 0)]  # list of tuples

    for i in inp:
        cmd = i.split(" ")
        dirr = cmd[0]
        mov = int(cmd[1])

        for step in range(mov):
            headPrevX = head['x']
            headPrevY = head['y']
            # Move Head
            if dirr == 'R':
                head['x'] += 1
            elif dirr == 'L':
                head['x'] -= 1
            elif dirr == 'U':
                head['y'] += 1
            elif dirr == 'D':
                head['y'] -= 1

            # Update Tail
            xDiff = abs(head['x'] - tail['x'])
            yDiff = abs(head['y'] - tail['y'])

            if xDiff > 1 or yDiff > 1:  # Update position
                tail['x'] = headPrevX
                tail['y'] = headPrevY
                tailTuple = (tail['x'], tail['y'])
                if tailTuple not in tailPositions:
                    tailPositions.append(tailTuple)

    print("Number of visited tail positions: ", len(tailPositions))


def part_two():

    rope = [{'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 0}]  # 0 is head, -1 is tail
    tailSet = {(0, 0)}

    for i in inp:
        cmd = i.split(" ")
        dirr = cmd[0]
        mov = int(cmd[1])

        for step in range(mov):

            # Move Head
            if dirr == 'R':
                rope[0]['x'] += 1
            elif dirr == 'L':
                rope[0]['x'] -= 1
            elif dirr == 'U':
                rope[0]['y'] += 1
            elif dirr == 'D':
                rope[0]['y'] -= 1

            for r in range(len(rope)):

                if r+1 < len(rope):
                    xDiff = rope[r]['x'] - rope[r+1]['x']
                    yDiff = rope[r]['y'] - rope[r+1]['y']

                    xDir = -1 if xDiff < 0 else 1
                    yDir = -1 if yDiff < 0 else 1
                    if abs(xDiff) > 1 and yDiff == 0:
                        rope[r+1]['x'] += xDir
                    elif abs(yDiff) > 1 and xDiff == 0:
                        rope[r+1]['y'] += yDir
                    elif abs(xDiff) > 1 or abs(yDiff) > 1:
                        rope[r+1]['x'] += xDir
                        rope[r+1]['y'] += yDir

                else:  # We have reached the tail and finished updates
                    setUpdate = {(rope[-1]['x'], rope[-1]['y'])}
                    tailSet.update(setUpdate)

    print("Number of visited tail positions: ", len(tailSet))


part_one()
part_two()
