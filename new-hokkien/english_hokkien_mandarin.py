from datetime import datetime
from iohelpers import lines_to_csv
from typing import Sequence
from zhmodules import ZhTopolectSynonyms, MandarinPronunciations, ZhTopolectPronunciations
from ph_hokkien import PhHokkien, mn_ph, mn_jj, mn_qz, mn_xm


class EnglishHokkienMandarin:
    def __init__(self, synonyms: ZhTopolectSynonyms, hokkien_pron: ZhTopolectPronunciations, mp: MandarinPronunciations):
        self._ehm = []
        ehm = []
        for mandarin, syndata in synonyms.all_words():
            english = syndata['meaning']
            if len(english) == 0:
                continue

            res = {}
            for locale in PhHokkien.syn_locales():
                try:
                    if len(syndata[locale]) > 0:
                        res[locale] = syndata[locale]

                except KeyError as err:
                    pass

            if len(res) > 0:
                if mn_ph in res:
                    hpron = self.hokkien_words_pron(res[mn_ph], hokkien_pron)
                else:
                    hpron = self.hokkien_words_pron(self.qz_xm(res), hokkien_pron)

                mpron = self.mandarin_word_pron(mandarin, mp)

                ehm.append([english, hpron, mpron])
                ehm.sort(key=lambda x: x[0].lower())

                self._ehm = ehm

    def mandarin_word_pron(self, mandarin, m_pron:MandarinPronunciations):
        pron = m_pron.pronunciation(mandarin)

        if pron is None:
            return f"{mandarin}"
        else:
            return f"{mandarin} [{pron}]"

    def hokkien_words_pron(self, hokkien_words, mn_pron: ZhTopolectPronunciations):
        res = []

        for word in hokkien_words:
            word_note = word.split(':')
            pron = mn_pron.pronunciation(word_note[0])

            if pron is None:
                display_pron = ''
            else:
                display_pron = f"[{pron}]"

            res.append(f'{":".join(word_note)} {display_pron}')

        return '\n'.join(res)

    def qz_xm(self, syndata):
        precedence = {}
        for locale in [mn_jj, mn_qz, mn_xm]:
            if locale in syndata:
                for word in syndata[locale]:
                    if word not in precedence:
                        precedence[word] = PhHokkien.synonym_weight(locale)
                    else:
                        precedence[word] += PhHokkien.synonym_weight(locale)

        if len(precedence) == 0:
            return []
        else:
            precedence_syns = sorted([(v, k) for k, v in precedence.items()], reverse=True)
            ordered_syns = [syn for count, syn in precedence_syns]
            return ordered_syns

    def items(self):
        for item in self._ehm:
            yield item


if __name__ == '__main__':
    synonyms = ZhTopolectSynonyms.from_local_folder('../data/enwiktionary/module-zh-data-json/dial-syn')

    mp = MandarinPronunciations.from_local_json_file('../data/enwiktionary/module-zh-data-json/combined-mandarin-pron.json')
    h = ZhTopolectPronunciations.from_local_json_folder('../data/enwiktionary/module-zh-data-json/nan-pron')

    ehm = EnglishHokkienMandarin(synonyms, h, mp)
    lines_to_csv('../data/tmp/english-hokkien-mandarin.csv', ehm.items())
