from abc import ABC, abstractmethod
from typing import Sequence, Any, Optional
import re

"""
https://en.wiktionary.org/wiki/Template:zh-pron
"""
langname: {
    "cdo": "Min Dong",
    "cmn": "Mandarin",
    "cjy": "Jin",
    "dng": "Dungan",
    "gan": "Gan",
    "hak": "Hakka",
    "hsn": "Xiang",
    "mnp": "Min Bei",
    "nan": "Min Nan",
    "wuu": "Wu",
    "yue": "Cantonese",
}

langname_abbr: {
    "m": "Mandarin",
    "m-s": "Sichuanese",
    "dg": "Dungan",
    "c": "Cantonese",
    "c-t": "Taishanese",
    "g": "Gan",
    "h": "Hakka",
    "j": "Jin",
    "mb": "Min Bei",
    "md": "Min Dong",
    "mn": "Min Nan",
    "mn-t": "Teochew",
    "w": "Wu",
    "x": "Xiang",
}


_SupportedTopolects = {"m", "m-s", "c", "c-t", "g", "h", "j",
                       "mb", "md", "mn", "mn-t", "w", "x"}


class TopolectPronunciation(ABC):
    @abstractmethod
    def dialect(self, dial: str = None) -> Sequence[str]:
        pass

    @abstractmethod
    def notes(self):
        pass


class IEnWiktChinesePronunciation(ABC):
    """
    https://en.wiktionary.org/wiki/Template:zh-pron#Empty_template
    """
    pattern_note = re.compile('[a-z]+_note$')

    @abstractmethod
    def topolect(self, 方言: str) -> TopolectPronunciation:
        pass

    @classmethod
    def is_note(cls, lang_note) -> bool:
        return cls.pattern_note.match(lang_note) is not None

    @classmethod
    def is_supported(cls, topolect: str) -> bool:
        return topolect in _SupportedTopolects

    @classmethod
    def note_owner(cls, x_note: str) -> Optional[str]:
        sep = x_note.find('_')

        if sep > -1:
            return x_note[:sep]
        else:
            return None


class Minnan(TopolectPronunciation):
    """
    https://en.wiktionary.org/wiki/Module:nan-pron

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

    def __init__(self, pojs: Sequence[str], notes: Sequence[str] = None):
        super().__init__(pojs, notes)

    def dialect(self, dial: str) -> Sequence[str]:
        pass

    def notes(self):
        pass


class Mandarin(TopolectPronunciation):
    def __init__(self, pron: Sequence[str], notes: Sequence[str] = None):
        pass

    def dialect(self, dial: str) -> Sequence[str]:
        pass

    def notes(self):
        pass

