from typing import IO
from zhmodules import ZhModuleDataIndex

import argparse
import io


def save_pron_index_entries(ostream: IO[str]) -> None:
    mdi = ZhModuleDataIndex()

    for nan_entry in mdi.list_pronunciations(ZhModuleDataIndex.pron_minnan):
        try:
            s = (nan_entry.encode('ascii', 'ignore')).decode("utf-8")
            """
            for nanpron index page, numeric-string names indicate pronunciation files
            """
            int(s)
            ostream.write(f"{s}\n")
        except ValueError:
            pass


def filestream_zhminnan_pronunciations_list(outfilepath):
    with io.open(outfilepath, "w", encoding='utf-8') as ostream:
        save_pron_index_entries(ostream)


def memstream_zhminnan_pronunciations_list():
    s = io.StringIO()
    save_pron_index_entries(s)
    print(s.getvalue())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--outfilepath", help="dialectal synonym output filepath", type=str, required=True)
    args = parser.parse_args()

    filestream_zhminnan_pronunciations_list(args.outfilepath)
    #memstream_zhminnan_pronunciations_list()






