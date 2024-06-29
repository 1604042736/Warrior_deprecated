from PyQt5.QtCore import Qt
from itemdetail import ItemDetail
from list import List
from page import Page
from globals import Globals


class Bag(Page):
    def __init__(self) -> None:
        self.window = Globals.window
        self.player = Globals.player
        self.set_list()

    def set_list(self):
        self.list = List(nonetext='没有任何东西在背包里',
                         event=self.show_detail)
        for i in self.player.bag:
            self.list.append(i.name)

    def draw(self, qp) -> None:
        self.list.draw(qp)

    def keyPress(self, a0):
        self.list.keyPress(a0)

    def show_detail(self, index, item):
        self.window.page.append(ItemDetail(self.player.bag[index]))
