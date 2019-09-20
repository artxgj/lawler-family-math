import csv
import argparse
from typing import IO


def chars_to_file(f: IO[str] , s) -> None:
    if isinstance(s, list):
        s = ''.join(s)
    elif not isinstance(s, str):
        raise TypeError("chars_to_file's s argument must a list of strings or a string")

    for c in s:
        f.write(f'{c}\n')

def chars_title_poem(csv_poems_filepath, hanzi_filepath):
    with open(csv_poems_filepath, 'r') as csv_in:
        reader = csv.DictReader(csv_in)
        with open(hanzi_filepath, 'w') as hanzi_out:
            for row in reader:
                chars_to_file(hanzi_out, row['title'])
                chars_to_file(hanzi_out, row['poem'].split('+'))



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-z', '--hanzi', help='The Chinese characters in the title and body of the poem', required=True)
    parser.add_argument('-c', '--csv-poems', help='The poems csv file', required=True)
    args = parser.parse_args()

    chars_title_poem(args.csv_poems, args.hanzi)


if __name__ == '__main__':
    main()
