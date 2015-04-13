import sys, math

import collections
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input()) # the number of adjacency relations
nodeDict = collections.defaultdict(lambda: list())
linkList = list()

parentSet = set()
childSet = set()

for i in xrange(n):
    # xi: the ID of a person which is adjacent to yi
    # yi: the ID of a person which is adjacent to xi
    xi, yi = [int(i) for i in raw_input().split()]
    linkList.append((xi, yi))
    parentSet.add(xi)
    childSet.add(yi)

root = parentSet.difference(childSet).pop()

for link in linkList:
    nodeDict[link[0]].append(link[1])
    nodeDict[link[1]].append(link[0])


def checkPath(nodeNum, fromNode=None):
    routeLength = None
    for nodeN in nodeDict[nodeNum]:
        if nodeN == fromNode:
            continue
        val = checkPath(nodeN, nodeNum)
        if routeLength is None or routeLength < val:
            routeLength = val
    if routeLength is None:
        return 1
    else:
        return routeLength + 1


bestVal = None

vals = list()
for child in nodeDict[root]:
    vals.append(checkPath(child, root))

vals.sort(key=lambda x: x)

if len(vals) > 1:
    vals.reverse()
    bestVal = vals[0] + vals[1]
else:
    bestVal = vals[0]

if bestVal % 2 != 0:
    bestVal = bestVal / 2 + 1
else:
    bestVal /= 2

print bestVal