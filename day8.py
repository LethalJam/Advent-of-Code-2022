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


# print(yTreeList)
#estt = [0, 1, 2, 3, 4, 5]
#around = lists_around(testt, 5)
#print("TESTLIST: ", around)

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

            if x == 1 and y == 2:
                print("TEEEEEEEEEEEEST")
                print(aroundX)
                print(aroundY)
                print("Height: ", treeH)
                print("Maxes X: ", max(aroundX[0]), max(aroundX[1]))

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


for i in matrix:
    print(i)
print("===========================")
for i in visibleMatrix:
    print(i)

print("Visible trees are: ", visibleTrees)
