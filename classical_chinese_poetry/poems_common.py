import csv
import io
from typing import Generator, Tuple
from p3lib.ngrams import ngrams

attr_poet = 'poet'
attr_title = 'title'
attr_poem = 'poem'
verse_delim = '\n'

poem_fieldnames = [attr_title, attr_poet, attr_poem]


def lines_from_poems_csv(poems_csv_path: str) -> Generator[dict, None, None]:
    with io.open(poems_csv_path, 'r', encoding='utf-8') as istream:
        rdr = csv.DictReader(istream)
        for row in rdr:
            yield row


def poems_verse_ngrams(poems: Generator[dict, None, None], ngram_size: int) -> Generator[Tuple[str, ...], None, None]:
    for poem in poems:
        for verse in poem[attr_poem].split(verse_delim):
            for ngram in ngrams(verse, ngram_size):
                yield ngram

