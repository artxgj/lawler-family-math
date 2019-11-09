from zhmodules import ZhModuleDataPage
import argparse


def download_nanprons(infilepath, outfolder):
    dsapi = ZhModuleDataPage()
    with open(infilepath, 'r') as infile:
        for line in infile:
            subpage = line.strip()
            print(subpage, subpage.encode('utf-8'))
            res = dsapi.minnan_pron(subpage)
            with open(f"{outfolder}/{subpage}", 'w', encoding='utf-8') as outf:
                outf.write(res)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infilepath", help="nanprons index data filepath", required=True)
    parser.add_argument("-o", "--output-folder", help="nanprons output folder", required=True)
    args = parser.parse_args()

    download_nanprons(args.infilepath, args.output_folder)
