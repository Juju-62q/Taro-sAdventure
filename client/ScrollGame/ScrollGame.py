from random import randint
import pygame
from pygame.locals import Rect
from PyGameScreen import PyGameScreen
from ScrollGame.Player import Player
from ScrollGame.Score import Score

class ScrollGame(PyGameScreen):

    def __init__(self, width, height, surface, fpsClock, baseSize):
        super().__init__(width, height, surface, fpsClock)

        # game initialize
        # for player
        self.player = Player(0, height/2, 90, 60, pygame.image.load("GameContents/ship.png"), 20)

        # for enemy
        self.enemies = []
        self.baseSize = baseSize

        # for play zone
        self.playerZoneAbove = self.height / 6
        self.playerZoneBottom = self.height * 2 / 3

        # for score
        self.score = Score(0, 10, 600, 20)

        # for Images
        self.sysFont = pygame.font.SysFont(None, 36)
        self.bangImage = pygame.image.load("GameContents/bang.png")

    def gamePlay(self):

        # for game over
        gameOver = False

        playerZone = Rect(0, self.playerZoneAbove, self.width, self.playerZoneBottom)

        # main loutine
        while not gameOver:
            self.checkQuit()

            # check game over
            gameOver = self.isGameOver()

            # paint back ground
            self.surface.fill((103,65,49))

            # paint player zone
            pygame.draw.rect(self.surface,(0,0,0),playerZone)

            # make enemies
            edge = Rect(self.width - self.baseSize, randint(self.playerZoneAbove, self.playerZoneBottom - self.baseSize),
                        self.baseSize, self.baseSize) if randint(0, 5) == 0 else Rect(0, 0, 0, 0)
            self.enemies.append(edge)

            # delete if not used
            if len(self.enemies) >= self.width / self.baseSize:
                del self.enemies[0]

            # move enemies
            self.enemies = [x.move(- self.baseSize, 0) for x in self.enemies]

            # paint enemies
            for effect in self.enemies:
                pygame.draw.rect(self.surface, (255, 255, 0), effect)

            # update player
            pressedKey = pygame.key.get_pressed()
            self.player.movePlayer(pressedKey, self.width)
            self.surface.blit(self.player.image, (self.player.rect.x, self.player.rect.y))

            # update score
            scoreImage = self.sysFont.render("score is {}".format(self.score.update()), True, (0, 0, 225))
            self.surface.blit(scoreImage, (self.score.x, self.score.y))

            pygame.display.update()
            self.fpsClock.tick(15)

        self.gameOver()

        while(1):
            self.checkQuit()
            pressedKey = pygame.key.get_pressed()
            if pressedKey[pygame.K_RETURN]:
                break


    def isGameOver(self):
        if(self.player.rect.y <= self.playerZoneAbove or self.player.rect.y >= self.playerZoneBottom + 40):
            return True
        for effect in self.enemies:
            if self.isTouchEnemy(effect):
                return True
        return False

    def isTouchEnemy(self, effect):
        return self.player.rect.x <= effect.left \
               and self.player.rect.x + 90 >= effect.left \
               and self.player.rect.y + 10 <= effect.top \
               and self.player.rect.y + 50 >= effect.top

    def gameOver(self):
        self.surface.blit(self.bangImage, (self.player.rect.x, self.player.rect.y - 30))
        scoreImage = self.sysFont.render("score is {}".format(self.score.score), True, (255, 255, 255))
        tmp = self.sysFont.render("please press enter to back menu", True, (255, 255, 255))
        self.surface.blit(scoreImage, (200, 250))
        self.surface.blit(tmp, (200, 300))
        pygame.display.update()

