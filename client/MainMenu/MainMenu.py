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
        glay = (51, 51, 51)
        self.surface.fill(glay)


    def mainMenu(self):
        # 描画用初期設定
        sysFont = pygame.font.SysFont(None, 50)
        titleFont = pygame.font.SysFont(None, 100)
        scoreFont = pygame.font.SysFont(None, 36)
        blue = (0, 0, 255)
        white = (255, 255, 255)

        play = sysFont.render("PLAY", True, white)
        playWidth, playHeight = sysFont.size("PLAY")
        rank = sysFont.render("RANKING", True, white)
        rankWidth, rankHeight = sysFont.size("RANKING")
        title = titleFont.render("Terra Formers", True, (255, 0, 0))
        userName = getpass.getuser()

        # ソケット通信 全体のハイスコア
        temp = ''
        while temp != 'connected': ##'connected'が返されるまで再送
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host = 'localhost' #適宜変更
            port = 59630       #ここも
            client.connect((host, port))
            client.send("1".encode("ascii"))
            temp = client.recv(4096).decode("ascii")#connected
            allHighScore = client.recv(4096)
            allHighScore = allHighScore.decode("ascii").replace('\x00','')
            #print(allHighScore)
            allHighScore = allHighScore.replace(" ", " : ")
            #print(allHighScore)
            aHSWidth, aHSHeight = scoreFont.size(allHighScore)
            scoreX = self.width - aHSWidth - 50 #ハイスコアのX座標を設定
            highScore = scoreFont.render("{0}".format(allHighScore), True, white)
            client.close()

        #ソケット通信　ユーザーハイスコア
        temp = ''
        while temp != 'connected': ##'connected'が返されるまで再送
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((host, port))
            client.sendall(b'2')
            temp = client.recv(4096).decode("ascii")#"Connected"
            #print(temp)
            client.sendall(userName.encode("ascii"))
            userHighScore = client.recv(4096).decode("ascii")
            userScore = userName + " : " + userHighScore
            user = scoreFont.render(userScore, True, white)
            #print(userHighScore)
            client.close()

        flag = False

        while (1):
            #self.checkQuit()
            if(not flag):
                self.surface.blit(title, (170, 150))
                self.surface.blit(play, (200, 250))
                self.surface.blit(rank, (200, 320))
                self.surface.blit(highScore, (scoreX, 450))
                self.surface.blit(user, (scoreX, 500))
                pygame.display.update()

                for event in pygame.event.get():
                    #マウスポインタの位置を取る
                    if event.type == MOUSEMOTION:
                        x, y = event.pos
                        if 200 <= x <= 200 + playWidth and 250 <= y <= 250 + playHeight:
                            play = sysFont.render("PLAY", True, blue)
                        elif 200 <= x <= 200 + rankWidth and 320 <= y <= 320 + rankHeight:
                            rank = sysFont.render("RANKING", True, blue)
                        else:
                            play = sysFont.render("PLAY", True, white)
                            rank = sysFont.render("RANKING", True, white)

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
