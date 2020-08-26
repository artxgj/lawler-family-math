from dataclasses import dataclass
from typing import List, Dict, Tuple


@dataclass
class Item:
    name: str
    weight: float
    value: float


class Knapsack:
    def __init__(self, max_weight: float, unit_weight: float, items: List[Item]):
        self._max_weight = max_weight
        self._items = items.copy()
        self._table: Dict[Tuple[int, float], float] = Knapsack.build_table(max_weight, unit_weight, items)

    @staticmethod
    def build_table(sack_weight: float, unit_weight: float, items: List[Item]) -> Dict[Tuple[int, float], float]:
        table: Dict[Tuple[int, float], float] = {}
        for i, item in enumerate(items):
            j = unit_weight
            while j <= sack_weight:
                item_value = item.value if j >= item.weight else 0.0
                table[(i, j)] = max(table.get((i-1, j), 0), item_value + table.get((i-1, j-item.weight), 0))
                j += unit_weight

        return table

    @property
    def max_value(self) -> float:
        return self._table[(len(self._items)-1, self._max_weight)]


if __name__ == '__main__':
    items = [Item('stereo', 4.0, 3000.0),
             Item('laptop', 3.0, 2000.0),
             Item('guitar', 1.0, 1500.0)]

    knapsack = Knapsack(4.0, 1.0, items)
    print(knapsack._table)
    assert(knapsack.max_value == 3500.0)
