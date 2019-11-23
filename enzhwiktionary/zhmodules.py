from typing import Generator, Tuple, Optional, Dict
from p3lib.wiktionary import WiktionaryModuleDataPage, WiktionarySpecialPrefixIndex, Namespace
from io import StringIO
from luaparser import ast, astnodes
from abc import ABC, abstractmethod
from iohelpers import filenames_from_folder, local_json_resource, dictlines_from_csv


class ZhModuleDataIndex(ABC):
    def __init__(self, modulepage, maxpages):
        self._maxpages = maxpages
        self._modulepagepath = f"zh/data/{modulepage}"
        self._modulepage = modulepage
        self._spi = WiktionarySpecialPrefixIndex()

    def _remove_prefix(self, subpage):
        lastrightslash= subpage.rfind('/')
        return subpage[lastrightslash+1:]

    def get_contents(self, stripprefix: bool = True):
        index_pages = self._spi.query(self._modulepagepath, Namespace.module, max_pages=self._maxpages)

        if stripprefix:
            index_pages = map(self._remove_prefix, index_pages)

        return filter(self.filter_predicate, index_pages)

    @abstractmethod
    def filter_predicate(self, sub_page_names):
        pass


class BaiyueIndex(ZhModuleDataIndex):
    """
        https://en.wikipedia.org/wiki/Baiyue

        This class is used for extracting the items of en.wiktionary.org's index pages for nan-pron (Minnan 閩南發音),
        hak-pron (Hakka 客家發音) and yue-word (Cantonese 廣東發音)
    """
    _doc = 'documentation'
    _list = 'list'

    def __init__(self, modulepage, maxpages=1):
        super().__init__(modulepage, maxpages)

    def filter_predicate(self, sub_page_name):
        return sub_page_name[-len(self._modulepage):] != self._modulepage and \
               sub_page_name[-len(self._doc):] != self._doc and \
               sub_page_name[-len(self._list):] != self._list


class DialectalSynonymsIndex(ZhModuleDataIndex):
    _template = 'template'
    _doc = 'documentation'

    def __init__(self, modulepage='dial-syn'):
        super().__init__(modulepage, maxpages=10)

    def filter_predicate(self, sub_page_name):
        return sub_page_name[-len(self._modulepage):] != self._modulepage and \
                    sub_page_name[-len(self._doc):] != self._doc and \
                    sub_page_name[-len(self._template):] != self._template


class ZhModuleDataResource:
    def get_synonym_data(self, word: str) -> str:
        pass


class ZhModuleDataPage:
    Module_name = "Module:zh/data"

    def __init__(self):
        self._mdp = WiktionaryModuleDataPage()

    def dialectal_synonyms(self, word: str) -> str:
        return self._mdp.get_contents(f"{self.Module_name}/dial-syn/{word}")

    def minnan_pron(self, subpage: str) -> str:
        return self._mdp.get_contents(f"{self.Module_name}/nan-pron/{subpage}")

    def mandarin_pron(self):
        return self._mdp.get_contents(f"{self.Module_name}/cmn-pron")

    def cantonese_pron(self) -> str:
        return self._mdp.get_contents(f"{self.Module_name}/yue-pron")

    def cantonese_word(self, word) -> str:
        return self._mdp.get_contents(f"{self.Module_name}/yue-word/{word}")

    def hakka_pron(self, subpage: str) -> str:
        return self._mdp.get_contents(f"{self.Module_name}/hak-pron/{subpage}")

    def st(self) -> str:
        """
        simple to traditional characters
        :return:
        """
        return self._mdp.get_contents(f"{self.Module_name}/st")

    def ts(self) -> str:
        """
        traditional to simple characters
        :return:
        """
        return self._mdp.get_contents(f"{self.Module_name}/ts")

    def wordlist(self, page=''):
        if len(page) == 0:
            wl = "wordlist"
        else:
            wl = f"wordlist/{page}"

        return self._mdp.get_contents(f"{self.Module_name}/{wl}")


class ZhModuleDataFile:
    def __init__(self, dirpath: str):
        self._dirpath = dirpath

    def get_contents(self, key: str) -> str:
        s = StringIO()
        with open(f"{self._dirpath}/{key}", "r", encoding='utf-8') as f:
            for line in f.readline():
                s.write(line)

        return s.getvalue()


class ZhTopolectSynonyms:
    def __init__(self, top_syn: Tuple[str, dict]):
        self._top_syn = {word: synonyms for word, synonyms in top_syn}

    @classmethod
    def from_local_folder(cls, folder: str):
        return cls((f, local_json_resource(f"{folder}/{f}")) for f in filenames_from_folder(folder))

    def mandarin_words(self):
        return self._top_syn.keys()

    def all_words(self):
        return ((word, synonyms) for word, synonyms in self._top_syn.items())


class ZhTopolectPronunciations:
    def __init__(self, pron_dicts: Generator[dict, None, None]):
        self._prons = {}
        for pron_dict in pron_dicts:
            self._prons.update(pron_dict)

    @classmethod
    def from_local_json_folder(cls, folder: str):
        return cls(local_json_resource(f"{folder}/{f}") for f in filenames_from_folder(folder))

    @classmethod
    def from_local_json_file(cls, filepath: str):
        return cls((d for d in [local_json_resource(filepath)]))

    def pronunciation(self, word):
        return self._prons.get(word, None)


class MandarinPronunciations(ZhTopolectPronunciations):
    @classmethod
    def from_frequencies_csv(cls, csv_filepath: str) -> ZhTopolectPronunciations:
        pron = {}
        for line in dictlines_from_csv(csv_filepath):
            pron[line['Traditional']] = line['Pinyin']

        return cls((d for d in [pron]))

