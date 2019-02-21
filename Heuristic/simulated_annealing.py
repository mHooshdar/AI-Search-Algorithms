import random
import math


def sa(problem, tempreature):
    nodePath = list()
    startState = problem.initialState()
    currentState = startState

    expandedNodes = 0
    seenNodes = 0

    while tempreature > 0:
        neighbors = problem.actions(currentState)
        nextState = random.choice(neighbors)
        delta = problem.getFitness()[nextState] - problem.getFitness()[currentState]
        nodePath.append(currentState)
        expandedNodes += 1
        seenNodes += len(neighbors)

        if problem.goalTest(currentState):
            return {"seen": seenNodes, "expanded": expandedNodes, "route": nodePath, "fitness": problem.getFitness()[currentState]}

        if delta > 0:
            currentState = nextState
        else:
            # p = math.exp(delta / float(tempreature))
            # p = 1 / float(tempreature)
            p = random.uniform(0, 1)
            tmp = list()
            l = 100
            k = math.ceil(p * l)
            for i in range(l):
                if i >= k:
                    tmp.append(nextState)
                else:
                    tmp.append(currentState)
            currentState = random.choice(tmp)
        tempreature -= 1