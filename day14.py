from ast import parse
from site import execsitecustomize
import parser_util


def parse_grid(grid, maxX, padding, paths):
    return None


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


inp = parser_util.readList("inputs/14.txt", "string", True, False)

dim = min_max_coords(inp)
print("Grid dimensions: ", dim)
min = dim[0]
max = dim[1]
xPadding = 5  # Empty side on each side of cave structure

# Add padding on each side. Offset X-coords with padding
gridRow = [" . "] * ((max[1] - min[1]) + (xPadding * 2))
# Keep the diff between min and max as room for sand to move
grid = [gridRow] * (max[0] + 1)

print("gridX: ", len(gridRow))
print("gridY: ", len(grid))

# EACH COORD = (Y=Y, X = (max(x) - X) + xPadding)
grid = parse_grid(grid, max[1], xPadding, inp)
