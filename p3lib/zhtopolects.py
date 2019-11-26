from enzhwiktionary import RawTopolectPronunciation
from typing import Sequence


class Minnan:
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
        self._notes = []
        for topo in topo_pron:
            if topo.note:
                self._notes.append(topo.note)

            for dialects in topo.info.split('/'):
                dials_pron = dialects.split(':')

                if dials_pron[0].find(','):
                    dialects = dials_pron[0].split(',')

                if len(dialects) == 1:
                    self._prons['xm'] = dialects[0]
                    self._prons['qz'] = dialects[0]
                    self._prons['zz'] = dialects[0]
                else:
                    pron = dials_pron[1]
                    for dial in dialects:
                        if dial == 'ml':
                            self._prons['xm'] = pron
                            self._prons['qz'] = pron
                            self._prons['zz'] = pron
                        else:
                            self._prons[dial] = pron

            print(self._prons, self._notes)

    def dialect(self, dial: str) -> Sequence[str]:
        return self._prons.get(dial, None)

    def notes(self):
        return None if len(self._notes) == 0 else self._notes[0]


class Mandarin:
    """
    普通話
    """
    def __init__(self, topo_pron: Sequence[RawTopolectPronunciation]):

        pass

    def dialect(self, dial: str) -> Sequence[str]:
        pass

    def notes(self):
        pass


if __name__ == '__main__':
    tests = [
        [RawTopolectPronunciation(info='chúi/súi', note='chúi - vernacular; súi - literary')],
        [RawTopolectPronunciation(info='qz:lia̍k-sír/tw,xm,zz:le̍k-sú/jj,ph:lia̍k-sí', note=None)],
        [RawTopolectPronunciation(info='lîm', note=None)],
        [RawTopolectPronunciation(info='qz:ian-pit-soān', note=None)]
    ]

    for test in tests:
        mn = Minnan(test)
