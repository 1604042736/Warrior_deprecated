from Controls.List import List
from Objects.Creature import Creature
from PyQt5.QtGui import QPainter, QPaintEvent
from PyQt5.QtWidgets import QWidget
from System.Key import Key


class AttackIndicator(QWidget):
    def __init__(self, target, parent=None):
        super().__init__(parent)
        self.setWindowTitle("AttackIndicator")
        self.target = target
        x, y = self.target.x, self.target.y
        directions = ["north", "south", "east", "west",
                      "northeast", "northwest", "southeast", "southwest"]
        self.l_targets = List(spacing=[10, 10])
        for i, dxy in enumerate(((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1))):
            dx, dy = dxy
            direction = directions[i]
            for creature in Creature.instances:
                if creature.x == x+dx and creature.y == y+dy:
                    self.l_targets.values.append(
                        [direction, creature, creature.hp])

        Key().connect(self)

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)
        self.l_targets.paint(painter, self.rect())
        return super().paintEvent(a0)

    def keyPress(self, action: str):
        if action == "move_selector_up":
            self.l_targets.back()
        elif action == "move_selector_down":
            self.l_targets.next()
        elif action == "select":
            creature = self.l_targets.values[self.l_targets.selection][1]
            self.target.attack(creature)
            self.close()
