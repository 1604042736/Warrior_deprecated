from Objects.Unit import Unit
from System.Key import Key

from Core.Tile import Tile


class Camera:
    """摄像机"""

    def __init__(self, x=0, y=0, z=0) -> None:
        self._follow: Unit = None  # 跟随的单元
        self._x = x
        self._y = y
        self._z = z
        self.tile = Tile(5, 8, color=(255, 255, 0))
        Key().connect(self)

    def follow(self, follow_unit: Unit):
        """跟随一个单元

        Args:
            follow_unit (Unit): 要跟随的单元
        """
        self._follow = follow_unit

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    @property
    def gx(self):
        if self._follow:
            return self._follow.gx+self._x
        return self._x

    @property
    def gy(self):
        if self._follow:
            return self._follow.gy+self._y
        return self._y

    @property
    def gz(self):
        if self._follow:
            return self._follow.gz+self._z
        return self._z

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value

    @z.setter
    def z(self, value):
        self._z = value

    def keyPress(self, action: str):
        if action == "move_camera_up":
            self.y += 1
        elif action == "move_camera_down":
            self.y -= 1
        elif action == "move_camera_right":
            self.x += 1
        elif action == "move_camera_left":
            self.x -= 1
