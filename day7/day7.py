from sets import Set

def parseInput(input):
    return [line for line in open(input, "r").read().split("\n")]

def partOne(input):
    noParents = Set()
    parents = Set()

    for line in input:
        if ' -> ' in line:
            left, right = line.split(" -> ")
            name, weight_str = left.split(" ")
            weight = int(weight_str.translate(None, '()'))
            children = right.split(", ")
            if name not in parents:
                noParents.add(name)
            for childName in children:
                parents.add(childName)
                if childName in noParents:
                    noParents.remove(childName)
        else:
            name, weight_str = line.split(" ")
            weight = int(weight_str.translate(None, '()'))
            if name not in parents:
                noParents.add(name)

    return noParents.pop()


class Handle:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.treeWeight = 0
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def __str__(self):
        return "[" + self.name + "] - " + str(self.weight) + " - " + str(self.treeWeight) + " [" + str(self.children) + "]"


def calcWeight(node):
    if len(node.children) == 0:
        return node.weight

    weightsDict = dict()
    weights = []

    for child in node.children:
        weightsDict[child.name] = calcWeight(child)
        weights.append(weightsDict[child.name])

    if all(x == weights[0] for x in weights):
        node.treeWeight = sum(weights) + node.weight
        return sum(weights) + node.weight

    else:
        # for child in node.children:
        #     if child.name == 'whzdf':
        #         for chil in child.children:
        #             print chil
            # print child
        print weightsDict
        return sum(weights) + node.weight


def partTwo(input, rootNodeName):
    handleByName = dict()

    for line in input:
        if ' -> ' in line:
            left, right = line.split(" -> ")
            name, weight_str = left.split(" ")
            weight = int(weight_str.translate(None, '()'))
            children = right.split(", ")
        else :
            name, weight_str = line.split(" ")
            weight = int(weight_str.translate(None, '()'))
            children = []


        if name in handleByName:
            handle = handleByName[name]
            handle.weight = weight
        else :
            handle = Handle(name, weight)
            handleByName[name] = handle

        for child in children:
            if child not in handleByName:
                childHandle = Handle(child, 0)
                handleByName[child] = childHandle

            handle.addChild(handleByName[child])

    rootHandle = handleByName[rootNodeName]


    calcWeight(rootHandle)

    print handleByName['lnpuarm'].weight

    for c in handleByName['lnpuarm'].children:
        print c

root = partOne(parseInput("day7.txt"))
print root
partTwo(parseInput("day7.txt"), root)