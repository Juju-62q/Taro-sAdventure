import pygame
from pygame.locals import Rect

class Player:

    def __init__(self, x, y, width, height, image, move):
        self._rect = Rect(x, y, width, height)
        self._image = image
        self._move = move

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, rect):
        self._rect = rect

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        self._image = image

    @property
    def move(self):
        return self._move

    @move.setter
    def move(self, move):
        self._move = move

    def movePlayer(self, pressedKey, fieldWidth):
        if pressedKey[pygame.K_UP]:
            self.rect.y -= self.move
        elif pressedKey[pygame.K_DOWN]:
            self.rect.y += self.move
        if pressedKey[pygame.K_RIGHT]:
            self.rect.x += self.move if self.rect.x < fieldWidth - self.rect.width else 0
        elif pressedKey[pygame.K_LEFT]:
            self.rect.x -= self.move if self.rect.x > 0 else 0