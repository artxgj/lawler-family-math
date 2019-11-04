from typing import IO, Iterator
from p3lib.wiktionary import WiktionaryModuleDataPage, WiktionarySpecialPrefixIndex, Namespace


class ZhModuleDataIndex:
    pron_minnan = "nan-pron"

    def __init__(self):
        self._spi = WiktionarySpecialPrefixIndex()

    def list_synonyms(self, ostream: IO[str], stripprefix: bool = True) -> None:
        for syn_mod in self._spi.query('zh/data/dial-syn', Namespace.module, max_pages=50):
            past_rightslash = syn_mod.rfind('/') + 1

            if past_rightslash < len(syn_mod) and ord(syn_mod[past_rightslash]) < 0x80:
                continue    # ignore ascii

            if stripprefix:
                outstr = syn_mod[past_rightslash:]
            else:
                outstr = syn_mod

            ostream.write(f"{outstr}\n")

    def list_pronunciations(self, topolect: str, stripprefix: bool = True):
        prefix = f"zh/data/{topolect}"

        for syn_mod in self._spi.query(prefix, Namespace.module, max_pages=50):
            past_rightslash = syn_mod.rfind('/') + 1

            if stripprefix:
                outstr = syn_mod[past_rightslash:]
            else:
                outstr = syn_mod

            yield outstr


class ZhModuleDataPage:
    prefix_dialectal_syn = "Module:zh/data/dial-syn/"

    def __init__(self):
        self._mdp = WiktionaryModuleDataPage()

    def get_synonym_data(self, word: str):
        page = f"{self.prefix_dialectal_syn}{word}"
        return self._mdp.get_contents(page)



