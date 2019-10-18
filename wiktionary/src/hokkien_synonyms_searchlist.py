from minnanwikt import list_minnan_synonyms
import argparse
import csv
import io


def synonyms_searchlist(synonyms: str, searchlist: str):
    with io.open(synonyms, 'r', encoding='utf-8') as csvinput:
        rdr = csv.DictReader(csvinput)
        synset = set()
        for row in rdr:
            phwords = row['Philippines']
            if len(phwords) > 0:
                synset.update(list_minnan_synonyms(phwords))

            xmwords = row['Xiamen']
            if len(xmwords) > 0:
                synset.update(list_minnan_synonyms(xmwords))

            qzwords = row['Quanzhou']
            if len(qzwords) > 0:
                synset.update(list_minnan_synonyms(qzwords))

    with io.open(searchlist, 'w', encoding='utf-8') as wrtr:
        for syn in synset:
            wrtr.write(f"{syn}\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--synonyms-csv", help="hokkien synonyms csv file", required=True)
    parser.add_argument("-w", "--wikt-search-list", help="hokkien wiktionary search list", required=True)
    args = parser.parse_args()
    synonyms_searchlist(args.synonyms_csv, args.wikt_search_list)



