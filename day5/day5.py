def partOne(input):
    index = 0
    count = 0
    max = len(input)
    while (index >= 0 and index < max):
        lastIndex = index
        index += input[index]
        input[lastIndex] = input[lastIndex] + 1
        count = count + 1

    return count

def partTwo(input):
    index = 0
    count = 0
    max = len(input)
    while (index >= 0 and index < max):
        lastIndex = index
        index += input[index]
        if(input[lastIndex] >= 3):
            input[lastIndex] = input[lastIndex] - 1
        else:
            input[lastIndex] = input[lastIndex] + 1
        count = count + 1

    return count


def parseInput(input):
    return [int(line) for line in input.split("\n")]

print partOne(parseInput(open("day5.txt", "r").read()))
print partTwo(parseInput(open("day5.txt", "r").read()))