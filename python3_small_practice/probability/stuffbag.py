from collections import Counter
import random


class StuffBagWithoutReplacement:
    def __init__(self, bag: Counter):
        self._bag = bag.copy()

    def draw(self) -> str:
        if len(self._bag) == 0:
            raise Exception("bag is empty.")
        elements_last = []
        elements_index = {}

        high = 0
        for i, k in enumerate(self._bag.keys()):
            elements_index[i] = k
            high += self._bag[k]
            elements_last.append(high)

        drew = random.randint(1, high)

        # assumption: number of colors is small, thus the linear search
        for i, elem_max in enumerate(elements_last):
            if drew <= elem_max:
                break

        drawn_element = elements_index[i]
        self._bag[drawn_element] -= 1
        if self._bag[drawn_element] == 0:
            del self._bag[drawn_element]

        return drawn_element

    def count(self, color):
        return self._bag.get(color, 0)

