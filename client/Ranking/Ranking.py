import pygame
from PyGameScreen import PyGameScreen

class Ranking(PyGameScreen):

    def __init__(self, width, height, surface, fpsClock):
        super().__init__(width, height, surface, fpsClock)
        self.surface.fill((0, 0, 0))

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