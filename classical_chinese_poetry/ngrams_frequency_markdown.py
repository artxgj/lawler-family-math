from poems_common import ngram_frequency
from p3lib.markdown import Markdown
from typing import List, Tuple

import argparse
import io


def ngram_name(ngram_size):
    if ngram_size == 1:
        return 'Unigram'
    elif ngram_size == 2:
        return 'Bigram'
    elif ngram_size == 3:
        return 'Trigram'
    else:
        return f"{ngram_size}-gram"


def markdown_report(ngram_size: int, num_poems: int,
                    rawfreqdata: List[Tuple[Tuple[str, ...], int]]) -> str:

    gram_name = ngram_name(ngram_size)

    frequency_data_rows = '\n'.join([Markdown.table_row([''.join(ngram), str(count)]) for ngram, count in rawfreqdata])

    ngram_report = f"""## Tang Poems: {gram_name}s Frequency Table   
_Computed using the verses from {num_poems} Tang poems_

| {gram_name} | Frequency |
|:-----------------:|:-------------:|  
{frequency_data_rows}
"""
    return ngram_report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--ngram-size', help='The size of the ngram', type=int, required=True)
    parser.add_argument('-m', '--markdown-file', help='The output file of ngrams', required=True)
    parser.add_argument('-c', '--csv-poems', help='The poems csv file', required=True)

    args = parser.parse_args()
    freqtable = ngram_frequency(args.csv_poems, args.ngram_size)
    ordered_freq = sorted(freqtable.items(), key=lambda kv: kv[1], reverse=True)
    ngramfreq = markdown_report(args.ngram_size, 73, ordered_freq)

    with io.open(args.markdown_file, 'w', encoding='utf-8') as ostream:
        ostream.write(ngramfreq)


if __name__ == '__main__':
    main()
