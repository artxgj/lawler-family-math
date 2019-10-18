import csv
import argparse

_MD_NEW_POEM = '---'
_MD_POEM_TITLE = '###'
_MD_POEM_poet = '**'
_POET_SPLIT = '*'
_TITLE_SPLIT = '#'
_POEM_LINE_SEP = '+'

_ATTR_POET = 'poet'
_ATTR_POEM = 'poem'
_ATTR_TITLE = 'title'

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
        return _POEM_LINE_SEP.join(self._lines)

    def __repr__(self):
        return f"{self.title},{self.poet},{self.poem}"


def markdown_to_csv(poems_md, poems_csv):
    tangpoem = None
    poem_line = False

    fieldnames = [_ATTR_TITLE, _ATTR_POET, _ATTR_POEM]
    writer = csv.DictWriter(poems_csv, fieldnames, lineterminator='\n')
    writer.writeheader()
    for line in poems_md:
        line = line.strip()

        if line.startswith(_MD_NEW_POEM):
            if tangpoem:
                writer.writerow({_ATTR_TITLE: tangpoem.title,
                _ATTR_POET: tangpoem.poet,
                _ATTR_POEM: tangpoem.poem})

            tangpoem = Poem()
            poem_line = False
        elif line.startswith(_MD_POEM_TITLE):
            tangpoem.title = ''.join(line.split(_TITLE_SPLIT)).strip()
        elif line.startswith(_MD_POEM_poet):
            tangpoem.poet = ''.join(line.split(_POET_SPLIT)).strip()
            poem_line=True
        elif line != '' and poem_line:
            tangpoem.add_line(line)

    if poem_line :
        writer.writerow({_ATTR_TITLE: tangpoem.title,
        _ATTR_POET: tangpoem.poet,
        _ATTR_POEM: tangpoem.poem})

    poems_md.close()
    poems_csv.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--poems-md', help='The poems file written in markdown.', type=argparse.FileType('r'), required=True)
    parser.add_argument('-c', '--csv-poems', help='The output csv file', type=argparse.FileType('w'), required=True)
    args = parser.parse_args()

    markdown_to_csv(args.poems_md, args.csv_poems)



if __name__ == '__main__':
    main()
