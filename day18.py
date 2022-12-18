import copy
import parser_util


def get_neighbours(c):
    neighbs = list()
    neighbs.append((c[0]+1, c[1], c[2]))
    neighbs.append((c[0]-1, c[1], c[2]))
    neighbs.append((c[0], c[1]+1, c[2]))
    neighbs.append((c[0], c[1]-1, c[2]))
    neighbs.append((c[0], c[1], c[2]+1))
    neighbs.append((c[0], c[1], c[2]-1))
    return neighbs


def get_neighbours_outer(c, coords, range):
    neighbs = list()
    min = range[0]
    max = range[1]
    if c[0]+1 < max:
        neighbs.append((c[0]+1, c[1], c[2]))
    if c[0]-1 > min:
        neighbs.append((c[0]-1, c[1], c[2]))
    if c[1]+1 < max:
        neighbs.append((c[0], c[1]+1, c[2]))
    if c[1]-1 > min:
        neighbs.append((c[0], c[1]-1, c[2]))
    if c[2]+1 < max:
        neighbs.append((c[0], c[1], c[2]+1))
    if c[2]-1 > min:
        neighbs.append((c[0], c[1], c[2]-1))

    lavaEdges = [x for x in neighbs if x in coords]
    return ([x for x in neighbs if x not in coords], len(lavaEdges))


def parse_cube_coords(inp):

    coords = list()
    for i in inp:
        poses = i.split(",")
        coords.append((int(poses[0]), int(poses[1]), int(poses[2])))
    return coords


def get_real_neighbours(piv, coords):
    nL = list()
    p_nL = get_neighbours(piv)
    for pN in p_nL:
        if pN in coords:
            nL.append(pN)
    return nL


def get_no_sides_breadth(coords, root, sides):
    xpl = [root]
    q = [root]

    while len(q) > 0:
        c = q.pop(0)
        nL = get_real_neighbours(c, coords)
        sides += 6 - len(nL)

        for n in nL:
            if n not in xpl:
                xpl.append(n)
                q.append(n)

    unExpl = [x for x in coords if x not in xpl]
    return (sides, unExpl)


def get_no_sides_outher_breadth(coords, sides, range):
    min = range[0]
    xpl = [(min, min, min)]
    q = [(min, min, min)]

    while len(q) > 0:
        c = q.pop(0)
        (nL, lava) = get_neighbours_outer(c, coords, range)
        sides += lava

        for n in nL:
            if n not in xpl:
                xpl.append(n)
                q.append(n)

    return sides


inp = parser_util.readList("inputs/18.txt", "string", True, False)

coords = parse_cube_coords(inp)
coords2 = copy.copy(coords)

sides = 0
while len(coords) > 0:
    (sideAdd, coords) = get_no_sides_breadth(
        coords, coords[0], 0)
    sides += sideAdd
print("Total sides: ", sides)

sides = 0
sides = get_no_sides_outher_breadth(coords2, sides, (-10, 30))
print("Total outer sides: ", sides)
