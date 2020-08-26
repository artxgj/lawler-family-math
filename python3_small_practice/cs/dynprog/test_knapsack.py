from unittest import TestCase
from python3_small_practice.cs.dynprog.knapsack import Knapsack, Item

"""
    Test cases come from Dynamic Programming lessons of  Aditya Y. Bhargava's 
    "Grokking Algorithms: An Illustrated Guide For Programmers and Other Curious People"
"""


class TestKnapsack(TestCase):
    def test_stealing(self):
        items = [Item('stereo', 4.0, 3000.0),
                 Item('laptop', 3.0, 2000.0),
                 Item('guitar', 1.0, 1500.0)]

        knapsack = Knapsack(4.0, 1.0, items)
        self.assertEqual(3500.0, knapsack.max_value)

    def test_itinerary(self):
        itinerary = [
            Item('Westminster Abbey', 0.5, 7),
            Item('Globe Theater', 0.5, 6),
            Item('National Gallery', 1, 9),
            Item('British Museum', 2, 9),
            Item('St. Paul\'s Cathedral', 0.5, 8)
        ]

        knapsack = Knapsack(2.0, 0.5, itinerary)
        self.assertEqual(24.0, knapsack.max_value)

