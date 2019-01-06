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
        self._rollMany(20, 0)
        self.assertEqual(0, self._target.score())

    def test_when_all_rolls_are_1_score_is_1(self):
        self._rollMany(20, 1)
        self.assertEqual(20, self._target.score())

    def test_when_a_spare_is_followed_by_3_score_is_16(self):
        self._rollSpare()
        self._target.roll(3)
        self._rollMany(17, 0)
        self.assertEqual(16, self._target.score())

    def _rollSpare(self):
        self._target.roll(5)
        self._target.roll(5) 
        
    def _rollMany(self, rolls, pins):
        for roll in range(rolls):
            self._target.roll(pins)


        