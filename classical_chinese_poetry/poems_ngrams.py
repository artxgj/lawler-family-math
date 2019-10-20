import csv
import   argparse
from p3lib.ngrams import ngrams


def poem_ngrams(csv_poems_filepath: str, output_filepath: str, ngram_size: int) -> None:
    with open(csv_poems_filepath, 'r') as csv_in:
        reader = csv.DictReader(csv_in)
        with open(output_filepath, 'w') as outf:
            for row in reader:
                for line in row['poem'].split('+'):
                    for ngram in ngrams(line, ngram_size):
                        out = ''.join(list(ngram))
                        outf.write(f"{out}\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--ngram-size', help='The size of the ngram', type=int, required=True)
    parser.add_argument('-o', '--output-file', help='The output file of ngrams', required=True)
    parser.add_argument('-c', '--csv-poems', help='The poems csv file', required=True)

    args = parser.parse_args()
    poem_ngrams(args.csv_poems, args.output_file, args.ngram_size)


if __name__ == '__main__':
    main()
