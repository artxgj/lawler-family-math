from typing import List

__all__ = ['cjk_ngrams']


def cjk_ngrams(s: str, n: int) -> List[str]:
    if not isinstance(s, str):
        raise TypeError('cjk_ngrams expects s argument to be string.')

    ngrams = []
    q = []
    for c in s:
        if len(q) == n-1:
            ngrams.append(f"{''.join(q)}{c}")
            q.pop(0)
            q.append(c)
        else:
            q.append(c)

    return ngrams
