from Controls.List import List
from Objects.Falling import Falling
from PyQt5.QtGui import QPainter, QPaintEvent
from PyQt5.QtWidgets import QWidget

from System.Key import Key


class Pickuper(QWidget):
    def __init__(self, target, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Pickuper")
        self.target = target
        self.l_fallings = List(spacing=[10])
        x, y = self.target.x, self.target.y
        directions = ["north", "south", "east", "west",
                      "northeast", "northwest", "southeast", "southwest"]
        for i, dxy in enumerate(((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1))):
            dx, dy = dxy
            direction = directions[i]
            for falling in Falling.instances:
                if falling.x == x+dx and falling.y == y+dy:
                    self.l_fallings.values.append([direction, falling])
        Key().connect(self)

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)
        self.l_fallings.paint(painter, self.rect())
        return super().paintEvent(a0)

    def keyPress(self, action: str):
        if action == "move_selector_up":
            self.l_fallings.back()
        elif action == "move_selector_down":
            self.l_fallings.next()
        elif action == "select":
            falling = self.l_fallings.values[self.l_fallings.selection][1]
            falling.pickup(self.target)
            self.close()
