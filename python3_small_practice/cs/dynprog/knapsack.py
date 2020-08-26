from dataclasses import dataclass
from typing import List, Dict, Tuple


@dataclass(frozen=True)
class Item:
    name: str
    weight: float
    value: float


class Knapsack:
    def __init__(self, max_weight: float, unit_weight: float, items: List[Item]):
        self._max_weight = max_weight
        self._unit_weight = unit_weight
        self._items: Dict[int, Item] = {i: item for i, item in enumerate(items)}
        self._table: Dict[Tuple[int, float], float] = self._build_table()
        self._optimal_items = None

    def _build_table(self) -> Dict[Tuple[int, float], float]:
        table: Dict[Tuple[int, float], float] = {}
        for i in range(len(self._items)):
            j = self._unit_weight
            item = self._items[i]
            while j <= self._max_weight:
                item_value = item.value if j >= item.weight else 0.0
                table[(i, j)] = max(table.get((i-1, j), 0), item_value + table.get((i-1, j-item.weight), 0))
                j += self._unit_weight

        return table

    @property
    def max_value(self) -> float:
        return self._table[(len(self._items)-1, self._max_weight)]

    @property
    def optimal_items(self):
        if not self._optimal_items:
            i = len(self._items) - 1
            j = self._max_weight
            optimal_items = set()
            while (value := self._table.get((i, j), 0)) > 0:
                max_value_previous_items = self._table.get((i-1, j-self._items[i].weight), 0)
                if max_value_previous_items + self._items[i].value > self._table.get((i-1, j), 0):
                    optimal_items.add(self._items[i])
                    j -= self._items[i].weight

                i -= 1
            self._optimal_items = optimal_items

        return self._optimal_items
