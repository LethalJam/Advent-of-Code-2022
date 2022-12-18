import parser_util


def get_manhattan(pos1, pos2):
    xDiff = abs(pos2[0] - pos1[0])
    yDiff = abs(pos2[1] - pos1[1])
    return xDiff + yDiff


def get_beacon_pairs(inp):
    beaconMap = dict()
    for l in inp:
        [str1, str2] = l.split(": closest beacon is at ")
        [xStr, yP] = str1.split(", y=")
        [_, xP] = xStr.split("x=")
        sensor = (int(xP), int(yP))

        [xStr, yP] = str2.split(", y=")
        [_, xP] = xStr.split("x=")
        beacon = (int(xP), int(yP))

        beaconMap.update({sensor: beacon})
    return (beaconMap)


def get_positions_at_y(y, set):
    count = 0
    for p in set:
        if p[1] == y:
            count += 1
    return count


inp = parser_util.readList("inputs/15.txt", "string", True, False)

beaconMap = get_beacon_pairs(inp)
posSet = set()
posRange = dict()  # yCoord: [(minX, maxY) .. ]

for sens in beaconMap:
    maxDist = get_manhattan(sens, beaconMap.get(sens))
    yPos = sens[1]
    yUp = sens[1]-maxDist
    yDown = sens[1]+maxDist

    xpInd = 0
    for y in range(yUp, yDown+1):
        minX = sens[0]-xpInd
        maxX = sens[0]+xpInd
        # if y in posRange:
        #    ranges = posRange.get(y)
        #    for r in ranges:
        #        if minX >= r[0] and minX <= r[0]:
        #            minX = maxX
        #        if maxX < =
        #    posRange.get(y).append((minX, maxX))
        # else:
        #    posRange.update({y: [(minX, maxX)]})
        # for x in range(sens[0]-xpInd, sens[0]+xpInd+1):
        #    posSet.update({(x, y)})
        if y < sens[1]:
            xpInd += 1
        elif y >= sens[1]:
            xpInd -= 1

# print(posSet)
print("Positions at 10: ", posRange.get(10))
