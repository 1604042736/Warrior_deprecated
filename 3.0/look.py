from PyQt5.QtCore import Qt

from item import Item


class Look(Item):
    '''
    查看四周
    '''

    def __init__(self, x, y, z):
        super().__init__('look')
        self.x, self.y, self.z = x, y, z
        self._x, self._y, self._z = self.x, self.y, self.z
        self.lookat = None  # 看向的item

    def keyPress(self, a0):
        self._x, self._y,self._z = self.x, self.y,self.z
        if a0.key() == Qt.Key_8:
            self.y -= 1
        elif a0.key() == Qt.Key_2:
            self.y += 1
        elif a0.key() == Qt.Key_4:
            self.x -= 1
        elif a0.key() == Qt.Key_6:
            self.x += 1
        elif a0.key() == Qt.Key_3:
            self.x += 1
            self.y += 1
        elif a0.key() == Qt.Key_9:
            self.x += 1
            self.y -= 1
        elif a0.key() == Qt.Key_7:
            self.x -= 1
            self.y -= 1
        elif a0.key() == Qt.Key_1:
            self.x -= 1
            self.y += 1
        elif a0.key()==Qt.Key_Up:
            self.z+=1
        elif a0.key()==Qt.Key_Down:
            self.z-=1
        try:
            self.lookat = self.localmap[f'{self.x}_{self.y}_{self.z}']
        except KeyError:
            self.lookat = []
