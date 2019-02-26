def hillClimbingFirstChoice(problem):
    nodePath = list()
    currentState = problem.initialState()

    expandedNodes = 0
    seenNodes = 0

    while True:
        nodePath.append(currentState)
        if problem.goalTest(currentState):
            return {"seen": seenNodes, "expanded": expandedNodes, "route": nodePath, "fitness": problem.getFitness()[currentState]}
        nextState, nextFitness, lenNeighbors = problem.generateRandomState(currentState)
        expandedNodes += 1
        seenNodes += lenNeighbors
        if nextFitness > problem.getFitness()[currentState]:
            currentState = nextState
