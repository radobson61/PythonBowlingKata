class Game():
    
    def __init__(self, *args, **kwargs):
        self._score = 0
    
    def roll(self, pins):
        self._score += pins
    
    def score(self):
        return self._score 