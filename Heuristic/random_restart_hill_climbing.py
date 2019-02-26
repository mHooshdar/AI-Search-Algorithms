def hillClimbingRandomRestart(problem):
    nodePath = list()
    currentState = problem.initialState()

    expandedNodes = 0
    seenNodes = 0
    cost = 0

    while True:
        neighbors = problem.actions(currentState)
        nodePath.append(currentState)
        expandedNodes += 1
        if problem.goalTest(currentState):
            return {"seen": seenNodes, "expanded": expandedNodes, "route": nodePath, "cost": cost}
        counter = 0
        for node in neighbors:
            seenNodes += 1
            if problem.getFitness()[node] > problem.getFitness()[currentState]:
                currentState = node
                counter += 1
        if counter == 0:
            currentState = random.randint(0, len(problem.graph.graph) - 1)
            