from iohelpers import lines_from_textfile
from wiktionary import WicktionaryRevisionEntrySearch
from iohelpers import lines_to_textfile

import datetime
import errno
import os


def get_words(words):
    wikt = WicktionaryRevisionEntrySearch()

    for word in words:
        try:
            res = wikt.find(word)
            yield word, res.content
        except Exception as e:
            print(e)


if __name__ == '__main__':
    today = datetime.datetime.today().strftime('%Y%m%d')
    folder = f'../data/enwiktionary/zh-words/{today}'

    try:
        os.mkdir(folder)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise

    for word, wiktcontent in get_words(lines_from_textfile('../data/enwiktionary/words-search/words-retrieval-list.20191125.txt')):
        print(word)
        lines_to_textfile(f'{folder}/{word}', [wiktcontent])

