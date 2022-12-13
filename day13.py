from ast import parse
import parser_util

inp = parser_util.readList("inputs/13.txt", "string", False, False)


def parse_list(line):
    pList = []
    for cI in range(len(line)):
        print(cI)
        if line[cI] == '[':
            resL = parse_list(line[cI+1:len(line)])
            pList.append(resL[0])
            if resL[1] < len(line):
                resR = parse_list(line[resL[1]:len(line)])
                pList.append(resR[0])
            return (pList, len(line))
        elif line[cI] == ']':
            return (pList, cI)
        elif line[cI] == ',':
            continue
        else:
            pList.append(int(line[cI]))


pairs = list()
pairs.append(([[], []]))

testList = parse_list(inp[3][1:len(inp[3])])
print(testList)

for i in inp:
    ind = 0
    if len(i) == 0:
        ind = 0
        pairs.append(([], []))
    else:
        # parse_list(i)
        ind += 1

# print(pairs)
