from p3lib.markdown import Markdown
from iohelpers import lines_from_textfile
from english_hokkien_mandarin import EnglishHokkienMandarin
from zhmodules import ZhTopolectSynonyms, MandarinPronunciations, ZhTopolectPronunciations
from io import StringIO
from datetime import datetime

if __name__ == '__main__':
    synonyms = ZhTopolectSynonyms.from_local_folder('../data/enwiktionary/module-zh-data-json/dial-syn')

    mp = MandarinPronunciations.from_local_json_file('../data/enwiktionary/module-zh-data-json/combined-mandarin-pron.json')
    h = ZhTopolectPronunciations.from_local_json_folder('../data/enwiktionary/module-zh-data-json/nan-pron')

    ehm = EnglishHokkienMandarin(synonyms, h, mp)

    s = StringIO()
    for line in lines_from_textfile('template/hokkien-synonyms-poj.template'):
        s.write(f"{line}\n")

    md_template = s.getvalue()
    tb_header = Markdown.table_header(['English', 'Minnan/Hokkien', 'Mandarin'])
    tb_data = '\n'.join([Markdown.table_row(item) for item in ehm.items()])

    hokkien_table = f"{tb_header}\n{tb_data}"
    tbl_gen_date = datetime.now().strftime("%Y-%m-%d")
    md_ehm = md_template.format(hokkien_table=hokkien_table, tbl_gen_date=tbl_gen_date)

    with open('../data/tmp/hokkien-english-mandarin.md', 'w', encoding='utf-8') as ostr:
        ostr.write(md_ehm)






