from typing import Iterator

mn_ph = 'Philippine-MN'
mn_qz = 'Quanzhou'
mn_xm = 'Xiamen'
mn_jj = 'Jinjiang'

ph = 'ph'
jj = 'jj'
qz = 'qz'
xm = 'xm'

_syn_hokkien_locales = {mn_ph, mn_qz, mn_xm, mn_jj}
_hokkien_pron_locales = {ph, jj, qz, xm}
_locale_weight = {ph: 4, jj: 3, qz: 2, xm: 1}

_aliases = {
    mn_ph: ph,
    mn_qz: qz,
    mn_xm: xm,
    mn_jj: jj
}


class PhHokkien:
    @staticmethod
    def locale_weight(loc: str) -> int:
        return _locale_weight[loc]

    @staticmethod
    def synonym_weight(syn: str) -> int:
        return PhHokkien.locale_weight(_aliases[syn])

    @staticmethod
    def pron_locales() -> Iterator[str]:
        for loc in _hokkien_pron_locales:
            yield loc

    @staticmethod
    def syn_locales() -> Iterator[str]:
        for loc in _syn_hokkien_locales:
            yield loc
