def hillClimbingStochastic(problem):
    nodePath = list()
    currentState = problem.initialState()

    expandedNodes = 0
    seenNodes = 0

    while True:
        neighbors = problem.actions(currentState)
        nodePath.append(currentState)
        counter = 0
        bestList = list()
        expandedNodes += 1
        for node in neighbors:
            seenNodes += 1
            if problem.getFitness()[node] > problem.getFitness()[currentState]:
                bestList.append(node)
                counter += 1
        if problem.goalTest(currentState):
            return {"seen": seenNodes, "expanded": expandedNodes, "route": nodePath, "fitness": problem.getFitness()[currentState]}
        if counter == 0:
            print "Local"
            return {"seen": seenNodes, "expanded": expandedNodes, "route": nodePath, "fitness": problem.getFitness()[currentState]}
        currentState = random.choice(bestList)
