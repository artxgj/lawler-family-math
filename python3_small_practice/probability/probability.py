from collections import Counter
from typing import Any
import random


class UrnException(Exception):
    pass


class Urn:
    def __init__(self, urn: Counter):
        self._urn = []
        for elem, count in urn.items():
            self._urn += [elem]*count

        self._size = len(self._urn)

    def is_empty(self):
        return self._size == 0

    def peek(self) -> Any:
        """
        Shows a random element in the urn (Draw with replacement)
        :return: a randomly selected element
        """
        if self.is_empty():
            raise UrnException('Empty urn')

        rnd_elem = random.randint(0, self._size-1)
        return self._urn[rnd_elem]

    def pop(self) -> Any:
        """
        Removes a randomly selected element from the urn (Draw without replacement)
        :return: A randomly selected element
        """
        if self.is_empty():
            raise UrnException('Empty urn')
        last_elem = self._size - 1
        rnd_elem = random.randint(0, last_elem)
        picked = self._urn[rnd_elem]

        """
        swap selected element with the last element of the urn and 
        update size of unpicked elements
        """
        self._urn[rnd_elem], self._urn[last_elem] = self._urn[last_elem], self._urn[rnd_elem]
        self._size -= 1
        return picked

    @property
    def size(self):
        return self._size

