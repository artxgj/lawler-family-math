import sys
sys.path.append('../')

import unittest
from ngrams import cjk_ngrams

class TestNgrams(unittest.TestCase):
    def test_emptystr(self):
        self.assertEqual([], cjk_ngrams('', 2))

    def test_not_string(self):
        with self.assertRaises(TypeError):
            cjk_ngrams(None, 2)

    def test_bigram(self):
        s = '空山不見人'
        expected = ['空山', '山不', '不見', '見人']
        self.assertEqual(expected, cjk_ngrams(s, 2))

    def test_trigram(self):
        s = '空山不見人'
        expected = ['空山不', '山不見', '不見人']
        self.assertEqual(expected, cjk_ngrams(s, 3))
