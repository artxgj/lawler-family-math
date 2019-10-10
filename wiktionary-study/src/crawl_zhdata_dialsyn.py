import urllib.parse
import requests
from bs4 import BeautifulSoup


class RequestsWrapper:
    def __init__(self, url):
        self.url = url
        self._params = {}

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def params(self):
        return self._params

    def post(self, params):
        if params is not None and not isinstance(params, dict):
            raise TypeError("params argument has to be a dictionary")

        if params:
            self._params = params

        req = requests.post(self._url, self._params)
        req.raise_for_status()
        return req

    def get(self, params):
        if params is not None and not isinstance(params, dict):
            raise TypeError("params argument has to be a dictionary")

        if params:
            self.params = params

        req = requests.post(self._url, self._params)
        req.raise_for_status()
        return req


class ZhDataDialSynIndexCrawler:
    def __init__(self, UrlRequestType, url="https://en.wiktionary.org/w/index.php"):
        self._request = UrlRequestType(url)
        self._next = None

    def _extract_dialsyn(self, soup):
        dialectal_synonyms = soup.find('ul', attrs={"class": "mw-prefixindex-list"})

        if dialectal_synonyms:
            return [a['title'] for a in dialectal_synonyms.find_all('a')]
        else:
            return []

    def _soup_response(self, params: dict) -> 'BeautifulSoup':
        resp = self._request.post(params)
        return BeautifulSoup(resp.text, 'lxml')

    def extract_index(self, params):
        soup = self._soup_response(params)
        return self._extract_dialsyn(soup)

    def extract_all_indices(self, params):
        results = []
        query_params = params
        while True:
            soup = self._soup_response(query_params)
            results.extend(self._extract_dialsyn(soup))
            nextpage = soup.find("div", attrs={'class': 'mw-prefixindex-nav'})

            if nextpage is None:
                break
            a = nextpage.find('a')
            qs_params = urllib.parse.unquote(a['href']).split('?')[1]

            query_params = {}
            for qp in qs_params.split('&'):
                k, v = qp.split('=')
                query_params[k] = v

        return results


"""
https://en.wiktionary.org/w/api.php?action=parse&page=Module:zh/data/dial-syn/地震&prop=wikitext&format=jsonfm
"""

if __name__ == '__main__':
    """
    simple test
    """
    crawler = ZhDataDialSynIndexCrawler(RequestsWrapper)

    params = {'title': 'Special:PrefixIndex',
              'prefix': 'Module:zh/data/dial-syn',
              'namespace': 0,'stripprefix': 1}

    dialsyn_datamodules = crawler.extract_all_indices(params)
    for i, dialsyn in enumerate(dialsyn_datamodules):
        print(i+1, dialsyn)







