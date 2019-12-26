import random

"""
If you have a fair 6-sided die with sides marked 1, 2, 3, 4, 5, and 6,
how many rolls on average will it take to roll a 6 if any sequence of rolls
containing an odd number prior to seeing a 6 doesn’t count.

So, 2, 4, 4, 6 would count, for example, and 2, 4, 5, 6 would not count.
"""

"""
https://gilkalai.wordpress.com/2017/09/07/tyi-30-expected-number-of-dice-throws/

You throw a dice until you get 6. What is the expected number of throws 
(including the throw giving 6) conditioned on the event that all throws gave even numbers.
"""


class Dice:
    def __init__(self, success):
        if success & 1 or success < 2 or success > 6:
            raise ValueError("Roll success must be 2, 4 or 6")
        self._success = success

    def roll_until_success(self) -> int:
        tosses = 0
        sequence = []

        thrown_out_seq = 0

        while True:
            tosses += 1
            lands_on = random.randint(1, 6)

            if lands_on & 1:
                sequence.clear()
                thrown_out_seq += 1
                tosses = 0
                continue

            sequence.append(lands_on)
            if lands_on == self._success:
                return tosses


def trials(dice: Dice, t: int) -> float:
    tosses = 0
    success = {}
    for _ in range(t):
        rolls = dice.roll_until_success()
        if rolls in success:
            success[rolls] += 1
        else:
            success[rolls] = 1

        tosses += rolls

    return tosses / t, success


if __name__ == '__main__':
    success = 6
    dice = Dice(success)

    for n in [10, 100, 1000, 10000, 100000, 1000000]:
        rolls_avg, rolls_distribution = trials(dice, n)
        print(f"Trials: {n}, number of rolls until a {success}: {rolls_avg}, {rolls_distribution}")
