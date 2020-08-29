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


def select(numbers: List[int], i: int) -> int:
    """
    :param numbers: List of unique integers
    :param i: the ith smallest element
    :return: the integer

    From: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2015/lecture-notes/MIT6_046JS15_lec02.pdf

    Select(S, i)

    Pick x ∈ S   # pick x cleverly
    Compute k = rank(x)
    B = { y ∈ S | y<x }
    C = { y ∈ S | y>x }

    if k=i
        return x
    elseif k > i
        return Select(B, i)
    elseif k < i
        return Select(C, i − k)


    Picking x Cleverly
    Need to pick x so rank(x) is not extreme.
        • Arrange S into columns of size 5 (I n5 l cols)
        • Sort each column (bigger elements on top) (linear time)
        • Find “median of medians” as x

    """
    if i < 0 or i > len(numbers):
        raise ValueError(f"i = {i} is not valid.")

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
