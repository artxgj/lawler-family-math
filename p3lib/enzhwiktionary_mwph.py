from enzhwiktionary import EnWiktChinesePronunciation, RawTopolectPronunciation
from wiktionary import WicktionaryRevisionEntrySearch
import mwparserfromhell


class MwphEnWiktChinesePronunciation(EnWiktChinesePronunciation):
    def __init__(self, wiktentry: str):
        super().__init__(wiktentry)

    def parse_topolects(self, wiktentry: str) -> None:
        wikicode = mwparserfromhell.parse(wiktentry)
        zhprons = wikicode.filter_templates(matches='zh-pron')

        if len(zhprons) == 0:
            raise ValueError('WiktEntry does not have a Chinese pronunciation template.')

        for zhpron in zhprons:
            for param in zhpron.params:
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

    for 詞 in ['凱', '水', '瑟', '緊', '琳', '歷史', '冠', '哭', '吼']:
        res = wikt.find(詞)
        # print(res.content)
        print("\n* * * * * * *\n")
        zhpron = MwphEnWiktChinesePronunciation(res.content)
        print(zhpron.topolect('m'))
        print("\n+ + + + + + +\n")
