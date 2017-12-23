from random import randint
import pygame
from pygame.locals import QUIT,Rect
from PyGameScreen import PyGameScreen

class ScrollGame(PyGameScreen):

    def __init__(self, width, height, surface, fpsClock, baseSize):
        super().__init__(width, height, surface, fpsClock)

        # game initialize
        # for player
        self.playerX = 0
        self.playerY = self.height / 2

        # for enemy
        self.effects = []
        self.baseSize = baseSize

        # for play zone
        self.playerZoneAbove = self.height / 6
        self.playerZoneBottom = self.height * 2 / 3

    def gamePlay(self):
        # for score
        score = 0
        scoreUpdate = 10
        scorePosX = 600
        scorePosY = 20

        # for Images
        sysFont = pygame.font.SysFont(None, 36)
        playerImage = pygame.image.load("GameContents/ship.png")
        bangImage = pygame.image.load("GameContents/bang.png")

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
            self.effects.append(edge)

            # delete if not used
            if len(self.effects) >= self.width / self.baseSize:
                del self.effects[0]

            # move enemies
            self.effects = [x.move(- self.baseSize, 0) for x in self.effects]

            # paint enemies
            for effect in self.effects:
                pygame.draw.rect(self.surface, (255, 255, 0), effect)

            # update player
            pressedKey = pygame.key.get_pressed()
            self.movePlayer(pressedKey)
            self.surface.blit(playerImage, (self.playerX, self.playerY))

            # update score
            score += scoreUpdate
            scoreImage = sysFont.render("score is {}".format(score),True,(0,0,225))
            self.surface.blit(scoreImage,(scorePosX,scorePosY))


            pygame.display.update()
            self.fpsClock.tick(15)

        # TODO score
        self.surface.blit(bangImage, (self.playerX, self.playerY - 40))
        scoreImage = sysFont.render("score is {}".format(score), True, (255, 255, 255))
        tmp = sysFont.render("please press enter to back menu", True, (255, 255, 255))
        self.surface.blit(scoreImage, (200, 250))
        self.surface.blit(tmp, (200, 300))
        pygame.display.update()

        while(1):
            self.checkQuit()
            pressedKey = pygame.key.get_pressed()
            if pressedKey[pygame.K_RETURN]:
                break


    def isGameOver(self):
        if(self.playerY <= self.playerZoneAbove or self.playerY >= self.playerZoneBottom + 40):
            return True
        for effect in self.effects:
            if self.isTouchEnemy(effect):
                return True
        return False

    def isTouchEnemy(self, effect):
        return self.playerX <= effect.left and self.playerX + 75 >= effect.left and self.playerY + 10 <= effect.top and self.playerY + 50 >= effect.top

    def movePlayer(self, pressedKey):
        if pressedKey[pygame.K_UP]:
            self.playerY -= self.baseSize * 2
        elif pressedKey[pygame.K_DOWN]:
            self.playerY += self.baseSize * 2
        if pressedKey[pygame.K_RIGHT]:
            self.playerX += self.baseSize * 2 if self.playerX < self.width - 100 else 0
        elif pressedKey[pygame.K_LEFT]:
            self.playerX -= self.baseSize * 2 if self.playerX > 0 else 0

