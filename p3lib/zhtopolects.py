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
        pass

    def dialect(self, dial: str) -> Sequence[str]:
        pass

    def notes(self):
        pass


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

