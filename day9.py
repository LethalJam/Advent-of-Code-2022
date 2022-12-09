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
    head = {'x': 0, 'y': 0}
    rope = [{'x': 0, 'y': 0}, {'x': 0, 'y': 0}, {'x': 0, 'y': 0}, {'x': 0, 'y': 0}, {
        'x': 0, 'y': 0}, {'x': 0, 'y': 0}, {'x': 0, 'y': 0}, {'x': 0, 'y': 0}, {'x': 0, 'y': 0}]  # 0 is tail, -1 is front

    # tailPositions = [(0, 0)]  # list of tuples
    tailSet = {(0, 0)}

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

            # Update Rope
            front = rope[-1]
            xDiff = abs(head['x'] - front['x'])
            yDiff = abs(head['y'] - front['y'])

            if xDiff > 1 or yDiff > 1:  # Update position
                #tail['x'] = headPrevX
                #tail['y'] = headPrevY
                headPrevX = front['x']
                headPrevY = front['y']
                rope.append({'x': headPrevX, 'y': headPrevY})  # Move front
                rope.pop(0)  # Move back

                upSet = {(rope[0]['x'], rope[0]['y'])}
                tailSet.update(upSet)

                # for r in rope:
                #    tailTuple = (r['x'], r['y'])
                #    if tailTuple not in tailPositions:
                #        tailPositions.append(tailTuple)

            for i in range(len(rope)):
                if i+1 < len(rope):
                    seg1 = rope[0]
                    seg2 = rope[1]

                    xDiff = abs(seg1['x'] - seg2['x'])
                    yDiff = abs(seg1['y'] - seg2['y'])

                    if xDiff > 1 or yDiff > 1:
                        seg2 = rope[i]
                        headPrevX = seg2['x']
                        headPrevY = seg2['y']

    print(tailSet)
    print("Number of visited tail positions: ", len(tailSet))


part_one()
part_two()
