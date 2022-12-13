import parser_util

inp = parser_util.readList("inputs/13.txt", "string", False, False)


def pair_is_sorted(left, right):

    # Both integers
    if type(left) is int and type(right) is int:
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return None

    if type(left) is list and type(right) is list:
        cInd = 0
        while True:
            inRangeL = cInd < len(left)
            inRangeR = cInd < len(right)
            if inRangeL and inRangeR:  # Continue checking elements in left and right
                sorted = pair_is_sorted(left[cInd], right[cInd])
                if sorted == None:
                    cInd += 1
                else:
                    return sorted
            elif not inRangeL and inRangeR:  # left list runs out first => In order
                return True
            elif inRangeL and not inRangeR:  # right list runs out first => NOT in order
                return False
            else:
                return None

    if type(left) is not list:
        return pair_is_sorted([left], right)
    if type(right) is not list:
        return pair_is_sorted(left, [right])


def get_sorted_pairs(pairs):
    sortedIndexes = []
    for pI in range(len(pairs)):
        if pair_is_sorted(pairs[pI][0], pairs[pI][1]):
            sortedIndexes.append(pI+1)
    return sortedIndexes


def print_pairs(pairs):
    for i in pairs:
        print("Pair:")
        print("     : ", i[0])
        print("     : ", i[1])


def bubble_sort(pairs):

    swapped = False
    index = 0
    while True:
        isSorted = pair_is_sorted(pairs[index], pairs[index+1])
        if isSorted == False:
            temp = pairs[index]
            pairs[index] = pairs[index+1]
            pairs[index+1] = temp
            swapped = True

        if index+2 == len(pairs):  # end of list
            index = 0
            if not swapped:
                break
            swapped = False
        else:
            index += 1

    return pairs


pairs = list()
pairs.append(([], []))  # REMEMBER PAIR 0 IS ACTUALLY "INDEX 1" IN PROBLEM

ind = 0
for i in inp:

    if len(i) == 0:
        pairs.append(([], []))
    elif ind == 0:
        pairs[-1] = (eval(i), pairs[-1][1])
        ind += 1
    else:
        pairs[-1] = (pairs[-1][0], eval(i))
        ind = 0

sortedPairs = get_sorted_pairs(pairs)
print("Sorted Pairs: ", sortedPairs)
print("Sum of indexes that are sorted: ", sum(sortedPairs))


## PART 2 ##
inp2 = parser_util.readList("inputs/13.txt", "string", True, False)

pairs = [[[2]], [[6]]]  # [[2]] and [[6]] are divider packets
for i in inp2:
    pairs.append(eval(i))

sortedPairs = bubble_sort(pairs)

div1 = pairs.index([[2]])+1
div2 = pairs.index([[6]])+1
print("Indexes: ", div1, ", ", div2)
print("Product of dividers is: ", div1 * div2)
