import argparse
import csv
import io


def hokkien_synonyms(cellwords: str):
    """
    Cases of Hokkien synonym-strings
        荷蘭西水:dated
        內公:non-face-to-face
        闊喙婆:humorous
        雪文
        摩托車, 摩托, 摩托駛甲, 噗噗車
        查某, 查某人, 婦人人, 諸娘:dated, 諸娘人:dated
    """
    synlist = []
    words = cellwords.split(',')
    for word_note in words:
        wn = word_note.split(':')
        synlist.append(wn[0].strip())

    return synlist


def synonyms_searchlist(synonyms: str, searchlist: str):
    with io.open(synonyms, 'r', encoding='utf-8') as csvinput:
        rdr = csv.DictReader(csvinput)
        synset = set()
        for row in rdr:
            phwords = row['Philippines']
            if len(phwords) > 0:
                synset.update(hokkien_synonyms(phwords))

            xmwords = row['Xiamen']
            if len(xmwords) > 0:
                synset.update(hokkien_synonyms(xmwords))

            qzwords = row['Quanzhou']
            if len(qzwords) > 0:
                synset.update(hokkien_synonyms(qzwords))

    with io.open(searchlist, 'w', encoding='utf-8') as wrtr:
        for syn in synset:
            wrtr.write(f"{syn}\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--synonyms-csv", help="hokkien synonyms csv file", required=True)
    parser.add_argument("-w", "--wikt-search-list", help="hokkien wiktionary search list", required=True)
    args = parser.parse_args()
    synonyms_searchlist(args.synonyms_csv, args.wikt_search_list)



