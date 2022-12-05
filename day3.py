from calendar import c
import parser_util

rugsacks = parser_util.readList("inputs/3.txt", "string", True, False)
# input = parser_util.readAsMatrix("inputs/2.txt", "string", " ")


def part_one():
    sum = 0
    aPrio = ord('a')
    aPrioBig = ord('A')

    for rugsack in rugsacks:
        comp1, comp2 = rugsack[:len(
            rugsack)//2], rugsack[len(rugsack)//2:]
        cSet = set(comp1) & set(comp2)
        cItem = cSet.pop()

        itemPrio = 0
        if (cItem.islower()):
            itemPrio = (ord(cItem)-aPrio)+1
        elif (cItem.isupper()):
            itemPrio = (ord(cItem)-aPrioBig)+27

        sum += itemPrio

    print(sum)


def part_two():

    aPrio = ord('a')
    aPrioBig = ord('A')

    groups = list()

    while len(rugsacks) > 0:
        group = list()
        for x in range(3):
            sack = rugsacks.pop()
            group += [sack]
        groups.append(group)

    sum = 0
    for g in groups:
        cSet = set(g[0]) & set(g[1]) & set(g[2])
        cItem = cSet.pop()

        itemPrio = 0
        if (cItem.islower()):
            itemPrio = (ord(cItem)-aPrio)+1
        elif (cItem.isupper()):
            itemPrio = (ord(cItem)-aPrioBig)+27
        sum += itemPrio

    print(sum)


# part_one()
part_two()
