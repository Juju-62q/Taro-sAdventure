import getpass
import pygame
from ScrollGame.ScrollGame import ScrollGame
from Ranking.Ranking import Ranking
from PyGameScreen import PyGameScreen
from pygame.locals import *
import json,requests

class MainMenu(PyGameScreen):

    def __init__(self, width, height, surface, fpsClock):
        super().__init__(width, height, surface, fpsClock)


    def mainMenu(self):
        # 描画用初期設定
        sysFont = pygame.font.SysFont(None, 50)
        titleFont = pygame.font.SysFont(None, 100)
        scoreFont = pygame.font.SysFont(None, 36)
        blue = (0, 0, 255)
        white = (255, 255, 255)
        glay = (51, 51, 51)

        play = sysFont.render("PLAY", True, white)
        playWidth, playHeight = sysFont.size("PLAY")
        rank = sysFont.render("RANKING", True, white)
        rankWidth, rankHeight = sysFont.size("RANKING")
        title = titleFont.render("Taro's Adventure", True, (255, 0, 0))
        userName = getpass.getuser()

        renderedFlag = False
        click = "DEFAULT"

        while (1):
            #イベント処理
            for event in pygame.event.get():
                # マウスポインタの位置を取る
                if event.type == MOUSEMOTION:
                    x, y = event.pos
                    renderedFlag = False
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
                    elif 200 <= x <= 200 + rankWidth and 320 <= y <= 320 + rankHeight:
                        click = "RANKING"

                if event.type == QUIT:
                    pygame.quit()
                    exit()

            if(not renderedFlag):

                highScoreDict = self.getHighScore()
                highScoreString = "{} : {}".format(highScoreDict['name'], highScoreDict['score'])
                highScoreStringWidth, _ = scoreFont.size(highScoreString)
                scoreX = self.width - highScoreStringWidth - 50
                highScore = scoreFont.render(highScoreString, True, white)

                userHighScoreDict = self.getUserHighScore(userName)
                userHighScoreString = "{} : {}".format(userName, userHighScoreDict['score'])
                userHighScoreStringWidth, _ = scoreFont.size(userHighScoreString)
                uscoreX = self.width - userHighScoreStringWidth - 50
                userHighScore = scoreFont.render(userHighScoreString, True, white)

                self.surface.fill(glay)
                self.surface.blit(title, (120, 150))
                self.surface.blit(play, (200, 250))
                self.surface.blit(rank, (200, 320))
                self.surface.blit(highScore, (scoreX, 450))
                self.surface.blit(userHighScore, (uscoreX, 500))
                pygame.display.update()
                renderedFlag = True

            else:
                if click == "PLAY":
                    scrollGame = ScrollGame(self.width, self.height, self.surface, self.fpsClock)
                    scrollGame.gamePlay()
                    renderedFlag = False
                    click = "DEFAULT"
                elif click == "RANKING":
                    ranking = Ranking(self.width, self.height, self.surface, self.fpsClock)
                    ranking.Ranking()
                    renderedFlag = False
                    click = "DEFAULT"


    def getHighScore(self):
        url = "http://localhost/api/highScore"
        responseBody = requests.get(url)

        resultDict = json.loads(responseBody.content)

        if (resultDict['status'] != "OK"):
            raise Exception

        return resultDict['result']


    def getUserHighScore(self, name):
        url = "http://localhost/api/getUserHighScore"
        data = '{{"name":"{}"}}'.format(name)
        responseBody = requests.post(url, data)

        resultDict = json.loads(responseBody.content)

        if (resultDict['status'] != "OK"):
            raise Exception

        return resultDict['result']

if __name__ == '__main__':
    pygame.init()
    pygame.key.set_repeat(5, 5)
    width = 800
    height = 600
    surface = pygame.display.set_mode((width, height))
    fpsClock = pygame.time

    play = MainMenu(width, height, surface, fpsClock)
    play.mainMenu()
