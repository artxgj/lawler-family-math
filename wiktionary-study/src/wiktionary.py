from bs4 import BeautifulSoup

import copy
import mwparserfromhell
import requests



__all__ = ['WiktionaryAPICrawler', 'WiktionaryHtmlCrawler', 'WiktionaryTitles', 'WiktionaryRevision', 'querystring_todict']

"""
https://en.wiktionary.org/w/api.php?action=parse&prop=wikitext&format=jsonfm&page=Module:zh/data/dial-syn/地震
"""

_wiktionary_index_url = "https://en.wiktionary.org/w/index.php"
_wiktionary_api_url = "https://en.wiktionary.org/w/api.php"


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
    def __init__(self, url):
        self._requests = RequestsWrapper(url)

    def _soup_response(self, response: 'requests_response') -> 'BeautifulSoup':
        return BeautifulSoup(response.text, 'lxml')

    def post(self, params):
        resp = self._requests.post(params)
        return self._soup_response(resp)

    def get(self, params):
        resp = self._requests.get(params)
        return self._soup_response(resp)


class WiktionaryAPICrawler:
    def __init__(self, url=None):
        url = url or _wiktionary_api_url
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


class WiktionaryActionAPI(WiktionaryAPICrawler):
    """
    https://www.mediawiki.org/wiki/API:Main_page
    """

    def query(self, params):
        new_params = copy.deepcopy(params)
        new_params['action'] = 'query'
        return self.post(new_params)

    def parse(self, params):
        new_params = copy.deepcopy(params)
        new_params['action'] = 'parse'
        return self.post(new_params)


class WiktionaryTitles:
    def __init__(self):
        self._crawler = WiktionaryActionAPI()

    def find(self, titles):
        params = {"prop": "revisions",
                  "titles": titles,
                  "rvprop": "content|ids",
                  "rvslots": "main",
                  "rvlimit": 1,
                  "format": "json",
                  "formatversion": 2}

        return self._crawler.query(params)


class WiktionaryRevision:
    def __init__(self, revision):
        self.ns = revision['ns']
        self.results_continue = revision['continue']
        self.pageid = revision['pageid']
        self.title = revision['title']
        self.revid = revision['revid']
        self.content = revision['content']
        self.contentmodel = revision['contentmodel']
        self.contentformat  = revision['contentformat']

    @classmethod
    def jsoncreate(cls, queryres: dict):
        """
        
        :param query_result: 
        :return: 
        """

        page = queryres['query']['pages'][0]
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


def section_chinese(wikicode : 'mwparserfromhell.wikicode.Wikicode'):
    sections = wikicode.get_sections(matches="Chinese")

    if len(sections) == 0:
        raise ValueError("wikicode doesn't have a Chinese section")

    return sections[0]


def wikicode(wiktionary_entry_text) -> 'mwparserfromhell.wikicode.Wikicode':
    return mwparserfromhell.parse(wiktionary_entry_text)




if __name__ == '__main__':
    #
    # sample code
    #
    wikt_title = WiktionaryTitles()
    love = WiktionaryRevision.jsoncreate(wikt_title.find('愛'))

    wc_content = wikicode(love.content)
    section = section_chinese(wc_content)
    print(section)
    print("\n---------\n")

    house_family = WiktionaryRevision.jsoncreate(wikt_title.find('家'))
    section = section_chinese(wikicode(house_family.content))
    print(section)

    behind = WiktionaryRevision.jsoncreate(wikt_title.find('後面'))
    section = section_chinese(wikicode(behind.content))
    print(section)

