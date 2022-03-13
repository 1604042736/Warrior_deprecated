import sys, os
from PyQt5.QtWidgets import *
from __pyqt__.Launcher import *


class Launcher(QWidget, Ui_Launcher):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb_startgame.clicked.connect(self.StartGame)

    def StartGame(self):
        username = self.le_username.text()
        path = f'.warrior\\users\\{username}'
        if not os.path.exists(path):
            os.makedirs(path)
        os.popen(f'start pythonw Warrior.py {path}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    launcher = Launcher()
    launcher.show()
    sys.exit(app.exec_())
