from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFontMetrics, QPainter

from Controls.Control import Control


class List(Control):
    """列表控件"""

    def __init__(self, values: list[list] = (), spacing: list[int] = ()) -> None:
        super().__init__()
        self.selection = 0  # 选择的项
        self.values: list[list] = list(values)  # 每行的数据
        self.spacing: list[int] = list(spacing)  # 每列数据的间距
        self.width = 0  # 宽度

    def paint(self, painter: QPainter, rect: QRect):
        fontm = QFontMetrics(painter.font())
        maxlen = max([len(i)for i in self.values])
        shift = [0]  # 每列的偏移
        for i in range(maxlen):
            w = []
            for j in self.values:
                if i < len(j):
                    w.append(fontm.width(str(j[i])))
            shift.append(max(w))
        for i in range(1, len(shift)-1):
            shift[i] += shift[i-1]+self.spacing[i-1]
        shift[-1] += shift[-2]
        self.width = shift[-1]

        x, y = rect.x(), rect.y()
        for i, row_values in enumerate(self.values):
            for j, value in enumerate(row_values):
                painter.drawText(x+shift[j],
                                 y+(i+1)*fontm.height(),
                                 str(value))
            if i == self.selection:
                painter.drawRect(x,
                                 y+i*fontm.height(),
                                 self.width,
                                 fontm.height())
        return super().paint(painter)

    def next(self, roll=True):
        if roll:
            self.selection = (self.selection+1) % len(self.values)
        else:
            self.selection += 1
            if self.selection >= len(self.values):
                self.selection = len(self.values-1)

    def back(self, roll=True):
        if roll:
            self.selection = (self.selection-1) % len(self.values)
        else:
            self.selection -= 1
            if self.selection < 0:
                self.selection = 0
