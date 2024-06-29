from PyQt5.QtCore import Qt
from itemdetail import ItemDetail
from list import List
from page import Page
from globals import Globals

class EatDrink(Page):
    '''
    吃喝
    '''
    def __init__(self):
        self.player=Globals.player
        self.food=[]
        self.window=Globals.window
        self.set_list()

    def set_list(self):
        self.food=[]
        self.list=List(nonetext='没有任何食物和饮料',event=self.show_detail)
        for item in self.player.bag:
            if item.eat!=0 or item.drink!=0:    #可以吃或喝
                self.list.append(item.name)
                self.food.append(item)

    def draw(self, qp):
        self.list.draw(qp)

    def keyPress(self, a0):
        if a0.key()==Qt.Key_U:   #使用
            index=self.list.curindex
            item=self.food[index]
            self.player.hungry-=item.eat
            self.player.thirsty-=item.drink
            if self.player.hungry<0:
                self.player.hungry=0
            if self.player.thirsty<0:
                self.player.thirsty=0
            for _index,_item in enumerate(self.player.bag):
                if _item.realname==item.realname:
                    self.player.bag.pop(_index)
                    break
            self.set_list()
        else:
            self.list.keyPress(a0)

    def show_detail(self, index, item):
        self.window.page.append(ItemDetail(self.food[index]))