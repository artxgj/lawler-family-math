import sys

sys.path.append('../')
import unittest
from utf8unicode import Utf8

class TestUtf8(unittest.TestCase):
    def test_single_char(self):
        single_chars = ['∑', 'K', '詩', '诗', '🖋']

        for c in single_chars:
            with self.subTest(testcase=single_chars):
                u = Utf8(c)
                self.assertEqual([ord(c)], u.codepoint())

    def test_string(self):
        strings = ['ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ', '空山新雨後', '空山新雨后', '🌤🌴🍹📚🎶🎧😎', 'Fountain pen 鋼筆 🖋']

        for s in strings:
            with self.subTest(testcase=strings):
                u = Utf8(s)
                expected = [ord(c) for c in s]
                self.assertEqual(expected, u.codepoint())

    def test_badmultibytes(self):
        with self.assertRaises(ValueError):
            u = Utf8(b'\x85\xf2')
            u.codepoint()
