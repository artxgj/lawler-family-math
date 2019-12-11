from typing import Sequence
import random


class LetsMakeADeal:
    """
    See Harvard Stat 110 Lecture on Monty Hall Problem: https://www.youtube.com/watch?v=fDcjhAKuhqQ
    """
    def __init__(self):
        self._doors = [False] * 3
        self._top_prize = random.randint(0, len(self._doors) - 1)
        self._doors[self._top_prize] = True

    def contestant_won(self):
        monty = MontyHall(self._doors)
        contestant = Contestant()
        c_door = contestant.choose_door([i for i in range(len(self._doors))])
        opened_door = monty.open_door(c_door)
        other_closed_door = -1
        for door in range(len(self._doors)):
            if door != opened_door and door != c_door:
                other_closed_door = door
                break

        final_choice = contestant.switch_or_stay(opened_door, other_closed_door)
        win = (contestant.switch_or_stay(opened_door, other_closed_door) == self._top_prize)
        """
        print(f"doors: {self._doors}, opened: {opened_door}, first_choice: {c_door}, final_choice: {final_choice}, win: {win}")
        """
        return win


class MontyHall:
    def __init__(self, game_doors: Sequence[bool]):
        self._non_prize_doors = [i for i, prize in enumerate(game_doors) if not prize]

    def open_door(self, contestant_door: int) -> int:
        if contestant_door in self._non_prize_doors:
            for door in self._non_prize_doors:
                if door != contestant_door:
                    return door
        else:
            # contestant chose a prized door
            door = self._non_prize_doors[random.randint(0, len(self._non_prize_doors) - 1)]
            return door


class Contestant:
    def __init__(self):
        self._selected_door = None
        self._opened_door = None
        self._final_choice = None

    def choose_door(self, doors: Sequence) -> int:
        self._selected_door = random.randint(0, len(doors)-1)
        return self._selected_door

    def switch_or_stay(self, opened_door, other_closed_door) -> bool:
        # always switch
        self._opened_door = opened_door
        self._final_choice = other_closed_door
        return other_closed_door    # always switch door


def trials(t: int) -> float:
    success = 0
    for i in range(t):
        game = LetsMakeADeal()
        if game.contestant_won():
            success += 1

    return success/t


if __name__ == '__main__':
    for t in [10, 100, 1000, 10000, 100000, 1000000]:
        print(f"Trials:{t}, success: {trials(t)}")
