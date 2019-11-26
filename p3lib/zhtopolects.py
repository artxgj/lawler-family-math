from enzhwiktionary import RawTopolectPronunciation
from typing import Sequence


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

        for topo in topo_pron:
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
        res = set()
        dial_prons = s.split('/')
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

    def dialect(self, dial: str) -> Sequence[str]:
        return self._prons.get(dial, None)

    def notes(self):
        return None if len(self._notes) == 0 else self._notes[0]


class MandarinTopolect:
    """
    普通話
    """
    def __init__(self, topo_pron: Sequence[RawTopolectPronunciation]):

        pass

    def dialect(self, dial: str) -> Sequence[str]:
        pass

    def notes(self):
        pass

