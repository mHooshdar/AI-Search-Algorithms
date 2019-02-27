import Graph
def ucs(graph, startState, endState, isGraph):
    f = list()
    fWeight = list()
    e = list()
    nodePath = list()

    expandedNodes = 0
    seenNodes = 0
    maxH = 0

    try:
        f.append(startState)
        seenNodes +=1
        fWeight.append(0)
        nodePath.append([startState])
    except:
        print "invalid start state"

    while f:
        minWeightIndex = fWeight.index(min(fWeight))
        tempState = f.pop(minWeightIndex)
        tempCost = fWeight.pop(minWeightIndex)
        tempPath = nodePath.pop(minWeightIndex)
        if tempState == endState:
            return {"seen": seenNodes, "expanded": expandedNodes, "route": tempPath, "cost": tempCost, "max memory": maxH}
        if isGraph:
            e.append(tempState)
        expandedNodes += 1
        for node in graph.graph[tempState]:
            if (isGraph and (node not in e)) or (not isGraph):
                cost = graph.getCost(tempState, node)
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

        maxH = maxH = max(maxH, len(f))

# graph = [[1, 2, 5], [0, 2, 3], [0, 1, 3, 5], [1, 2, 4], [3, 5], [0, 2, 4]]
# cost = [[7, 9, 14], [7, 10, 15], [9, 10, 11, 2], [15, 11, 6], [6, 9], [14, 2, 9]]

graph = [[1, 7], [0, 2, 7], [1, 3, 5, 8], [2, 4, 5], [3, 5], [2, 3, 4, 6], [5, 7, 8], [0, 1, 6, 8], [2, 6, 7]]
cost = [[4, 8], [4, 8, 11], [8, 7, 4, 2], [7, 9, 14], [9, 10], [4, 14, 10, 2], [2, 1, 6], [8, 11, 1, 7], [2, 6, 7]]

myGraph = Graph.Graph(graph, cost)
print ucs(myGraph, 0, 8, False)