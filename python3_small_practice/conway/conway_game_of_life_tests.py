import unittest
from conway import ConwayGameOfLife


class TestConwayGameOfLife(unittest.TestCase):
    def test_init_exception(self):
        with self.assertRaises(ValueError):
            ConwayGameOfLife([[True, False, True],
                              [True, True, False],
                              [True, True]])

    def test_cell_is_alive(self):
        gol = ConwayGameOfLife([[True, False, False],
                                [True, True, False],
                                [True, True, True]])

        self.assertTrue(gol._cell_is_alive(0, 0))
        self.assertFalse(gol._cell_is_alive(0, 1))
        self.assertFalse(gol._cell_is_alive(-1, -1))

    def test_count_live_neighbors(self):
        gol = ConwayGameOfLife([[True, False, False],
                                [True, True, False],
                                [True, True, True]])

        self.assertEqual(2, gol._count_live_neighbors(0, 0))
        self.assertEqual(3, gol._count_live_neighbors(0, 1))
        self.assertEqual(1, gol._count_live_neighbors(0, 2))
        self.assertEqual(4, gol._count_live_neighbors(1, 0))
        self.assertEqual(5, gol._count_live_neighbors(1, 1))
        self.assertEqual(3, gol._count_live_neighbors(1, 2))
        self.assertEqual(3, gol._count_live_neighbors(2, 0))
        self.assertEqual(4, gol._count_live_neighbors(2, 1))
        self.assertEqual(2, gol._count_live_neighbors(2, 2))

    def test_still_life_block(self):
        grid_still_life_block = [[False, False, False, False],
                                 [False, True, True, False],
                                 [False, True, True, False],
                                 [False, False, False, False]]

        gol = ConwayGameOfLife(grid_still_life_block)
        self.assertEqual(grid_still_life_block, gol.next_state())
        self.assertEqual(grid_still_life_block, gol.next_state())

    def test_still_life_beehive(self):
        grid_still_life_beehive = [[False, False, False, False, False, False],
                                   [False, False, False, False, False, False],
                                   [False, False, False, False, False, False],
                                   [False, False, False, False, False, False],
                                   [False, False, False, False, False, False],
                                   [False, False, False, False, False, False]]

        gol = ConwayGameOfLife(grid_still_life_beehive)
        self.assertEqual(grid_still_life_beehive, gol.next_state())
        self.assertEqual(grid_still_life_beehive, gol.next_state())

    def test_oscillator_blinker(self):
        grid_blinker_horizontal = [
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, True, True, True, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
        ]

        grid_blinker_vertical = [
            [False, False, False, False, False],
            [False, False, True, False, False],
            [False, False, True, False, False],
            [False, False, True, False, False],
            [False, False, False, False, False],
        ]

        gol = ConwayGameOfLife(grid_blinker_horizontal)
        self.assertEqual(grid_blinker_vertical, gol.next_state())
        self.assertEqual(grid_blinker_horizontal, gol.next_state())
        self.assertEqual(grid_blinker_vertical, gol.next_state())

    def test_oscillator_beacon(self):
        grid_beacon_period1 = [
            [False, False, False, False, False, False],
            [False, True, True, False, False, False],
            [False, True, True, False, False, False],
            [False, False, False, True, True, False],
            [False, False, False, True, True, False],
            [False, False, False, False, False, False]
        ]

        grid_beacon_period2 = [
            [False, False, False, False, False, False],
            [False, True, True, False, False, False],
            [False, True, False, False, False, False],
            [False, False, False, False, True, False],
            [False, False, False, True, True, False],
            [False, False, False, False, False, False]
        ]

        gol = ConwayGameOfLife(grid_beacon_period1)
        self.assertEqual(grid_beacon_period2, gol.next_state())
        self.assertEqual(grid_beacon_period1, gol.next_state())
        self.assertEqual(grid_beacon_period2, gol.next_state())
