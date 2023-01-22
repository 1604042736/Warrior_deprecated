from Controls.List import List
from PyQt5.QtCore import QCoreApplication, QRect
from PyQt5.QtGui import QFontMetrics, QPainter, QPaintEvent
from PyQt5.QtWidgets import QWidget
from System.Key import Key

_translate = QCoreApplication.translate


class EquipmentViewer(QWidget):
    def __init__(self, target, parnet=None) -> None:
        super().__init__(parnet)
        self.setWindowTitle("EquipmentViewer")
        self.l_equipment = List(spacing=[10])
        self.l_choices = List(spacing=[10])
        self.target = target
        Key().connect(self)

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)
        self.l_equipment.values = []
        for key, val in self.target.equipments.items():
            self.l_equipment.values.append((_translate("Bodypart", key), val))
        self.l_equipment.paint(painter, self.rect())

        self.l_choices.values = [[None]]
        bodypart = self.l_equipment.values[self.l_equipment.selection][0]
        for i in self.target.inventory:
            if bodypart in ["head", "leg", "feet", "body"]:
                if getattr(i, "wearable", False):
                    self.l_choices.values.append([i])
            else:
                self.l_choices.values.append([i])
        self.l_choices.paint(painter, QRect(
            self.l_equipment.width+10, 0, self.width(), self.height()))
        return super().paintEvent(a0)

    def keyPress(self, action: str):
        if action == "move_selector_up":
            self.l_equipment.back()
            self.l_choices.selection = 0
        elif action == "move_selector_down":
            self.l_equipment.next()
            self.l_choices.selection = 0
        elif action == "move_selector2_up":
            self.l_choices.back()
        elif action == "move_selector2_down":
            self.l_choices.next()
        elif action == "select":
            bodypart = self.l_equipment.values[self.l_equipment.selection][0]
            equipment = self.l_choices.values[self.l_choices.selection][0]
            self.target.equip(bodypart, equipment)
