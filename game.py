class Game():
    
    def __init__(self, *args, **kwargs):
        self._rolls = []
    
    def roll(self, pins):
        self._rolls.append(pins)
    
    def score(self):
        score = 0
        roll = 0
        for frame in range(10):
            score += self.newmethod947(roll)
        return score

    def newmethod947(self, roll):
        return self._rolls[roll] + self._rolls[roll+1]

    