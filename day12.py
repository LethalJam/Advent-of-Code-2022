from operator import ne
import parser_util

inp = parser_util.readList("inputs/12.txt", "string", False, False)


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


def a_star(start, goal, grid):
    costMap = {start: 1 + get_manhattan(start, goal)}
    openList = []
    closedList = []
    openList.append(start)

    while len(openList) > 0:

        curr = openList[-1]
        for n in openList:
            if costMap[n] < costMap[curr]:
                curr = n

        if curr == goal:
            break  # closedList is now the path
        openList.remove(curr)
        closedList.append(curr)

        neighb = get_neighbours(curr, len(grid[0])-1, len(grid)-1)
        for nei in neighb:

            # print(nei)
            height = grid[nei[0]][nei[1]]
            climb = height - grid[curr[0]][curr[1]]
            if nei in closedList or climb > 1:  # If elevation higher than 1, dont consider
                continue

            # + height if we use weighted node (heuristic)
            cost = costMap[curr] + get_manhattan(nei, goal) + height

            if nei in openList:
                if cost < costMap[nei]:
                    openList.remove(nei)  # Better cost to nei found
            if nei in closedList:
                if cost < costMap[nei]:
                    closedList.remove(nei)
            if nei not in openList and nei not in closedList:
                openList.append(nei)
                costMap.update({nei: cost})
                # h(n)
                # f(n)
    print(closedList)
    print(len(closedList))


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

print_grid(grid)
print("StartPos: ", start)
print("Goal: ", goal)

a_star(start, goal, grid)
