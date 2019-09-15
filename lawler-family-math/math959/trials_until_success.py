import argparse
import random
import math

"""
Before watching the lesson-videos, this is my interpretation of
trials until success.

"""

class FairDie:
    def __init__(self, sides):
        self._sides = sides

    def roll(self):
        return math.ceil(random.random() * self._sides)

class LuckyDieRoll:
    def __init__(self, die, win_outcome):
        self._die = die
        self._win_outcome = win_outcome

    def is_win(self):
        x = self._die.roll()
        return self._die.roll() == self._win_outcome


def simulations(tests, pred):
    sum_of_rolls = 0
    for _ in range(tests+1):
        num_rolls = 0
        while True:
            num_rolls += 1
            if pred():
                break
        sum_of_rolls += num_rolls
    return sum_of_rolls/tests


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number",help="the 'success' number of a rolled die; the default is the 6-side of the die.", type=int, default=6)
    parser.add_argument("-s", "--sides", help="the number of sides of a fair die; the default is 6.", type=int, default=6)
    parser.add_argument("-t", "--tests", help="the number of tests to run for the simulation.", type=int, default=10000)
    args = parser.parse_args()

    if args.sides < 6:
        raise ValueError("6 is the minimum number of sides for a die.")

    if args.number < 1 and args.number > args.sides:
        raise ValueError("Successful number %d is not valid for %d-sided die" % (args.number, args.sides))

    fairdie = FairDie(args.sides)
    diegame = LuckyDieRoll(fairdie, args.number)
    res = simulations(args.tests, diegame.is_win)
    print(f"{res} trials until first success for {args.sides}-sided die [{args.tests} tests].")
