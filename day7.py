import parser_util

inp = parser_util.readList("inputs/7.txt", "string", True, False)


def build_tree():

    inp.pop(0)  # Remove initial cd /
    #prevDir = ''
    prevDirStack = []
    currDir = '/'
    tree = {'/': []}
    sizeMap = {'/': 0}

    for l in inp:
        if " ls" in l or "dir" in l:
            continue
        elif "cd " in l:
            cmd = l.split(" ")
            newDir = cmd[2]

            if ".." in newDir:
                currDir = prevDirStack.pop()
            elif newDir == '/':
                currDir = '/'
            else:
                while newDir in sizeMap:
                    newDir = newDir+'x'

                prevDirStack.append(currDir)
                currDir = newDir

                sizeMap.update({currDir: 0})
        else:
            file = l.split(" ")
            sizeMap[currDir] = sizeMap.get(currDir) + int(file[0])

            for pDir in prevDirStack:
                sizeMap[pDir] = sizeMap.get(pDir) + int(file[0])

    result = 0
    for dir in sizeMap.keys():
        if sizeMap.get(dir) <= 100000:
            result += sizeMap.get(dir)
    print("Dirs with size <= 100000")
    print(result)

    maxSpace = 70000000
    needed = 30000000
    unusedSpace = maxSpace - sizeMap.get('/')
    toDelete = needed - unusedSpace
    print("UNUSED")
    print(unusedSpace)
    print("TOL DELETE")
    print(toDelete)

    dSizes = []
    for dir in sizeMap.keys():
        dSizes.append(sizeMap.get(dir))
    dSizes.sort()
    print(dSizes)

    smallestDiff = maxSpace
    smallest = maxSpace
    for d in dSizes:
        if d >= toDelete:
            diff = d - toDelete
            if diff < smallestDiff:
                smallestDiff = diff
                smallest = d
                print(d)

    print("Smallest to delete:")
    print(smallest)


build_tree()
