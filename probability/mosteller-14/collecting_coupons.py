from random import randint


class CouponsCollector:
    """
    Problem 14: Collecting Coupons
    """

    def __init__(self, coupons):
        self._coupons = coupons

    def run(self) -> int:
        boxes = 0
        coupons = set()

        while True:
            boxes += 1
            coupons.add(randint(1, self._coupons))

            if len(coupons) == self._coupons:
                return boxes

    def trials(self, n):
        frequencies = {}

        for _ in range(n):
            boxes = self.run()

            if boxes in frequencies:
                frequencies[boxes] += 1

            else:
                frequencies[boxes] = 1

        return frequencies


def stats(frequencies: dict):
    total_observations = sum(x * y for x, y in frequencies.items())
    max_x = max(x for x in frequencies.keys())
    min_x = min(x for x in frequencies.keys())

    total_count = sum(y for y in frequencies.values())
    print(total_count)
    print(f"average: {total_observations/total_count}")
    print(max_x)
    print(min_x)


if __name__ == '__main__':
    cc = CouponsCollector(5)
    for trials in [10, 100, 1000, 10000, 100000, 1000000]:
        freq = cc.trials(trials)
        stats(freq)
        print("...")
