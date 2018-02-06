import pygame
from pygame.locals import Rect

class Player:

    def __init__(self, x, y, width, height, normalImage, killerWidth, killerImage, move):
        self._rect = Rect(x, y, width, height)
        self._normalImage = normalImage
        self._killerWidth = killerWidth
        self._killerImage = killerImage
        self._killerFlag = False
        self._killerCount = 3
        self._count = 0
        self._move = move

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, rect):
        self._rect = rect

    @property
    def killerWidth(self):
        return self._killerWidth

    @killerWidth.setter
    def killerWidth(self, killerWidth):
        self._killerWidth = killerWidth

    @property
    def killerFlag(self):
        return self._killerFlag

    @killerFlag.setter
    def killerFlag(self, killerFlag):
        self._killerFlag = killerFlag

    @property
    def killerCount(self):
        return self._killerCount

    @killerCount.setter
    def killerCount(self, killerCount):
        self._killerCount = killerCount

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count):
        self._count = count
    @property
    def move(self):
        return self._move

    @move.setter
    def move(self, move):
        self._move = move

    def getImage(self):
        return self._killerImage if self.killerFlag else self._normalImage

    def movePlayer(self, pressedKey, fieldWidth, fieldAbove, fieldBottom):
        if pressedKey[pygame.K_UP]:
            self.rect.y -= self.move if self.rect.y > fieldAbove else 0
        elif pressedKey[pygame.K_DOWN]:
            self.rect.y += self.move if self.rect.y < fieldBottom - self.rect.height else 0
        if pressedKey[pygame.K_RIGHT]:
            self.rect.x += self.move if self.rect.x < fieldWidth - self.rect.width else 0
        elif pressedKey[pygame.K_LEFT]:
            self.rect.x -= self.move if self.rect.x > 0 else 0

    def updatePlayerImage(self, pressedKey):
        if self.killerFlag:
            self.count += 1
        elif pressedKey[pygame.K_z] and self.killerCount > 0:
            self.killerCount -= 1
            self.count = 0
            self.killerFlag = True
        if self.count > 100:
            self.killerFlag = False