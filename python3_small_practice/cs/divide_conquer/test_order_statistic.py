import random
import unittest

from python3_small_practice.cs.divide_conquer.order_statistic import median, select


class MyTestCase(unittest.TestCase):
    def test_median_odd_list(self):
        numbers = [1, 2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 43, 47, 53, 61, 67, 73, 79]
        med = numbers[len(numbers) // 2]
        random.shuffle(numbers)
        self.assertEqual(med, median(numbers))

    def test_median_even_list(self):
        numbers = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 43, 47, 53, 59, 61, 67, 73, 79, 97]
        med = (numbers[len(numbers)//2] + numbers[len(numbers)//2 - 1]) / 2
        random.shuffle(numbers)
        self.assertEqual(med, median(numbers))

    def test_order_statistic(self):
        numbers = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 43, 47, 53, 59, 61, 67, 73, 79, 97]
        random.shuffle(numbers)
        self.assertEqual(17, select(numbers, 7))
        self.assertEqual(37, select(numbers, 12))


if __name__ == '__main__':
    unittest.main()
