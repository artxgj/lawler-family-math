"""
If you have a fair 6-sided die with sides marked 1, 2, 3, 4, 5, and 6,
how many rolls on average will it take to roll a 6 if any sequence of rolls
containing an odd number prior to seeing a 6 doesn’t count.

So, 2, 4, 4, 6 would count, for example, and 2, 4, 5, 6 would not count.
"""

import random


class Dice:
    def __init__(self, success):
        if success & 1 or success < 2 or success > 6:
            raise ValueError("Roll success must be 2, 4 or 6")
        self._success = success

    def roll_until_success(self) -> int:
        tosses = 0

        tosses = 0
        is_even_sequence = True
        sequence = []

        while True:
            tosses += 1
            lands_on = random.randint(1, 6)
            sequence.append(lands_on)
            if lands_on == self._success and is_even_sequence:
                return tosses
            elif lands_on == self._success:
                is_even_sequence = True
                sequence.clear()
            elif lands_on & 1:
                is_even_sequence = False


def trials(dice: Dice, t: int) -> float:
    tosses = 0

    for _ in range(t):
        tosses += dice.roll_until_success()

    return tosses/t


if __name__ == '__main__':
    success = 6
    dice = Dice(success)

    for n in [10, 100, 1000, 10000, 100000, 1000000]:
        rolls_avg = trials(dice, n)
        print(f"Trials: {n}, number of rolls until a {success}: {rolls_avg}")
