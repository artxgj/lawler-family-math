import random
import argparse


class BirthdayParadox:
    def __init__(self, items: int, pigeonholes: int):
        self._items = items
        self._pigeonholes = [0] * pigeonholes

    def run(self) -> float:
        birthday = {}

        for i in range(len(self._pigeonholes)):
            bday = random.randint(1, self._items)
            self._pigeonholes[i] = bday
            if bday in birthday:
                birthday[bday].append(i)
            else:
                birthday[bday] = [i]

        matches = 0
        output = []
        for i in range(len(self._pigeonholes)):
            bday = self._pigeonholes[i]
            if len(birthday[bday]) > 1:
                matches += 1
                output.append(f"* {bday} *")
            else:
                output.append(f"{bday}")

        return matches

    def trials(self, n: int):
        matches = 0

        for _ in range(n):
            if self.run() > 0:
                matches += 1

        return matches/n


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--items", type=int, required=True, help="number of items (e.g., number of days in a year")
    parser.add_argument("-p", "--people", type=int, required=True, help="number of people in a room")
    args = parser.parse_args()
    bp = BirthdayParadox(args.items, args.people)

    for t in [10, 100, 1000, 10000, 100000]:
        print(t, bp.trials(t))
