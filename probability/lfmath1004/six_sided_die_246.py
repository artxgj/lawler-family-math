"""
If you have a fair 6-sided die with sides marked 2, 2, 4, 4, 6, and 6,
how many rolls on average will it take for you to roll a 6.
"""

import random


class Dice:
    def __init__(self, success: int):
        if success & 1 or success < 2 or success > 6:
            raise ValueError("Roll success must be 2, 4 or 6")
        self._success = success

    def roll_until_success(self) -> int:
        tosses = 0

        while True:
            tosses += 1
            lands_on = random.randint(1, 6)
            if lands_on == self._success or lands_on == self._success - 1:
                return tosses


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
