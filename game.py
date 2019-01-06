class Game():
    
    def __init__(self, *args, **kwargs):
        self._rolls = []
    
    def roll(self, pins):
        self._rolls.append(pins)
    
    def score(self):
        score = 0
        roll = 0
        for frame in range(10):
            if (self._isStrike(roll)):
                score += 10 + self._strikeBonus(roll)
                roll += 1
            elif (self._isSpare(roll)):
                score += 10 + self._spareBonus(roll)
                roll += 2
            else:
                score += self._frameScore(roll)
                roll += 2
        return score

    def _isStrike(self, roll):
        return self._rolls[roll] == 10

    def _strikeBonus(self, roll):
        return self._rolls[roll+1] + self._rolls[roll+2]

    def _isSpare(self, roll):
        return self._frameScore(roll) == 10

    def _spareBonus(self, roll):
        return self._rolls[roll+2]

    def _frameScore(self, roll):
        return self._rolls[roll] + self._rolls[roll+1]


    