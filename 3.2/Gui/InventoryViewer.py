from Controls.List import List
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFontMetrics, QPainter, QPaintEvent
from PyQt5.QtWidgets import QWidget
from System.Key import Key


class InventoryViewer(QWidget):
    def __init__(self, target, parnet=None) -> None:
        super().__init__(parnet)
        self.setWindowTitle("InventoryViewer")
        self.target = target
        self.l_inventory = List()
        Key().connect(self)

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)
        self.l_inventory.values = [[i]for i in self.target.inventory]
        self.l_inventory.paint(painter, self.rect())
        return super().paintEvent(a0)

    def keyPress(self, action: str):
        if action == "move_selector_up":
            self.l_inventory.back()
        elif action == "move_selector_down":
            self.l_inventory.next()
