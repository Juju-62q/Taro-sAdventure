from pygame.locals import Rect

class Goki:

    def __init__(self, x, y, width, height, image, moveSpeed):
        self._rect = Rect(x, y, width, height)
        self._image = image
        self._moveSpeed = moveSpeed
        self._speedChangeCount = 0

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, rect):
        self._rect = rect

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        self._image = image

    @property
    def moveSpeed(self):
        return self._moveSpeed

    @moveSpeed.setter
    def moveSpeed(self, moveSpeed):
        self._moveSpeed = moveSpeed

    def moveGoki(self):
        self.rect.x -= self.moveSpeed
        return self
