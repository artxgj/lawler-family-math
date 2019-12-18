from graph import Graph, Vertex
from typing import Optional
import random

"""
https://www.johndcook.com/blog/2017/01/04/cover-time-of-a-graph-cliques-chains-and-lollipops/
"""


class CoverTime:
    @staticmethod
    def random_walk(v: Vertex, source_vertex: Optional[Vertex], visited: set, completed: set, walk_stats: dict):
        neighbors = v.neighbors()

        while visited != completed:
            chosen = random.randrange(0, v.degree)
            neighbor = neighbors[chosen]
            walk_stats['count'] += 1
            if neighbor == source_vertex:
                return walk_stats['count']
            else:
                visited.add(neighbor)
                CoverTime.random_walk(neighbor, v, visited, completed, walk_stats)

        return walk_stats['count']

    @staticmethod
    def cover_time(g: Graph) -> float:
        cover = []
        completed = {v for v in g}

        for v in g:
            visited = {v}
            walk_stats = {'count': 0}
            cover.append((v.id, CoverTime.random_walk(v, None, visited, completed, walk_stats)))

        return max(cover, key=lambda x: x[1])[1]


def trials(g: Graph, runs: int):
    total_cover = 0
    for _ in range(runs):
        total_cover += CoverTime.cover_time(g)

    return total_cover/runs


if __name__ == '__main__':
    num_trials = 10000

    complete = Graph()
    s = 'abcdefghij'
    for i, v in enumerate(s):
        s1 = s[i+1:]
        for w in s1:
            complete.add_edge(v, w)

    print(f"Computing cover time of a complete graph of {complete.order} nodes...")
    print(f"Average cover time of {num_trials} trials: {trials(complete, 10000)}")

    chain = Graph()
    for i in range(1, 10):
        chain.add_edge(i, i+1)

    print(f"Computing cover time of a chain graph of {chain.order} nodes...")
    print(f"Average cover time of {num_trials} trials: {trials(chain, 10000)}")

    lollipop = Graph()
    for i in range(1, 5):
        lollipop.add_edge(i, i+1)

    s = 'abcde'
    for j, v in enumerate(s):
        s1 = s[j+1:]
        for w in s1:
            lollipop.add_edge(v, w)

    lollipop.add_edge('e', 1)
    print(f"Computing cover time of a lollipop graph of {lollipop.order} nodes...")
    print(f"Average cover time of {num_trials} trials: {trials(lollipop, 10000)}")




