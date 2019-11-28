from p3lib.enzhwiktionary_mwph import MwphEnWiktChinesePronunciation
from p3lib.zhtopolects import MandarinTopolect
import datetime
from iohelpers import filenames_from_folder, lines_from_textfile, to_json_file
import io

if __name__ == '__main__':
    folder_path = '../data/enwiktionary/zh-words/20191125'
    i = 0
    j = 0
    mandarin_pron = {}

    for fname in filenames_from_folder(folder_path):
        s = io.StringIO()
        j += 1
        for line in lines_from_textfile(f'{folder_path}/{fname}'):
            s.write(f"{line}\n")

        try:
            zh_pron = MwphEnWiktChinesePronunciation(s.getvalue())
            mandarin = MandarinTopolect(zh_pron.topolect('m'))
            m_pron = mandarin.dialect()
            i += 1

            if m_pron is None:
                print(f"- - - - - - {fname}")
            else:
                mandarin_pron[fname] = '/'.join(m_pron)
        except Exception as e:
            print(f"* * * * *{fname}, {e}")

    print("-----------------------------------------")
    print(f"Number of words with Mandarin: {i}")
    print(f"Total number of words in local folder: {j}")
    print(mandarin_pron)

    today = datetime.datetime.now().strftime('%Y%m%d')
    my_mandarin_pron = f'../data/enwiktionary/module-zh-data-json/mandarin-pron/411{today}'
    to_json_file(my_mandarin_pron, mandarin_pron, indent=4)
