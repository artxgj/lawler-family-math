from typing import List


def medians_of_sublists(a_list: List[int], sublist_size) -> List[int]:
    medians = []

    for i in range(0, len(a_list), sublist_size):
        sublist = sorted(a_list[i:i+sublist_size], key=lambda n: -n)
        medians.append(sublist[len(sublist) // 2])

    return medians


def partition(numbers: List[int], pivot: int) -> int:
    i, j, last = -1, 0, len(numbers) - 1

    while j < last:
        if numbers[j] < pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
        elif numbers[j] == pivot:
            numbers[j], numbers[last] = numbers[last], numbers[j]
            if numbers[j] < pivot:
                j -= 1
        j += 1

    numbers[i+1], numbers[last] = numbers[last], numbers[i+1]
    return i+1


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
        • Arrange S into columns of sublist_size 5 (I n5 l cols)
        • Sort each column (bigger elements on top) (linear time)
        • Find “median of medians” as x
    """

    if i < 0 or i > len(numbers):
        raise ValueError(f"i = {i} is not valid.")

    sublist_size = 5
    medians = medians_of_sublists(numbers, sublist_size)

    if len(medians) <= sublist_size:
        pivot = sorted(medians)[len(medians)//2]
    else:
        pivot = select(medians)

    rank = partition(numbers,  pivot)

    if rank == i:
        return pivot
    elif rank > i:
        return select(numbers[:rank], i)
    else:
        return select(numbers[rank+1:], i-rank-1)   # -1 is to account for python's zero-based list index


def median(numbers: List[int]) -> float:
    if len(numbers) % 2 == 1:
        return select(numbers, len(numbers) // 2)
    else:
        lower_median = select(numbers, len(numbers) // 2 - 1)
        upper_median = select(numbers, len(numbers) // 2)
        return (lower_median + upper_median) / 2
