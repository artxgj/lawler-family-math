import sys
import unittest
from covfefe_martingale import MartingaleGambler, PlayerAdmission

sys.path.append('../')


class TestPlayerAdmission(unittest.TestCase):
    def test_player_admit(self):
        admission = PlayerAdmission(MartingaleGambler, 1)
        player = admission.admit()
        self.assertTrue(isinstance(player, MartingaleGambler))
