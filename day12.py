from operator import ne
import parser_util

inp = parser_util.readList("inputs/12.txt", "string", False, False)


def print_path(path, grid):
    print("========= Grid =========")
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            coord = (y, x)
            if coord in path:
                print("#", end='')
            else:
                print("X", end='')
        print("")


def print_grid(grid):
    print("========= Grid =========")
    for i in grid:
        print(i)


def get_neighbours(pos, maxX, maxY):
    posY = pos[0]
    posX = pos[1]
    neighb = list()
    if posX != 0:
        neighb.append((posY, posX-1))
    if posY != 0:
        neighb.append((posY-1, posX))
    if posX < maxX:
        neighb.append((posY, posX+1))
    if posY < maxY:
        neighb.append((posY+1, posX))
    return neighb


def get_manhattan(pos, goal) -> int:
    distY = abs(goal[0] - pos[0])
    distX = abs(goal[1] - pos[1])

    return distY + distX


def get_path(cameFrom, start, end):

    path = list()
    curr = end
    while curr != start:
        curr = cameFrom[curr]
        path.append(curr)
    return path


def a_star(start, goal, grid):

    costMap = {start: get_manhattan(start, goal)}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if y != 0 and x != 0:
                costMap.update({(y, x): 99999})

    openList = []
    closedList = []
    cameFrom = {(0, 0): (-1, -1)}
    path = list()
    openList.append(start)

    while len(openList) > 0:

        curr = openList[-1]
        for n in openList:
            if costMap[n] < costMap[curr]:
                curr = n

        if curr == goal:
            path = get_path(cameFrom, start, curr)
            break
        openList.remove(curr)
        closedList.append(curr)

        neighb = get_neighbours(curr, len(grid[0])-1, len(grid)-1)
        for nei in neighb:

            height = grid[nei[0]][nei[1]]
            climb = height - grid[curr[0]][curr[1]]
            if nei in closedList or climb > 1:  # Already considered or too high
                continue

            # + height if we use weighted node (heuristic)
            cost = costMap[curr] + get_manhattan(curr, nei)

            if nei in openList and cost < costMap[nei]:
                openList.remove(nei)
            if nei in closedList and cost < costMap[nei]:
                closedList.remove(nei)
            if nei not in openList and nei not in closedList:
                openList.append(nei)
                costMap.update({nei: cost})
                cameFrom.update({nei: curr})

    print(path)
    print(len(path))


grid = list()  # [y][x]
start = (0, 0)  # (y,x)
goal = (0, 0)  # (y,x)

for i in range(len(inp)):
    row = list()
    for c in range(len(inp[i])):
        newChar = inp[i][c]
        if newChar == 'S':
            newChar = 'a'
            start = (i, c)
        elif newChar == 'E':
            newChar = 'z'
            goal = (i, c)

        value = abs(ord('a')-ord(newChar))
        row.append(value)
    grid.append(row)


print("StartPos: ", start)
print("Goal: ", goal)

a_star(start, goal, grid)
