from random import randint

from Objects.Creature import Creature


class Animal(Creature):
    def next_turn(self):
        dx = randint(-1, 1)
        dy = randint(-1, 1)
        self.x += dx
        self.y += dy
        return super().next_turn()
