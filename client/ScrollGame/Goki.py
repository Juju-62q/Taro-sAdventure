from pygame.locals import Rect
from random import randint

class Goki:

    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        safeZone = 10
        self._hitZone = Rect(x + safeZone, y + safeZone, width - safeZone * 2, height - safeZone * 2)
        self._moveSpeed = randint(2,5)

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

    @property
    def hitZone(self):
        return self._hitZone

    @hitZone.setter
    def hitZone(self, hitZone):
        self._hitZone = hitZone

    @property
    def moveSpeed(self):
        return self._moveSpeed

    @moveSpeed.setter
    def moveSpeed(self, moveSpeed):
        self._moveSpeed = moveSpeed

    def moveGoki(self):
        if randint(0, 100) == 0:
            self.moveSpeed = randint(2,5)
        self.x -= self.moveSpeed
        self.hitZone = self.hitZone.move(- self.moveSpeed, 0)
        return self
