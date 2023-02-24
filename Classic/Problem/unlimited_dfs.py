def dfsUnlimited(problem, isGraph):
    startState = problem.initialState()
    f = list()
    e = list()
    nodePath = list()

    expandedNodes = 0
    seenNodes = 0
    cost = 0
    maxH = 0
    tempState = startState

    try:
        f.append(startState)
        seenNodes += 1
        nodePath.append([startState])
    except:
        print ("invalid start state")

    while f:
        tempState = problem.result(tempState, f.pop(0))
        tempPath = nodePath.pop(0)
        if isGraph:
            e.append(tempState)
        expandedNodes += 1
        neighbors = problem.actions(tempState)
        count = 0
        for node in neighbors:
            if (isGraph and (node not in e and node not in f)) or (not isGraph):
                tempList = list(tempPath)
                tempList.append(node)
                f.insert(0 + count, node)
                seenNodes += 1
                nodePath.insert(0 + count, tempList)
                count += 1
                if problem.goalTest(node):
                    maxH = max(maxH, len(f))
                    return {"seen": seenNodes, "expanded": expandedNodes, "route": tempList, "cost": cost,
                            "max memory": maxH}
        maxH = max(maxH, len(f))
