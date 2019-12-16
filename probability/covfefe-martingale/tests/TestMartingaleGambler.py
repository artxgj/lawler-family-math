import sys
import unittest
from covfefe_martingale import MartingaleGambler
sys.path.append('../')


class TestMartingaleGambler(unittest.TestCase):
    def test_wager(self):
        expected = 101
        gambler = MartingaleGambler(expected)
        actual = gambler.cash
        self.assertEqual(expected, actual)

    def test_wins(self):
        gambler = MartingaleGambler(1)
        win_returns = 10

        for _ in range(3):
            gambler.wins(gambler.wager*win_returns)

        expected = 1000
        self.assertEqual(expected, gambler.cash)

    def test_play(self):
        gambler = MartingaleGambler(1)
        win_returns = 10

        for _ in range(5):
            gambler.wins(gambler.wager*win_returns)

        expected = 5
        actual = gambler.play
        self.assertEqual(expected, actual)

