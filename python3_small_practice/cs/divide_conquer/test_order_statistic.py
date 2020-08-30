import random
import unittest

import python3_small_practice.cs.divide_conquer.order_statistic as ord_stat


class MyTestCase(unittest.TestCase):
    def test_median_odd_list(self):
        numbers = [1, 2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 43, 47, 53, 61, 67, 73, 79]
        med = numbers[len(numbers) // 2]
        random.shuffle(numbers)
        self.assertEqual(med, ord_stat.median(numbers))

    def test_median_even_list(self):
        numbers = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 43, 47, 53, 59, 61, 67, 73, 79, 97]
        med = (numbers[len(numbers)//2] + numbers[len(numbers)//2 - 1]) / 2
        random.shuffle(numbers)
        self.assertEqual(med, ord_stat.median(numbers))

    def test_select_ith_smallest(self):
        numbers = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 43, 47, 53, 59, 61, 67, 73, 79, 97]
        random.shuffle(numbers)
        rank_17 = ord_stat.select(numbers, 7)
        self.assertEqual(17, rank_17)
        rank_37 = ord_stat.select(numbers, 12)
        self.assertEqual(37, rank_37)

    def test_select_exception(self):
        with self.assertRaises(ValueError):
            ord_stat.select([12, 7, 13, 15], -1)

        with self.assertRaises(ValueError):
            ord_stat.select([12, 7, 13, 15], 15)

    def test_medians_of_sublists(self):
        numbers = [29, 2, 23, 5, 67, 53, 13, 11, 97, 3, 61, 31, 37, 79, 47, 1, 19, 17, 7, 73, 43, 59]
        medians = ord_stat.medians_of_sublists(numbers, 5)
        self.assertEqual([23, 13, 47, 17, 43], medians)

    def test_partition(self):
        numbers = [29, 2, 23, 5, 67, 53, 13, 11, 97, 3, 61, 31, 37, 79, 47, 1, 19, 17, 7, 73, 59, 43]
        pivot = 43
        rank = ord_stat.partition(numbers, pivot)
        self.assertEqual(13, rank)


if __name__ == '__main__':
    unittest.main()
