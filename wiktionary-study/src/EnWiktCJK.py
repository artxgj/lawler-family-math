from wiktionary import WiktionaryHtmlCrawler, WiktionaryAPICrawler, querystring_todict
import urllib.parse


class ZhDataDialSynIndexCrawler:
    """
    Index Pages listing the data modules of dialectal synonyms

    https://en.wiktionary.org/wiki/Module:zh/data/dial-syn
    """
    def __init__(self):
        self._crawler = WiktionaryHtmlCrawler()
        self._next = None

    def _crawler_params(self):
        return {'title': 'Special:PrefixIndex',
                'prefix': 'Module:zh/data/dial-syn',
                'namespace': 0,
                'stripprefix': 1}

    def _extract_dialsyn(self, soup):
        dialectal_synonyms = soup.find('ul', attrs={"class": "mw-prefixindex-list"})

        if dialectal_synonyms:
            return [a['title'] for a in dialectal_synonyms.find_all('a')]
        else:
            return []

    def extract_index(self, params=None):
        lparams = params or self._params()
        soup = self._crawler.post(lparams)
        return self._extract_dialsyn(soup)

    def extract_all_indices(self, params=None, maxindices=10):
        if maxindices <= 0:
            raise ValueError('maxindices must be at least 1')

        results = []
        query_params = params or self._params()

        visits = 0
        while True:
            soup = self._crawler.post(query_params)
            results.extend(self._extract_dialsyn(soup))
            visits += 1

            if visits == maxindices:
                break

            nextpage = soup.find("div", attrs={'class': 'mw-prefixindex-nav'})

            if nextpage is None:
                break

            a = nextpage.find('a')
            qs_params = urllib.parse.unquote(a['href']).split('?')[1]
            query_params = querystring_todict(qs_params)

        return results


class ZhDialectalSynonym:
    def __init__(self):
        self._crawler = WiktionaryAPICrawler()

    def find(self, module_zh_dialsyn: str) -> 'wikitext':

        """

        :param module_zh_dialsyn: dialectal-synonym module name
        :return:
        """
        params = {'action': 'parse',
                  'prop': 'wikitext',
                  'format': 'json',
                  'page': module_zh_dialsyn}
        return self._crawler.post(params)


