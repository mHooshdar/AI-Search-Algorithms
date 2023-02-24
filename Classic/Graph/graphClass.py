class Graph:
    def __init__(self, graph, weight=None):
        self.edges = list()
        self.nodes = list()
        self.graph = graph
        self.generateEdges(graph, weight)
        self.generateNodes(graph)

    def generateEdges(self, graph, weight):
        if weight:
            for nodeIndex in range(len(graph)):
                for neighbourIndex in range(len(graph[nodeIndex])):
                    self.edges.append((nodeIndex, graph[nodeIndex][neighbourIndex], weight[nodeIndex][neighbourIndex]))
        else:
            for nodeIndex in range(len(graph)):
                for neighbourIndex in range(len(graph[nodeIndex])):
                    self.edges.append((nodeIndex, graph[nodeIndex][neighbourIndex], 0))

    def generateNodes(self, arr):
        for i in range(len(arr)):
            self.nodes.append(i)

    def getCost(self, fromNode, toNode):
        for edge in self.edges:
            if edge[0] == fromNode and edge[1] == toNode:
                return edge[2]
