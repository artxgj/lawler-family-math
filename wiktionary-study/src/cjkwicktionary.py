import mwparserfromhell
from typing import List


class WiktEntryCJKV:
    def __init__(self):
        self._parser = mwparserfromhell

    def _language_section(self, wiktentrytext: str, language:str) -> str:
        wikicode = self._parser.parse(wiktentrytext)
        section = wikicode.get_sections(matches=language)

        if len(section) == 0:
            raise ValueError(f"Wiktionary entry does not have a {language} section.")

        return str(section[0])

    @staticmethod
    def chinese(self, wiktentrytext: str) -> str:
        return self._language_section(wiktentrytext, 'Chinese')

    def japanese(self, wiktentrytext: str) -> str:
        return self._language_section(wiktentrytext, 'Japanese')

    def korean(self, wiktentrytext: str) -> str:
        return self._language_section(wiktentrytext, 'Korean')

    def vietnamese(self, wiktentrytext: str) -> str:
        return self._language_section(wiktentrytext, 'Vietnamese')


class iWiktZhTopolectPronunciation:
    # This is not pythonic, but this serves as Interface
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
        :param wiktentry:
        :return:
        """

        if not isinstance(wiktentry, str):
            raise TypeError('wiktentry has to be a string.')

        wikicode = mwparserfromhell.parse(wiktentry)
        zhprons = wikicode.filter_templates(matches='zh-pron')

        if len(zhprons) == 0:
            raise ValueError('WiktEntry is not a Chinese word entry')

        notes = []
        pojs = {}
        for zhpron in zhprons:
            if zhpron.has('mn'):
                pojranks = self._ranked_pojs(zhpron.get('mn').value)

                for k in pojranks.keys():
                    if k not in pojs:
                        pojs[k] = pojranks[k]
                    else:
                        pojs[k] += pojranks[k]

            if zhpron.has('mn_note'):
                notes.append(zhpron.get('mn_note').value)

        ord_pojs = sorted(pojs, key=pojs.get, reverse=True)

        if include_note:
            ord_pojs.extend(notes)

        return ord_pojs


class WiktMandarinPronunciation(iWiktZhTopolectPronunciation):
    def pronunciation(self):
        pass


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
