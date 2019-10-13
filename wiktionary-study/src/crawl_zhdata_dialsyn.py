from EnWiktCJK import ZhDataDialSynIndexCrawler
import argparse


def chinese_module_dialectal_synonyms(outfilepath):
    crawler = ZhDataDialSynIndexCrawler()

    params = {'title': 'Special:PrefixIndex',
              'prefix': 'Module:zh/data/dial-syn',
              'namespace': 0,
              'stripprefix': 1}

    dialsyn_datamodules = crawler.extract_all_indices(params)

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






