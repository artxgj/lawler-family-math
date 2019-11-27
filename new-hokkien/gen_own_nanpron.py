from p3lib.enzhwiktionary_mwph import MwphEnWiktChinesePronunciation
from p3lib.zhtopolects import MinnanTopolect
from ph_hokkien import PhHokkien
import datetime
from iohelpers import filenames_from_folder, lines_from_textfile, to_json_file
import io


def ph_hokkien_pronunciation(mt: MinnanTopolect):
    precedence = {}

    for locale in PhHokkien.pron_locales():
        prons = mt.dialect(locale)
        if prons is not None:
            for pron in prons:
                if pron not in precedence:
                    precedence[pron] = PhHokkien.locale_weight(locale)
                else:
                    precedence[pron] += PhHokkien.locale_weight(locale)

    if len(precedence) == 0:
        return None
    else:
        precedence_prons = sorted([(v, k) for k, v in precedence.items()], reverse=True)
        ordered_prons = '/'.join([pron for count, pron in precedence_prons])
        return ordered_prons


if __name__ == '__main__':
    folder_path = '../data/enwiktionary/zh-words/20191125'
    i = 0
    j = 0
    hokkien_pron = {}

    for fname in filenames_from_folder(folder_path):
        s = io.StringIO()
        j += 1
        for line in lines_from_textfile(f'{folder_path}/{fname}'):
            s.write(f"{line}\n")

        try:
            zh_pron = MwphEnWiktChinesePronunciation(s.getvalue())
            mn_pron = MinnanTopolect(zh_pron.topolect('mn'))
            i += 1
            lan_lang_oe = ph_hokkien_pronunciation(mn_pron)
            if lan_lang_oe is None:
                print(f"- - - - - - {fname}")
            else:
                hokkien_pron[fname] = lan_lang_oe
        except Exception as e:
            print(f"* * * * *{fname}, {e}")

    print("-----------------------------------------")
    print(f"Number of words with Minnan: {i}")
    print(f"Total number of words in local folder: {j}")

    today = datetime.datetime.now().strftime('%Y%m%d')
    my_nan_pron = f'../data/enwiktionary/module-zh-data-json/nan-pron/411{today}'
    to_json_file(my_nan_pron, hokkien_pron, indent=4)
