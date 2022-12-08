import parser_util

inp = parser_util.readList("inputs/8.txt", "string", True, False)


def lists_around(l, e: int):
    behind = l[0:e]
    front = list
    if e < len(l):
        front = l[e+1:len(l)]
    else:
        front = []

    return [behind, front]


def get_y_trees(matrix, myY):
    yTrees = list()
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if y == myY:
                yTrees.append(matrix[x][y])

    return yTrees


matrix = list()  # [y][x]
visibleMatrix = list()

for i in inp:
    insideList = list()
    visListIns = list()
    for no in i:
        insideList.append(int(no))
        visListIns.append(0)
    matrix.append(insideList)
    visibleMatrix.append(visListIns)

visibleTrees = 0
flippedMatrix = list()

for i in range(len(matrix)):
    flippedMatrix.append(get_y_trees(matrix, i))

scenicScores = []
for y in range(len(matrix)):
    lowestTree = 0
    for x in range(len(matrix[y])):
        treeH = matrix[y][x]
        if x == 0 or y == 0 or y == len(matrix)-1 or x == len(matrix[y])-1:
            visibleTrees += 1
            visibleMatrix[y][x] = 1
        else:
            xTrees = matrix[y]
            yTrees = flippedMatrix[x]
            aroundX = lists_around(xTrees, x)
            aroundY = lists_around(yTrees, y)

            visible = bool
            if treeH <= max(aroundX[0]) and treeH <= max(aroundX[1]):
                visible = False
                visibleMatrix[y][x] = 0
            else:
                visible = True
                visibleMatrix[y][x] = 1

            if treeH <= max(aroundY[0]) and treeH <= max(aroundY[1]):
                if not visible:
                    visible = False
                visibleMatrix[y][x] = 0
            else:
                visible = True
                visibleMatrix[y][x] = 1

            if visible:
                visibleTrees += 1

            up = aroundY[0]
            down = aroundY[1]
            left = aroundX[0]
            right = aroundX[1]
            down.reverse()
            right.reverse()
            dirLists = [up, left, down, right]

            scores = [0,0,0,0]
            for treeIndex in range(len(dirLists)):

                dirList = dirLists[treeIndex]
                while len(dirList) > 0:
                    scores[treeIndex] += 1
                    if dirList[-1] >= treeH:
                        break
                    dirList.pop()
                    
                    
            scenicScores.append(scores[0] * scores[1] * scores[2] * scores[3])

print("Visible trees are: ", visibleTrees)
print("Highest scenics score is: ", max(scenicScores))
