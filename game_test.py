import unittest
from game import Game

class Game_Tests(unittest.TestCase):

    def test_when_all_rolls_are_0_score_is_0(self):
        target = Game()
        for roll in range(20):
            target.roll(0)
        self.assertEqual(0, target.score())

    def test_when_all_rolls_are_1_score_is_1(self):
        target = Game()
        for roll in range(20):
            target.roll(1)
        self.assertEqual(20, target.score())


        