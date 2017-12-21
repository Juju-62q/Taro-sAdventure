import pygame
from pygame.locals import QUIT

class Ranking:

    def __init__(self, width, height, surface, fpsClock):
        # pygame and window initialize
        self.width = width
        self.height = height
        self.surface = surface
        self.fpsClock = fpsClock
        self.surface.fill((0, 0, 0))

    def checkQuit(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

    def Ranking(self):
        # TODO
        sysFont = pygame.font.SysFont(None, 36)
        tmp = sysFont.render("please press backspace to back menu", True, (255, 255, 255))
        self.surface.blit(tmp, (200, 300))
        pygame.display.update()

        while (1):
            self.checkQuit()
            pressedKey = pygame.key.get_pressed()
            if pressedKey[pygame.K_BACKSPACE]:
                break