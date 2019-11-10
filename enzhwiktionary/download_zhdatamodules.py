from zhmodules import ZhModuleDataPage
import argparse
import os


class ModuleDataPageLoader:
    def __init__(self, toc_folder, download_folder):
        self._zhmdp = ZhModuleDataPage()
        self._download_folder = download_folder
        self._toc_folder = toc_folder

        try:
            os.mkdir(download_folder)
        except FileExistsError:
            pass

        self._load_configs = [
            {'method': 'cantonese_pron', 'args': [], 'toc_filename': None, 'relpath': 'yue-pron'},
            {'method': 'mandarin_pron', 'args': [], 'toc_filename': None, 'relpath': 'cmn-pron'},
            {'method': 'st', 'args': [], 'toc_filename': None, 'relpath': 'st'},
            {'method': 'ts', 'args': [], 'toc_filename': None, 'relpath': 'ts'},
            {'method': 'wordlist', 'args': ['1'], 'toc_filename': None, 'relpath': 'wordlist-1'},
            {'method': 'wordlist', 'args': ['2'], 'toc_filename': None, 'relpath': 'wordlist-2'},
            {'method': 'wordlist', 'args': ['3'], 'toc_filename': None, 'relpath': 'wordlist-3'},
            {'method': 'cantonese_word', 'args': [], 'toc_filename': 'yue-word-toc.txt', 'relpath': 'yue-word'},
            {'method': 'hakka_pron', 'args': [], 'toc_filename': 'hakka-pron-toc.txt', 'relpath': 'hak-pron'},
            {'method': 'minnan_pron', 'args': [], 'toc_filename': 'nan-pron-toc.txt', 'relpath': 'nan-pron'},
            {'method': 'dialectal_synonyms', 'args': [], 'toc_filename': 'dialectal-synonyms-toc.txt',
             'relpath': 'dial-syn'}
        ]

    def load_all(self):
        for load_config in self._load_configs:
            print(load_config)
            if load_config['toc_filename']:
                self.download_data_toc_items(load_config)
            else:
                download_filepath = f"{self._download_folder}/{load_config['relpath']}"
                self.download_data_page(download_filepath, load_config['method'], load_config['args'])

    def download_data_page(self, download_filepath, method, method_args):
        with open(download_filepath, 'w', encoding='utf-8') as outf:
            try:
                outf.write(getattr(self._zhmdp, method)(*method_args))
            except ValueError as e:
                print(e)
                print(method, *method_args)
                print()

    def download_data_toc_items(self, load_config):
        download_folder = f"{self._download_folder}/{load_config['relpath']}"
        try:
            os.mkdir(download_folder)
        except FileExistsError:
            pass

        toc_filepath = f"{self._toc_folder}/{load_config['toc_filename']}"
        print(toc_filepath)
        with open(toc_filepath, 'r', encoding='utf-8') as f:
            for line in f:
                key = line.strip()
                download_filepath = f"{download_folder}/{key}"
                self.download_data_page(download_filepath, load_config['method'], [key])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--download-folder", help="download folder", required=True)
    parser.add_argument("-t", "--toc-pages-folder", help="toc pages folder", required=True)
    args = parser.parse_args()
    mdp = ModuleDataPageLoader(args.toc_pages_folder, args.download_folder)
    mdp.load_all()
