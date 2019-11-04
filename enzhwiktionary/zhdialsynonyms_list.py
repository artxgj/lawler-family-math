from zhmodules import ZhModuleDataIndex
import argparse
import io


def filestream_zhsynonyms_list(outfilepath):
    mdi = ZhModuleDataIndex()
    with io.open(outfilepath, "w", encoding='utf-8') as ostream:
        mdi.list_synonyms(ostream)


def memstream_zhsynonyms_list():
    mdi = ZhModuleDataIndex()
    s = io.StringIO()
    mdi.list_synonyms(s)
    print(s.getvalue())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--outfilepath", help="dialectal synonym output filepath", type=str, required=True)
    args = parser.parse_args()

    filestream_zhsynonyms_list(args.outfilepath)
    # memstream_zhsynonyms_list()






