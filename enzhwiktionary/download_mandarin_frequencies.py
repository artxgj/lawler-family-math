from iohelpers import dictlines_to_csv
from wiktionary import WiktionaryModuleDataPage
from typing import Iterator, List, Tuple, Union
import argparse

_mandarin_freq_pages = ['1-1000',
                        '1001-2000',
                        '2001-3000',
                        '3001-4000',
                        '4001-5000',
                        '5001-6000',
                        '6001-7000',
                        '7001-8000',
                        '8001-9000',
                        '9001-10000']


class ZhMandarinFrequencies:
    fieldnames = ['Rank', 'Traditional', 'Simplified', 'Pinyin', 'Meaning']

    def __init__(self, pages: Union[List, Tuple]):
        self._mdp = WiktionaryModuleDataPage()
        self._pages = pages

    def get_contents(self) -> Iterator[dict]:
        rank = 0
        for page in self._pages:
            fql = self._mdp.get_contents(f"Appendix:Mandarin_Frequency_lists/{page}")
            lines = fql.split('\n')
            for line in lines:
                if line.startswith('|'):
                    rank += 1
                    fields = line.split('|')
                    yield {'Rank': rank, 'Traditional': fields[1],
                           'Simplified': fields[2],
                           'Pinyin': fields[3],
                           'Meaning': fields[4]}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--csv-filepath", help="Mandarin Frequencies csv filepath", required=True)
    args = parser.parse_args()

    mfreq = ZhMandarinFrequencies(_mandarin_freq_pages)
    dictlines_to_csv(args.csv_filepath, ZhMandarinFrequencies.fieldnames, mfreq.get_contents())
