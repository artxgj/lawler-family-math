from typing import IO, Optional
from p3lib.wiktionary import WiktionaryModuleDataPage, WiktionarySpecialPrefixIndex, Namespace
from io import StringIO
from luaparser import ast, astnodes
from abc import ABC, abstractmethod


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

    def __init__(self, modulepage, maxpages=1):
        super().__init__(modulepage, maxpages)

    def filter_predicate(self, sub_page_name):
        return sub_page_name[-len(self._modulepage):] != self._modulepage and sub_page_name[-len(self._doc):] != self._doc


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


class ZhModuleDataPage(ZhModuleDataResource):
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
        return self._mdp.get_contents(f"{self.Module_name}/st")

    def ts(self) -> str:
        return self._mdp.get_contents(f"{self.Module_name}/ts")

    def wordlist(self, page=''):
        if len(page) == 0:
            wl = "wordlist"
        else:
            wl = f"wordlist/{page}"

        return self._mdp.get_contents(f"{self.Module_name}/${wl}")


class ZhModuleDataFile(ZhModuleDataResource):
    def __init__(self, dirpath: str):
        self._dirpath = dirpath

    def get_synonym_data(self, word: str) -> str:
        s = StringIO()
        with open(f"{self._dirpath}/{word}", "r", encoding='utf-8') as f:
            s.writelines(f.readlines())

        return s.getvalue()


class ZhSynonymsLuaModule:
    def __init__(self):
        self._luapy_dispatch = {
            astnodes.Table: self.rhs_table_to_list,
            astnodes.String: self.rhs_string_to_str,
            astnodes.Field: self.rhs_field_to_str
        }

    @classmethod
    def rhs_table_to_list(cls, table):
        return [field.value.s for field in table.fields]

    @classmethod
    def rhs_string_to_str(cls, luastr):
        return luastr.s

    @classmethod
    def rhs_field_to_str(field):
        return f"{field.key}  = {field.value}"

    @classmethod
    def find_synonyms_table(cls, astree: ast.Node) -> Optional[ast.Table]:
        """
        This method converts a lua table of dialectal synonyms to a python dictionary

        astree is an abstract tree that represents a dialectal synoynyms resource written in Lua.
        The following is an example of the dialectal synonyms for 麵包:

            local export = {}

            export.list = {
                ["meaning"]		= "bread",
                ["note"]		= "",
                ["Singapore-MN"]	= { "loti" },
                ["Philippine-MN"]	= { "饅頭", "麵包" }

            }

            return export


        For the entire list of synoynms for 麵包, see https://en.wiktionary.org/wiki/Module:zh/data/dial-syn/麵包
        """
        for node in ast.walk(astree):
            if isinstance(node, ast.Assign) and not isinstance(node, ast.LocalAssign):
                for offset, target in enumerate(node.targets):
                    if isinstance(target, ast.Index):
                        if target.value.id == 'export' and target.idx.s == 'list' and  \
                                isinstance(node.values[offset], ast.Table):
                            return node.values[offset]

        return None

    def extract_pydict(self, lua_synonym_mod: str) -> Optional[dict]:
        """
        See above's find_synonyms_table regarding the string contents of lua_synonym_mod
        """
        tree = ast.parse(lua_synonym_mod)
        synluatbl = self.find_synonyms_table(tree)

        if synluatbl:
            return {field.key.s: self._luapy_dispatch[type(field.value)](field.value) for field in synluatbl.fields}

        else:
            return None
