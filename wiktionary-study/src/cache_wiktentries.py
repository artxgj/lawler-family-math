from wiktionary import WicktionaryRevisionEntrySearch
import argparse
import csv
import io

fieldnames = ['word', 'wiktionary_entry']


def extractNcache(words_file, cache_file, errlog):
    with io.open(words_file, 'r', encoding='utf-8') as wf:
        with io.open(cache_file, 'w', encoding='utf-8') as cf:
            with io.open(errlog, 'w', encoding='utf-8') as npf:
                wrtr = csv.DictWriter(cf, fieldnames=fieldnames, lineterminator='\n', quoting=csv.QUOTE_ALL)
                wrtr.writeheader()
                wiktsearch = WicktionaryRevisionEntrySearch()

                for entry in wf:
                    try:
                        word = entry.strip()
                        res = wiktsearch.find(word)
                        print(word)
                        wrtr.writerow({'word': word, 'wiktionary_entry': res.content})
                    except Exception as e:
                        npf.write(f"{word}:{str(e)}\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cache wiktionary entries')
    parser.add_argument("-w", "--words-filepath", help="words to extract from Wiktionary", required=True)
    parser.add_argument("-c", "--cache-filepath", help="cached-results filepath", required=True)
    parser.add_argument("-e", "--errlog", help="error log file", required=True)

    args = parser.parse_args()

    extractNcache(args.words_filepath, args.cache_filepath, args.errlog)

