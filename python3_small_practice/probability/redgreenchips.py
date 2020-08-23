from collections import Counter
from python3_small_practice.probability.probability import Urn

"""
2016 AMC 8 Problems/Problem 21

A box contains 3 red chips and 2 green chips. Chips are drawn randomly, one at a time without
replacement, until all 3 of the reds are drawn or until both green chips are drawn.
What is the probability that the 3 reds are drawn?
 
(A) 3/10  (B) 2/5  (C) 1/2  (D) 3/5  (E) 7/10

"""


class RedGreen:
    def __init__(self, red=3, green=2):
        self._box = Urn(Counter(red=red, green=green))
        self._red = red
        self._green = green

    def draw(self) -> Counter:
        drawn = Counter(red=0, green=0)

        while drawn['red'] < self._red and drawn['green'] < self._green:
            chip = self._box.pop()
            drawn[chip] += 1

        return drawn


def all_reds_drawn(trials=10000):
    red, green = 3, 2
    success = 0
    for _ in range(trials):
        rg = RedGreen(red=red, green=green)
        drawn = rg.draw()
        if drawn['red'] == red:
            success += 1

    return round(success/trials, 2)


if __name__ == '__main__':
    rgprob = all_reds_drawn(trials=100000)
    print(rgprob)



