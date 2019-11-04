from zhdialsyn import ZhDataDialSynIndexCrawler
import argparse


def chinese_module_dialectal_synonyms(outfilepath):
    crawler = ZhDataDialSynIndexCrawler()
    dialsyn_datamodules = crawler.extract_all_indices()

    with open(outfilepath, "w") as f:
        for dialsyn in dialsyn_datamodules:
            past_rightslash = dialsyn.rfind('/') + 1

            if past_rightslash < len(dialsyn) and ord(dialsyn[past_rightslash]) < 0x80:
                continue    # ignore ascii

            f.write(f"{dialsyn}\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--outfilepath", help="dialectal synonym output filepath", type=str, required=True)
    args = parser.parse_args()

    chinese_module_dialectal_synonyms(args.outfilepath)






