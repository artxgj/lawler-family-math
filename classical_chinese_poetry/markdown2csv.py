import argparse
import csv
import io

from typing import IO
from poems_common import attr_poem, attr_poet, attr_title, verse_delim, poem_fieldnames


_MD_NEW_POEM = '---'
_MD_POEM_TITLE = '###'
_MD_POEM_poet = '**'
_POET_SPLIT = '*'
_TITLE_SPLIT = '#'


class Poem:
    def __init__(self):
        self._lines = []

    @property
    def poet(self):
        return self._poet

    @poet.setter
    def poet(self, poet):
        self._poet = poet

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def add_line(self, line):
        self._lines.append(line)

    @property
    def poem(self):
        return verse_delim.join(self._lines)

    def __repr__(self):
        return f"{self.title},{self.poet},{self.poem}"


def markdown_to_csv(istream_md: IO[str], ostream_csv: IO[str]) -> None:
    tangpoem = None
    poem_line = False

    writer = csv.DictWriter(ostream_csv, poem_fieldnames, lineterminator='\n', quoting=csv.QUOTE_ALL)
    writer.writeheader()

    for line in istream_md:
        line = line.strip()

        if line.startswith(_MD_NEW_POEM):
            if tangpoem:
                writer.writerow({attr_title: tangpoem.title,
                                 attr_poet: tangpoem.poet,
                                 attr_poem: tangpoem.poem})

            tangpoem = Poem()
            poem_line = False
        elif line.startswith(_MD_POEM_TITLE):
            tangpoem.title = ''.join(line.split(_TITLE_SPLIT)).strip()
        elif line.startswith(_MD_POEM_poet):
            tangpoem.poet = ''.join(line.split(_POET_SPLIT)).strip()
            poem_line = True
        elif line != '' and poem_line:
            tangpoem.add_line(line)

    if poem_line:
        writer.writerow({attr_title: tangpoem.title,
                         attr_poet: tangpoem.poet,
                         attr_poem: tangpoem.poem})


def dump_to_memory(istream: IO[str]) -> None:
    ostream = io.StringIO()
    markdown_to_csv(istream, ostream)
    print(ostream.getvalue())


def dump_to_file(istream: IO[str], outfilepath: str) -> None:
    with io.open(outfilepath, 'w', encoding='utf-8') as ostream:
        markdown_to_csv(istream, ostream)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--poems-md', help='The poems file written in markdown.', required=True)
    parser.add_argument('-c', '--csv-poems', help='The output csv file', required=True)
    args = parser.parse_args()

    with io.open(args.poems_md, 'r', encoding='utf-8') as istream:
        # dump_to_memory(istream)
        dump_to_file(istream, args.csv_poems)


if __name__ == '__main__':
    main()
