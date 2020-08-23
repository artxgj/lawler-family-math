import unittest
from collections import Counter

from python3_small_practice.probability.probability import Urn, UrnException


class TestUrn(unittest.TestCase):
    def test_pop(self):
        bag = Counter(red=3, green=2)
        box = Urn(bag)
        elem = box.pop()
        self.assertTrue(elem in bag and box.size == 4)

    def test_peek(self):
        bag = Counter(red=3, green=2)
        box = Urn(bag)
        elem = box.peek()
        self.assertTrue(elem in bag and box.size == 5)

    def test_urn_is_empty(self):
        bag = Counter(red=3, green=2)
        box = Urn(bag)
        while box.size > 0:
            box.pop()

        self.assertTrue(box.is_empty())

    def test_urn_is_not_empty(self):
        bag = Counter(red=3, green=2)
        box = Urn(bag)
        box.pop()
        self.assertFalse(box.is_empty())

    def test_pop_exception(self):
        box = Urn(Counter(red=1))
        box.pop()

        with self.assertRaises(UrnException):
            box.pop()

    def test_peek_exception(self):
        box = Urn(Counter(red=1))
        box.pop()

        with self.assertRaises(UrnException):
            box.peek()

