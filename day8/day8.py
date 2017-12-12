def parseInput(input):
    return [line for line in open(input, "r").read().split("\n")]

def partOne(input):
    registers = dict()

    [processChange(registers, line.split(" ")) for line in input]

    return max(registers.values())


def test(testRegister, operator, testVal):

    if operator == '<=':
        return testRegister <= testVal
    elif operator == '<':
        return testRegister < testVal
    elif operator == '>=':
        return testRegister >= testVal
    elif operator == '>':
        return testRegister > testVal
    elif operator == '==':
        return testRegister == testVal
    elif operator == '!=':
        return testRegister != testVal

    return False

def modifyReg(change, diff):
    if change == 'inc':
        return diff
    elif change == 'dec':
        return -1 * diff

def processChange(registers, inputs):
    registerName = inputs[0]
    change = inputs[1]
    diff = int(inputs[2])
    testReg = inputs[4]
    compOp = inputs[5]
    testVal = int(inputs[6])
    if registerName not in registers:
        registers[registerName] = 0
    if testReg not in registers:
        registers[testReg] = 0

    if test(registers[testReg], compOp, testVal):
        registers[registerName] += modifyReg(change, diff)



def partTwo(input):
    registers = dict()
    maxSoFar = 0

    for line in input:
        processChange(registers, line.split(" "))
        if max(registers.values()) > maxSoFar:
            maxSoFar = max(registers.values())

    return maxSoFar

print partOne(parseInput("day8.txt"))
print partTwo(parseInput("day8.txt"))