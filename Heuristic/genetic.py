import random
import math
# state formats : [[1, 2, 3], [1, 0, 3], ...]
def genetic(problem, numberOfRepeat, n, mutationProb):
    counter = 0
    maxFitnessOutput = list()
    minFitnessOutput = list()
    avrageFitnessOutput = list()
    def mutate(cc):
        # just mutate the states with numbers
        pos = random.randrange(len(cc))
        num = random.randrange(max(cc) + 1)
        cc[pos] = num
        return cc

    individual = list()

    doMutationList = list()
    l = 100
    k = math.ceil(mutationProb * l)
    for j in range(l):
        if j >= k:
            doMutationList.append(False)
        else:
            doMutationList.append(True)

    for i in range(n):
        while True:
            tmp = random.choice(problem.getGeneratedNumbers())
            if tmp not in individual:
                individual.append(tmp)
                break
            else:
                continue

    while numberOfRepeat > 0:
        if problem.getGoal() in individual:
            print ("best answer")
            print ("number of repeats:", counter)
            return {"individual": individual, "maxFitness": maxFitnessOutput, "minFitness": minFitnessOutput, "averageFitness": avrageFitnessOutput}
        prob = list()
        parents = list()
        individualFitness = list()
        fitnessMaxes = list()
        individualMaxes = list()

        print ("individual:", individual)
        for i in individual:
            individualFitness.append(problem.getFitness()[problem.getGeneratedNumbers().index(i)])

        print ("fitness:", individualFitness)
        for i in range(len(individualFitness)):
            for j in range(individualFitness[i]):
                prob.append(i)

        for i in range(n):
            parents.append(individual[random.choice(prob)])
        print ("parents:", parents)

        if n % 2 != 0:
            child = list(random.choice(parents))
            parents.remove(child)
            doMutation = random.choice(doMutationList)
            if doMutation:
                child = list(mutate(child))
            if child in problem.getGeneratedNumbers():
                individual.append(child)
                individualFitness.append(problem.getFitness()[problem.getGeneratedNumbers().index(child)])
            if n == 1:
                maxFitnessOutput.append(max(individualFitness))
                minFitnessOutput.append(min(individualFitness))
                avrageFitnessOutput.append(sum(individualFitness) / float(len(individualFitness)))
                print ("max fitness:", max(individualFitness))
                print ("min fitness:", min(individualFitness))
                print ("max fitness:", sum(individualFitness) / float(len(individualFitness)))
        for i in range(0, len(parents), 2):
            cr1 = list(parents[i])
            cr2 = list(parents[i + 1])
            crPos = random.randrange(len(cr1))

            child1 = list(cr1[:crPos] + cr2[crPos:])
            doMutation = random.choice(doMutationList)
            if doMutation:
                child1 = list(mutate(child1))
            child2 = list(cr2[:crPos] + cr1[crPos:])
            doMutation = random.choice(doMutationList)
            if doMutation:
                child2 = list(mutate(child2))

            if child1 in problem.getGeneratedNumbers():
                individual.append(child1)
                individualFitness.append(problem.getFitness()[problem.getGeneratedNumbers().index(child1)])
            if child2 in problem.getGeneratedNumbers():
                individual.append(child2)
                individualFitness.append(problem.getFitness()[problem.getGeneratedNumbers().index(child2)])
            maxFitnessOutput.append(max(individualFitness))
            minFitnessOutput.append(min(individualFitness))
            avrageFitnessOutput.append(sum(individualFitness) / float(len(individualFitness)))
            print ("max fitness:", max(individualFitness))
            print ("min fitness:", min(individualFitness))
            print ("max fitness:", sum(individualFitness) / float(len(individualFitness)))
            print ("cr1:", cr1)
            print ("cr2:", cr2)
            print ("child1:", child1)
            print ("child2:", child2)

        for j in range(n):
            maxFitness = max(individualFitness)
            maxIndex = individualFitness.index(maxFitness)
            maxIndividual = individual[maxIndex]
            fitnessMaxes.append(maxFitness)
            individualFitness.remove(maxFitness)
            individualMaxes.append(maxIndividual)
            individual.remove(maxIndividual)

        numberOfRepeat -= 1
        counter += 1
        individualFitness = list(fitnessMaxes)
        individual = list(individualMaxes)
        print ("individual: ", individual)
        print ("fitness: ", individualFitness, "\n")

        print ("")
    return {"individual": individual, "maxFitness": maxFitnessOutput, "minFitness": minFitnessOutput,
            "averageFitness": avrageFitnessOutput}
