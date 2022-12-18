from PyQt5.QtCore import QEvent, QObject, Qt
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QApplication

from System.Key import Key


class Application(QApplication):
    def notify(self, a0: QObject, a1: QEvent) -> bool:
        if a1.type() in [QEvent.Type.KeyPress, QEvent.Type.KeyRelease]:
            Key().eventFilter(a0, a1)
        elif a1.type() == QEvent.Type.Close:
            self.sendEvent(a0, QKeyEvent(QEvent.Type.KeyPress,
                                         Qt.Key.Key_Escape,
                                         Qt.KeyboardModifier.NoModifier))
            Key().disconnect(a0)
        return super().notify(a0, a1)
