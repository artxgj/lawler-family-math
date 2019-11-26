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

    for 詞 in ['嗷嗷念', '鉛筆璇', '凱', '水', '瑟', '緊', '琳', '歷史', '冠', '哭', '吼', '三點水', '趁食查某', '霸灰']:
        try:
            res = wikt.find(詞)
        except Exception as e:
            print(e)
            continue

        # print(res.content)
        print("\n* * * * * * *\n")
        zhpron = MwphEnWiktChinesePronunciation(res.content)
        try:
            print(詞, 'mandarin', zhpron.topolect('m'))
        except Exception as e1:
            print(e1)
            print(dir(res), "\n", res.content)

        try:
            print(詞, 'minnan', zhpron.topolect('mn'))
        except Exception as e2:
            print(e2)

        print("\n+ + + + + + +\n")
