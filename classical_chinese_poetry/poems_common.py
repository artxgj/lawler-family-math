from typing import Generator, Tuple
from p3lib.ngrams import ngrams
from p3lib.csvhelper import dictlines_from_csv


attr_poet = 'poet'
attr_title = 'title'
attr_poem = 'poem'
verse_delim = '\n'

poem_fieldnames = [attr_title, attr_poet, attr_poem]


def poems_verse_ngrams(poems: Generator[dict, None, None], ngram_size: int) -> Generator[Tuple[str, ...], None, None]:
    for poem in poems:
        for verse in poem[attr_poem].split(verse_delim):
            for ngram in ngrams(verse, ngram_size):
                yield ngram


def ngram_frequency(poems_csv_path: str, ngram_size: int) -> dict:
    frequency = {}

    poems = dictlines_from_csv(poems_csv_path)

    for ngram in poems_verse_ngrams(poems, ngram_size):
        if ngram not in frequency:
            frequency[ngram] = 1
        else:
            frequency[ngram] += 1

    return frequency

