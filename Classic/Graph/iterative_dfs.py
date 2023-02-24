def dfsIterative(graph, startState, endState, isGraph):
    l = 1

    expandedNodes = 0
    seenNodes = 0
    cost = 0
    maxH = 0
    while True:
        f = list()
        e = list()
        nodePath = list()

        try:
            f.append(startState)
            seenNodes += 1
            nodePath.append([startState])
        except:
            print ("invalid start state")

        while f:
            tempState = f.pop(0)
            tempPath = nodePath.pop(0)
            if len(tempPath) >= l:
                continue
            if isGraph:
                e.append(tempState)
            expandedNodes += 1
            count = 0
            for node in graph[tempState]:
                if (isGraph and (node not in e and node not in f)) or (not isGraph):
                    tempList = list(tempPath)
                    tempList.append(node)
                    f.insert(0 + count, node)
                    seenNodes += 1
                    nodePath.insert(0 + count, tempList)
                    count += 1
                    if node == endState:
                        maxH = max(maxH, len(f))
                        return {"seen": seenNodes, "expanded": expandedNodes, "route": tempList, "cost": cost, "max memory": maxH}
            maxH = max(maxH, len(f))
        l += 1


graph = [[], [3, 4, 2], [5], [1], [1], [9, 10, 8], [], [], [], [], [], []]
# graph = [[], [2, 3, 4, 8], [5], [6, 7, 10], [8], [9, 10], [], [], [], [], [], []]

print (dfsIterative(graph, 1, 8, True))