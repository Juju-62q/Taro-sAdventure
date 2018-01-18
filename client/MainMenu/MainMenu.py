import sys,os
sys.path.append(os.getcwd())
import socket, getpass
import pygame
from ScrollGame.ScrollGame import ScrollGame
from Ranking.Ranking import Ranking
from PyGameScreen import PyGameScreen
from pygame.locals import *

class MainMenu(PyGameScreen):

    def __init__(self, width, height, surface, fpsClock):
        super().__init__(width, height, surface, fpsClock)
        self.surface.fill((0, 0, 0))


    def mainMenu(self):
        # 描画用初期設定
        sysFont = pygame.font.SysFont(None, 36)
        play = sysFont.render("PLAY", True, (255, 255, 255))
        playWidth, playHeight = sysFont.size("PLAY")
        rank = sysFont.render("RANKING", True, (255, 255, 255))
        rankWidth, rankHeight = sysFont.size("RANKING")
        title = sysFont.render("Dodge Cockroach", True, (255, 0, 0))
        userName = getpass.getuser()

        # ソケット通信
        #client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #client.connect(("127.0.0.1", 50000))
        #client.send("1".encode("ascii"))
        allHighScore = "test 10000"#client.recv(4096).decode("ascii")
        allHighScore = allHighScore.replace(" ", " : ")
        highScore = sysFont.render("{0}".format(allHighScore), True, (255, 255, 255))

        #client.send("2".encode("ascii"))
        #temp = client.recv(4096) #"Connected"
        #client.send(userName.encode("ascii"))
        userHighScore = "10000"#client.recv(4096).decode("ascii")
        userScore = userName + " : " + userHighScore
        user = sysFont.render(userScore, True, (255, 255, 255))

        flag = False

        #client.close()

        while (1):
            #self.checkQuit()
            if(not flag):
                self.surface.blit(title, (200, 200))
                self.surface.blit(play, (200, 250))
                self.surface.blit(rank, (200, 300))
                self.surface.blit(highScore, (500, 450))
                self.surface.blit(user, (500, 500))
                pygame.display.update()

                for event in pygame.event.get():
                    #マウスポインタの位置を取る
                    if event.type == MOUSEMOTION:
                        x, y = event.pos
                        if 200 <= x <= 200 + playWidth and 250 <= y <= 250 + playHeight:
                            play = sysFont.render("PLAY", True, (255, 0, 0))
                        elif 200 <= x <= 200 + rankWidth and 300 <= y <= 300 + rankHeight:
                            rank = sysFont.render("RANKING", True, (255, 0, 0))
                        else:
                            play = sysFont.render("PLAY", True, (255, 255, 255))
                            rank = sysFont.render("RANKING", True, (255, 255, 255))

                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        x, y = event.pos
                        if 200 <= x <= 200 + playWidth and 250 <= y <= 250 + playHeight:
                            click = "PLAY"
                            flag = True
                        elif 200 <= x <= 200 + rankWidth and 300 <= y <= 300 + rankHeight:
                            click = "RANKING"
                            flag = True

                    if event.type == QUIT:
                        pygame.quit()
                        exit()

                #flag = True
            #pressedKey = pygame.key.get_pressed()
            #if pressedKey[pygame.K_s]:
            else:
                if click == "PLAY":
                    scrollGame = ScrollGame(self.width, self.height, self.surface, self.fpsClock)
                    scrollGame.gamePlay()
                    self.surface.fill((0, 0, 0))
                    flag = False
            #elif pressedKey[pygame.K_r]:
                elif click == "RANKING":
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
