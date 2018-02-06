import pygame
from Ranking.ClickedString import ClickedString
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

