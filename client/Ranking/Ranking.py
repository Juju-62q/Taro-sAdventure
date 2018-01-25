import pygame
import socket
import sys
import getpass
from PyGameScreen import PyGameScreen
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from datetime import datetime

class Ranking(PyGameScreen):

    def __init__(self, width, height, surface, fpsClock):
        super().__init__(width, height, surface, fpsClock)
        self.backColor = (107, 73, 45) # 茶色
        self.surface.fill(self.backColor)

    def Ranking(self):
        # TODO
        host = 'localhost' # 適宜変えること
        port = 59630
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port)) # サーバーに接続
        client.sendall(b'3') # サーバーに要求する処理の識別子
        #resTemp = client.recv(4096).decode('ascii') # 引数4096だと, "connected"を受け取る(タイミングの問題でバグる)
        expectedLen = len( 'connected'.encode('ascii') ) # (最大で)"connected"と同じ文字数のみ受け取る
        resTemp = client.recv(expectedLen).decode('ascii')
        if(resTemp != 'connected'): # エラー処理
            print('[Error] expected to receive "connected" but receive "{}"'.format(resTemp), file=sys.stderr)
            sys.exit()
        response = client.recv(4096).decode('ascii', errors = 'ignore').replace('\x00', '')
        rankingTemp = response.splitlines()
        client.close() # サーバーとの通信終了

        

        # ランキングの取得
        rankFontSize = 36
        rankingFont = pygame.font.SysFont(None, rankFontSize)
        rankingData = [] # タプルのリスト
        for rank, data in enumerate(rankingTemp, 1):
            name, score, t = data.split()
            playTime = (datetime.fromtimestamp(float(t))).strftime('%Y/%m/%d')
            rankingData.append((str(rank), name, score, playTime))

        sysFont = pygame.font.SysFont(None, 36) # フォントの設定
        returnObj = ClickedString("please click HERE to back menu", 50, 550) # メインメニューへ戻る関連
        nextObj = NextString("please click HERE to rank 11 to 20", 450, 550, 0) # ランキング順位切り替え関連
        returnFlag = False # メインメニューに戻るフラグ
        mousepos = [] # マウスクリックの座標のリスト
        while (not returnFlag):
            self.surface.fill(self.backColor) # 初期化
            returnObj.blitString(self.surface, (128, 0, 0), (238, 120, 0)) # メインメニューに戻る文章の描画
            nextObj.blitString(self.surface, (0, 0, 128), (238, 120, 0)) # ページ移動の文章の描画
            self.blitRanking(rankingData, nextObj.page) # ランキングの描画
            
            # 画面トップの描画
            topFont = pygame.font.SysFont(None, 60)
            tmp = topFont.render("Rank {0} to {1}".format(nextObj.thisStart, nextObj.thisEnd), True, (255, 234, 0))
            self.surface.blit(tmp, (270, 50))

            # イベントチェック
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == MOUSEBUTTONDOWN:
                    mousepos.append(event.pos)
            
            # マウスの座標について処理
            for x, y in mousepos:
                # メインメニューに戻る
                if returnObj.x <= x <= returnObj.x+returnObj.width and returnObj.y <= y <= returnObj.y+returnObj.height:
                    returnFlag = True
                # ランキング順位切り替え
                if nextObj.x <= x <= nextObj.x+nextObj.width and nextObj.y <= y <= nextObj.y+nextObj.height:
                    if nextObj.page == 0:
                        nextObj.page = 1
                    else:
                        nextObj.page = 0
                    nextObj.strChange() # ページ移動の文章の内容変更
            mousepos.clear()
            pygame.display.update()


    def blitRanking(self, rankingData, page): # ランキングを表示する関数
        rankFontSize = 36
        rankingFont = pygame.font.SysFont(None, rankFontSize)
        charLength, _ = rankingFont.size('   ') # ランキング表示整形のための文字幅(文字によって横幅異なる)
        userName = getpass.getuser()

        limitLength = 16
        maxLength = 0
        for i in range(10): # 最長のプレイヤー名を求める
            if maxLength < len(rankingData[i+10*page][1]):
                maxLength = len(rankingData[i+10*page][1]) 
        nameWidth = charLength * maxLength # 整形のための処理
        
        
        def blitItem(item, start, line, color): # ランキングの各要素を出力する補助関数
            temp = rankingFont.render(item, True, color)
            self.surface.blit(temp, (start, line))

        for i in range(10): # 以下ランキング出力
            rank, name, score, playTime = rankingData[i+10*page]
            line = 120 + i*rankFontSize

            if name == userName: # ユーザー名がランキング上にあるかチェック
                rankingFont.set_underline(True)
                userFlag = True
            else:
                rankingFont.set_underline(False)
                userFlag = False
            
            # 順位の表示
            startRank = 85 + (limitLength-maxLength)*charLength /2
            rankColor = (255, 255, 255)#(208, 175, 76)
            if userFlag: # ユーザーの順位の色を変える
                rankColor = (0, 200, 0)
            elif page == 0: #1位～3位の色を変える
                if i == 0:
                    rankColor = (255, 215, 0)
                elif i == 1:
                    rankColor = (192, 192, 192)
                elif i == 2:
                    rankColor = (196, 112, 34)
            blitItem(rank, startRank, line, rankColor)                 

            # プレイヤー名の表示
            startName = startRank + charLength*3
            nameColor = (254, 242, 99)
            blitItem(name, startName, line, nameColor)

            # スコアの表示
            startScore = startName + nameWidth
            scoreColor = (184, 210, 0)
            blitItem(score, startScore, line, scoreColor)

            # プレイ時間の表示
            startTime = startScore + charLength*6
            timeColor = (206, 228, 174)
            blitItem(playTime, startTime, line, timeColor)




# クリックされる文字列のクラス(画面下部)
class ClickedString():   

    def __init__(self, string, x, y):
        self._sysFont = pygame.font.SysFont(None, 30)
        self._string = string
        self._width, self._height = self.sysFont.size(string)
        self._x = x
        self._y = y

    @property
    def sysFont(self):
        return self._sysFont

    @sysFont.setter
    def sysFont(self, sysFont):
        self._sysFont = sysFont


    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, string):
        self._string = string

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x
    
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    # 文字列を表示する関数
    def blitString(self, surface, textColor, backgroundColor):
        tmp = self.sysFont.render(self.string, True, textColor, backgroundColor)
        surface.blit(tmp, (self.x, self.y))


# 表示する順位を切り替えるには...についてのクラス
class NextString(ClickedString):
    
    def __init__(self, string, x, y, page):
        super().__init__(string, x, y)
        self._page = page
        self._thisStart, self._thisEnd = 1, 10
        self._nextStart, self._nextEnd = 11, 20
    
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, page):
        self._page = page

    @property
    def thisStart(self):
        return self._thisStart

    @thisStart.setter
    def thisStart(self, thisStart):
        self._thisStart = thisStart

    @property
    def thisEnd(self):
        return self._thisEnd

    @thisEnd.setter
    def thisEnd(self, thisEnd):
        self._thisEnd = thisEnd

    @property
    def nextStart(self):
        return self._nextStart

    @nextStart.setter
    def nextStart(self, nextStart):
        self._nextStart = nextStart

    @property
    def nextEnd(self):
        return self._nextEnd

    @nextEnd.setter
    def nextEnd(self, nextEnd):
        self._nextEnd = nextEnd

    def strChange(self): # 表示内容を変更する関数
        (self.nextStart, self.nextEnd), (self.thisStart, self.thisEnd) = (self.thisStart, self.thisEnd), (self.nextStart, self.nextEnd)
        self.string = "please click HERE to rank {0} to {1}".format(self.nextStart, self.nextEnd)
        self.width, self.height = self.sysFont.size(self.string)
