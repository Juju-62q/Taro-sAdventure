from pygame.locals import Rect

class Enemy():

    def __init__(self, baseSize):
        self._enemies = []
        self._baseSize = baseSize

    @property
    def baseSize(self):
        return self._baseSize

    @baseSize.setter
    def baseSize(self, baseSize):
        self._baseSize = baseSize