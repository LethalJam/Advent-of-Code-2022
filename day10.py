import parser_util

insts = parser_util.readList("inputs/10.txt", "string", True, False)


def print_screen(screen):
    for r in screen:
        for pix in r:
            print(pix, end='')
        print("")


reg = 1
instIndex = 0
signals = []
busy = 0
cmd = list()
oper = str()

screen = list()
for i in range(6):
    row = [' '] * 40
    screen.append(row)

pos = {'x': 0, 'y': 0}

for c in range(240):

    # Check if we need a new command
    if busy == 0:

        cmd = insts[instIndex].split(" ")
        oper = cmd[0]
        if oper == "noop":
            busy = 1
        elif oper == "addx":
            busy = 2

    # Part one
    cycle = c+1
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
        signals.append(cycle * reg)

    # Part two
    pos['x'] = c - (pos['y'] * 40)
    if pos['x'] >= reg-1 and pos['x'] <= reg+1:
        screen[pos['y']][pos['x']] = "#"
    if cycle % 40 == 0:
        pos['y'] += 1

    # End cycle and see if cmd is ready to run
    busy -= 1
    if busy == 0:
        if oper == "addx":
            no = int(cmd[1])
            reg += no

        instIndex += 1
        if instIndex == len(insts):
            instIndex = 0

print_screen(screen)
print(signals)
print("Sum of signals: ", sum(signals))
