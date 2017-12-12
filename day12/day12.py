lines = [line for line in open("day12.txt", "r").read().split("\n")]
tabs = [line for line in open("day12.txt", "r").read().split("\t")]
commas = [line for line in open("day12.txt", "r").read().split(",")]

class DJS:
    def __init__(self):
        self.parent = self
        self.rank = 0
        self.size = 1

connected = dict()
for x in range(2000):
    connected[x] = DJS()

def find(djs):
    if djs.parent != djs:
        djs.parent = find(djs.parent)
    return djs.parent

def union(djsA, djsB):
    aRoot = find(djsA)
    bRoot = find(djsB)

    if aRoot == bRoot:
        return
    if aRoot.rank < bRoot.rank:
        aRoot.parent = bRoot
        bRoot.size += aRoot.size
    elif aRoot.rank > bRoot.rank:
        bRoot.parent = aRoot
        aRoot.size += bRoot.size
    else:
        bRoot.parent = aRoot
        aRoot.rank = aRoot.rank + 1
        aRoot.size += bRoot.size

for line in lines:
    left, right = line.split(" <-> ")
    pipes = right.split(", ")
    for pipe in pipes:
        union(connected[int(left)], connected[int(pipe)])

from sets import Set
z = Set()
for djs in connected.values():
    z.add(find(djs))

print len(z)

st = connected[0]
while(st.parent != st):
    st = st.parent

print st.size