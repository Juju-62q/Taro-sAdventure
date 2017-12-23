
class Score:

    def __init__(self, score, scoreUpdate, x, y):
        self._score = score
        self._scoreUpdate = scoreUpdate
        self._x = x
        self._y = y

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    @property
    def scoreUpdate(self):
        return self._scoreUpdate

    @scoreUpdate.setter
    def scoreUpdate(self, scoreUpdate):
        self._scoreUpdate = scoreUpdate

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    def update(self):
        self.score += self.scoreUpdate
        return self.score
