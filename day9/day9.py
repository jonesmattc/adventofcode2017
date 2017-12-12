def parseInput(input):
    return list(open(input, "r").read())

def partOne(input):
    score = 0
    depth = 1
    char_count = 0
    skip_next = False
    inside_garbage = False

    for char in input:
        if skip_next:
            skip_next = False
        elif char == '!':
            skip_next = True
        elif char == '>':
            inside_garbage = False
        elif inside_garbage:
            char_count += 1
        elif char == '<':
            inside_garbage = True
        elif char == '{':
            score += depth
            depth += 1
        elif char == '}':
            depth -= 1

    print score
    print char_count


inp = parseInput("day9.txt")
partOne(inp)