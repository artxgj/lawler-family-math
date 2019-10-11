from wiktionary import WiktionaryHtmlCrawler, WiktionaryActionAPI, querystring_todict, WIKTIONARY_INDEX_URL
import urllib.parse


class ZhDataDialSynIndexCrawler(WiktionaryHtmlCrawler):
    def __init__(self, url=WIKTIONARY_INDEX_URL):
        super().__init__(url)
        self._next = None

    def _extract_dialsyn(self, soup):
        dialectal_synonyms = soup.find('ul', attrs={"class": "mw-prefixindex-list"})

        if dialectal_synonyms:
            return [a['title'] for a in dialectal_synonyms.find_all('a')]
        else:
            return []

    def extract_index(self, params):
        soup = self.post(params)
        return self._extract_dialsyn(soup)

    def extract_all_indices(self, params, maxindices=10):
        if maxindices <= 0:
            raise ValueError('maxindices must be at least 1')

        results = []
        query_params = params
        visits = 0
        while True:
            soup = self.post(query_params)
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


# https://en.wiktionary.org/w/api.php?action=parse&prop=wikitext&format=json&page=Module:zh/data/dial-syn
class ZhDialectalSynonym:
    def __init__(self):
        self._crawler = WiktionaryActionAPI()

    def find(self, module_zh_dialsyn):
        params = {'prop': 'wikitext', 'format': 'json', 'page': module_zh_dialsyn}
        return self._crawler.parse(params)



