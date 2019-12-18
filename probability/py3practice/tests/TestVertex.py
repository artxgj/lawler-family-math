import unittest
from graph import Vertex


class TestVertex(unittest.TestCase):
    def test_no_neighbors(self):
        v = Vertex(1)
        expected = 0
        self.assertEqual(expected, len(v.neighbors()))

    def test_add_neighbor(self):
        v_a = Vertex('a')
        v_b = Vertex('b')
        v_c = Vertex('c')
        v_a.add_neighbor(v_b)
        v_a.add_neighbor(v_c)

        expected = 2
        self.assertEqual(expected, len(v_a.neighbors()))

    def test_add_self_neighbor(self):
        v_a = Vertex('a')

        with self.assertRaises(ValueError):
            v_a.add_neighbor(v_a)

    def test_neighbors(self):
        v_a = Vertex('a')
        v_b = Vertex('b')
        v_c = Vertex('c')
        v_a.add_neighbor(v_b)
        v_a.add_neighbor(v_c)

        expected = {v_b, v_c}
        actual = set(v_a.neighbors())

        self.assertEqual(expected, actual)

    def test_degree(self):
        v_a = Vertex('a')
        v_b = Vertex('b')
        v_c = Vertex('c')
        v_d = Vertex('d')
        v_a.add_neighbor(v_b)
        v_a.add_neighbor(v_c)
        v_a.add_neighbor(v_d)

        self.assertEqual(3, v_a.degree)


if __name__ == '__main__':
    unittest.main()
