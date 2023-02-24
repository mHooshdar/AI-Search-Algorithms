def hillClimbingSimple(problem):
    nodePath = list()
    currentState = problem.initialState()

    expandedNodes = 0
    seenNodes = 0

    while True:
        neighbors = problem.actions(currentState)
        nodePath.append(currentState)
        if problem.goalTest(currentState):
            return {"seen": seenNodes, "expanded": expandedNodes, "route": nodePath, "fitness": problem.getFitness()[currentState]}
        counter = 0
        expandedNodes += 1
        for node in neighbors:
            seenNodes += 1
            if problem.getFitness()[node] > problem.getFitness()[currentState]:
                currentState = node
                counter += 1
        if counter == 0:
            print ("Local")
            return {"seen": seenNodes, "expanded": expandedNodes, "route": nodePath, "fitness": problem.getFitness()[currentState]}
            