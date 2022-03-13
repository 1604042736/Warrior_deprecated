from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QColor, QFont, QFontDatabase, QFontMetrics

from globals import Globals


class List(list):
    '''
    绘制列表
    '''

    def __init__(self, startpos=(0, 0), nonetext='', event=None):
        self.window = Globals.window
        self.font = QFontDatabase.addApplicationFont(r'data\font\default.ttf')
        self.startindex = 0  # 显示的起始位置
        self.shift = 0  # 偏移,因为下面可能会有其他文字
        self.curindex = 0  # 选中文字的索引
        self.l = 0xffff  # 显示的行数
        self.nonetext = nonetext  # 列表没有东西时的文字
        self.startpos = startpos  # 位置
        self.event = event  # 按enter后的事件

    def draw(self, qp):
        font = QFont(QFontDatabase.applicationFontFamilies(self.font)[0], 14)
        qp.setFont(font)
        fm = QFontMetrics(font)
        font_height = fm.height()  # 文字高度
        if len(self) > 0:
            l = self.l = int((self.window.height()-self.shift)/font_height)
            reali = 0
            for i in range(self.startindex, self.startindex+l+1):
                if i < len(self):
                    text = self[i]
                    if i == self.curindex:
                        qp.setPen(QColor(255, 255, 255))
                    else:
                        qp.setPen(QColor(170, 170, 170))
                    qp.drawText(QRect(self.startpos[0], self.startpos[1]+reali*font_height, fm.width(text),
                                font_height), Qt.AlignLeft, text)
                reali += 1
        else:
            qp.setPen(QColor(255, 255, 255))
            qp.drawText(QRect(0, 0, fm.width(self.nonetext), font_height),
                        Qt.AlignLeft, self.nonetext)

    def keyPress(self, a0):
        if a0.key() == Qt.Key_Down:
            self.curindex += 1
        elif a0.key() == Qt.Key_Up:
            self.curindex -= 1
        elif a0.key() == Qt.Key_Enter:
            if self.event != None:
                self.event(self.curindex, self[self.curindex])
        if self.curindex < 0:
            self.curindex = 0
        if self.curindex >= len(self):
            self.curindex = len(self)-1
        elif self.curindex >= self.startindex+self.l:
            self.startindex += 1
        elif self.curindex < self.startindex:
            self.startindex -= 1
