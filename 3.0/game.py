from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QColor, QFont, QFontDatabase, QFontMetrics, QPainter
from PyQt5.QtWidgets import QApplication, QWidget
from bag import Bag
from eatdrink import EatDrink
from inventory import Inventory
from localmap import LocalMap
from look import Look
from pausegame import PauseGame
from player import Player
from state import State
from texture import Texture
import sys
from globals import Globals


class Game(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.font = QFontDatabase.addApplicationFont(r'data\font\default.ttf')
        self.setWindowTitle('Warrior')
        self.resize(1000, 618)
        self.setStyleSheet('background:black')
        self.setMouseTracking(True)

        Globals.window = self
        self.texture = Texture()
        Globals.texture = self.texture
        self.player = Player()
        Globals.player = self.player
        self.localmap = LocalMap()
        Globals.localmap = self.localmap
        self.page = [self.localmap]  # 当前页面

        self.time = 0  # 时间,每帧增加1

        self.debug = False

    def paintEvent(self, a0) -> None:
        self.time += 1
        qp = QPainter()
        qp.begin(self)
        self.page[-1].draw(qp)
        if self.debug and len(self.page) == 1:
            self.draw_debug(qp)
        qp.end()

    def keyPressEvent(self, a0) -> None:
        if len(self.page) > 1:
            self.page[-1].keyPress(a0)
        else:  # 处于第1页
            self.localmap.camera.keyPress(a0)
            if a0.key() == Qt.Key_B:
                self.page.append(Bag())
            elif a0.key() == Qt.Key_I:
                self.page.append(Inventory())
            elif a0.key() == Qt.Key_Z:
                self.page.append(State())
            elif a0.key() == Qt.Key_U:
                structure=self.player.get_structure()
                if structure:
                    self.page.append(structure)
            elif a0.key() == Qt.Key_F3:
                self.debug = not self.debug
            elif a0.key() == Qt.Key_K:
                self.localmap.update = False
                self.localmap.camera = Look(
                    self.player.x, self.player.y, self.player.z)
            elif a0.key()==Qt.Key_E:
                self.page.append(EatDrink())
        if a0.key() == Qt.Key_Escape:
            if len(self.page) > 1:
                self.page.pop()
            elif isinstance(self.localmap.camera, Look):  # 当前模式
                self.localmap.update = True
                # 将这个item抹除
                item = self.localmap.camera
                key = f'{item.x}_{item.y}_{item.z}'
                for index, _item in enumerate(self.localmap[key]):
                    if _item.name == item.name:
                        self.localmap[key].pop(index)
                        break
                self.localmap.camera = self.player
            else:
                self.page.append(PauseGame())
        self.repaint()

    def draw_debug(self, qp):
        font = QFont(QFontDatabase.applicationFontFamilies(self.font)[0], 14)
        qp.setFont(font)
        fm = QFontMetrics(font)
        font_height = fm.height()  # 文字高度
        qp.setPen(QColor(255, 255, 255))
        i = 0  # 保存当前索引
        for index, text in enumerate([f'x,y,z={self.localmap.camera.x},{self.localmap.camera.y},{self.localmap.camera.z}',
                                      f'isAttack: {self.player.isAttack}',
                                      f'Time: {self.time}',
                                      f'Count: {self.player.conut}']):
            qp.drawText(QRect(0, index*font_height, fm.width(text),
                        font_height), Qt.AlignLeft, text)
            i = index
        i += 1
        if 'lookat' in self.localmap.camera.__dict__:  # 摄像机里存储了当前看向的内容
            itemlist = self.localmap.camera.lookat
            if itemlist != None:
                for index, item in enumerate(itemlist):
                    text = f'Look At: {item}'
                    qp.drawText(QRect(0, (i+index)*font_height, fm.width(text),
                                      font_height), Qt.AlignLeft, text)

    def closeEvent(self, a0) -> None:
        if not isinstance(self.page[-1],PauseGame):
            self.page.append(PauseGame())
            self.repaint()
        a0.ignore()

    def exit(self):
        exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Game()
    game.show()
    sys.exit(app.exec_())
