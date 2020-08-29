import unittest
from python3_small_practice.conway.conway import ConwayGameOfLife, ConwayGrid


class TestConwayGrid(unittest.TestCase):
    def setUp(self) -> None:
        self.grid_display = ConwayGrid('o', '-')

    def test_still_life_block(self):
        live = self.grid_display.live
        dead = self.grid_display.dead

        grid_still_life_block = [[False, False, False, False],
                                 [False, True, True, False],
                                 [False, True, True, False],
                                 [False, False, False, False]]

        expected_display = [
            [dead, dead, dead, dead],
            [dead, live, live, dead],
            [dead, live, live, dead],
            [dead, dead, dead, dead],
        ]

        self.assertEqual(expected_display, self.grid_display.map(grid_still_life_block))

        gol = ConwayGameOfLife(grid_still_life_block)
        self.assertEqual(expected_display, self.grid_display.map(gol.next_state()))

    def test_oscillator_blinker(self):
        live = self.grid_display.live
        dead = self.grid_display.dead

        grid_blinker_horizontal = [
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, True, True, True, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
        ]

        grid_blinker_horizontal_display = [
            [dead, dead, dead, dead, dead],
            [dead, dead, dead, dead, dead],
            [dead, live, live, live, dead],
            [dead, dead, dead, dead, dead],
            [dead, dead, dead, dead, dead],
        ]

        grid_blinker_vertical_display = [
            [dead, dead, dead, dead, dead],
            [dead, dead, live, dead, dead],
            [dead, dead, live, dead, dead],
            [dead, dead, live, dead, dead],
            [dead, dead, dead, dead, dead],
        ]

        self.assertEqual(grid_blinker_horizontal_display,
                         self.grid_display.map(grid_blinker_horizontal))

        gol = ConwayGameOfLife(grid_blinker_horizontal)
        self.assertEqual(grid_blinker_vertical_display, self.grid_display.map(gol.next_state()))
        self.assertEqual(grid_blinker_horizontal_display, self.grid_display.map(gol.next_state()))
        self.assertEqual(grid_blinker_vertical_display, self.grid_display.map(gol.next_state()))
