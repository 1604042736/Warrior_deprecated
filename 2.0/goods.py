from item import *


class Goods(Item):
    def __init__(self, name, attack, defense, enchant, money):
        super().__init__(name, attack, defense, enchant)
        self.money = money
