import parser_util

inp = parser_util.readList("inputs/6.txt", "string", True, False)


def all_unique(buffer: list, size: int) -> bool:
    bufferSet = set(buffer)
    if len(bufferSet) == size:
        return True
    else:
        return False


def solve(size):
    stream = list(inp[0])
    buffer = stream[0:size]
    index = size

    for i in range(size):
        stream.pop(0)

    while len(stream) > 0:
        if all_unique(buffer, size):
            break
        buffer.pop(0)
        buffer += stream.pop(0)
        index += 1

    print("Answer is: ")
    print(index)


solve(14)
