import copy


class SynonymsRank:
    def __init__(self, locale_weights: dict):
        if not isinstance(locale_weights, dict):
            raise TypeError('locale_weights must be a dictionary.')

        if len(locale_weights) == 0:
            raise ValueError('locale_weights cannot be an empty dictionary.')

        self._locale_weights = copy.deepcopy(locale_weights)

    def rank(self, **locale_synonyms):
        syns_rank = {}
        for locale, synonyms in locale_synonyms.items():
            weight = self._locale_weights[locale]
            synlist = synonyms.split(',')

            for syn in synlist:
                key = syn.strip()
                if key in syns_rank:
                    syns_rank[key] += weight
                else:
                    syns_rank[key] = weight

        return sorted(syns_rank, key=syns_rank.get, reverse=True)
