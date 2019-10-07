import requests

__all__ = ['WiktionaryAPI', 'WiktionaryRawEntry']


class WiktionaryAPI:
    def __init__(self):
        self._url = "https://en.wiktionary.org/w/api.php"
        self._params = {"action": "query",
                        "prop": "revisions",
                        "rvprop": "content|ids",
                        "rvslots": "main",
                        "rvlimit": 1,
                        "format": "json",
                        "formatversion": 2
                        }

    def query(self, titles):
        self._params["titles"] = titles
        resp = requests.post(self._url, self._params)
        resp.raise_for_status()

        respjson = resp.json()
        if 'error' in respjson:
            raise ValueError(respjson['error'])

        return respjson


class WiktionaryRawEntry:
    def __init__(self, wiktdict):
        if 'continue' in wiktdict:
            self.wikt_continue = wiktdict['continue']
        else:
            self.wikt_continue = {}

        page = wiktdict['query']['pages'][0]
        self.pageid = page['pageid']
        self.ns = page['ns']
        self.title = page['title']

        revision = page['revisions'][0]
        self.revid = revision['revid']
        self.content = revision['slots']['main']['content']
        self.contentmodel = revision['slots']['main']['contentmodel']
        self.contentformat = revision['slots']['main']['contentformat']

    @property
    def wikt_continue(self):
        return self._continue

    @wikt_continue.setter
    def wikt_continue(self, value):
        if not isinstance(value, dict):
            raise TypeError('continue is not a dictionary.')

        self._continue = value

    @property
    def pageid(self):
        return self._pageid

    @pageid.setter
    def pageid(self, value):
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


if __name__ == '__main__':
    wikt = WiktionaryAPI()
    rawentry = WiktionaryRawEntry(wikt.query('愛'))
    print(rawentry.content)
