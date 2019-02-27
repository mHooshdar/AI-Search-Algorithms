def ucs(problem, isGraph):
    startState = problem.initialState()
    f = list()
    fWeight = list()
    e = list()
    nodePath = list()
    tempState = startState

    expandedNodes = 0
    seenNodes = 0
    maxH = 0

    try:
        f.append(startState)
        seenNodes += 1
        fWeight.append(0)
        nodePath.append([startState])
    except:
        print "invalid start state"

    while f:
        minWeightIndex = fWeight.index(min(fWeight))
        tempState = problem.result(tempState, f.pop(minWeightIndex))
        tempCost = fWeight.pop(minWeightIndex)
        tempPath = nodePath.pop(minWeightIndex)
        if problem.goalTest(tempState):
            return {"seen": seenNodes, "expanded": expandedNodes, "route": tempPath, "cost": tempCost,
                    "max memory": maxH}
        if isGraph:
            e.append(tempState)
        expandedNodes += 1
        neighbors = problem.actions(tempState)
        for node in neighbors:
            if (isGraph and (node not in e)) or (not isGraph):
                cost = problem.pathCost(tempState, node)
                tempList = list(tempPath)
                tempList.append(node)
                if node in f:
                    if cost + tempCost < fWeight[f.index(node)]:
                        fWeight[f.index(node)] = cost + tempCost
                        nodePath[f.index(node)] = tempList
                else:
                    f.append(node)
                    seenNodes += 1
                    fWeight.append(cost + tempCost)
                    nodePath.append(tempList)
        maxH = max(maxH, len(f))
