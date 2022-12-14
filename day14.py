import parser_util


def move_point(grid, p):

    if grid[p[0]+1][p[1]] == ".":  # Down
        return (p[0]+1, p[1])
    elif grid[p[0]+1][p[1]+1] == ".":  # Down-Left
        return (p[0]+1, p[1]+1)
    elif grid[p[0]+1][p[1]-1] == ".":  # Down-Right
        return (p[0]+1, p[1]-1)
    else:
        return p


def drop_sand(grid, maxX, breakAtBound):
    oob = False
    point = (0, maxX-500)
    while True:
        newPoint = move_point(grid, point)
        if newPoint == point:  # Hasn't moved -> Done
            grid[point[0]][point[1]] = 'O'
            if not breakAtBound and newPoint == (0, maxX-500):
                oob = True
            break
        point = newPoint

        if point[0]+1 == len(grid) and breakAtBound:
            oob = True
            break
        elif point[1]+1 == len(grid[0]) and breakAtBound:
            oob = True
            break
    return oob


def fill_cave(grid, maxX, breakAtBound):

    noOfSand = 0
    while not drop_sand(grid, maxX, breakAtBound):
        noOfSand += 1
    print("Sand required: ", noOfSand)


def parse_grid(grid, maxX, paths):
    grid[0][maxX - 500] = "+"

    for p in paths:
        coords = [c.split(",") for c in p.split("->")]
        coords = [(int(c[1]), maxX - int(c[0])) for c in coords]

        while len(coords) > 1:
            left = coords[0]
            right = coords[1]
            yP = left[0]
            xP = left[1]
            grid[left[0]][left[1]] = "#"
            grid[right[0]][right[1]] = "#"

            while (yP, xP) != right:
                if yP < right[0]:
                    yP += 1
                if yP > right[0]:
                    yP -= 1

                if xP < right[1]:
                    xP += 1
                if xP > right[1]:
                    xP -= 1

                grid[yP][xP] = "#"

            coords.pop(0)

    return grid


def min_max_coords(lines):
    xList = list()
    yList = list()
    for l in lines:
        coords = l.split("->")
        for c in coords:
            coord = c.split(",")
            xList.append(int(coord[0]))
            yList.append(int(coord[1]))

    return [(min(yList), min(xList)), (max(yList), max(xList))]


def print_grid(grid):
    for r in grid:
        for c in r:
            print(c, end='')
        print("")


inp = parser_util.readList("inputs/14.txt", "string", True, False)

dim = min_max_coords(inp)
print("Grid dimensions: ", dim)
min = dim[0]
max = dim[1]
padding = 300
max = (max[0], max[1]+padding)

grid = list()
for y in range(max[0] + 1):
    row = list()
    for x in range(max[1]+1 - min[1]):
        row.append('.')
    grid.append(row)

### PART 2 #######

emptRow = list()
for x in range(max[1]+1 - min[1]):
    emptRow.append('.')
grid.append(emptRow)

emptRow = list()
for x in range(max[1]+1 - min[1]):
    emptRow.append('#')
grid.append(emptRow)

### PART 2 #######

# EACH COORD = (Y=Y, X = (max(x) - X))
grid = parse_grid(grid, max[1]-int(padding/2), inp)

#
fill_cave(grid, max[1]-int(padding/2), False)  # True = P1, False = P2

print_grid(grid)
