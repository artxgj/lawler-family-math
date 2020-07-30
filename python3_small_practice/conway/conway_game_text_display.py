from conway import ConwayGrid, ConwayGameOfLife
from typing import List
from collections import namedtuple

GridConfig = namedtuple('GridConfig', ('name', 'state', 'live', 'dead'))


def exec_conway_game(grid_config: GridConfig, frequency: int = 6):
    cgd = ConwayGrid(grid_config.live, grid_config.dead)
    conway = ConwayGameOfLife(grid_config.state)
    grid_state = grid_config.state
    print("= = = = = = = = = = = = = = = = = =")
    print(f"Pattern: {grid_config.name}")
    print("= = = = = = = = = = = = = = = = = =")

    for _ in range(frequency):
        for row in cgd.map(grid_state):
            print(''.join(row))
        print()
        grid_state = conway.next_state()


def grid_configurations() -> List[GridConfig]:
    #
    # See https://en.wikipedia.org/wiki/Conway's_Game_of_Life for list of pattern examples
    #
    n = 17
    live = True
    dead = False

    pulsar = [
        [dead] * n,
        [dead, dead, dead, dead, dead, live, dead, dead, dead, dead, dead, live, dead, dead, dead, dead, dead],
        [dead, dead, dead, dead, dead, live, dead, dead, dead, dead, dead, live, dead, dead, dead, dead, dead],
        [dead, dead, dead, dead, dead, live, live, dead, dead, dead, live, live, dead, dead, dead, dead, dead],
        [dead] * n,
        [dead, live, live, live, dead, dead, live, live, dead, live, live, dead, dead, live, live, live, dead],
        [dead, dead, dead, live, dead, live, dead, live, dead, live, dead, live, dead, live, dead, dead, dead],
        [dead, dead, dead, dead, dead, live, live, dead, dead, dead, live, live, dead, dead, dead, dead, dead],
        [dead] * n,
        [dead, dead, dead, dead, dead, live, live, dead, dead, dead, live, live, dead, dead, dead, dead, dead],
        [dead, dead, dead, live, dead, live, dead, live, dead, live, dead, live, dead, live, dead, dead, dead],
        [dead, live, live, live, dead, dead, live, live, dead, live, live, dead, dead, live, live, live, dead],
        [dead] * n,
        [dead, dead, dead, dead, dead, live, live, dead, dead, dead, live, live, dead, dead, dead, dead, dead],
        [dead, dead, dead, dead, dead, live, dead, dead, dead, dead, dead, live, dead, dead, dead, dead, dead],
        [dead, dead, dead, dead, dead, live, dead, dead, dead, dead, dead, live, dead, dead, dead, dead, dead],
        [dead] * n,
    ]

    n = 7
    glider = [
        [dead] * n,
        [dead, dead, live] + [dead] * (n-3),
        [dead, dead, dead, live] + [dead] * (n-4),
        [dead, live, live, live] + [dead] * (n-4),
        [dead] * n,
        [dead] * n,
        [dead] * n,
    ]

    return [GridConfig("pulsar", pulsar, 'o', ' '), GridConfig("glider", glider, 'O', '-')]


def main():
    for grid_config in grid_configurations():
        exec_conway_game(grid_config, 12)


if __name__ == '__main__':
    main()
