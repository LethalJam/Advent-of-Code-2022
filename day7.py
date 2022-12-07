import parser_util

inp = parser_util.readList("inputs/7.txt", "string", True, False)

def build_tree():
    prevDirStack = []
    currDir = '/'
    sizeMap = {'/': 0}
    
    for l in inp:
        fil = l.split(" ")
        if "$ ls" in l or "dir" in l:
            continue
        elif "$ cd" in l:
            cmd = l.split(" ")
            newDir = cmd[2]

            if ".." in newDir:
                currDir = prevDirStack.pop()
            elif newDir == '/':
                prevDirStack = []
                currDir = '/'
            else:
                while newDir in sizeMap.keys():
                    newDir = newDir+'x'

                prevDirStack.append(currDir)
                currDir = newDir

                sizeMap.update({currDir: 0})
        else:
            sizeMap[currDir] = sizeMap.get(currDir) + int(fil[0])

            for pDir in prevDirStack:
                sizeMap[pDir] += int(fil[0])

    result = 0
    for d in sizeMap.keys():
        if sizeMap.get(d) <= 100000:
            result += sizeMap.get(d)
    print("Dirs with size <= 100000: ", result)

    maxSpace = 70000000
    needed = 30000000
    unusedSpace = maxSpace - sizeMap.get('/')

    dSizes = []
    for d in sizeMap.keys():
        dSizes.append(sizeMap.get(d))

    dSizes = [d for d in dSizes if d+unusedSpace > needed]
    dSizes.sort()
    print("Delete folder with size: ", min(dSizes))

build_tree()
