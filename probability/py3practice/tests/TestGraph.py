import unittest
from graph import Graph


class TestGraph(unittest.TestCase):
    def test__iter__(self):
        g = Graph()
        g.add_edge(1, 2)
        vertices = [v.id for v in g]
        self.assertTrue(1 in vertices and 2 in vertices)

    def test_add_edge(self):
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(2, 3)

        # for unit-test purposes, access private member _vertices
        actual = set([(v.id, n.id) for v in g for n in v.neighbors()])
        expected = {(1, 2), (2, 1), (2, 3), (3, 2)}
        self.assertEqual(actual, expected)

    def test_order(self):
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        self.assertEqual(3, g.order)


if __name__ == '__main__':
    unittest.main()
