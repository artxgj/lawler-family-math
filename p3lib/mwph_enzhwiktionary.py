from enzhwiktionary import IEnWiktChinesePronunciation, TopolectPronunciation
from wiktionary import WicktionaryRevisionEntrySearch
import mwparserfromhell


class MwphEnWiktChinesePronunciation(IEnWiktChinesePronunciation):
    def __init__(self, wiktentry: str):
        if not isinstance(wiktentry, str):
            raise TypeError('Wiktentry has to be a string.')

        wikicode = mwparserfromhell.parse(wiktentry)
        zhprons = wikicode.filter_templates(matches='zh-pron')

        if len(zhprons) == 0:
            raise ValueError('WiktEntry does not have a Chinese pronunciation template.')

        self._topolect_values = {}
        self._topolect_notes = {}

        for zhpron in zhprons:
            for param in zhpron.params:
                topolect = str(param.name)

                if self.is_supported(topolect):
                    if topolect not in self._topolect_values:
                        self._topolect_values[topolect] = [str(param.value).strip()]
                    else:
                        self._topolect_values[topolect].append(str(param.value).strip())
                elif self.is_note(topolect):
                    note_owner = self.note_owner(topolect)

                    if note_owner not in self._topolect_notes:
                        self._topolect_notes[note_owner] = [str(param.value).strip()]
                    else:
                        self._topolect_notes[note_owner].append(str(param.value).strip())

    def topolect(self, 方言: str) -> TopolectPronunciation:
        pass


if __name__ == "__main__":

    wikt = WicktionaryRevisionEntrySearch()

    for 詞 in ['凱', '水', '瑟', '緊', '琳', '歷史']:
        res = wikt.find(詞)
        # print(res.content)
        print("\n* * * * * * *\n")
        zhpron = MwphEnWiktChinesePronunciation(res.content)
        print(zhpron._topolect_values)
        print(zhpron._topolect_notes)
        print("\n+ + + + + + +\n")
