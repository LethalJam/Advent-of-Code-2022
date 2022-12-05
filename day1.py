import parser_util

calories = parser_util.readList(
    "inputs/1.txt", "string", False, False)

calSum = 0
allSums = []

for calStr in calories:
    if len(calStr) > 0:
        calSum += int(calStr)
    else:
        allSums += [calSum]
        calSum = 0

allSums.sort(reverse=True)
print(sum(allSums[0:3]))
