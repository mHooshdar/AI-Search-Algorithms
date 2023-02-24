def bi_bfs(graph, startState, endState, isGraph):
    fR = list()
    eR = list()
    nodePathR = list()

    fB = list()
    eB = list()
    nodePathB = list()

    expandedNodes = 0
    seenNodes = 0
    cost = 0
    maxH = 0

    try:
        fR.append(startState)
        seenNodes += 1
        nodePathR.append([startState])

        fB.append(endState)
        seenNodes += 1
        nodePathB.append([endState])
    except:
        print ("invalid start state")

    while fR or fB:
        if fR:
            tempState = fR.pop(0)
            expandedNodes += 1
            tempPath = nodePathR.pop(0)
            if isGraph:
                eR.append(tempState)
            for node in graph[tempState]:
                if (isGraph and (node not in eR and node not in fR)) or (not isGraph):
                    tempList = list(tempPath)
                    tempList.append(node)
                    fR.append(node)
                    seenNodes += 1
                    nodePathR.append(tempList)
                    if node == endState:
                        maxH = max(maxH, len(fR) + len(fB))
                        return {"seen": seenNodes, "expanded": expandedNodes, "route": tempList, "cost": cost, "max memory": maxH}
            for node in fR:
                if node in fB:
                    s = nodePathB[fB.index(node)]
                    s = s[: len(s) - 1]
                    maxH = max(maxH, len(fR) + len(fB))
                    return {"seen": seenNodes, "expanded": expandedNodes, "route": nodePathR[fR.index(node)] + list(reversed(s)), "cost": cost, "max memory": maxH}
            maxH = max(maxH, len(fR) + len(fB))
        if fB:
            tempState = fB.pop(0)
            tempPath = nodePathB.pop(0)
            if isGraph:
                eB.append(tempState)
            expandedNodes += 1
            for node in graph[tempState]:
                if (isGraph and (node not in eB and node not in fB)) or (not isGraph):
                    tempList = list(tempPath)
                    tempList.append(node)
                    fB.append(node)
                    seenNodes += 1
                    nodePathB.append(tempList)
                    maxH = max(maxH, len(fR) + len(fB))
                    if node == startState:
                        return {"seen": seenNodes, "expanded": expandedNodes, "route": tempList, "cost": cost, "max memory": maxH}
            for node in fR:
                if node in fB:
                    s = nodePathB[fB.index(node)]
                    s = s[: len(s) - 1]
                    maxH = max(maxH, len(fR) + len(fB))
                    return {"seen": seenNodes, "expanded": expandedNodes, "route": nodePathR[fR.index(node)] + list(reversed(s)), "cost": cost, "max memory": maxH}
            maxH = max(maxH, len(fR) + len(fB))

# graph = [[1, 7], [0, 2, 7], [1, 3, 5, 8], [2, 4, 5], [3, 5], [2, 3, 4, 6], [5, 7, 8], [0, 1, 6, 8], [2, 6, 7]]
# graph = [[], [3, 4, 2], [5], [1], [1], [9, 10, 8], [], [], [], [], [], []]
# graph = [[], [2, 3, 4, 8], [5], [6, 7, 10], [8], [9, 10], [], [], [], [], [], []]
graph = [[1, 7], [0, 2, 7], [1, 3, 5, 8], [2, 4, 5], [3, 5], [2, 3, 4, 6], [5, 7, 8], [0, 1, 6, 8], [2, 6, 7]]

print (bi_bfs(graph, 0, 8, True))