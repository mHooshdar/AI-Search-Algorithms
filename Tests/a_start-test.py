import unittest
import Graph

class TestAStar(unittest.TestCase):

    def test_valid_input(self):
        graph = [[1, 2], [0, 3], [0, 4], [1, 5], [2, 6], [3, 6], [4, 5]]
        cost = [[1.5, 2], [1.5, 2], [2, 3], [2, 3], [3, 2], [3, 4], [2, 4]]
        h = [8, 4, 4.5, 2, 2, 4, 0]
        myGraph = Graph.Graph(graph, cost)
        result = aStar(myGraph, 0, 6, h, False)
        self.assertEqual(result['seen'], 7)
        self.assertEqual(result['expanded'], 8)
        self.assertEqual(result['cost'], 7.5)
        self.assertEqual(result['max memory'], 3)
        self.assertEqual(result['route'], [0, 2, 4, 5, 6])

    def test_invalid_start_state(self):
        graph = [[1, 2], [0, 3], [0, 4], [1, 5], [2, 6], [3, 6], [4, 5]]
        cost = [[1.5, 2], [1.5, 2], [2, 3], [2, 3], [3, 2], [3, 4], [2, 4]]
        h = [8, 4, 4.5, 2, 2, 4, 0]
        myGraph = Graph.Graph(graph, cost)
        with self.assertRaises(Exception):
            aStar(myGraph, 7, 6, h, False)

if __name__ == '__main__':
    unittest.main()