class Game():
    
    def __init__(self, *args, **kwargs):
        self._rolls = []
    
    def roll(self, pins):
        self._rolls.append(pins)
    
    def score(self):
        score = 0
        roll = 0
        for frame in range(10):
            if (self._frameScore(roll) == 10):
                score += 10 + self._rolls[roll+2]
            else:
                score += self._frameScore(roll)
            roll += 2
        return score

    def _frameScore(self, roll):
        return self._rolls[roll] + self._rolls[roll+1]


    