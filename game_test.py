import unittest
from game import Game

class Game_Tests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self._target = Game()
        super().__init__(*args, **kwargs)

    def setUp(self):
        self._target = Game()

    def tearDown(self):
        self._target = None

    def test_when_all_rolls_are_0_score_is_0(self):
        for roll in range(20):
            self._target.roll(0)
        self.assertEqual(0, self._target.score())

    def test_when_all_rolls_are_1_score_is_1(self):
        for roll in range(20):
            self._target.roll(1)
        self.assertEqual(20, self._target.score())


        