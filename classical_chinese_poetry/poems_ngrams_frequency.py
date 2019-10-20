import argparse
import csv
import io

from poems_common import lines_from_poems_csv, poems_verse_ngrams


def ngram_frequency(poems_csv_path: str, ngram_size: int) -> dict:
    frequency = {}

    poems = lines_from_poems_csv(poems_csv_path)

    for ngram in poems_verse_ngrams(poems, ngram_size):
        key = ''.join(ngram)
        if key not in frequency:
            frequency[key] = 1
        else:
            frequency[key] += 1

    return frequency


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--ngram-size', help='The size of the ngram', type=int, required=True)
    parser.add_argument('-o', '--output-file', help='The output file of ngrams', required=True)
    parser.add_argument('-c', '--csv-poems', help='The poems csv file', required=True)

    args = parser.parse_args()
    freqtable = ngram_frequency(args.csv_poems, args.ngram_size)
    ordered_freq = sorted(freqtable.items(), key=lambda kv: kv[1], reverse=True)

    with io.open(args.output_file, 'w', encoding='utf-8') as ostream:
        wrtr = csv.DictWriter(ostream, fieldnames=['bigram', 'count'], lineterminator='\n', quoting=csv.QUOTE_ALL)
        wrtr.writeheader()
        for ngram, count in ordered_freq:
            wrtr.writerow({'bigram': ngram, 'count': count})


if __name__ == '__main__':
    main()
