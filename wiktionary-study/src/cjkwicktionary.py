from typing import List
from collections import namedtuple

import io
import json
import mwparserfromhell


class WiktEntryCJKV:
    def __init__(self):
        self._parser = mwparserfromhell

    def _language_section(self, wiktentrytext: str, language: str) -> str:
        wikicode = self._parser.parse(wiktentrytext)
        section = wikicode.get_sections(matches=language)

        if len(section) == 0:
            raise ValueError(f"Wiktionary entry does not have a {language} section.")

        return str(section[0])

    def chinese(self, wiktentrytext: str) -> str:
        return self._language_section(wiktentrytext, 'Chinese')

    def japanese(self, wiktentrytext: str) -> str:
        return self._language_section(wiktentrytext, 'Japanese')

    def korean(self, wiktentrytext: str) -> str:
        return self._language_section(wiktentrytext, 'Korean')

    def vietnamese(self, wiktentrytext: str) -> str:
        return self._language_section(wiktentrytext, 'Vietnamese')


class iWiktZhTopolectPronunciation:
    # This is not pythonic but it serves as my Java-like Interface
    @property
    def pronunciation(self):
        NotImplemented


class WiktMinnanPronunciation(iWiktZhTopolectPronunciation):
    _default_weights = {
        'ph': 5,
        'ml': 4,
        'qz': 3,
        'xm': 2,
        'zz': 1
    }

    def __init__(self, dialect_weights=None):
        self._dialect_weights = dialect_weights or self._default_weights
        self._heavyweight = max(self._dialect_weights.values()) + 1

    def _ranked_pojs(self, mn_prons):
        """
        https://en.wiktionary.org/wiki/Template:zh-pron

        Real examples:
        |mn=ke/ka
        |mn=xm,zz,ta,kh,tp,tn,yl,lk,sx,hc,pn:ka/qz,jj,ph:kāi/zz,kh,tc:ka/km,mg:kai

        |mn=xm,qz,lk:kha/zz,tp,kh,tn,sx,yl,hc,tc:khia/xm,zz,twv:khia

        |mn=koàn
        |mn=qz,twv,xm,zz:koàn/tw:koan

        """

        pojs = {}

        for mn_pron in mn_prons.split('/'):
            dialect_poj = mn_pron.split(':')

            if len(dialect_poj) == 1:
                poj = dialect_poj[0].strip(' \n')

                if poj not in pojs:
                    pojs[poj] = self._heavyweight
                else:
                    pojs[poj] += self._heavyweight
            else:
                poj = dialect_poj[1].strip(' \n')

                if poj not in pojs:
                    pojs[poj] = 0

                dialects = dialect_poj[0].split(',')

                for dialect in dialects:
                    variant = dialect.strip(' \n')
                    if variant in self._dialect_weights:
                        pojs[poj] += self._dialect_weights[variant]

        return pojs

    def pronunciation(self, wiktentry: str, include_note: bool=True) -> List[str]:
        """
        Returns an ordered list of strings

        https://en.wiktionary.org/wiki/Template:zh-pron/documentation

        mn=x/y/z
        Min Nan (Hokkien) POJ (with the addition of the Quanzhou and Zhangzhou dialect vowels ee, er, and ir and use of a caron for tone mark 6 and a double acute accent for tone mark 9, adopted from Tâi-lô)
        # can be used to disable tone sandhi between syllables.
        Labels followed by a colon can be placed before a pronunciation to specify information about the pronunciation. Multiple abbreviations are separated with commas ,.
        Label	Information
        xm	Xiamen
        qz	Quanzhou
        zz	Zhangzhou
        kh	Kaohsiung
        tp	Taipei
        tn	Tainan
        tc	Taichung
        hc	Hsinchu
        yl	Yilan
        lk	Lukang
        sx	Sanxia
        km	Kinmen
        mg	Magong
        sg	Singapore
        pn	Penang
        ph	Philippines
        xmd	dated in Xiamen
        qzd	dated in Quanzhou
        ml	Mainland China (Xiamen, Quanzhou, Zhangzhou)
        tw	mainstream Taiwan
        twk	mainstream Taiwan (Kaohsiung)
        twt	mainstream Taiwan (Taipei)
        twv, twd, twr	variant/dated/rare in Taiwan
        twvk, twdk, twrk	variant/dated/rare in Taiwan (Kaohsiung)
        twvt, twdt, twrt	variant/dated/rare in Taiwan (Taipei)

        """

        if not isinstance(wiktentry, str):
            raise TypeError('Wiktentry has to be a string.')

        wikicode = mwparserfromhell.parse(wiktentry)
        zhprons = wikicode.filter_templates(matches='zh-pron')

        if len(zhprons) == 0:
            raise ValueError('WiktEntry does not have a Chinese pronunciation template.')

        notes = set()
        pojs = {}

        for zhpron in zhprons:
            if zhpron.has('mn'):
                pojranks = self._ranked_pojs(zhpron.get('mn').value)

                for key in pojranks.keys():
                    k = key.strip(' \n')
                    if k not in pojs:
                        pojs[k] = pojranks[k]
                    else:
                        pojs[k] += pojranks[k]

            if zhpron.has('mn_note'):
                notes.add(str(zhpron.get('mn_note').value).strip(' \n'))

        ord_pojs = sorted(pojs, key=pojs.get, reverse=True)

        if include_note:
            return ord_pojs, list(notes)

        return ord_pojs, None


class WiktMandarinPronunciation(iWiktZhTopolectPronunciation):
    def pronunciation(self, wiktentry):
        """
        https://en.wiktionary.org/wiki/Template:zh-pron/documentation

        m=x,y,z,A=a,B=b,C=c
        Mandarin Pinyin. To show tone sandhi for 一 and 不, use 一 or 不 instead of pinyin. Chinese characters are used
        instead of pinyin for characters that have different pronunciations due to regional variation, e.g. 危, 血. #
        can be used to block sequential tone 3 + 3 sandhis (e.g. in 紙老虎, 一把好手).

        Additional "parameters" (A, B, C, etc.) for |m=:

        |xn=	replace label for the xth pronunciation
        |xna=, |xnb=, |xnc=, |xnd=	replace the first/second/third/fourth part of the label for the xth pronunciation (see 娶 for an example)
        |xpy=	change the displayed pinyin for the xth pronunciation (x is omitted for the first pronunciation)
        |xcap=y	capitalize pinyin for the xth pronunciation (x is omitted for the first pronunciation)
        |xtl=y	toneless variant on the last syllable for the xth pronunciation (x is omitted for the first pronunciation)
        |xtl2=y, |xtl3=y	toneless variant on the second/third last syllable for the xth pronunciation (x is omitted for the first pronunciation)
        |xa=y, |xaudio=y	pronunciation file for the xth pronunciation (x is omitted for the first pronunciation)
        |xer=	syllable(s) (separated by ;) to have erhua for the xth pronunciation (if equals y, erhua on last syllable)
        |xertl=y	erhua and toneless variant on the last syllable for the xth pronunciation
        |xertl2=y, |xertl3=y	erhua and toneless variant on the second/third last syllable for the xth pronunciation
        |xera=y, |xeraudio=y	pronunciation file for the xth erhua pronunciation


        """
        if not isinstance(wiktentry, str):
            raise TypeError('Wiktentry has to be a string.')

        wikicode = mwparserfromhell.parse(wiktentry)
        zhprons = wikicode.filter_templates(matches='zh-pron')

        if len(zhprons) == 0:
            raise ValueError('WiktEntry does not have a Chinese pronunciation template.')

        pinyins = {}

        for zhpron in zhprons:
            if zhpron.has('m'):
                mandarin = zhpron.get('m').value.split(',')

                i = 0
                while i < len(mandarin):
                    if mandarin[i].find('=') > -1:
                        break
                    pinyins[mandarin[i].strip(' \n')] = None
                    i += 1

        return list(pinyins.keys())


ChineseRomanization = namedtuple('ChineseRomanization', ['pinyin', 'poj', 'notespoj'])


class PojPinyin:
    def __init__(self):
        self._pojpinyin = None

    @classmethod
    def loadfile(cls, jsonfilepath):
        dictionary = cls()

        with io.open(jsonfilepath, 'r', encoding='utf-8') as jsf:
            dictionary._pojpinyin = json.load(jsf)

        return dictionary

    def lookup(self, 詞):
        try:
            pron = self._pojpinyin[詞]

            if pron is not None:
                return ChineseRomanization(pron['mandarin'],
                                           pron['minnan']['pojs'],
                                           pron['minnan']['notes'])
            else:
                return None

        except KeyError as e:
            return None


if __name__ == '__main__':
    hokkien = WiktMinnanPronunciation()

    entry = """{{zh-pron
|mn=xm,qz,lk:kha/zz,tp,kh,tn,sx,yl,hc,tc:khia/xm,zz,twv:khia
|mn-t=kia1
|dial=n
|cat=n
}}
    """
    print(hokkien.pronunciation(entry))
