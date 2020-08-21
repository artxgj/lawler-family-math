from collections import Counter
from python3_small_practice.probability.stuffbag import StuffBagWithoutReplacement


class RedGreen:
    def __init__(self, red=3, green=2):
        self._bag = StuffBagWithoutReplacement(Counter(red=red, green=green))
        self._red = red
        self._green = green

    def draw(self) -> Counter:
        drawn = Counter(red=0, green=0)

        while drawn['red'] < self._red and drawn['green'] < self._green:
            chip = self._bag.draw()
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



