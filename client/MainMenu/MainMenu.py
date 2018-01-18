import os, sys
sys.path.append(os.getcwd())

import pygame
from ScrollGame.ScrollGame import ScrollGame
from Ranking.Ranking import Ranking
from PyGameScreen import PyGameScreen

class MainMenu(PyGameScreen):

    def __init__(self, width, height, surface, fpsClock):
        super().__init__(width, height, surface, fpsClock)
        self.surface.fill((0, 0, 0))

    def mainMenu(self):
        sysFont = pygame.font.SysFont(None, 36)
        play = sysFont.render("please press s to play", True, (255, 255, 255))
        rank = sysFont.render("please press r to ranking", True, (255, 255, 255))
        flag = False

        while (1):
            self.checkQuit()
            if(not flag):
                self.surface.blit(play, (200, 250))
                self.surface.blit(rank, (200, 300))
                pygame.display.update()
                flag = True
            pressedKey = pygame.key.get_pressed()
            if pressedKey[pygame.K_s]:
                scrollGame = ScrollGame(self.width, self.height, self.surface, self.fpsClock, 10)
                scrollGame.gamePlay()
                self.surface.fill((0, 0, 0))
                flag = False
            elif pressedKey[pygame.K_r]:
                ranking = Ranking(self.width, self.height, self.surface, self.fpsClock)
                ranking.Ranking()
                self.surface.fill((0, 0, 0))
                flag = False


if __name__ == '__main__':
    pygame.init()
    pygame.key.set_repeat(5, 5)
    width = 800
    height = 600
    surface = pygame.display.set_mode((width, height))
    fpsClock = pygame.time

    play = MainMenu(width, height, surface, fpsClock)
    play.mainMenu()
