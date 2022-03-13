from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QColor, QFont, QFontDatabase, QFontMetrics
from globals import Globals
from itemdetail import ItemDetail
from list import List
from item import Item
from page import Page


class Shop(Page):
    def __init__(self):
        self.font = QFontDatabase.addApplicationFont(r'data\font\default.ttf')
        self.player = Globals.player
        self.texture = Globals.texture
        self.window = Globals.window
        with open('data\goods.txt', encoding='utf-8')as file:
            self.goods = {}
            for good in file.readlines():
                item = Item(good.split()[0])
                self.goods[item.name] = item
        self.set_list()

    def set_list(self):
        font = QFont(QFontDatabase.applicationFontFamilies(self.font)[0], 14)
        fm = QFontMetrics(font)
        self.list = List(startpos=(0,fm.height()),nonetext='商店里没有东西',
                         event=self.show_detail)
        for key, val in self.goods.items():
            self.list.append(f'{val.name}')

    def draw(self, qp):
        font = QFont(QFontDatabase.applicationFontFamilies(self.font)[0], 14)
        qp.setFont(font)
        fm = QFontMetrics(font)
        font_height = fm.height()  # 文字高度
        text = f'商店'
        font_width = fm.width(text)
        qp.setPen(QColor(255, 255, 255))
        qp.drawText(QRect(int((self.window.width()-font_width)/2),
                    0, font_width, font_height), Qt.AlignLeft, text)
                    
        self.list.draw(qp)

    def keyPress(self, a0):
        if a0.key() == Qt.Key_U:  # 买商品
            index, text = self.list.curindex, self.list[self.list.curindex]
            good = self.goods[text.split()[0]]
            if self.player.money >= good.value:
                self.player.money -= good.value
                self.player.bag.append(good)
        elif a0.key() == Qt.Key_S:  # 卖商品
            index, text = self.list.curindex, self.list[self.list.curindex]
            good = self.goods[text.split()[0]]
            for index, item in enumerate(self.player.bag):
                if item.name == good.name:
                    self.player.bag.pop(index)
                    self.player.money += good.value
        else:
            self.list.keyPress(a0)

    def show_detail(self, index, item):
        self.window.page.append(ItemDetail(self.goods[item]))
