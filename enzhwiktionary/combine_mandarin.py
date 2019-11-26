from iohelpers import to_json_file
from zhmodules import ZhTopolectSynonyms, MandarinPronunciations


mandarin_sources = [
    ('../data/enwiktionary/module-zh-data-json/cmn-pron', 'from_local_json_file'),
    ('../data/enwiktionary/module-zh-data-json/wordlist', 'from_local_json_folder'),
    ('../data/enwiktionary/module-zh-data-json/mandarin-frequencies-list.csv', 'from_frequencies_csv'),
]

combine = {}
num_words = 0
for source, method in mandarin_sources:
    mp = getattr(MandarinPronunciations, method)(source)
    for word, prons in mp.words_pronunciations():
        num_words += 1
        if word not in combine:
            combine[word] = prons

to_json_file('../data/enwiktionary/module-zh-data-json/combined-mandarin-pron.json', combine, indent=4)

print(f"Total number of words: {num_words}\nNumber of unique words: {len(combine)}")


