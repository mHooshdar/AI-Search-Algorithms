def biBfs(problem, isGraph):
    startState = problem.initialState()
    endState = problem.getGoalState()
    fR = list()
    eR = list()
    nodePathR = list()
    tempStateR = startState

    fB = list()
    eB = list()
    nodePathB = list()
    tempStateB = endState

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
        print "invalid start state"

    while fR or fB:
        if fR:
            tempStateR = problem.result(tempStateR, fR.pop(0))
            expandedNodes += 1
            tempPath = nodePathR.pop(0)
            if isGraph:
                eR.append(tempStateR)
            neighbors = problem.actions(tempStateR)
            for node in neighbors:
                if (isGraph and (node not in eR and node not in fR)) or (not isGraph):
                    tempList = list(tempPath)
                    tempList.append(node)
                    fR.append(node)
                    seenNodes += 1
                    nodePathR.append(tempList)

                    if problem.goalTest(node):
                        maxH = max(maxH, len(fR) + len(fB))
                        return {"seen": seenNodes, "expanded": expandedNodes, "route": tempList, "cost": cost,
                                "max memory": maxH}
            for node in fR:
                if node in fB:
                    s = nodePathB[fB.index(node)]
                    s = s[: len(s) - 1]
                    maxH = max(maxH, len(fR) + len(fB))
                    return {"seen": seenNodes, "expanded": expandedNodes,
                            "route": nodePathR[fR.index(node)] + list(reversed(s)), "cost": cost, "max memory": maxH}
            maxH = max(maxH, len(fR) + len(fB))
        if fB:
            tempStateB = problem.result(tempStateB, fB.pop(0))
            tempPath = nodePathB.pop(0)
            if isGraph:
                eB.append(tempStateB)
            expandedNodes += 1
            neighbors = problem.actions(tempStateB)
            for node in neighbors:
                if (isGraph and (node not in eB and node not in fB)) or (not isGraph):
                    tempList = list(tempPath)
                    tempList.append(node)
                    fB.append(node)
                    seenNodes += 1
                    nodePathB.append(tempList)

                    maxH = max(maxH, len(fR) + len(fB))
                    if problem.goalTest(node, True):
                        return {"seen": seenNodes, "expanded": expandedNodes, "route": tempList, "cost": cost,
                                "max memory": maxH}
            for node in fR:
                if node in fB:
                    s = nodePathB[fB.index(node)]
                    s = s[: len(s) - 1]
                    maxH = max(maxH, len(fR) + len(fB))
                    return {"seen": seenNodes, "expanded": expandedNodes,
                            "route": nodePathR[fR.index(node)] + list(reversed(s)), "cost": cost, "max memory": maxH}
            maxH = max(maxH, len(fR) + len(fB))
