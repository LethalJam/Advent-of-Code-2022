from re import I
import parser_util

inp = parser_util.readList("inputs/5.txt", "string", False, False)


def stripInts(insts):
    sepInsts = list()
    for inst in insts:
        sep = inst.split(" ")
        sep.remove("move")
        sep.remove("from")
        sep.remove("to")
        sepInsts += [{'move': int(sep[0]),
                      'from': int(sep[1]), 'to': int(sep[2])}]
    return sepInsts


def move_boxes(noOfPiles, reverse):
    boxPic = list()
    piles = list()

    for i in range(noOfPiles):
        piles.append([])

    for i in inp:
        row = inp.pop(0)
        if len(row) > 0:
            boxPic += [row]
        else:
            break
    boxPic.pop()  # Remove row with pile number indication

    for row in boxPic:
        boxNos = list()
        for i in range(noOfPiles):
            boxNo = row[1+4*i]
            if boxNo != ' ':
                piles[i] += boxNo
    print("====BEFORE====")
    print(piles)

    insts = stripInts(inp)

    for inst in insts:
        move = inst.get('move')
        fro = inst.get('from')-1  # to make into index
        to = inst.get('to') - 1  # to make into index

        # Get boxes from
        toMove = piles[fro][0:move]
        if reverse:
            toMove.reverse()
        # Remove taken boxes
        piles[fro] = piles[fro][move:len(piles[fro])]

        # Move to new pile
        piles[to] = toMove + piles[to]

    print("====AFTER====")
    print(piles)

    result = list()
    for p in piles:
        result += p[0]
    print(result)


move_boxes(9, False)
