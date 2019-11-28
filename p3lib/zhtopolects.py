from enzhwiktionary import RawTopolectPronunciation
from typing import Sequence, Optional
import re

_rcomments = re.compile(r'<!--.+-->')

"""
https://en.wiktionary.org/wiki/Template:zh-pron
"""


class MinnanTopolect:
    """
    https://en.wiktionary.org/wiki/Module:nan-pron

    閩南話
    """
    loc_code = {
        "Xiamen": "x",
        "Xiamen-d": "a",
        "Tong'an": "d",
        "Quanzhou": "q",
        "Jinjiang": "c",
        "Zhangzhou": "z",
        "Taipei": "t",
        "Kaohsiung": "k",
        "Kinmen": "j",
        "Singapore": "s",
        "Penang": "p",
        "Philippines": "f",
    }

    location_list = {
        "ax": "Anxi",
        "ct": "Changtai",
        "hc": "Hsinchu",
        "jj": "Jinjiang",
        "kh": "Kaohsiung",
        "km": "Kinmen",
        "lk": "Lukang",
        "md": "Medan",
        "mg": "Magong",
        "ml": "Mainland",
        "ph": "Philippines",
        "pn": "Penang",
        "qz": "Quanzhou",
        "qzd": "Quanzhou-d",
        "sg": "Singapore",
        "sx": "Sanxia",
        "ta": "Tong'an",
        "tc": "Taichung",
        "tn": "Tainan",
        "tp": "Taipei",
        "tt": "Taitung",
        "wh": "Wanhua",
        "wq": "Wuqi",
        "xm": "Xiamen",
        "xmd": "Xiamen-d",
        "yl": "Yilan",
        "zp": "Zhangpu",
        "zz": "Zhangzhou",
        "tw": "Taiwan",
        "twt": "Taiwan-t",
        "twk": "Taiwan-k",
        "twv": "Taiwan-v",
        "twvt": "Taiwan-vt",
        "twvk": "Taiwan-vk",
        "twd": "Taiwan-d",
        "twdt": "Taiwan-dt",
        "twdk": "Taiwan-dk",
        "twr": "Taiwan-r",
        "twrt": "Taiwan-rt",
        "twrk": "Taiwan-rk",
        "twq": "Taiwan-Q",
        "twz": "Taiwan-Z",
    }

    def __init__(self, topo_pron: Sequence[RawTopolectPronunciation]):
        self._prons = {}
        self._notes = set()
        self._all_keys = {loc for loc in self.location_list.keys()}

        if 'ml' in self._all_keys:
            self._all_keys.remove('ml')

        for topo in topo_pron:
            if len(topo.info) == 0:
                continue

            if topo.note:
                self._notes.add(topo.note)

            dial_prons = self.parse_dialect_pron(topo.info)
            for pron, loc in dial_prons:
                if loc == 'all':
                    for key in self._all_keys:
                        if key in self._prons:
                            self._prons[key].add(pron)
                        else:
                            self._prons[key] = {pron}
                elif loc in self._prons:
                    self._prons[loc].add(pron)
                else:
                    self._prons[loc] = {pron}

    @staticmethod
    def parse_dialect_pron(s: str):
        """

        :param s:
        :return:
        """
        res = set()
        s1 = _rcomments.sub('', s)
        s2 = s1.replace('仔', 'á')
        dial_prons = s2.split('/')
        for dial_pron in dial_prons:
            locs_pron = dial_pron.split(':')

            if len(locs_pron) > 1:
                pron = locs_pron[1].strip()
                locs = locs_pron[0].strip().split(',')
                for loc in locs:
                    if loc == 'ml':
                        res.add((pron, 'xm'))
                        res.add((pron, 'zz'))
                        res.add((pron, 'qz'))
                    else:
                        res.add((pron, loc))
            else:
                res.add((locs_pron[0].strip(), 'all'))

        return res

    def dialect(self, dial: str) -> Optional[Sequence[str]]:
        return self._prons.get(dial, None)

    def notes(self):
        return None if len(self._notes) == 0 else self._notes[0]


class MandarinTopolect:
    """
    普通話
    """
    def __init__(self, topo_pron: Sequence[RawTopolectPronunciation]):
        self._notes = set()

        for topo in topo_pron:
            if len(topo.info) == 0:
                continue

            dial_prons = self.parse_dialect_pron(topo.info)

        self._prons = [x for x in dial_prons]

    def dialect(self, dial: str = None) -> Optional[Sequence[str]]:
        return self._prons if len(self._prons) > 0 else None

    def notes(self):
        return self._notes

    @staticmethod
    def parse_dialect_pron(s: str):
        res = set()
        s1 = _rcomments.sub('', s)
        dial_prons = s1.split(',')
        for dial_pron in dial_prons:
            if dial_pron.find('=') == -1:
                res.add(dial_pron)

        return res


if __name__ == '__main__':
    folder_path = '../data/enwiktionary/zh-words/20191125'
    i = 0
    j = 0
    hokkien_pron = {}

    from iohelpers import filenames_from_folder, lines_from_textfile
    from enzhwiktionary_mwph import MwphEnWiktChinesePronunciation
    import io

    for fname in filenames_from_folder(folder_path):
        s = io.StringIO()
        j += 1
        for line in lines_from_textfile(f'{folder_path}/{fname}'):
            s.write(f"{line}\n")

        try:
            zh_pron = MwphEnWiktChinesePronunciation(s.getvalue())
            m_pron = zh_pron.topolect('m')
            print(fname, m_pron)
            i += 1
        except Exception as e:
            print(f"* * * * *{fname}, {e}")

    print("-----------------------------------------")
    print(f"Number of words with Minnan: {i}")
    print(f"Total number of words in local folder: {j}")
