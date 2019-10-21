from typing import Tuple, Sequence, Generator
from collections import deque

__all__ = ['ngrams']



def ngrams(grams: Sequence[str], n: int = 1) -> Generator[Tuple[str, ...], None, None]:
    if not isinstance(grams, Sequence):
        raise TypeError('grams is not of type Sequence[str]')

    if n > len(grams):
        return

    qgrams = deque()

    for gram in grams:
        qgrams.append(gram)

        if len(qgrams) == n:
            nitems = tuple(item for item in qgrams)
            yield nitems
            qgrams.popleft()

