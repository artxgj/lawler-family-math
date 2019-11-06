from zhmodules import ZhModuleDataPage, ZhSynonymsLuaModule, ZhModuleDataFile, ZhModuleDataResource
import argparse
import json


def extract_dialectal_synonyms(zhdatapage: ZhModuleDataResource, infilepath, outfilepath):
    outdict = {}
    synlua = ZhSynonymsLuaModule()
    with open(infilepath, 'r') as infile:
        for line in infile:
            word = line.strip()
            lua_export = zhdatapage.get_synonym_data(word)
            outdict[word] = synlua.extract_pydict(lua_export)

    with open(outfilepath, 'w', encoding='utf8') as outfile:
        json.dump(outdict, outfile,  ensure_ascii=False)


def local_extract_synonyms(folder, infilepath, outfilepath):
    print("Local")
    local_mod = ZhModuleDataFile(folder)
    extract_dialectal_synonyms(local_mod, infilepath, outfilepath)


def remote_extract_synonyms(infilepath, outfilepath):
    print("Remote")
    remote_mod = ZhModuleDataPage()
    extract_dialectal_synonyms(remote_mod, infilepath, outfilepath)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--local-resource", help="locally stored dialectal synonyms data")
    parser.add_argument("-i", "--infilepath", help="filepath containing the list of words with dialectal synonyms", required=True)
    parser.add_argument("-o", "--outfilepath", help="json store filepath", required=True)
    args = parser.parse_args()

    local_extract_synonyms(args.local_resource, args.infilepath, args.outfilepath)
    # remote_extract_synonyms(args.infilepath, args.outfilepath)

