from typing import IO
from zhmodules import BaiyueIndex, DialectalSynonymsIndex
import argparse
import io

index_configs = {
    'minnan': {'type': BaiyueIndex, 'data_index': 'nan-pron', 'index-filename': 'nan-pron-index.txt'},
    'cantonese': {'type': BaiyueIndex, 'data_index': 'yue-word', 'index-filename': 'yue-word-index.txt'},
    'hakka': {'type': BaiyueIndex, 'data_index': 'hak-pron', 'index-filename': 'hakka-pron-index.txt'},
    'dialectic_synonyms': {'type': DialectalSynonymsIndex, 'data_index': 'dial-syn', 'index-filename': 'dialectal-synonyms-index.txt'}
}


def output_pron_index_entries(v: dict, ostream: IO[str]) -> None:
    mdi = v['type'](v['data_index'])

    for entry in mdi.get_contents():
        try:
            print(f"entry is {entry}")
            ostream.write(f"{entry}\n")
        except ValueError:
            pass


def filestream_zhminnan_pronunciations_list(index, outfilepath):
    with io.open(outfilepath, "w", encoding='utf-8') as ostream:
        output_pron_index_entries(index, ostream)


def memstream_zhminnan_pronunciations_list(index):
    s = io.StringIO()
    output_pron_index_entries(index, s)
    print(s.getvalue())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--outfilepath", help="dialectal synonym output filepath", type=str, required=True)
    args = parser.parse_args()

    for k, v in index_configs.items():
        memstream_zhminnan_pronunciations_list(v)
        filestream_zhminnan_pronunciations_list(v, f"{args.outfilepath}/{v['index-filename']}")








