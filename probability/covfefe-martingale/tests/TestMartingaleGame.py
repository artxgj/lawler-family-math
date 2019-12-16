import string
import sys
import unittest
from covfefe_martingale import MartingaleGambler, PlayerAdmission, MartingaleGame, MartingaleGameConfiguration

sys.path.append('../')


class TestMartingaleGame(unittest.TestCase):
    @staticmethod
    def _calc_total_winnings(winners):
        total = 0
        for winner in winners:
            total += winner.cash

        return total

    def test_HHHH(self):
        player_admission = PlayerAdmission(MartingaleGambler, 1)
        game_config = MartingaleGameConfiguration('HHHH', 'HT')
        game = MartingaleGame(player_admission, game_config)
        winners = game.run()
        expected = 30
        self.assertEqual(expected, self._calc_total_winnings(winners))

    def test_HHHT(self):
        player_admission = PlayerAdmission(MartingaleGambler, 1)
        game_config = MartingaleGameConfiguration('HHHT', 'HT')
        game = MartingaleGame(player_admission, game_config)
        winners = game.run()
        expected = 16
        self.assertEqual(expected, self._calc_total_winnings(winners))

    def test_HHTH(self):
        player_admission = PlayerAdmission(MartingaleGambler, 1)
        game_config = MartingaleGameConfiguration('HHTH', 'HT')
        game = MartingaleGame(player_admission, game_config)
        winners = game.run()
        expected = 18
        self.assertEqual(expected, self._calc_total_winnings(winners))

    def test_covfefe(self):
        player_admission = PlayerAdmission(MartingaleGambler, 1)
        game_config = MartingaleGameConfiguration('COVFEFE', string.ascii_uppercase)
        game = MartingaleGame(player_admission, game_config)
        winners = game.run()
        expected = 26**7
        self.assertEqual(expected, self._calc_total_winnings(winners))

    def test_abradacadabra(self):
        player_admission = PlayerAdmission(MartingaleGambler, 1)
        game_config = MartingaleGameConfiguration('ABRACADABRA', string.ascii_uppercase)
        game = MartingaleGame(player_admission, game_config)
        winners = game.run()
        expected = 26**11 + 26**4 + 26
        self.assertEqual(expected, self._calc_total_winnings(winners))
