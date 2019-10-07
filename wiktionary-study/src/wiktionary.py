import requests

__all__ = ['WiktionaryAPI', 'WiktionaryRawEntry']


class WiktionaryAPI:
    def __init__(self):
        self._url = "https://en.wiktionary.org/w/api.php"

    def query_revision(self, titles):
        params = {"action": "query", "prop": "revisions", "titles": titles, "rvprop": "content|ids", "rvslots": "main",
                  "rvlimit": 1, "format": "json", "formatversion": 2}

        resp = requests.post(self._url, params)
        resp.raise_for_status()

        respjson = resp.json()
        if 'error' in respjson:
            raise ValueError(respjson['error'])

        return respjson



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


if __name__ == '__main__':
    wikt = WiktionaryAPI()
    rawentry = WiktionaryRevision.jsoncreate(wikt.query_revision('愛'))
    print(rawentry.content)
