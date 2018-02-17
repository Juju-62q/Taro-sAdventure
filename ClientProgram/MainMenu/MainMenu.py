import getpass
import pygame
from ScrollGame.ScrollGame import ScrollGame
from Ranking.Ranking import Ranking
from PyGameScreen import PyGameScreen
from pygame.locals import *
import urllib.request, json
import requests

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
        title = titleFont.render("Taro's Adventure", True, (255, 0, 0))
        userName = getpass.getuser()

        renderedFlag = False

        while (1):
            if(not renderedFlag):

                a = self.getHighScore()
                b = self.getUserHighScore(userName)
                self.surface.blit(title, (120, 150))
                self.surface.blit(play, (200, 250))
                self.surface.blit(rank, (200, 320))
                self.surface.blit(highScore, (scoreX, 450))
                self.surface.blit(user, (uscoreX, 500))
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
                        elif 200 <= x <= 200 + rankWidth and 320 <= y <= 320 + rankHeight:
                            click = "RANKING"
                            flag = True

                    if event.type == QUIT:
                        pygame.quit()
                        exit()

            else:
                if click == "PLAY":
                    scrollGame = ScrollGame(self.width, self.height, self.surface, self.fpsClock)
                    scrollGame.gamePlay()
                    self.surface.fill((0, 0, 0))
                    renderedFlag = False
                elif click == "RANKING":
                    ranking = Ranking(self.width, self.height, self.surface, self.fpsClock)
                    ranking.Ranking()
                    self.surface.fill((0, 0, 0))
                    renderedFlag = False


    def getHighScore(self):
        url = "http://localhost/api/highScore"
        responseBody = requests.get(url)

        resultDict = json.loads(responseBody.content)

        if (resultDict['status'] != "OK"):
            raise Exception

        return resultDict['result']


    def getUserHighScore(self, name):
        url = "http://localhost/api/getUserHighScore"
        data = {"name":"test"}
        responseBody = requests.post(url, data)

        resultDict = json.loads(responseBody)

        if (resultDict['status'] != "OK"):
            raise Exception

        b'<!DOCTYPE html>\n<html lang="en">\n    <head>\n        <meta charset="utf-8">\n        <title>Taro\'s Adventure Admin Application</title>\n        <meta name="viewport" content="width=device-width, initial-scale=1.0">\n<meta http-equiv="X-UA-Compatible" content="IE=edge">\n        <!-- Le styles-->\n        <link href="/css/bootstrap.min.css" media="screen" rel="stylesheet" type="text/css">\n<link href="/css/bootstrap-theme.min.css" media="screen" rel="stylesheet" type="text/css">\n<link href="/css/style.css" media="screen" rel="stylesheet" type="text/css">\n<link href="/img/favicon.ico" rel="shortcut icon" type="image/vnd.microsoft.icon">\n        <!-- Scripts -->\n        <script type="text/javascript" src="/js/jquery-3.1.0.min.js"></script>\n<script type="text/javascript" src="/js/bootstrap.min.js"></script>    </head>\n    <body>\n        <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">\n            <div class="container">\n                <!--<div class="navbar-header">\n                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\n                        <span class="icon-bar"></span>\n                        <span class="icon-bar"></span>\n                        <span class="icon-bar"></span>\n                    </button>\n                    <a class="navbar-brand" href="/">\n                        <img src="/img/zf-logo-mark.svg" height="28" alt="Zend Framework 3.0.3-dev"/>&nbsp;Skeleton Application\n                    </a>\n                </div>-->\n                <div class="collapse navbar-collapse">\n                    <ul class="nav navbar-nav">\n                        <li class="active"><a href="/">Home</a></li>\n                    </ul>\n                </div>\n            </div>\n        </nav>\n        <div class="container">\n            <h1>An error occurred</h1>\n<h2>An error occurred during execution; please try again later.</h2>\n\n    <hr/>\n\n<h2>Additional information:</h2>\n<h3>Zend\\Json\\Exception\\RuntimeException</h3>\n<dl>\n    <dt>File:</dt>\n    <dd>\n        <pre>/var/www/vendor/zendframework/zend-json/src/Json.php:272</pre>\n    </dd>\n    <dt>Message:</dt>\n    <dd>\n        <pre>Decoding failed: Syntax error</pre>\n    </dd>\n    <dt>Stack trace:</dt>\n    <dd>\n        <pre>#0 /var/www/vendor/zendframework/zend-json/src/Json.php(49): Zend\\Json\\Json::decodeViaPhpBuiltIn(&#039;name=test&#039;, 1)\n#1 /var/www/module/ScoreApi/src/Controller/ScoreApiController.php(89): Zend\\Json\\Json::decode(&#039;name=test&#039;, 1)\n#2 /var/www/vendor/zendframework/zend-mvc/src/Controller/AbstractRestfulController.php(345): ScoreApi\\Controller\\ScoreApiController-&gt;getUserHighScoreAction()\n#3 /var/www/vendor/zendframework/zend-eventmanager/src/EventManager.php(322): Zend\\Mvc\\Controller\\AbstractRestfulController-&gt;onDispatch(Object(Zend\\Mvc\\MvcEvent))\n#4 /var/www/vendor/zendframework/zend-eventmanager/src/EventManager.php(179): Zend\\EventManager\\EventManager-&gt;triggerListeners(Object(Zend\\Mvc\\MvcEvent), Object(Closure))\n#5 /var/www/vendor/zendframework/zend-mvc/src/Controller/AbstractController.php(106): Zend\\EventManager\\EventManager-&gt;triggerEventUntil(Object(Closure), Object(Zend\\Mvc\\MvcEvent))\n#6 /var/www/vendor/zendframework/zend-mvc/src/Controller/AbstractRestfulController.php(313): Zend\\Mvc\\Controller\\AbstractController-&gt;dispatch(Object(Zend\\Http\\PhpEnvironment\\Request), Object(Zend\\Http\\PhpEnvironment\\Response))\n#7 /var/www/vendor/zendframework/zend-mvc/src/DispatchListener.php(138): Zend\\Mvc\\Controller\\AbstractRestfulController-&gt;dispatch(Object(Zend\\Http\\PhpEnvironment\\Request), Object(Zend\\Http\\PhpEnvironment\\Response))\n#8 /var/www/vendor/zendframework/zend-eventmanager/src/EventManager.php(322): Zend\\Mvc\\DispatchListener-&gt;onDispatch(Object(Zend\\Mvc\\MvcEvent))\n#9 /var/www/vendor/zendframework/zend-eventmanager/src/EventManager.php(179): Zend\\EventManager\\EventManager-&gt;triggerListeners(Object(Zend\\Mvc\\MvcEvent), Object(Closure))\n#10 /var/www/vendor/zendframework/zend-mvc/src/Application.php(332): Zend\\EventManager\\EventManager-&gt;triggerEventUntil(Object(Closure), Object(Zend\\Mvc\\MvcEvent))\n#11 /var/www/public/index.php(40): Zend\\Mvc\\Application-&gt;run()\n#12 {main}</pre>\n    </dd>\n</dl>\n\n                        <hr>\n            <footer>\n                <!--<p>&copy; 2005 - 2018 by Zend Technologies Ltd. All rights reserved.</p>-->\n            </footer>\n        </div>\n            </body>\n</html>\n'

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
