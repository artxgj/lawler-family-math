from datetime import datetime
from iohelpers import lines_to_textfile
from typing import Iterator, List, Sequence
from zhmodules import ZhTopolectSynonyms, MandarinPronunciations, ZhTopolectPronunciations


def missing_philippine_hokkien_words_generator(synonyms: ZhTopolectSynonyms, hokprons: ZhTopolectPronunciations):
    all_hokkien = set()
    for word, syn_data in synonyms.all_words():
        minnan = set(syn_data['Philippine-MN'])
        minnan.update(syn_data['Quanzhou'])
        minnan.update(syn_data['Xiamen'])

        for hokkien in minnan:
            banlamoe = hokkien.split(':')
            all_hokkien.add(banlamoe[0])

    return words_missing_prons(all_hokkien, hokprons)


def words_missing_prons(corpus: Sequence[str], prons: ZhTopolectPronunciations):
    return [word for word in corpus if prons.pronunciation(word) is None and all(ord(char) > 255 for char in word)]


if __name__ == '__main__':
    synonyms = ZhTopolectSynonyms.from_local_folder('../data/enwiktionary/module-zh-data-json/dial-syn')

    mp = MandarinPronunciations.from_local_json_file('../data/enwiktionary/module-zh-data-json/combined-mandarin-pron.json')
    missing_mandarin_prons = iter(words_missing_prons(synonyms.mandarin_words(), mp))
    h = ZhTopolectPronunciations.from_local_json_folder('../data/enwiktionary/module-zh-data-json/nan-pron')
    missing_hokkien_prons = iter(missing_philippine_hokkien_words_generator(synonyms, h))

    today = datetime.today().strftime("%Y%m%d")
    lines_to_textfile(f'../data/enwiktionary/words-search/missing-hokkien.{today}.txt', missing_hokkien_prons)
    lines_to_textfile(f'../data/enwiktionary/words-search/missing-mandarin.{today}.txt', missing_mandarin_prons)
