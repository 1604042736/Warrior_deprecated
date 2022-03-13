from creature import Creature
from random import randint


class Animal(Creature):
    '''
    动物
    '''

    def __init__(self, name, x=0, y=0, z=0) -> None:
        super().__init__(name, x, y, z)

    def action(self):
        if self.dead:
            return
        dx = randint(-1, 1)
        dy = randint(-1, 1)
        self._x, self._y, self._z = self.x, self.y, self.z
        self.x += dx
        self.y += dy
        self.collision()
