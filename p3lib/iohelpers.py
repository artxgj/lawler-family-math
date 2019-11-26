from typing import Generator, Iterator, Sequence, List

import csv
import io
import json
import os


def dictlines_from_csv(csv_path: str, fieldnames: Sequence[str] = None, encoding: str = 'utf-8') -> Generator[dict, None, None]:
    with io.open(csv_path, 'r', encoding=encoding) as istream:
        rdr = csv.DictReader(istream, fieldnames)
        for row in rdr:
            yield row


def dictlines_to_csv(csv_path: str, fieldnames, dictlines: Iterator[dict], encoding: str = 'utf-8'):
    with open(csv_path, 'w', encoding=encoding) as ostream:
        wrtr = csv.DictWriter(ostream, fieldnames=fieldnames)
        wrtr.writeheader()

        for row in dictlines:
            wrtr.writerow(row)


def lines_from_csv(csv_path: str, encoding: str = 'utf-8') -> Generator[List[str], None, None]:
    with io.open(csv_path, 'r', encoding=encoding) as istream:
        rdr = csv.reader(istream)
        for row in rdr:
            yield row


def lines_to_csv(csv_path: str, lines: Iterator[Sequence], encoding: str = 'utf-8', dialect=csv.unix_dialect):
    with io.open(csv_path, 'w', encoding=encoding) as ostream:
        wrtr = csv.writer(ostream, dialect=dialect)
        for line in lines:
            wrtr.writerow(line)


def lines_from_textfile(filepath: str, encoding: str = 'utf-8'):
    with open(filepath, 'r', encoding=encoding) as istream:
        for line in istream:
            yield line.strip()


def lines_to_textfile(filepath: str, lines: Iterator[str], encoding: str = 'utf-8'):
    with io.open(filepath, 'w', encoding=encoding) as ostream:
        for line in lines:
            ostream.write(f"{line}\n")


def filenames_from_folder(folder_path: str) -> Iterator[str]:
    for f in os.listdir(folder_path):
        yield f


def local_json_resource(file_path: str) -> dict:
    with open(file_path, 'r', encoding='utf-8') as fs:
        return json.load(fs)


def to_json_file(file_path: str, data_dict: dict, indent=None):
    with open(file_path, 'w', encoding='utf-8') as ostr:
        json.dump(data_dict, ostr, ensure_ascii=False, indent=indent)
