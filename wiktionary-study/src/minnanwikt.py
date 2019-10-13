from wiktionary import WicktionaryRevisionEntrySearch
import mwparserfromhell


class MinnanPronunciation:
    def __init__(self, word, wikitext):
        self._wikitext = wikitext
        wikicode = mwparserfromhell.parse(wikitext)
        sections = wikicode.get_sections(matches="Chinese")

        if len(sections) == 0:
            raise ValueError("wikicode doesn't have a Chinese section")

        chinese = sections[0]
        prons = chinese.get_sections(matches='Pronunciation')

        self._mandarin = set()
        self._qz = set()
        self._xm = set()
        self._ph = set()
        self._poj = set()
        self._vernacular = None
        self._literary = None

        for i, pron in enumerate(prons):
            zhpron = pron.filter_templates(matches='zh-pron')
            topolects = zhpron[0].params

            for param in topolects:
                if param.count('=') > 1:
                    # hakka can have something like this: 'h=pfs=kâ;gd=ga1\n'
                    continue

                k, v = param.split('=')
                k = k.strip()
                v = v.strip()

                if k == 'm':
                    self._mandarin.add(v)
                elif k == 'mn':
                    self._mn(v)
                elif k == 'mn_note':
                    self._vernacular, self._literary = self._mn_note(v)

    def _mn(self, pojs):
        """
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

        self._poj = self.xiamen & self.quanzhou

    def _mn_note(self, notes):
        """
        Process |mn_note=ke - vernacular; ka - literary

        :param notes:
        :return:
        """

        notedict = {}
        for note in notes.split(';'):
            poj, pojtype = note.split('-')
            notedict[pojtype.strip()] = poj.strip()

        return notedict['vernacular'], notedict['literary']

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
    def vernacular(self):
        return self._vernacular

    @property
    def literary(self):
        return self._literary

    @property
    def mandarin(self):
        return self._mandarin


if __name__ == '__main__':

    wikt_title = WicktionaryRevisionEntrySearch()
    bahay = wikt_title.find('家')

    mn = MinnanPronunciation('家', bahay.content)
    print(mn.xiamen)
    print(mn.vernacular)
    print(mn.literary)
    print(mn.quanzhou)
    print(mn.mandarin)
    print(mn.ph)
    print(mn.poj)
