from dataclasses import dataclass
from typing import List, Any, Optional, Union

from python3_small_practice.cs.common.task import Task


@dataclass
class TaskEvent:
    val: Any
    type: str
    index: int


class WeightedIntervalScheduleHardWay:
    """
    The hard way of doing things: Using the 0-based indexing of python List.
    Better to "waste" the 0th element
    """
    def __init__(self, tasks: List[Task]):
        sorted_tasks = sorted(tasks, key=lambda t: (t.finish, t.start))
        self._p = self._compute_predecessor(sorted_tasks)
        self._opts = self._compute_opts(sorted_tasks)
        self._solution = self._compute_solution(sorted_tasks)

    def _compute_predecessor(self, tasks: List[Task]) -> List[Optional[int]]:
        task_events = []
        for i, task in enumerate(tasks):
            task_events.append(TaskEvent(val=task.start, type='s', index=i))
            task_events.append(TaskEvent(val=task.finish, type='f', index=i))

        task_events.sort(key=lambda e: (e.val, e.type))
        predecessor = [0] * len(tasks)
        prev_largest_compatible_index = None

        for event in task_events:
            if event.type == 's':
                predecessor[event.index] = prev_largest_compatible_index
            else:
                prev_largest_compatible_index = event.index

        return predecessor

    def _compute_opts(self, tasks: List[Task]):
        opts: List[int] = [0] * len(tasks)
        enumerate_opts = enumerate(opts)
        j, opt = next(enumerate_opts)
        opts[j] = tasks[j].weight

        for j, opt in enumerate_opts:
            weight_previous = 0 if self._p[j] is None else opts[self._p[j]]
            opts[j] = max(tasks[j].weight + weight_previous,
                          opts[j-1])

        return opts

    def _compute_solution(self, tasks):
        solutions = []
        j = len(self._opts) - 1

        while j is not None:
            prev_opt_val = self._opts[j-1] if j > 0 else 0
            opt_val = 0 if self._p[j] is None else self._opts[self._p[j]]
            if tasks[j].weight + opt_val > prev_opt_val:
                solutions.append(tasks[j])
                j = self._p[j]
            else:
                j -= 1
        return solutions

    @property
    def optimal(self):
        return self._opts[-1]

    @property
    def solution(self):
        return self._solution


class WeightedIntervalSchedule:
    def __init__(self, tasks: List[Task]):
        sorted_tasks: List[Optional[Task]] = [None] + sorted(tasks, key=lambda t: (t.finish, t.start))
        self._p = self._compute_predecessor(sorted_tasks)
        self._opts = self._compute_opts(sorted_tasks)
        self._solution = self._compute_solution(sorted_tasks)

    def _compute_predecessor(self, tasks: List[Task]) -> List[Optional[int]]:
        task_events = []
        enumerated_tasks = enumerate(tasks)
        next(enumerated_tasks)

        """
        Implementation of https://www.cs.colostate.edu/~cs320/spring20/slides/06_dynpro-v2.pdf
        """
        for i, task in enumerated_tasks:
            task_events.append(TaskEvent(val=task.start, type='s', index=i))
            task_events.append(TaskEvent(val=task.finish, type='f', index=i))

        task_events.sort(key=lambda e: (e.val, e.type))
        predecessor = [0] * len(tasks)
        prev_largest_compatible_index = 0

        for event in task_events:
            if event.type == 's':
                predecessor[event.index] = prev_largest_compatible_index
            else:
                prev_largest_compatible_index = event.index

        return predecessor

    def _compute_opts(self, tasks: List[Task]):
        opts: List[int] = [0] * len(tasks)
        enumerate_opts = enumerate(opts)
        next(enumerate_opts)

        """
        From https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2015/recitation-notes/MIT6_046JS15_Recitation1.pdf        
        M[0] = 0
        for j=1 to n
            M[j] = max(w(j) + M[p(j)], M[j - 1])
        """
        for j, opt in enumerate_opts:
            opts[j] = max(tasks[j].weight + opts[self._p[j]], opts[j-1])

        return opts

    def _compute_solution(self, tasks):
        solutions = []
        """
        Implementation of https://www.cs.colostate.edu/~cs320/spring20/slides/06_dynpro-v2.pdf
        """
        j = len(self._opts) - 1

        while j > 0:
            if tasks[j].weight + self._opts[self._p[j]] > self._opts[j-1]:
                solutions.append(tasks[j])
                j = self._p[j]
            else:
                j -= 1
        return solutions

    @property
    def optimal(self):
        return self._opts[-1]

    @property
    def solution(self):
        return self._solution


if __name__ == '__main__':
    tasks = [Task(3, 9, 8), Task(5, 8, 4), Task(10, 14, 3), Task(1, 4, 5), Task(7, 11, 1), Task(2, 4, 2)]

    wis = WeightedIntervalScheduleHardWay(tasks)
    print(wis.optimal)
    print(wis.solution)

    print("======")
    wis2 = WeightedIntervalSchedule(tasks)
    print(wis2.optimal)
    print(wis2.solution)

