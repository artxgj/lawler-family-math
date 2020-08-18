from typing import List, Union, Optional
from dataclasses import dataclass

from python3_small_practice.cs.common.task import Task


@dataclass
class IntervalEvent:
    val: Union[float, int]
    type: str
    index: int


class IntervalScheduling:
    def __init__(self, tasks: List[Task]):
        self._scheduled_intervals = self._greedy(tasks)
        self._opt_intervals = len(self._scheduled_intervals)

    def _greedy(self, tasks: List[Task]):
        sorted_tasks = sorted(tasks, key=lambda t: (t.finish, t.start))

        prev_fin = sorted_tasks[0].start
        solution = []
        for t in sorted_tasks:
            if t.start >= prev_fin:
                solution.append(t)
                prev_fin = t.finish

        return solution

    @property
    def optimal_intervals(self) -> int:
        return self._opt_intervals

    @property
    def optimal_schedule(self) -> List[Task]:
        return self._scheduled_intervals


if __name__ == '__main__':
    tasks = [Task(3, 9), Task(5, 8), Task(10, 14), Task(1, 4), Task(7, 11), Task(2, 4)]
    sked = IntervalScheduling(tasks)
    assert sked.optimal_intervals == 3
    print(tasks)
    print(sked.optimal_schedule)
    print("==----==")
    tasks_list = [Task(1, 6, 5), Task(7, 9, 1), Task(10, 12, 2),
                  Task(2, 3, 1), Task(4, 5, 2), Task(6, 7, 3), Task(8, 9, 2), Task(11, 13, 5)]
    sked1 = IntervalScheduling(tasks_list)
    assert sked1.optimal_intervals == 5
    print(tasks_list)
    print(sked1.optimal_schedule)

