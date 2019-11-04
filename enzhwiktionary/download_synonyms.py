from zhmodules import ZhModuleDataPage
import argparse


def download_dialectal_synonyms(infilepath, outfolder):
    dsapi = ZhModuleDataPage()
    with open(infilepath, 'r') as infile:
        for line in infile:
            word = line.strip()
            res = dsapi.get_synonym_data(word)
            with open(f"{outfolder}/{word}", 'w', encoding='utf-8') as outf:
                outf.write(res)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infilepath", help="dialectal synonyms module data filepath", required=True)
    parser.add_argument("-o", "--output-folder", help="dialectal synonyms output filepath", required=True)
    args = parser.parse_args()

    download_dialectal_synonyms(args.infilepath, args.output_folder)
