from Core.Map import Map

from Objects.Object import Object


class Unit(Object):
    """在地图上显示的单元"""
    instances: list["Unit"] = []  # 所有的unit

    def __init__(self, type_: str, x=0, y=0, z=0, parent: "Unit" = None) -> None:
        super().__init__(type_, parent)
        self._x = x
        self._y = y
        self._z = z
        Unit.instances.append(self)

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
        if self.parent:
            return self.parent.gx+self._x
        return self._x

    @property
    def gy(self):
        if self.parent:
            return self.parent.gy+self._y
        return self._y

    @property
    def gz(self):
        if self.parent:
            return self.parent.gz+self._z
        return self._z

    @x.setter
    def x(self, value):
        x = self._x
        self._x = value
        if Map.instance and not Map.instance.moveable(self.gx, self.gy, self.gz):
            self._x = x

    @y.setter
    def y(self, value):
        y = self._y
        self._y = value
        if Map.instance and not Map.instance.moveable(self.gx, self.gy, self.gz):
            self._y = y

    @z.setter
    def z(self, value):
        z = self._z
        self._z = value
        if Map.instance and not Map.instance.moveable(self.gx, self.gy, self.gz):
            self._z = z

    def next_turn(self):
        """下一回合"""
