import json
import io
import csv

kmeaning = 'meaning'
knote = 'note'
kphilippines = 'Philippine-MN'
kquanzhou = "Quanzhou"
kxiamen = "Xiamen"


def find_minnan_synonyms(infile, outfile):
    with open(infile, "r") as json_file:
        data = json.load(json_file)
        with io.open(outfile, "w", encoding='utf-8') as csvfile:
            fieldnames = ['Mandarin', 'Philippines', 'Xiamen', 'Quanzhou', 'meaning', 'note']
            dictwrtr = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect=csv.unix_dialect)
            dictwrtr.writeheader()

            for word, synonyms in data.items():
                if kmeaning in synonyms:
                    meaning = synonyms[kmeaning]
                else:
                    meaning = ''

                if knote in synonyms:
                    note = synonyms[knote]
                else:
                    note = ''

                if kphilippines in synonyms:
                    pinas = synonyms[kphilippines]
                else:
                    pinas = ''

                if kxiamen in synonyms:
                    xiamen = synonyms[kxiamen]
                else:
                    xiamen = ''


                if kquanzhou in synonyms:
                    quanzhou = synonyms[kquanzhou]
                else:
                    quanzhou = ''

                if (len(pinas) > 0 and pinas != word) or \
                        (len(xiamen) > 0 and xiamen != word) or \
                        (len(quanzhou) > 0 and quanzhou != word):
                    dictwrtr.writerow({'Mandarin': word,
                                       'Philippines': pinas,
                                       'Xiamen': xiamen,
                                       'Quanzhou': quanzhou,
                                       'meaning': meaning,
                                       'note': note})


if __name__ == '__main__':
    find_minnan_synonyms('../data/wikt-dial-syns.json', '../data/minnan-synonyms.csv')
