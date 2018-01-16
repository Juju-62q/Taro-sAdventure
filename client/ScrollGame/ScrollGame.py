from random import randint
import pygame
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
        self.player = Player(0, height / 2, 44, 70, pygame.image.load("GameContents/boy.png"), 157, pygame.image.load("GameContents/boy_killing.png"), 5)

        # for enemy
        self.gokis = []
        self.gokiImage = pygame.image.load("GameContents/goki.png")

        # for play zone
        self.playerZoneAbove = self.height / 6
        self.playerZoneBottom = self.height * 5 / 6

        # for score
        self.score = Score(0, 1, 100, 600, 20)

        # for Images
        self.sysFont = pygame.font.SysFont(None, 36)
        self.bangImage = pygame.image.load("GameContents/bang.png")
        self.backGround = pygame.image.load("GameContents/block.jpg")
        self.playZone = pygame.image.load("GameContents/playzone.png")

    def tutrial(self):
        self.surface.fill((155, 155, 155))

        tutrial = self.sysFont.render("TUTRIAL", True, (0, 0, 0))
        self.surface.blit(tutrial, (340, 30))

        moveDescribe = self.sysFont.render("1.Avoid the cockroaches by moving with direction keys", True, (0, 0, 0))
        self.surface.blit(moveDescribe, (75, 100))
        self.surface.blit(self.player.getImage(), (200, 150))
        self.surface.blit(self.gokiImage, (500, 160))

        insecticideDescribe = self.sysFont.render("2.You can use insecticide by pressing Z (3 times)", True, (0, 0, 0))
        self.surface.blit(insecticideDescribe, (75, 250))
        self.surface.blit(pygame.image.load("GameContents/boy_killing.png"), (200, 300))
        self.surface.blit(self.gokiImage, (400, 310))

        difficultyDescribe = self.sysFont.render("3.The degree of difficulty will gradually rise", True, (0, 0, 0))
        self.surface.blit(difficultyDescribe, (75, 400))
        self.surface.blit(self.player.getImage(), (200, 450))
        self.surface.blit(self.gokiImage, (400, 440))
        self.surface.blit(self.gokiImage, (500, 470))
        self.surface.blit(self.gokiImage, (450, 490))

        gameStart = self.sysFont.render("Press Enter to start game", True, (0, 0, 0))
        self.surface.blit(gameStart, (230, 550))

        pygame.display.update()

        while (1):
            self.checkQuit()
            pressedKey = pygame.key.get_pressed()
            if pressedKey[pygame.K_RETURN]:
                break


    def gamePlay(self):
        self.tutrial()

        # for game over
        gameOver = False

        # main loutine
        while not gameOver:
            self.checkQuit()

            # check game over
            gameOver = self.isGameOver()

            # paint back ground
            self.surface.blit(self.backGround, (0, 0))

            # paint player zone
            self.surface.blit(self.playZone, (0, self.playerZoneAbove))

            # make goki
            probability = 60 - int(self.score.score / 200)
            if randint(0, probability if probability > 20 else 20) == 0:
                gokiHeight = 50
                gokiWidth = 64
                goki = Goki(self.width - gokiWidth, randint(self.playerZoneAbove, self.playerZoneBottom - gokiHeight), gokiWidth, gokiHeight)
                self.gokis.append(goki)

            # delete if not used
            for i in range(len(self.gokis) - 2):
                if self.gokis[i].x <= - gokiWidth:
                    del self.gokis[i]

            # move enemies
            self.gokis = [goki.moveGoki() for goki in self.gokis]

            # paint enemiess
            for goki in self.gokis:
                self.surface.blit(self.gokiImage, (goki.x, goki.y))

            # update player
            pressedKey = pygame.key.get_pressed()
            self.player.movePlayer(pressedKey, self.width, self.playerZoneAbove, self.playerZoneBottom)
            self.player.updatePlayerImage(pressedKey)
            self.surface.blit(self.player.getImage(), (self.player.rect.x, self.player.rect.y))

            # kill goki
            if self.player.killerFlag:
                self.checkKillGokis()

            # update score
            scoreImage = self.sysFont.render("score is {}".format(self.score.update()), True, (0, 0, 225))
            self.surface.blit(scoreImage, (self.score.x, self.score.y))

            # update display
            pygame.display.update()
            self.fpsClock.delay(3)

        self.gameOver()

        while(1):
            self.checkQuit()
            pressedKey = pygame.key.get_pressed()
            if pressedKey[pygame.K_RETURN]:
                break


    def isGameOver(self):
        for goki in self.gokis:
            if self.isTouchGoki(goki):
                return True
        return False

    def isTouchGoki(self, goki):
        return self.player.rect.x <= goki.hitZone.x + goki.hitZone.width \
               and self.player.rect.x + self.player.rect.width >= goki.hitZone.x \
               and self.player.rect.y <= goki.hitZone.y + goki.hitZone.height \
               and self.player.rect.y + self.player.rect.height >= goki.hitZone.y

    def checkKillGokis(self):
        for goki in self.gokis:
            if self.isKillGoki(goki):
                self.gokis.remove(goki)
                self.score.killedBornus()

    def isKillGoki(self, goki):
        return self.player.rect.x + self.player.rect.width <= goki.hitZone.x + goki.hitZone.width \
               and self.player.rect.x + self.player.rect.width + self.player.killerWidth >= goki.hitZone.x \
               and self.player.rect.y <= goki.hitZone.y + goki.hitZone.height \
               and self.player.rect.y + self.player.rect.height >= goki.hitZone.y

    def gameOver(self):
        rank = "01"#self.sendUserNameAndScore()

        self.surface.blit(self.bangImage, (self.player.rect.x, self.player.rect.y - 30))
        scoreResult = self.sysFont.render("score is {}".format(self.score.score), True, (255, 255, 255))
        Rank = self.sysFont.render("your rank was {}".format(rank), True, (255, 255, 255))
        backMenu = self.sysFont.render("please press enter to back menu", True, (255, 255, 255))
        self.surface.blit(scoreResult, (200, 250))
        self.surface.blit(Rank, (200, 300))
        self.surface.blit(backMenu, (200, 350))
        pygame.display.update()

    def sendUserNameAndScore(self):
        userName = getpass.getuser()
        sendData = "{0} {1}".format(userName, self.score.score).encode("ascii")
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("127.0.0.1", 50000))
        client.sendall(b'4')
        response = client.recv(4096)
        client.sendall(sendData)
        response = client.recv(4096)
        client.close()
        return response.decode("ascii")
