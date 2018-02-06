import pygame

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

