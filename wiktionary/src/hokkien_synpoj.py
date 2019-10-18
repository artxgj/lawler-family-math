from meltingpot import LocaleRank, hokkien_word_weights, poj_weights
from minnanwikt import POJ, list_minnan_synonyms
import argparse
import csv
import io


def hokkien_synonyms_poj(syncsv, pojcsv, outcsv):
    poj = POJ.load_file(pojcsv)
    synbanlam = LocaleRank(hokkien_word_weights)
    pojbanlam = LocaleRank(poj_weights)

    fieldnames = ['Mandarin', 'meaning', 'Hokkien_synonyms']
    with io.open(outcsv, 'w', encoding='utf-8') as csv_out:
        wrtr = csv.DictWriter(csv_out, fieldnames=fieldnames,
                              dialect=csv.unix_dialect, quoting=csv.QUOTE_ALL)
        wrtr.writeheader()
        with io.open(syncsv, 'r', encoding='utf-8') as synonyms:
            rdr = csv.DictReader(synonyms)

            for row in rdr:
                ph = ','.join(list_minnan_synonyms(row['Philippines']))
                qz = ','.join(list_minnan_synonyms(row['Quanzhou']))
                xm = ','.join(list_minnan_synonyms(row['Xiamen']))
                ranked_hokkien_words = synbanlam.rank(ph=ph, xm=xm, qz=qz)

                hokkien_synonyms = []

                for word in ranked_hokkien_words:
                    wordpoj = poj.lookup(word)

                    if wordpoj is not None:
                        ranked_pojs = pojbanlam.rank(ph=wordpoj['ph'],
                                                     ml=wordpoj['poj'],
                                                     xm=wordpoj['xm'],
                                                     qz=wordpoj['qz'])

                        pronunciations = f"({','.join(ranked_pojs)})"

                        if len(wordpoj['note']) > 0:
                            notabene = wordpoj['note'].strip(' \n')
                            if len(notabene) > 0:
                                pronunciations = f'{pronunciations}\t[Note] {notabene}'
                    else:
                        pronunciations = ''

                    synonym = f'{word} {pronunciations}'
                    hokkien_synonyms.append(synonym)

                wrtr.writerow({'Mandarin':row['Mandarin'],
                               'meaning': row['meaning'],
                               'Hokkien_synonyms': "\n".join(hokkien_synonyms)})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--syn-csv", help="hokkien synonyms csv", required=True)
    parser.add_argument("-p", "--poj-csv", help="poj csv output file", required=True)
    parser.add_argument("-c", "--combined-csv", help="combined output file", required=True)
    args = parser.parse_args()
    hokkien_synonyms_poj(args.syn_csv, args.poj_csv, args.combined_csv)


