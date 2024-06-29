from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QColor, QFont, QFontDatabase, QFontMetrics
from globals import Globals
from page import Page


class ItemDetail(Page):
    '''
    显示一个item的细节
    '''

    def __init__(self, item):
        self.font = QFontDatabase.addApplicationFont(r'data\font\default.ttf')
        self.window = Globals.window
        self.item = item
        self.chinesemap = Globals.chinesemap

    def draw(self, qp):
        font = QFont(QFontDatabase.applicationFontFamilies(self.font)[0], 14)
        qp.setFont(font)
        fm = QFontMetrics(font)
        font_height = fm.height()  # 文字高度
        text = f'{self.item.name}的细节'
        font_width = fm.width(text)
        qp.setPen(QColor(255, 255, 255))
        qp.drawText(QRect(int((self.window.width()-font_width)/2),
                    0, font_width, font_height), Qt.AlignLeft, text)
        index = 1
        for key in ("name", "realname", "value", "weight", "attack", "defense","eat","drink"):
            val = self.item.__dict__[key]
            text = f'{self.chinesemap[key]}: {val}'
            font_width = fm.width(text)
            qp.drawText(QRect(0, index*font_height, font_width,
                        font_height), Qt.AlignLeft, text)
            index += 1
