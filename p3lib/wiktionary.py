from bs4 import BeautifulSoup
from enum import IntEnum, unique
from typing import Generator, Iterator
import requests
import urllib.parse


__all__ = ['WiktionaryAPICrawler', 'WiktionaryHtmlCrawler', "WiktionarySpecialPrefixIndexTool", "WicktionaryRevisionEntrySearch",
           "WiktionaryRevision", 'querystring_todict']

"""
https://en.wiktionary.org/w/api.php?action=parse&prop=wikitext&format=jsonfm&page=Module:zh/data/dial-syn/地震
"""

WIKTIONARY_INDEX_URL = "https://en.wiktionary.org/w/index.php"
WIKTIONARY_API_URL = "https://en.wiktionary.org/w/api.php"


@unique
class Namespace(IntEnum):
    """
    Reference: https://en.wiktionary.org/wiki/Wiktionary:Namespace

    Below is a list of namespaces that are of interest
    """
    main = 0,
    file = 6,
    template = 10,
    category = 14,
    module = 828


def querystring_todict(qs_params):
    query_params = {}
    for qp in qs_params.split('&'):
        k, v = qp.split('=')
        query_params[k] = v

    return query_params


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


class WiktionaryHtmlCrawler:
    def __init__(self, endpoint=None):
        self._endpoint = endpoint or WIKTIONARY_INDEX_URL
        self._requests = RequestsWrapper(self._endpoint)

    def _soup_response(self, response: 'requests_response') -> BeautifulSoup:
        return BeautifulSoup(response.text, 'lxml')

    def post(self, params):
        resp = self._requests.post(params)
        return self._soup_response(resp)

    def get(self, params):
        resp = self._requests.get(params)
        return self._soup_response(resp)


class WiktionaryAPICrawler:
    def __init__(self, url=None):
        url = url or WIKTIONARY_API_URL
        self._requests = RequestsWrapper(url)

    def _handle_response(self, response):
        response.raise_for_status()
        respjson = response.json()

        if 'error' in respjson:
            raise ValueError(respjson['error'])

        return respjson

    def post(self, params):
        resp = self._requests.post(params)
        return self._handle_response(resp)

    def get(self, params):
        resp = self._requests.get(params)
        return self._handle_response(resp)


class WiktionaryRevision:
    def __init__(self, revision):
        self.ns = revision['ns']
        self.results_continue = revision['continue']
        self.pageid = revision['pageid']
        self.title = revision['title']
        self.revid = revision['revid']
        self.content = revision['content']
        self.contentmodel = revision['contentmodel']
        self.contentformat = revision['contentformat']

    @classmethod
    def jsoncreate(cls, queryres: dict):
        """

        :param query_result:
        :return:
        """

        page = queryres['query']['pages'][0]

        if 'missing' in page and page['missing']:
            raise Exception(f"{page['title']} does not exist in Wiktionary.")

        page_revision = page['revisions'][0]
        revision = {'pageid': page['pageid'],
                    'ns': page['ns'],
                    'title': page['title'],
                    'revid': page_revision['revid'],
                    'content': page_revision['slots']['main']['content'],
                    'contentmodel': page_revision['slots']['main']['contentmodel'],
                    'contentformat': page_revision['slots']['main']['contentformat']
                    }

        if 'continue' in queryres:
            revision['continue'] = queryres['continue']
        else:
            revision['continue'] = {}

        return cls(revision)

    @property
    def ns(self):
        return self._ns

    @ns.setter
    def ns(self, val):
        if val < 0:
            raise ValueError('namespace is not >= 0')
        else:
            self._ns = val

    @property
    def results_continue(self):
        return self._continue

    @results_continue.setter
    def results_continue(self, value):
        if not isinstance(value, dict):
            raise TypeError('continue is not a dictionary.')

        self._continue = value

    @property
    def pageid(self):
        return self._pageid

    @pageid.setter
    def pageid(self, value):
        if value < 0:
            raise ValueError('pageid < 0')

        self._pageid = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, val):
        self._title = val

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, val):
        self._content = val

    @property
    def revid(self):
        return self._revid

    @revid.setter
    def revid(self, val):
        self._revid = val

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def contentformat(self):
        return self._contentformat

    @contentformat.setter
    def contentformat(self, val):
        self._contentformat = val

    @property
    def contentmodel(self):
        return self._contentmodel

    @contentmodel.setter
    def contentmodel(self, val):
        self._contentmodel = val


class IWicktionarySearch:
    """
      like a "Java Interface Type"
    """
    def __init__(self):
        NotImplemented

    def find(self, params: dict):
        NotImplemented


class WicktionaryRevisionEntrySearch(IWicktionarySearch):
    def __init__(self):
        self._crawler = WiktionaryAPICrawler()

    def find(self, entry: str) -> 'WiktionaryRevision':
        """
            https://www.mediawiki.org/wiki/API:Main_page
        """

        params = {"action": "query",
                  "prop": "revisions",
                  "titles": entry,
                  "rvprop": "content|ids",
                  "rvslots": "main",
                  "rvlimit": 1,
                  "format": "json",
                  "formatversion": 2}

        results = self._crawler.post(params)
        return WiktionaryRevision.jsoncreate(results)


class WiktionaryRenderedTitle(IWicktionarySearch):
    def __init__(self):
        self._crawler = WiktionaryHtmlCrawler()

    def find(self, title):
        params = {
            'title': title,
            'action': 'render'
        }

        resp = self._crawler.post(params)
        return resp.text


class WiktionaryRawTitle(IWicktionarySearch):
    def __init__(self):
        self._crawler = WiktionaryHtmlCrawler()

    def find(self, title):
        params = {
            'title': title,
            'action': 'raw'
        }

        resp = self._crawler.post(params)
        return resp.text


class WiktionarySpecialPrefixIndex(WiktionaryHtmlCrawler):
    def _query(self, params: dict, max_pages: int) -> Iterator[Generator]:
        page = 0
        while params and page < max_pages:
            soup = super().post(params)
            results = soup.find('ul', attrs={"class": "mw-prefixindex-list"})

            nextpage = soup.find("div", attrs={'class': 'mw-prefixindex-nav'})

            if results:
                yield (a['title'] for a in results.find_all('a'))

            if nextpage:
                a = nextpage.find('a')
                qs_params = urllib.parse.unquote(a['href']).split('?')[1]
                params = querystring_todict(qs_params)
            else:
                params = {}

            page += 1

    def query(self, prefix: str, ns: Namespace, max_pages: int = 1):
        params = {'prefix': prefix,
                  'namespace': ns.value,
                  'title': 'Special:PrefixIndex'}

        for gexp in self._query(params, max_pages):
            for item in gexp:
                yield item
