from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QColor, QFont, QFontDatabase, QFontMetrics
from globals import Globals
from page import Page


class State(Page):
    def __init__(self) -> None:
        self.player = Globals.player
        self.font = QFontDatabase.addApplicationFont(r'data\font\default.ttf')

    def draw(self, qp):
        font = QFont(QFontDatabase.applicationFontFamilies(self.font)[0], 14)
        qp.setFont(font)
        fm = QFontMetrics(font)
        font_height = fm.height()  # 文字高度
        qp.setPen(QColor(255, 255, 255))
        index=0
        for key in ('heart','attack','defense','money','hungry','thirsty'):
            text=f'{Globals.chinesemap[key]}: {self.player.__dict__[key]}'
            qp.drawText(QRect(0, font_height*index, fm.width(text),
                        font_height), Qt.AlignLeft, text)
            index+=1
