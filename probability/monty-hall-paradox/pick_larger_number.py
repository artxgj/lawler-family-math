import random

"""
See NYMC Talk by Dr. Po-Shen Loh on Probability for this Charlotte-Maya problem

https://www.youtube.com/watch?v=fNaCeCRH0Ao
"""


class PickLargerNumberGame:
    Left_Number = 0
    Right_Number = 1

    def maya_picked_correctly(self) -> bool:
        charlotte = Charlotte()
        maya = Maya()
        selected_number = charlotte.show_number(maya.coin_flip_pick)
        side_picked = maya.stay_or_switch(selected_number)
        win = charlotte.is_larger_number(side_picked)
        return win


class Charlotte:
    def __init__(self):
        self._real_numbers = (random.random(), random.random())
        self._higher = 1 if self._real_numbers[1] > self._real_numbers[0] else 0

    def show_number(self, side: int) -> float:
        if side < 0 or side > 1:
            raise ValueError(f"{side} is not a valid side.")
        return self._real_numbers[side]

    def is_larger_number(self, side):
        if side < 0 or side > 1:
            raise ValueError(f"{side} is not a valid side.")

        return side == self._higher

    def __str__(self):
        return f"left, right = {self._real_numbers}"


class Maya:
    def __init__(self):
        self._real_number = random.random()
        self._coin_flip_pick = random.randint(PickLargerNumberGame.Left_Number, PickLargerNumberGame.Right_Number)
        self._picked_side = None

    @property
    def coin_flip_pick(self):
        return self._coin_flip_pick

    def stay_or_switch(self, number: float) -> int:
        if self._real_number < number:
            self._picked_side = self._coin_flip_pick
        else:
            self._picked_side = abs(self._coin_flip_pick - PickLargerNumberGame.Right_Number)

        return self._picked_side

    def __str__(self):
        return f"real_number={self._real_number}, coin_flip_pick={self._coin_flip_pick}, picked_side={self._picked_side}"


def trials(t: int) -> float:
    success = 0
    for _ in range(t):
        game = PickLargerNumberGame()
        if game.maya_picked_correctly():
            success += 1

    return success/t


if __name__ == '__main__':
    for t in [10, 100, 1000, 10000, 100000, 1000000]:
        print(f"trials:{t}, success_probability={trials(t)}")



