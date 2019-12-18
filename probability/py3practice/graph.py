from __future__ import annotations
from typing import List, Union

"""
https://stackoverflow.com/questions/33533148/how-do-i-specify-that-the-return-type-of-a-method-is-the-same-as-the-class-itsel
"""


class Graph:
    def __init__(self):
        self._vertices = {}

    @property
    def order(self):
        return len(self._vertices)

    def add_edge(self, v1: Union[int, str], v2: Union[int, str]) -> None:
        if v1 in self._vertices:
            vv1 = self._vertices[v1]
        else:
            vv1 = Vertex(v1)
            self._vertices[v1] = vv1

        if v2 in self._vertices:
            vv2 = self._vertices[v2]
        else:
            vv2 = Vertex(v2)
            self._vertices[v2] = vv2

        vv1.add_neighbor(vv2)
        vv2.add_neighbor(vv1)

    def __iter__(self):
        return iter(self._vertices.values())


class Vertex:
    def __init__(self, name: Union[int, str]):
        self._id = name
        self._neighbors = set()

    @property
    def id(self) -> Union[int, str]:
        return self._id

    def add_neighbor(self, v: Vertex):
        if self == v:
            raise ValueError('vertex cannot be a neighbor of itself.')

        self._neighbors.add(v)

    def neighbors(self) -> List[Vertex]:
        return list(self._neighbors)

    @property
    def degree(self):
        return len(self._neighbors)
