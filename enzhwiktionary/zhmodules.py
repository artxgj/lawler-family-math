from typing import IO, Optional
from p3lib.wiktionary import WiktionaryModuleDataPage, WiktionarySpecialPrefixIndex, Namespace
from luaparser import ast, astnodes


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
        print(field)
        return f"{field.key}  = {field.value}"

    @classmethod
    def find_synonyms_table(cls, astree: ast.Node) -> Optional[ast.Table]:
        for node in ast.walk(astree):
            if isinstance(node, ast.Assign) and not isinstance(node, ast.LocalAssign):
                for offset, target in enumerate(node.targets):
                    if isinstance(target, ast.Index):
                        if target.value.id == 'export' and target.idx.s == 'list' and  \
                                isinstance(node.values[offset], ast.Table):
                            return node.values[offset]

        return None

    def extract_pydict(self, lua_synonym_mod: str) -> dict:
        tree = ast.parse(lua_synonym_mod)

        synluatbl = self.find_synonyms_table(tree)

        if synluatbl:
            return {field.key.s: self._luapy_dispatch[type(field.value)](field.value) for field in synluatbl.fields}

        else:
            return None
