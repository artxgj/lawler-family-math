from meltingpot import LocaleRank, hokkien_word_weights
from minnanwikt import POJ, list_minnan_synonyms
from cjkwicktionary import PojPinyin
import argparse
import csv
import io


def banlam_synonyms_pojs(syncsv, pronfilepath, outcsv):
    dictionary = PojPinyin.loadfile(pronfilepath)

    synbanlam = LocaleRank(hokkien_word_weights)

    fieldnames = ['Mandarin', 'pinyin', 'meaning', 'Hokkien_synonyms']
    with io.open(outcsv, 'w', encoding='utf-8') as csv_out:
        wrtr = csv.DictWriter(csv_out, fieldnames=fieldnames,
                              lineterminator='\n', quoting=csv.QUOTE_ALL)
        wrtr.writeheader()
        with io.open(syncsv, 'r', encoding='utf-8') as synonyms:
            rdr = csv.DictReader(synonyms)
            for row in rdr:
                mandarin = row['Mandarin']

                ph = ','.join(list_minnan_synonyms(row['Philippines']))
                qz = ','.join(list_minnan_synonyms(row['Quanzhou']))
                xm = ','.join(list_minnan_synonyms(row['Xiamen']))
                ranked_hokkien_words = synbanlam.rank(ph=ph, xm=xm, qz=qz)

                hokkien_synonyms = []
                for word in ranked_hokkien_words:
                    romanized = dictionary.lookup(word)

                    if romanized is not None and romanized.poj:
                        poj = f"({','.join(romanized.poj)})"

                        if romanized.notespoj and len(romanized.notespoj) > 0:
                            pronunciations = f"{poj}\nNote(s): {''.join(romanized.notespoj)}\n"
                        else:
                            pronunciations = poj
                    else:
                        pronunciations = ''

                    synonym = f'{word} {pronunciations}'
                    hokkien_synonyms.append(synonym)

                roman = dictionary.lookup(mandarin)

                wrtr.writerow({'Mandarin': mandarin,
                               'pinyin': ','.join(roman.pinyin) if roman and roman.pinyin else '',
                               'meaning': row['meaning'],
                               'Hokkien_synonyms': "\n".join(hokkien_synonyms)})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--syn-csv", help="hokkien synonyms csv", required=True)
    parser.add_argument("-p", "--pronunciations-json", help="pronunciatons json file", required=True)
    parser.add_argument("-c", "--combined-csv", help="combined output file", required=True)
    args = parser.parse_args()
    banlam_synonyms_pojs(args.syn_csv, args.pronunciations_json, args.combined_csv)

    """
    banlam_synonyms_pojs('../data/minnan-synonyms.csv',
                         '../data/chinese-words-pronunciation.20191017.json',
                         '../data/kjcrush.csv')
    """




