import pygame
from pygame.locals import QUIT,Rect

class PyGameScreen:

    def __init__(self, width, height, surface, fpsClock):
        # pygame and window initialize
        self.width = width
        self.height = height
        self.surface = surface
        self.fpsClock = fpsClock

    def checkQuit(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()