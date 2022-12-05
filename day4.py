import parser_util

input = parser_util.readList("inputs/4.txt", "string", True, False)


def getListByRange(sec: str) -> list:
    rangeNo = sec.split("-")
    return list(range(int(rangeNo[0]), int(rangeNo[1])+1))


def part_one():
    pairs = list()
    no_overlap_pairs = 0

    for i in input:
        pair = i.split(",")
        sec1 = getListByRange(pair[0])
        sec2 = getListByRange(pair[1])
        commonSet = set(sec1) & set(sec2)
        if len(commonSet) == len(sec1) or len(commonSet) == len(sec2):
            no_overlap_pairs += 1

    print(no_overlap_pairs)


def part_two():
    pairs = list()
    no_overlap_pairs_at_all = 0

    for i in input:
        pair = i.split(",")
        sec1 = getListByRange(pair[0])
        sec2 = getListByRange(pair[1])
        commonSet = set(sec1) & set(sec2)
        if len(commonSet) > 0:
            no_overlap_pairs_at_all += 1

    print(no_overlap_pairs_at_all)


part_one()
part_two()
