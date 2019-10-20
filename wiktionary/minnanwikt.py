from p3lib.wiktionary import WicktionaryRevisionEntrySearch

import csv
import io

import mwparserfromhell


def list_minnan_synonyms(wikt_minnan_synonyms: str):
    """
    Cases of Minnan synonym-strings
        荷蘭西水:dated
        內公:non-face-to-face
        闊喙婆:humorous
        雪文
        摩托車, 摩托, 摩托駛甲, 噗噗車
        查某, 查某人, 婦人人, 諸娘:dated, 諸娘人:dated
    """
    synlist = []
    words = wikt_minnan_synonyms.split(',')

    for word_note in words:
        wn = word_note.split(':')
        synlist.append(wn[0].strip())

    return synlist


class POJ:
    def __init__(self):
        self._poj = {}

    @classmethod
    def load_file(cls, csvfile):
        poj = cls()

        with io.open(csvfile, 'r', encoding='utf-8') as pojs:
            rdr = csv.DictReader(pojs)
            for row in rdr:
                poj._poj[row['word']] = {
                    'xm': row['xm'],
                    'qz': row['qz'],
                    'poj': row['poj'],
                    'ph': row['ph'],
                    'note': row['note']
                }

        return poj

    def lookup(self, word):
        if word in self._poj:
            return self._poj[word]
        else:
            return None


class MinnanPronunciation:
    def __init__(self, word, wikitext):
        self._wikitext = wikitext
        self._word = word
        self._mandarin = set()
        self._qz = set()
        self._xm = set()
        self._ph = set()
        self._poj = set()
        self._note = set()

        wikicode = mwparserfromhell.parse(wikitext)
        sections = wikicode.get_sections(matches="Chinese")

        if len(sections) == 0:
            raise ValueError("wikicode doesn't have a Chinese section")

        chinese = sections[0]
        prons = chinese.get_sections(matches='Pronunciation')

        for i, pron in enumerate(prons):
            zhpron = pron.filter_templates(matches='zh-pron')
            topolects = zhpron[0].params
            for param in topolects:
                """
                if param.count('=') > 1:
                    # hakka can have something like this: 'h=pfs=kâ;gd=ga1\n'
                    continue
                """

                sep = param.find('=')

                if sep == -1:
                    continue

                k = param[:sep].strip()
                v = param[sep+1:].strip()

                if k == 'm':
                    self._mandarin.add(v)
                elif k == 'mn':
                    self._mn(v)
                elif k == 'mn_note':
                    self._note.add(v)

    def _mn(self, pojs):
        """
        https://en.wiktionary.org/wiki/Template:zh-pron

        |mn=ke/ka
        |mn=xm,zz,ta,kh,tp,tn,yl,lk,sx,hc,pn:ka/qz,jj,ph:kāi/zz,kh,tc:ka/km,mg:kai

        |mn=xm,qz,lk:kha/zz,tp,kh,tn,sx,yl,hc,tc:khia/xm,zz,twv:khia

        |mn=koàn
        |mn=qz,twv,xm,zz:koàn/tw:koan

        """
        for poj in pojs.split('/'):
            geo_sounds = poj.split(':')
            if len(geo_sounds) == 1:
                self._poj.add(geo_sounds[0])
            else:
                sound = geo_sounds[1]
                geos = set(geo_sounds[0].split(','))

                if 'xm' in geos:
                    self._xm.add(sound)

                if 'qz' in geos:
                    self._qz.add(sound)

                if 'ph' in geos:
                    self._ph.add(sound)

                if 'ml' in geos:
                    self._poj.add(sound)

    @property
    def word(self):
        return self._word

    @property
    def poj(self):
        return self._poj

    @property
    def xiamen(self):
        return self._xm

    @property
    def quanzhou(self):
        return self._qz

    @property
    def ph(self):
        return self._ph

    @property
    def note(self):
        return self._note

    @property
    def mandarin(self):
        return self._mandarin


if __name__ == '__main__':

    wiktsearch = WicktionaryRevisionEntrySearch()
    words = ['馬擎仔',  '一起', '易', '家', '霍亂', '乞食']

    for word in words:
        wiktentry = wiktsearch.find(word)
        mn = MinnanPronunciation(word, wiktentry.content)
        print(word)
        print(f"m: {mn.mandarin}")
        print(f"xm: {mn.xiamen}")
        print(f"qz: {mn.quanzhou}")
        print(f"ph: {mn.ph}")
        print(f"poj: {mn.poj}")
        print(f"note: {mn.note}")
        print("===\n")

        print(wiktentry.content)

