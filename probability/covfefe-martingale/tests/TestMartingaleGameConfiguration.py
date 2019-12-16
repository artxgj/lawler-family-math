import string
import sys
import unittest
from covfefe_martingale import MartingaleGameConfiguration

sys.path.append('../')


class TestMartingaleGameConfiguration(unittest.TestCase):
    def setUp(self) -> None:
        self._gamestr = 'COVFEFE'
        self._alphabet = string.ascii_uppercase
        self._game_config = MartingaleGameConfiguration(self._gamestr, self._alphabet)

    def test_state(self):
        actual = self._game_config.state(5)
        expected = self._gamestr[5]
        self.assertEqual(expected, actual)

    def test_win_value(self):
        bet = len(self._alphabet)
        expected = bet * bet
        actual = self._game_config.win_value(bet)
        self.assertEqual(expected, actual)

    def test_is_absorbent_state(self):
        expected = True
        actual = self._game_config.is_absorbent_state(len(self._gamestr))

    def test_exceptions(self):
        methods_args = [('state', len(self._alphabet)+1), ('is_absorbent_state', -1)]

        for method, arg in methods_args:
            with self.subTest(text=method):
                with self.assertRaises(ValueError):
                    getattr(self._game_config, method)(arg)

