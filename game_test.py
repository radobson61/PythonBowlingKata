import unittest
from game import Game

class Game_Tests(unittest.TestCase):

    def test_when_all_rolls_are_0_score_is_0(self):
        target = Game()
        