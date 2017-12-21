import pygame
from ScrollGame.ScrollGame import ScrollGame
from Ranking.Ranking import Ranking
from pygame.locals import QUIT

class MainMenu:

    def __init__(self, width, height):
        self.width = width
        self.height = height

        # init pygame and window
        pygame.init()
        pygame.key.set_repeat(5, 5)
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.fpsClock = pygame.time.Clock()

    def checkQuit(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

    def mainMenu(self):
        sysFont = pygame.font.SysFont(None, 36)
        play = sysFont.render("please press s to play", True, (255, 255, 255))
        rank = sysFont.render("please press r to ranking", True, (255, 255, 255))
        flag = False

        while (1):
            if(not flag):
                self.surface.blit(play, (200, 250))
                self.surface.blit(rank, (200, 300))
                pygame.display.update()
                flag = True
            self.checkQuit()
            pressedKey = pygame.key.get_pressed()
            if pressedKey[pygame.K_s]:
                scrollGame = ScrollGame(self.width, self.height, 10, self.surface, self.fpsClock)
                scrollGame.gamePlay()
                self.surface.fill((0, 0, 0))
                flag = False
            elif pressedKey[pygame.K_r]:
                ranking = Ranking(self.width, self.height, self.surface, self.fpsClock)
                ranking.Ranking()
                self.surface.fill((0, 0, 0))
                flag = False


if __name__ == '__main__':
    play = MainMenu(800, 600)
    play.mainMenu()
