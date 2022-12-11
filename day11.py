import parser_util
import math

inp = parser_util.readList("inputs/11.txt", "string", False, False)

mToItems = {0: []}  # Carried items
mToOp = {0: ('+', 1)}  # Operator
mToDivTest = {0: 3}  # Divisible test number
mToThrow = {0: (1, 2)}  # Which monkey to throw to

timesInspected = list()
maxDivNo = 1


def update_item_value(value, op, divBy3):
    newValue = 0
    if op[0] == '+':
        if op[1] == "old":
            newValue = value + value
        else:
            newValue = value + int(op[1])
    if op[0] == '*':
        if op[1] == "old":
            newValue = value * value
        else:
            newValue = value * int(op[1])
    if divBy3 == True:
        return int(math.floor(newValue / 3))
    else:
        return newValue


def monkey_business(rounds: int):

    for r in range(rounds):
        for i in range(len(mToItems.keys())):
            items = mToItems[i]
            op = mToOp[i]
            divNo = mToDivTest[i]
            throw = mToThrow[i]

            for it in range(len(items)):
                timesInspected[i] += 1
                # Toggle bool for solution to p1 or p2
                newValue = update_item_value(items[it], op, False)
                moR = throw[0] if newValue % divNo == 0 else throw[1]
                newValue %= maxDivNo
                mToItems[moR].append(newValue)
            mToItems[i] = []
        print("Round: ", r)


def print_monkeys():
    for i in range(len(mToItems.keys())):
        print("Monkey ", i)
        print(mToItems[i])
        print(mToOp[i])
        print(mToDivTest[i])
        print(mToThrow[i])
        print("====================")
    timesInspected.sort()
    timesInspected.reverse()
    print("Times inspected: ", timesInspected)
    print("Monkey business is: ", timesInspected[0] * timesInspected[1])
    print("maxDivNo: ", maxDivNo)


def parse_monkeys():
    mIndex = 0
    global maxDivNo
    for l in inp:
        if "Monkey" in l:
            continue
        elif len(l) == 0:
            mIndex += 1
        else:
            if "Starting items:" in l:
                iNos = []
                iSpl = l.split(": ")
                iLis = iSpl[1].split(", ")
                for i in iLis:
                    iNos.append(int(i))
                mToItems[mIndex] = iNos
            elif "Operation" in l:
                lSpl = list()
                op = str()
                if "+" in l:
                    op = '+'
                    lSpl = l.split("+ ")
                elif "*" in l:
                    op = '*'
                    lSpl = l.split("* ")

                if lSpl[1] != "old":
                    mToOp[mIndex] = (op, int(lSpl[1]))
                else:
                    mToOp[mIndex] = (op, "old")
            elif "Test" in l:
                lSpl = l.split("Test: divisible by ")
                mToDivTest[mIndex] = int(lSpl[1])
            elif "true" in l:
                lSpl = l.split("If true: throw to monkey ")
                mToThrow[mIndex] = (int(lSpl[1]), 0)
            elif "false" in l:
                lSpl = l.split("If false: throw to monkey ")
                mToThrow[mIndex] = (mToThrow[mIndex][0], int(lSpl[1]))
    for i in range(len(mToItems.keys())):
        timesInspected.append(0)
        maxDivNo *= mToDivTest[i]


parse_monkeys()
monkey_business(10000)
print_monkeys()
