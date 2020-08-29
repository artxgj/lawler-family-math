from typing import List
import math
import random


def make_list_of_lists(a_list: List[int], subl_size=5) -> List[List[int]]:
    size = math.ceil(len(a_list) / subl_size)
    index = 0
    output = []

    for i in range(size):
        output.append(sorted(a_list[index:index+subl_size], key=lambda n: -n))
        index += subl_size

    return output


def find_median_of_medians(medians_list: List[int]):
    return select(medians_list, len(medians_list) // 2 - 1)


def select(numbers: List[int], i: int) -> int:
    lol = make_list_of_lists(numbers)
    medians_list = [lis[len(lis) // 2] for lis in lol]

    # randomized pivot
    approx_median = medians_list[random.randint(0, len(medians_list) - 1)]

    b, c = [], []
    for x in numbers:
        if x < approx_median:
            b.append(x)
        elif x > approx_median:
            c.append(x)

    rank_x = len(b)

    if rank_x == i:
        return approx_median
    elif rank_x > i:
        return select(b, i)
    else:
        return select(c, i - rank_x - 1)   # -1 is to account for python's zero-based list index


def median(numbers: List[int]) -> float:
    if len(numbers) % 2 == 1:
        return select(numbers, len(numbers) // 2)
    else:
        lower_median = select(numbers, len(numbers) // 2 - 1)
        upper_median = select(numbers, len(numbers) // 2)
        return (lower_median + upper_median) / 2
