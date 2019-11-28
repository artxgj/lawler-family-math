import unittest
import sys
from zhtopolects import MandarinTopolect

sys.path.append('../')


class TestMandarinTopolect(unittest.TestCase):
    def test_single_simple_pron(self):
        dial_prons = 'màikèfēng'
        actual = MandarinTopolect.parse_dialect_pron(dial_prons)
        expected = {'màikèfēng'}
        self.assertTrue(actual == expected)

    def test_multiple_simple_prons(self):
        dial_prons = 'nānzǐ,nānzi'
        actual = MandarinTopolect.parse_dialect_pron(dial_prons)
        expected = {'nānzǐ',
                    'nānzi'}
        self.assertTrue(actual == expected)

    def test_single_pron_with_info(self):
        dial_prons = 'pūkè,er=y,tl=y'
        actual = MandarinTopolect.parse_dialect_pron(dial_prons)
        expected = {'pūkè'}
        self.assertTrue(actual == expected)

    def test_multiple_prons_with_info(self):
        dial_prons = 'mántou,mántóu,1nb=standard in Mainland and Taiwan,2nb=literary or regional variant'
        actual = MandarinTopolect.parse_dialect_pron(dial_prons)
        expected = {'mántou',
                    'mántóu'}
        self.assertTrue(actual == expected)

    def test_comment_removed(self):
        dial_prons = 'zhē,zhě<!--tag needed-->'
        actual = MandarinTopolect.parse_dialect_pron(dial_prons)
        expected = {'zhē', 'zhě'}
        self.assertTrue(actual == expected)
