import random

"""
The coin flip conundrum - Po-Shen Loh
    https://www.youtube.com/watch?v=IAiNqQi30-Y
    
On average, which result will have a fewer coin flips? HH or HT?

A sample run output:

Trials: 10, HH avg. flips: 7.5, HT avg. flips: 4.8
Trials: 100, HH avg. flips: 5.3, HT avg. flips: 3.75
Trials: 1000, HH avg. flips: 5.927, HT avg. flips: 4.039
Trials: 10000, HH avg. flips: 5.9783, HT avg. flips: 4.0011
Trials: 100000, HH avg. flips: 6.00271, HT avg. flips: 3.99993
Trials: 1000000, HH avg. flips: 5.998515, HT avg. flips: 3.997266

"""


class CoinFlipsConundrum:
    def __init__(self, success_outcome: str):
        self._success_outcome = [0 if x == 'H' else 1 for x in success_outcome]

    def flips_until_success(self) -> int:
        flips = 0
        outcome = []

        while outcome != self._success_outcome:
            if len(outcome) == len(self._success_outcome):
                outcome.pop(0)

            outcome.append(random.randint(0, 1))
            flips += 1

        return flips


def trials(coinflipper: CoinFlipsConundrum, t: int) -> float:
    total_flips = 0

    for _ in range(t):
        total_flips += coinflipper.flips_until_success()

    return total_flips/t


if __name__ == '__main__':
    hh = CoinFlipsConundrum('HH')
    ht = CoinFlipsConundrum('HT')

    for n in [10, 100, 1000, 10000, 100000, 1000000]:
        hh_avg = trials(hh, n)
        ht_avg = trials(ht, n)
        print(f"Trials: {n}, HH avg. flips: {hh_avg}, HT avg. flips: {ht_avg}")

