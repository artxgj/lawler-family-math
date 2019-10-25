from enzhwiktionary import EnWiktChinesePronunciation, RawTopolectPronunciation
from wiktionary import WicktionaryRevisionEntrySearch
import wikitextparser


class WktpEnWiktChinesePronunciation(EnWiktChinesePronunciation):
    def __init__(self, wiktentry: str):
        super().__init__(wiktentry)

    def parse_topolects(self, wiktentry: str) -> None:
        wikicode = wikitextparser.parse(wiktentry)
        zhprons = [template for template in wikicode.templates if template.name.strip() == 'zh-pron']

        if len(zhprons) == 0:
            raise ValueError('wiktentry does not have a Chinese pronunciation template.')

        for zhpron in zhprons:
            for param in zhpron.arguments:
                topolect = str(param.name)

                if self.is_supported(topolect):
                    topolval = RawTopolectPronunciation(str(param.value).strip())
                    if topolect not in self._topolects:
                        self._topolects[topolect] = [topolval]
                    else:
                        self._topolects[topolect].append(topolval)
                elif self.is_note(topolect):
                    note_owner = self.note_owner(topolect)
                    self._topolects[note_owner][-1].note = str(param.value).strip()


if __name__ == "__main__":
    wikt = WicktionaryRevisionEntrySearch()

    for 詞 in ['凱', '水', '瑟', '緊', '琳', '歷史', '冠', '家']:
        res = wikt.find(詞)
        # print(res.content)
        print("\n* * * * * * *\n")
        zhpron = WktpEnWiktChinesePronunciation(res.content)
        try:
            print(zhpron.topolect('mn'))
        except Exception as e:
            print(f"{詞} | {e}")
        print("\n+ + + + + + +\n")
