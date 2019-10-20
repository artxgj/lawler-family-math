import copy

# qz: Quanzhou 泉州
# xm: Xiamen
# ph: Philippines

# Hokkien word weight symbols
hokkien_word_weights = {
    'ph': 4,
    'qz': 2,
    'xm': 1
}


"""
Wiktionary defines ml as mainland:

ml covers Quanzhou, Xiamen and Zhangzhou 
"""
poj_weights = {
    'ph': 4,
    'ml': 4,
    'qz': 2,
    'xm': 1
}


class LocaleRank:
    def __init__(self, locale_weights: dict):
        if not isinstance(locale_weights, dict):
            raise TypeError('locale_weights must be a dictionary.')

        if len(locale_weights) == 0:
            raise ValueError('locale_weights cannot be an empty dictionary.')

        self._locale_weights = copy.deepcopy(locale_weights)

    def rank(self, **locale_entities):
        """
        Weighted ranking of entities of different locales
        :param locale_entities: keyword arguments: each key matches a key
                    in locale_weights
        :return: 
        """
        entities_rank = {}
        for locale, entities in locale_entities.items():
            weight = self._locale_weights[locale]
            synlist = entities.split(',')

            for syn in synlist:
                key = syn.strip()

                if len(key) > 0:
                    if key in entities_rank:
                        entities_rank[key] += weight
                    else:
                        entities_rank[key] = weight

        return sorted(entities_rank, key=entities_rank.get, reverse=True)
