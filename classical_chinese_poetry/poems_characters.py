import argparse
import csv
import io

from typing import IO


def poetry_words_set(poems_csv: str, ostream: IO[str]) -> None:
    詞 = set()
    with io.open(poems_csv, 'r') as istream:
        reader = csv.DictReader(istream)
        for row in reader:
            詞.update(set(row['poet'].strip()))
            詞.update(set(row['title'].strip()))

            for verse in row['poem'].split('\n'):
                詞.update(set(verse.strip()))

    for word in 詞:
        ostream.write(f'{word}\n')


def dump_to_memory(poems_filepath: str) -> None:
    ostream = io.StringIO()
    poetry_words_set(poems_filepath, ostream)
    print(ostream.getvalue())


def dump_to_file(poems_filepath: str, output_filepath: str) -> None:
    with io.open(output_filepath, 'w', encoding='utf-8') as ostream:
        poetry_words_set(poems_filepath, ostream)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-z', '--hanzi', help='The Chinese characters in the title and body of the poem', required=True)
    parser.add_argument('-c', '--csv-poems', help='The poems csv file', required=True)
    args = parser.parse_args()

    # dump_to_memory(args.csv_poems)
    dump_to_file(args.csv_poems, args.hanzi)


if __name__ == '__main__':
    main()
