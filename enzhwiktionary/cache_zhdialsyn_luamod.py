from zhdialsyn import ZhDialectalSynonym

import argparse
import json
import re

# see sample input at the bottom of the file
regex_dialsyn = re.compile(r'^\s+\["(.+)"]\s+=\s*[{"](.*)["}],*$')


def lua2dict(lua_export):
    dialsyn_dict = {}
    for line in lua_export['parse']['wikitext']['*'].split('\n'):
        kvpair = re.match(regex_dialsyn, line)
        if kvpair:
            dialsyn_dict[kvpair.group(1).strip()] = kvpair.group(2).strip().replace('"', '')

    return dialsyn_dict


def extract_dialectal_synonyms(infilepath, outfolder):
    dsapi = ZhDialectalSynonym()
    with open(infilepath, 'r') as infile:
        for line in infile:
            module_zh = line.strip()
            word = module_zh[module_zh.rfind('/') + 1:]
            print(f"retrieving {word}")
            res = dsapi.find(module_zh)
            with open(f"{outfolder}/{word}", 'w', encoding='utf-8') as outf:
                outf.write(res['parse']['wikitext']['*'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infilepath", help="dialectal synonyms module data filepath", required=True)
    parser.add_argument("-o", "--output-folder", help="dialectal synonyms output filepath", required=True)
    args = parser.parse_args()

    extract_dialectal_synonyms(args.infilepath, args.output_folder)
