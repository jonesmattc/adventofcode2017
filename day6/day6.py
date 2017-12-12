from sets import Set

def parseInput(input):
    return [int(bank) for bank in open(input, "r").read().split("\t")]

def partOne(input):
    past = Set()
    currBanks = input
    bankString = ",".join(str(x) for x in currBanks)
    while bankString not in past:
        past.add(bankString)
        updateBank(currBanks)
        bankString = ",".join(str(x) for x in currBanks)
    return len(past)

def updateBank(bankArray):
    maxIndex = bankArray.index(max(bankArray))
    maxBank = bankArray[maxIndex]
    bankArray[maxIndex] = 0
    index = maxIndex + 1
    while maxBank > 0:
        bankArray[index % len(bankArray)] = bankArray[index % len(bankArray)] + 1
        index = index + 1
        maxBank = maxBank - 1

def partTwo(input):
    past = Set()
    currBanks = input
    bankString = ",".join(str(x) for x in currBanks)
    while bankString not in past:
        past.add(bankString)
        updateBank(currBanks)
        bankString = ",".join(str(x) for x in currBanks)

    loopString = bankString
    bankString = ""
    count = 0
    while bankString != loopString:
        updateBank(currBanks)
        bankString = ",".join(str(x) for x in currBanks)
        count = count + 1

    return count

print partOne(parseInput("day6.txt"))
print partTwo(parseInput("day6.txt"))