LEN = 256
ITERATIONS = 64

def parseInput(input):
    return [int(line) for line in open(input, "r").read().split(",")]

def parseInput2(input):
    inp = [ord(charz) for charz in list(open(input, "r").read())]
    inp.extend([17, 31, 73, 47, 23])
    return inp

def reverseSection(hashz, length, currentPosition):
    for x in range(0, length/ 2):
        z = (currentPosition + x) % LEN
        y = (currentPosition + length - x - 1) % LEN

        b = hashz[y]
        hashz[y] = hashz[z]
        hashz[z] = b

    return hashz

def partOne(input):
    hashz = [x for x in range(0, LEN)]
    skip = 0
    currentPosition = 0

    for length in input:
        hashz = reverseSection(hashz, length, currentPosition)
        currentPosition = (currentPosition + length + skip) % LEN
        skip += 1

    print hashz[0] * hashz[1]


def partTwo(input):
    hashz = [x for x in range(0, LEN)]
    skip = 0
    currentPosition = 0

    for x in range(0, ITERATIONS):
        for length in input:
            hashz = reverseSection(hashz, length, currentPosition)
            currentPosition = (currentPosition + length + skip) % LEN
            skip += 1

    dense = ""
    for w in range(0, 16):
        x = 0
        for y in range(0, 16):
            z = w * 16 + y
            x = x ^ hashz[z]
        dense = dense + ("%0.2x" % x)

    print dense

partOne(parseInput("day10.txt"))
partTwo(parseInput2("day10.txt"))