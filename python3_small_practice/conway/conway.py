from collections import namedtuple
from typing import List

ConwayCellState = namedtuple('ConwayCellState', ('live', 'neighbors'))


class ConwayGameOfLife:
    _state_transitions = {
        ConwayCellState(True, 2): True,
        ConwayCellState(True, 3): True,
        ConwayCellState(False, 3): True
    }

    def __init__(self, grid: List[List[bool]]):
        """
        :param grid: n x n grid, True means live cell, False means dead cell
        """
        if not all((len(row) == len(grid) for row in grid)):
            raise ValueError("grid is not a square matrix")

        self._grid = grid.copy()

    def next_state(self) -> List[List[bool]]:
        new_grid = [[ConwayGameOfLife._state_transitions.get(
                ConwayCellState(self._grid[row][col], self._count_live_neighbors(row, col)), False)
                for col in range(len(self._grid))] for row in range(len(self._grid))]

        for row in range(len(self._grid)):
            for col in range(len(self._grid)):
                self._grid[row][col] = new_grid[row][col]

        return new_grid

    def _cell_is_alive(self, row, col) -> bool:
        return False if row < 0 or row >= len(self._grid) or col < 0 or col >= len(self._grid) else self._grid[row][col]

    def _count_live_neighbors(self, row: int, col: int) -> int:
        return \
            (self._cell_is_alive(row-1, col-1) + self._cell_is_alive(row-1, col) + self._cell_is_alive(row-1, col+1) +
             self._cell_is_alive(row, col-1) + self._cell_is_alive(row, col+1) +
             self._cell_is_alive(row+1, col-1) + self._cell_is_alive(row+1, col) + self._cell_is_alive(row+1, col+1))


class ConwayGrid:
    def __init__(self, live: str = 'x', dead: str = ' '):
        self._cell_display = {True: live, False: dead}
        self._live = live
        self._dead = dead

    @property
    def live(self):
        return self._live

    @property
    def dead(self):
        return self._dead

    def map(self, conway_grid: List[List[bool]]):
        return [[self._cell_display[conway_grid[row][col]] for col in range(len(conway_grid))]
                for row in range(len(conway_grid))]