from random import randint
import pygame
from pygame.locals import Rect
from PyGameScreen import PyGameScreen
from ScrollGame.Player import Player
from ScrollGame.Score import Score
from ScrollGame.Goki import Goki
import socket,getpass

class ScrollGame(PyGameScreen):

    def __init__(self, width, height, surface, fpsClock):
        super().__init__(width, height, surface, fpsClock)

        # game initialize
        # for player
        self.player = Player(0, height / 2, 90, 60, pygame.image.load("GameContents/ship.png"), 5)

        # for enemy
        self.gokis = []
        self.gokiImage = pygame.image.load("GameContents/goki.png")

        # for play zone
        self.playerZoneAbove = self.height / 6
        self.playerZoneBottom = self.height * 5 / 6

        # for score
        self.score = Score(0, 1, 600, 20)

        # for Images
        self.sysFont = pygame.font.SysFont(None, 36)
        self.bangImage = pygame.image.load("GameContents/bang.png")
        self.image = pygame.image.load("GameContents/block.jpg")


    def gamePlay(self):

        # for game over
        gameOver = False

        playerZone = Rect(0, self.playerZoneAbove, self.width, self.playerZoneBottom - self.playerZoneAbove)

        # main loutine
        while not gameOver:
            self.checkQuit()

            # check game over
            gameOver = self.isGameOver()

            # paint back ground
            #self.surface.fill((103,65,49))
            self.surface.blit(self.image, (0, 0))

            # paint player zone
            pygame.draw.rect(self.surface,(255,255,255),playerZone)

            # make enemy
            if randint(0, 60) == 0:
                gokiHeight = 50
                gokiWidth = 64
                goki = Goki(self.width - gokiWidth, randint(self.playerZoneAbove, self.playerZoneBottom - gokiHeight), gokiWidth, gokiHeight, self.gokiImage, randint(2,5))
                self.gokis.append(goki)

            # delete if not used
            for i in range(len(self.gokis) - 2):
                if self.gokis[i].rect.x <= - gokiWidth:
                    del self.gokis[i]

            # move enemies
            self.gokis = [goki.moveGoki() for goki in self.gokis]

            # paint enemiess
            for goki in self.gokis:
                self.surface.blit(self.gokiImage, (goki.rect.x, goki.rect.y))
                #pygame.draw.rect(self.surface, (255, 255, 0), enemy)

            # update player
            pressedKey = pygame.key.get_pressed()
            self.player.movePlayer(pressedKey, self.width)
            self.surface.blit(self.player.image, (self.player.rect.x, self.player.rect.y))

            # update score
            scoreImage = self.sysFont.render("score is {}".format(self.score.update()), True, (0, 0, 225))
            self.surface.blit(scoreImage, (self.score.x, self.score.y))

            pygame.display.update()
            self.fpsClock.delay(5)

        self.gameOver()

        while(1):
            self.checkQuit()
            pressedKey = pygame.key.get_pressed()
            if pressedKey[pygame.K_RETURN]:
                break


    def isGameOver(self):
        if(self.player.rect.y <= self.playerZoneAbove or self.player.rect.y >= self.playerZoneBottom - 40):
            return True
        for effect in self.gokis:
            if self.isTouchEnemy(effect):
                return True
        return False

    def isTouchEnemy(self, enemy):
        return self.player.rect.x <= enemy.rect.left \
               and self.player.rect.x + 90 >= enemy.rect.left \
               and self.player.rect.y + 10 <= enemy.rect.top \
               and self.player.rect.y + 50 >= enemy.rect.top

    def gameOver(self):
        userName = getpass.getuser()

        #client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #client.connect(("127.0.0.1", 50000))
        #client.sendall(b"python test\r\n")
        #response = client.recv(4096)
        #client.sendall(b"python test222\r\n")
        #response = client.recv(4096)
        #client.close()


        self.surface.blit(self.bangImage, (self.player.rect.x, self.player.rect.y - 30))
        scoreImage = self.sysFont.render("score is {}".format(self.score.score), True, (255, 255, 255))
        tmp = self.sysFont.render("please press enter to back menu", True, (255, 255, 255))
        self.surface.blit(scoreImage, (200, 250))
        self.surface.blit(tmp, (200, 300))
        pygame.display.update()

