from PyQt5.QtCore import Qt
from globals import Globals
from list import List
from page import Page


class Inventory(Page):
    '''
    装备信息
    '''

    def __init__(self) -> None:
        self.window = Globals.window
        self.player = Globals.player
        self.chinesemap = Globals.chinesemap
        self.set_list()
        self.replace = [None, None]  # 替换的两个

    def set_list(self):
        self.list = List(event=self.replace_inventory1)
        for key, val in self.player.inventory.items():
            if val == None:
                self.list.append(f'{self.chinesemap[key]} -> None')
            else:
                self.list.append(f'{self.chinesemap[key]} -> {val.name}')

    def draw(self, qp):
        self.list.draw(qp)

    def keyPress(self, a0):
        self.list.keyPress(a0)

    def replace_inventory1(self, index, text):
        '''
        替换装备
        '''
        self.replace[0] = Globals.englishmap[text.split()[0]]
        self.list = List(event=self.replace_inventory2)
        self.list.append('None')
        for i in self.player.bag:
            self.list.append(i.name)

    def replace_inventory2(self, index, text):
        '''
        开始替换
        '''
        self.replace[1] = text
        if text == 'None':  # 相当于解除装备
            self.remove_equip()
            self.player.inventory[self.replace[0]] = None
        else:
            self.remove_equip()
            item = self.player.bag[index-1]
            # 穿戴位置正确
            if self.replace[0] in item.part:
                self.player.attack += item.attack
                self.player.defense += item.defense
            self.player.inventory[self.replace[0]] = self.player.bag[index-1]
            self.player.bag.pop(index-1)
        self.set_list()

    def remove_equip(self):
        '''
        解除装备
        '''
        item = self.player.inventory[self.replace[0]]
        if item:
            # 穿戴部位正确
            if self.replace[0] in item.part:
                self.player.attack -= item.attack
                self.player.defense -= item.defense
            self.player.bag.append(item)
