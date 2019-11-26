import unittest
import sys
from zhtopolects import MinnanTopolect

sys.path.append('../')


class TestMinnanTopolect(unittest.TestCase):
    def test_only_pron(self):
        dial_pron = 'lîm'
        self.assertEqual(MinnanTopolect.parse_dialect_pron(dial_pron), {('lîm', 'all')})

    def test_only_prons_multiple(self):
        dial_prons = 'chúi/súi'
        self.assertEqual(MinnanTopolect.parse_dialect_pron(dial_prons), {('chúi', 'all'), ('súi',  'all')})

    def test_one_pron_many_locs(self):
        dial_prons = 'xm,zz,tw:thoah-thang'
        self.assertEqual(MinnanTopolect.parse_dialect_pron(dial_prons),
                         {('thoah-thang', 'xm'), ('thoah-thang', 'zz'), ('thoah-thang', 'tw')})

    def test_multiple_prons_many_locs(self):
        dial_prons = 'qz:lia̍k-sír/tw,xm,zz:le̍k-sú/jj,ph:lia̍k-sí'
        self.assertEqual(MinnanTopolect.parse_dialect_pron(dial_prons),
                         {('lia̍k-sír', 'qz'),
                          ('le̍k-sú', 'tw'), ('le̍k-sú', 'xm'), ('le̍k-sú', 'zz'),
                          ('lia̍k-sí', 'jj'), ('lia̍k-sí', 'ph')})

    def test_location_many_prons(self):
        dial_prons = 'qz,jj,ph:bîn-â/ph:mîn-â'
        self.assertEqual(MinnanTopolect.parse_dialect_pron(dial_prons),
                         {('bîn-â', 'qz'), ('bîn-â', 'jj'), ('bîn-â', 'ph'),
                          ('mîn-â', 'ph')})

    def test_ml_loc(self):
        dial_prons = 'ml:phah-chhùi-kó '
        expected = {('phah-chhùi-kó', 'qz'), ('phah-chhùi-kó', 'xm'), ('phah-chhùi-kó', 'zz')}
        self.assertTrue(MinnanTopolect.parse_dialect_pron(dial_prons) == expected)

    def test_ml_and_xm_loc(self):
        dial_prons = 'ml,twv:kha-thâu-hu/jj,xm,zz,tp,kh,tn,tc,hc,lk,yl,km,mg:kha-thâu-u/pn:kha-tâ-u'
        actual = MinnanTopolect.parse_dialect_pron(dial_prons)
        expected = {
            ('kha-thâu-hu', 'qz'), ('kha-thâu-hu', 'xm'), ('kha-thâu-hu', 'zz'), ('kha-thâu-hu', 'twv'),
            ('kha-thâu-u', 'xm'), ('kha-thâu-u', 'zz'),
            ('kha-thâu-u', 'jj'), ('kha-thâu-u', 'tp'),  ('kha-thâu-u', 'kh'), ('kha-thâu-u', 'tn'),
            ('kha-thâu-u', 'tc'), ('kha-thâu-u', 'hc'), ('kha-thâu-u', 'hc'), ('kha-thâu-u', 'lk'),
            ('kha-thâu-u', 'yl'), ('kha-thâu-u', 'km'), ('kha-thâu-u', 'mg'), ('kha-tâ-u', 'pn')
        }
        self.assertTrue(actual == expected)
