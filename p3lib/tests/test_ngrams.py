import sys
sys.path.append('../')

import unittest
from ngrams import ngrams


class TestNgrams(unittest.TestCase):
    def test_emptystr(self):
        self.assertEqual([], list(ngrams('', 2)))

    def test_not_string(self):
        with self.assertRaises(TypeError):
            list(ngrams(None, 2))

    def test_unigram(self):
        s = '空山不見人'
        expected = ['空', '山', '不', '見', '人']
        actual = [''.join(unigram) for unigram in list(ngrams(s, 1))]
        self.assertEqual(expected, actual)

    def test_bigram(self):
        s = '空山不見人'
        expected = ['空山', '山不', '不見', '見人']
        actual = [''.join(bigram) for bigram in list(ngrams(s, 2))]
        self.assertEqual(expected, actual)

    def test_trigram(self):
        s = '空山不見人'
        expected = ['空山不', '山不見', '不見人']
        actual = [''.join(bigram) for bigram in list(ngrams(s, 3))]
        self.assertEqual(expected, actual)

    def test_bigram_list(self):
        words = ['the', 'woods', 'are', 'lovely', 'dark', 'and', 'deep']
        expected = ['the woods', 'woods are', 'are lovely', 'lovely dark', 'dark and', 'and deep']
        actual = [' '.join(bigram) for bigram in list(ngrams(words, 2))]
        self.assertEqual(expected, actual)
