from random import randint


class CouponsCollector:
    """
    Problem 14: Collecting Coupons
    """
    @staticmethod
    def run() -> int:
        boxes = 0
        coupons = set()

        while True:
            boxes += 1
            coupons.add(randint(1, 5))

            if len(coupons) == 5:
                break

        return boxes


if __name__ == '__main__':
    simulcount = 1000000
    total = 0
    for _ in range(simulcount):
        boxes = CouponsCollector.run()
        print(boxes)
        total += boxes

    print(f"Average: {total/simulcount}")
