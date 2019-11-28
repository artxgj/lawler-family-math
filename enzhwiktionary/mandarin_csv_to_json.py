from zhmodules import MandarinPronunciations
from iohelpers import to_json_file

m = MandarinPronunciations.from_frequencies_csv('../data/enwiktionary/module-zh-data-json/mandarin-frequencies-list.csv')
json_dict = {word: pronunciations for word, pronunciations in m.words_pronunciations()}

to_json_file('../data/enwiktionary/module-zh-data-json/mandarin-pron/frequencies.json', json_dict, indent=4)

