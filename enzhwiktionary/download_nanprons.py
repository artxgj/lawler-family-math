from zhmodules import ZhModuleDataPage
import argparse


def download_nanprons(infilepath, outfolder):
    dsapi = ZhModuleDataPage()
    with open(infilepath, 'r') as infile:
        for line in infile:
            index_name = line.strip()
            page = f"{ZhModuleDataPage.prefix_nan_pron}{index_name}"
            res = dsapi.get_pronunciation_data(page)
            with open(f"{outfolder}/{index_name}", 'w', encoding='utf-8') as outf:
                outf.write(res)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infilepath", help="nanprons index data filepath", required=True)
    parser.add_argument("-o", "--output-folder", help="nanprons output folder", required=True)
    args = parser.parse_args()

    download_nanprons(args.infilepath, args.output_folder)
