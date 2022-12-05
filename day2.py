import parser_util

input = parser_util.readList("inputs/2.txt", "string", True, False)

## =================================##
##   A: ROCK B: PAPER C: SCISSORS   ##
## =================================##
rounds = [s.split(" ") for s in input]
scoreMapper = {"A": 1, "B": 2, "C": 3}


def part_one():
    score = 0
    mapper = {"X": "A", "Y": "B", "Z": "C"}

    for r in rounds:
        opp = r[0]
        my = mapper.get(r[1])

        score += scoreMapper.get(my)
        if opp == my:  # draw
            score += 3
        else:  # win cons
            if my == "A" and opp == "C":
                score += 6
            elif my == "B" and opp == "A":
                score += 6
            elif my == "C" and opp == "B":
                score += 6

    print(score)


def part_two():
    score = 0
    winMapper = {"A": "C", "B": "A", "C": "B"}
    looseMapper = {"C": "A", "A": "B", "B": "C"}

    for r in rounds:
        opp = r[0]
        my = r[1]

        if my == "X":  # loose
            move = winMapper.get(opp)
            score += scoreMapper.get(move)
        if my == "Y":  # draw
            move = opp
            score += scoreMapper.get(move)
            score += 3
        if my == "Z":  # win
            move = looseMapper.get(opp)
            score += scoreMapper.get(move)
            score += 6

    print(score)


part_one()
part_two()
