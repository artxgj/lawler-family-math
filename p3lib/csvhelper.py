from typing import Generator, Sequence, List

import csv
import io


def dictlines_from_csv(csv_path: str, fieldnames: Sequence[str] = None) -> Generator[dict, None, None]:
    with io.open(csv_path, 'r', encoding='utf-8') as istream:
        rdr = csv.DictReader(istream, fieldnames)
        for row in rdr:
            yield row


def lines_from_csv(csv_path: str) -> Generator[List[str], None, None]:
    with io.open(csv_path, 'r', encoding='utf-8') as istream:
        rdr = csv.reader(istream)
        for row in rdr:
            yield row
