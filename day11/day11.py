def parseInput(input):
    return [cmd for cmd in open(input, "r").read().split(",")]

def partOne(input):
    x = 0
    y = 0
    z = 0
    dists = []
    for cmd in input:
        if cmd == 'n':
            y += 1
            z -= 1
        elif cmd == 'ne':
            x += 1
            z -= 1
        elif cmd == 'nw':
            x -= 1
            y += 1
        elif cmd == 's':
            y -= 1
            z += 1
        elif cmd == 'se':
            x += 1
            y -= 1
        elif cmd == 'sw':
            x -= 1
            z += 1

        dists.append((abs(x) + abs(y) + abs(z))/2)

    print max(dists)

    return (abs(x) + abs(y) + abs(z)) / 2

def partTwo(input):
    pass

print partOne(parseInput("day11.txt"))
print partTwo(parseInput("day11.txt"))