import Graph
import pytest
from .Classic.Graph.a_star import aStar
# import ../

def test_aStar():
    graph = [[1, 2], [0, 3], [0, 4], [1, 5], [2, 6], [3, 6], [4, 5]]
    cost = [[1.5, 2], [1.5, 2], [2, 3], [2, 3], [3, 2], [3, 4], [2, 4]]
    h = [8, 4, 4.5, 2, 2, 4, 0]
    myGraph = Graph.Graph(graph, cost)
    
    result = aStar(myGraph, 0, 6, h, False)
    assert result["seen"] == 7
    assert result["expanded"] == 8
    assert result["cost"] == 7.5
    assert result["max memory"] == 3
    assert result["route"] == [0, 2, 4, 5, 6]