from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Sequence, Optional, Union
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


@dataclass
class RawTopolectPronunciation:
    info: str
    note: Optional[str] = None


class EnWiktChinesePronunciation(ABC):
    """
    https://en.wiktionary.org/wiki/Template:zh-pron#Empty_template
    """
    pattern_note = re.compile('[a-z]+_note$')

    def __init__(self, wiktentry: str):
        if not isinstance(wiktentry, str):
            raise TypeError('wiktentry has to be a string.')
        self._topolects = {}
        self.parse_topolects(wiktentry)

    @abstractmethod
    def parse_topolects(self, something) -> None:
        """
            The implementation will use its mediawiki parser to parse the pronunciations of each topolect
            and save the parsed topolects and notes to self._topolect_values and self._topolect_notes
        """
        pass

    def topolect(self, 方言: str) -> Optional[Sequence[RawTopolectPronunciation]]:
        try:
            return self._topolects[方言]
        except KeyError as e:
            raise Exception(f"Pronunciation for {方言} is not available." )

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


