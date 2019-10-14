from minnanwikt import MinnanPronunciation
from wiktionary import WicktionaryRevisionEntrySearch
import argparse
import csv
import io


fieldnames = ['word', 'xm', 'qz', 'ph', 'poj', 'note']


def hokkien_poj(words_file, poj_outfile, nopoj_file):
    with io.open(words_file, 'r', encoding='utf-8') as wf:
        with io.open(nopoj_file, 'w', encoding='utf-8') as npf:
            with io.open(poj_outfile, 'w', encoding='utf-8') as pf:
                wrtr = csv.DictWriter(pf, fieldnames=fieldnames, dialect=csv.unix_dialect)
                wrtr.writeheader()
                wiktsearch = WicktionaryRevisionEntrySearch()

                for entry in wf:
                    try:
                        word = entry.strip()
                        res = wiktsearch.find(word.strip())
                        hokkien = MinnanPronunciation(word, res.content)

                        output = {
                            'word': word,
                            'xm': ','.join(hokkien.xiamen),
                            'qz': ','.join(hokkien.quanzhou),
                            'ph': ','.join(hokkien.ph),
                            'poj': ','.join(hokkien.poj),
                            'note': ','.join(hokkien.note),
                        }
                        print(word)
                        wrtr.writerow(output)
                    except Exception as e:
                        npf.write(f"{word}:{str(e)}\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--search-list", help="hokkien wiktionary search list", required=True)
    parser.add_argument("-p", "--poj-csv", help="poj csv output file", required=True)
    parser.add_argument("-e", "--errlog", help="error log file", required=True)
    args = parser.parse_args()

    hokkien_poj(args    .search_list, args.poj_csv, args.errlog)

