from Core.Camera import Camera
from Core.Map import Map
from Core.Tile import Tile
from Objects.Player import Player
from Objects.Unit import Unit
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter, QPaintEvent
from PyQt5.QtWidgets import QWidget
from System.Key import Key


class MapDisplay(QWidget):
    """绘制地图"""

    def __init__(self, map: Map, camera: Camera = None, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("MapDisplay")
        self.map = map
        if camera == None:
            camera = Camera()
        self.camera = camera
        Key().connect(self)

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)

        col_count = int(self.width()/Tile.WIDTH)  # 能显示的列数
        row_count = int(self.height()/Tile.HEIGHT)  # 能显示的行数
        minx = self.camera.gx-col_count
        maxx = self.camera.gx+col_count
        miny = self.camera.gy-row_count
        maxy = self.camera.gy+row_count

        # 窗口中心坐标
        centerx = int(self.width()/2)
        centery = int(self.height()/2)

        for x in range(minx, maxx):
            for y in range(miny, maxy):
                pos = (x, y, self.camera.gz)
                if pos in self.map.blocks:
                    block = self.map.blocks[pos]
                    # 与摄像机的相对坐标
                    rx = self.camera.gx-x
                    ry = self.camera.gy-y
                    painter.drawImage(QRect(centerx-rx*Tile.WIDTH,
                                            centery+ry*Tile.HEIGHT,
                                            Tile.WIDTH,
                                            Tile.HEIGHT),
                                      block.tile)
        # 绘制Unit
        for unit in Unit.instances[::-1]:  # 倒序绘制
            x, y, z = unit.gx, unit.gy, unit.gz
            if minx <= x <= maxx and miny <= y <= maxy and z == self.camera.gz:
                rx = self.camera.gx-x
                ry = self.camera.gy-y
                painter.drawImage(QRect(centerx-rx*Tile.WIDTH,
                                        centery+ry*Tile.HEIGHT,
                                        Tile.WIDTH,
                                        Tile.HEIGHT),
                                  unit.tile)
        if not self.camera._follow:
            painter.drawImage(QRect(centerx,
                                    centery,
                                    Tile.WIDTH,
                                    Tile.HEIGHT),
                              self.camera.tile)
        return super().paintEvent(a0)

    def keyPress(self, action: str):
        if action == "lookat":
            self.camera.x = self.camera.gx
            self.camera.y = self.camera.gy
            self.camera.z = self.camera.gz
            self.camera.follow(None)
        elif action == "quit_lookat":
            self.camera.x = 0
            self.camera.y = 0
            self.camera.z = 0
            self.camera.follow(Player())
