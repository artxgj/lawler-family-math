from typing import Generator, Sequence, List

import csv
import io


def dictlines_from_csv(csv_path: str, fieldnames: Sequence[str] = None, encoding: str = 'utf-8') -> Generator[dict, None, None]:
    with io.open(csv_path, 'r', encoding=encoding) as istream:
        rdr = csv.DictReader(istream, fieldnames)
        for row in rdr:
            yield row


def lines_from_csv(csv_path: str, encoding: str = 'utf-8') -> Generator[List[str], None, None]:
    with io.open(csv_path, 'r', encoding=encoding) as istream:
        rdr = csv.reader(istream)
        for row in rdr:
            yield row
