import pygame
from pygame.locals import QUIT,Rect

class PyGameScreen:

    def __init__(self, width, height, surface, fpsClock):
        # pygame and window initialize
        self._width = width
        self._height = height
        self._surface = surface
        self._fpsClock = fpsClock

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def surface(self):
        return self._surface

    @surface.setter
    def surface(self, surface):
        self._surface = surface

    @property
    def fpsClock(self):
        return self._fpsClock

    @fpsClock.setter
    def fpsClock(self, fpsClock):
        self._fpsClock = fpsClock

    def checkQuit(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()