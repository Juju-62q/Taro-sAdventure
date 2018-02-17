import pygame
import getpass
from PyGameScreen import PyGameScreen
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from Ranking.ClickedString import ClickedString
import requests, json

class Ranking(PyGameScreen):

    def __init__(self, width, height, surface, fpsClock):
        super().__init__(width, height, surface, fpsClock)
        self.backColor = (107, 73, 45) # 茶色
        self.surface.fill(self.backColor)

    def Ranking(self):
        # ランキングの取得
        rankingDict = self.getRanking()

        returnObj = ClickedString("please click HERE to back menu", 50, 550) # メインメニューへ戻る関連

        returnFlag = False # メインメニューに戻るフラグ
        while (not returnFlag):
            self.surface.fill(self.backColor) # 初期化
            returnObj.blitString(self.surface, (128, 0, 0), (238, 120, 0)) # メインメニューに戻る文章の描画
            self.blitRanking(rankingDict) # ランキングの描画

            # 画面トップの描画
            topFont = pygame.font.SysFont(None, 60)
            top = topFont.render("Top 10", True, (255, 234, 0))
            self.surface.blit(top, (330, 50))

            # イベントチェック
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if returnObj.x <= x <= returnObj.x + returnObj.width and returnObj.y <= y <= returnObj.y + returnObj.height:
                        returnFlag = True

            pygame.display.update()


    def blitRanking(self, rankingData): # ランキングを表示する関数
        rankFontSize = 40
        rankingFont = pygame.font.SysFont(None, rankFontSize)
        charLength, _ = rankingFont.size('   ') # ランキング表示整形のための文字幅(文字によって横幅異なる)
        userName = getpass.getuser()

        maxLength = 0
        for item in rankingData['ranking']: # 最長のプレイヤー名を求める
            if maxLength < len(item['name']):
                maxLength = len(item['name'])
        nameWidth = charLength * maxLength # 整形のための処理

        if(len(rankingData['ranking']) < 10):
            for i in range(10 - len(rankingData['ranking'])):
                tmp = {"name":"-----","score":"-----","created_at":"-----"}
                rankingData['ranking'].append(tmp)
        
        
        def blitItem(item, start, line, color): # ランキングの各要素を出力する補助関数
            temp = rankingFont.render(item, True, color)
            self.surface.blit(temp, (start, line))

        for i, rankData in enumerate(rankingData['ranking']): # 以下ランキング出力
            rank = i + 1
            name = rankData['name']
            score = rankData['score']
            playTime = rankData['created_at']
            line = 120 + i * rankFontSize

            if name == userName: # ユーザー名がランキング上にあるかチェック
                rankingFont.set_underline(True)
                userFlag = True
            else:
                rankingFont.set_underline(False)
                userFlag = False
            
            # 順位の表示
            startRank = 100
            rankColor = (255, 255, 255)#(208, 175, 76)
            if userFlag: # ユーザーの順位の色を変える
                rankColor = (0, 200, 0)
            elif i == 0:
                rankColor = (255, 215, 0)
            elif i == 1:
                rankColor = (192, 192, 192)
            elif i == 2:
                rankColor = (196, 112, 34)
            blitItem(str(rank), startRank, line, rankColor)

            # プレイヤー名の表示
            startName = startRank + charLength * 3
            nameColor = (254, 242, 99)
            blitItem(name, startName, line, nameColor)

            # スコアの表示
            startScore = startName + nameWidth
            scoreColor = (184, 210, 0)
            blitItem(score, startScore, line, scoreColor)

            # プレイ時間の表示
            startTime = startScore + charLength * 6
            timeColor = (206, 228, 174)
            blitItem(playTime, startTime, line, timeColor)

    def getRanking(self):
        url = "http://localhost/api/ranking"
        responseBody = requests.get(url)

        resultDict = json.loads(responseBody.content)

        if (resultDict['status'] != "OK"):
            raise Exception

        return resultDict['result']