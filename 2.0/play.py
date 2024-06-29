from random import *

from pygame.locals import *

from goods import *
from player import *
from wildanimals import *


class Play:
    goodslist = [
        ["Wooden sword", 100, 10, 0, "None"],
        ["Iron sword", 200, 20, 0, "None"],
        ["Golden sword", 300, 30, 0, "None"],
        ["Bronze sword", 400, 40, 0, "None"],
        ["Diamond sword", 500, 50, 0, "None"],
        ["Leather Helmet", 100, 0, 10, "None"],
        ["Leather Armor", 100, 0, 13, "None"],
        ["Leather shinguard", 100, 0, 16, "None"],
        ["Leather Boots", 100, 0, 19, "None"],
        ["Iron helmet", 200, 0, 20, "None"],
        ["Iron armor", 200, 0, 23, "None"],
        ["Iron shinguard", 200, 0, 26, "None"],
        ["Iron boots", 200, 0, 29, "None"],
        ["Gold helmet", 300, 0, 30, "None"],
        ["Gold armor", 300, 0, 33, "None"],
        ["Gold shinguard", 300, 0, 36, "None"],
        ["Golden boots", 300, 0, 39, "None"],
        ["Bronze Helmet", 400, 0, 40, "None"],
        ["Bronze armor", 400, 0, 43, "None"],
        ["Bronze shinguard", 400, 0, 46, "None"],
        ["Bronze boots", 400, 0, 49, "None"],
        ["Diamond helmet", 500, 0, 50, "None"],
        ["Diamond armor", 500, 0, 53, "None"],
        ["Diamond Leggings", 500, 0, 56, "None"],
        ["Diamond Boots", 500, 0, 59, "None"],
        ["Arch", 300, 30, 0, "None"],
        ["Shield", 300, 0, 100, "None"],
        ["Arrow", 1, 0, 0, "None"]
    ]

    def __init__(self, savepath):
        self.savepath = savepath
        self.player = Player(json.load(open(savepath + '/config.json', encoding='utf-8')))
        self.thingsstartindex = 0
        self.bagstartindex = 0
        self.page = 'main'
        self.log = []
        self.logstartindex = 0
        self.goods = []
        self.goodsstartindex = 0
        self.goods_color = [(200, 200, 200)] * len(self.goods)
        self.goods_index = 0
        for i in self.goodslist:
            self.goods.append(Goods(i[0], i[2], i[3], i[4], i[1]))
        self.bag_color = [(200, 200, 200)] * len(self.player.bag)
        self.bag_index = 0
        self.things_color = [(200, 200, 200)] * len(self.player.things)
        self.things_index = 0
        self.change_color()

    def explore(self, screen, console):
        self.logstartindex = 0
        self.log = []
        if not randint(0, 10):
            self.player.lvl += 1
            self.log.append('Upgrade')
        addmoney = randint(0, 100)
        self.player.money += addmoney
        self.log.append(f'Add {addmoney} money')
        if not randint(0, 20):
            self.log.append('You met wild animals')
            wildanimals = WildAnimals('wild animals', 50, 1, 0)
            while wildanimals.heart > 0 and self.player.heart[0] > 0:
                if not randint(0, 10):
                    self.player.heart[0] -= (wildanimals.attack - self.player.defense[0])
                    self.log.append(
                        f'Wild animals were knocked out your {wildanimals.attack - self.player.defense[0]} heart')
                    self.log.append(f'Now you have {self.player.heart[0]} heart')
                wildanimals.heart -= (self.player.attack[0] - wildanimals.defense)
                self.log.append(
                    f'You were knocked out wild animals {self.player.attack[0] - wildanimals.defense} heart')
                self.log.append(f'Now wild animals have {wildanimals.heart} heart')
            if wildanimals.heart <= 0:
                self.log.append('You win')
            else:
                self.log.append('You lose')

    def change_color(self):
        self.goods_color = [(200, 200, 200)] * len(self.goods)
        self.goods_color[self.goods_index] = (255, 255, 255)
        try:
            self.bag_color = [(200, 200, 200)] * len(self.player.bag)
            self.bag_color[self.bag_index] = (255, 255, 255)
        except:
            pass
        self.things_color = [(200, 200, 200)] * len(self.player.things)
        self.things_color[self.things_index] = (255, 255, 255)

    def updata(self, screen, console, event):
        if event.type == KEYDOWN:
            if event.key == K_t and self.page == 'main':
                self.thingsstartindex = 0
                self.things_index = 0
                self.page = 'things'
            elif event.key == K_b and self.page == 'main':
                self.bagstartindex = 0
                self.bag_index = 0
                self.page = 'bag'
            elif event.key == K_g and self.page == 'main':
                self.log = []
                self.logstartindex = 0
                self.page = 'go'
            elif event.key == K_s and self.page == 'main':
                self.goodsstartindex = 0
                self.goods_index = 0
                self.page = 'shop'
            elif event.key == K_DOWN and self.page == 'shop':
                self.goods_index = self.goods_index + 1
                if self.goods_index == len(self.goods):
                    self.goods_index -= 1
                if self.goods_index - (
                        self.goodsstartindex + int(screen.get_height() / console.baseheight) - 2) + 1 > 0:
                    self.goodsstartindex += 1
                self.change_color()
            elif event.key == K_UP and self.page == 'shop':
                self.goods_index = self.goods_index - 1
                if self.goods_index < 0:
                    self.goods_index = 0
                if self.goods_index - self.goodsstartindex < 0:
                    self.goodsstartindex -= 1
                    if self.goodsstartindex < 0:
                        self.goodsstartindex = 0
                self.change_color()
            elif event.key == K_e and self.page == 'go':
                self.explore(screen, console)
            elif event.key == K_DOWN and self.page == 'go':
                if (self.logstartindex + int(screen.get_height() / console.baseheight) - 2) < len(self.log):
                    self.logstartindex += 1
            elif event.key == K_UP and self.page == 'go':
                if (self.logstartindex + int(screen.get_height() / console.baseheight) - 2) <= len(self.log):
                    self.logstartindex -= 1
                    if self.logstartindex < 0:
                        self.logstartindex = 0
            elif event.key == K_DOWN and self.page == 'things':
                self.things_index = self.things_index + 1
                if self.things_index == len(self.player.things):
                    self.things_index -= 1
                if self.things_index - (
                        self.thingsstartindex + int(screen.get_height() / console.baseheight) - 2) + 1 > 0:
                    self.thingsstartindex += 1
                self.change_color()
            elif event.key == K_UP and self.page == 'things':
                self.things_index = self.things_index - 1
                if self.things_index < 0:
                    self.things_index = 0
                if self.things_index - self.thingsstartindex < 0:
                    self.thingsstartindex -= 1
                    if self.thingsstartindex < 0:
                        self.thingsstartindex = 0
                self.change_color()
            elif event.key == K_DOWN and self.page == 'bag':
                self.bag_index = self.bag_index + 1
                if self.bag_index == len(self.player.bag):
                    self.bag_index -= 1
                if self.bag_index - (
                        self.bagstartindex + int(screen.get_height() / console.baseheight) - 2) + 1 > 0:
                    self.bagstartindex += 1
                self.change_color()
            elif event.key == K_UP and self.page == 'bag':
                self.bag_index = self.bag_index - 1
                if self.bag_index < 0:
                    self.bag_index = 0
                if self.bag_index - self.bagstartindex < 0:
                    self.bagstartindex -= 1
                    if self.bagstartindex < 0:
                        self.bagstartindex = 0
                self.change_color()
            elif event.key == K_b and self.page == 'shop':
                buymoney = self.goods[self.goods_index].money
                if self.player.money >= buymoney:
                    self.player.money -= buymoney
                    self.player.bag.append(Item(self.goods[self.goods_index].name, self.goods[self.goods_index].attack,
                                                self.goods[self.goods_index].defense,
                                                self.goods[self.goods_index].enchant))
            elif event.key == K_s and self.page == 'shop':
                sellmoney = self.goods[self.goods_index].money
                i = len(self.player.bag) - 1
                while i >= 0:
                    if self.player.bag[i].name == self.goods[self.goods_index].name:
                        self.player.money += sellmoney
                        self.player.bag.pop(i)
                    i -= 1
            elif event.key == K_e and self.page == 'bag':
                try:
                    item = self.player.bag[self.bag_index]
                    for i in range(len(self.player.things)):
                        if self.player.things[i].name == 'None':
                            self.player.things[i].name = item.name
                            self.player.things[i].attack = item.attack
                            self.player.things[i].defense = item.defense
                            self.player.things[i].enchant = item.enchant
                            self.player.attack[0] += item.attack
                            self.player.defense[0] += item.defense
                            self.player.bag.pop(self.bag_index)
                            break
                except:
                    pass
            elif event.key == K_u and self.page == 'things':
                try:
                    item = self.player.things[self.things_index]
                    if item.name != "None":
                        self.player.attack[0] -= item.attack
                        self.player.defense[0] -= item.defense
                        self.player.bag.append(item)
                        self.player.things[self.things_index] = Item('None', 0, 0, 'None')
                except:
                    pass
            elif event.key == K_ESCAPE:
                if self.page == 'main':
                    self.player.save(self.savepath)
                    return 'homepage'
                elif self.page in ['things', 'bag', 'go', 'shop', 'equip']:
                    self.page = 'main'
        if self.page == 'main':
            console.goto(0, 0)
            console.print(screen, f'Level: {self.player.lvl}')
            console.goto(0, 1)
            console.print(screen, f'Money: {self.player.money}')
            console.goto(0, 2)
            console.print(screen, f"Heart: {'/'.join([str(i) for i in self.player.heart])}")
            console.goto(0, 3)
            console.print(screen, f"Attack: {'/'.join([str(i) for i in self.player.attack])}")
            console.goto(0, 4)
            console.print(screen, f"Defense: {'/'.join([str(i) for i in self.player.defense])}")
            console.goto(0, int(screen.get_height() / console.baseheight) - 1)
            console.print(screen, 'esc:back t:things b:bag g:go s:shop')
        elif self.page == 'things':
            console.goto(0, 0)
            console.print(screen, 'Name Attack Defense Enchant', color=(255, 196, 0))
            printthings = self.player.things[self.thingsstartindex:self.thingsstartindex + int(
                screen.get_height() / console.baseheight) - 2]
            for i in range(len(printthings)):
                item = printthings[i]
                console.goto(0, i + 1)
                console.print(screen, f'{item.name} ', color=self.things_color[self.thingsstartindex + i])
                console.print(screen, f'{item.attack} ', color=self.things_color[self.thingsstartindex + i])
                console.print(screen, f'{item.defense} ', color=self.things_color[self.thingsstartindex + i])
                console.print(screen, f'{item.enchant}', color=self.things_color[self.thingsstartindex + i])
            console.goto(0, int(screen.get_height() / console.baseheight) - 1)
            console.print(screen, 'esc:back u:unequip')
        elif self.page == 'bag':
            console.goto(0, 0)
            console.print(screen, 'Name Attack Defense Enchant', color=(255, 196, 0))
            printbag = self.player.bag[
                       self.bagstartindex:self.bagstartindex + int(screen.get_height() / console.baseheight) - 2]
            for i in range(len(printbag)):
                item = printbag[i]
                console.goto(0, i + 1)
                console.print(screen, f'{item.name} ', color=self.bag_color[self.bagstartindex + i])
                console.print(screen, f'{item.attack} ', color=self.bag_color[self.bagstartindex + i])
                console.print(screen, f'{item.defense} ', color=self.bag_color[self.bagstartindex + i])
                console.print(screen, f'{item.enchant}', color=self.bag_color[self.bagstartindex + i])
            console.goto(0, int(screen.get_height() / console.baseheight) - 1)
            console.print(screen, 'esc:back e:equip')
        elif self.page == 'go':
            printlog = self.log[
                       self.logstartindex:self.logstartindex + int(screen.get_height() / console.baseheight) - 2]
            for i in range(len(printlog)):
                console.goto(0, i)
                console.print(screen, printlog[i])
            console.goto(0, int(screen.get_height() / console.baseheight) - 1)
            console.print(screen, 'esc:back e:explore')
        elif self.page == 'shop':
            console.goto(0, 0)
            console.print(screen, 'Name Attack Defense Enchant Money', color=(255, 196, 0))
            printgoods = self.goods[
                         self.goodsstartindex:self.goodsstartindex + int(screen.get_height() / console.baseheight) - 2]
            for i in range(len(printgoods)):
                item = printgoods[i]
                console.goto(0, i + 1)
                console.print(screen, f'{item.name} ', color=self.goods_color[self.goodsstartindex + i])
                console.print(screen, f'{item.attack} ', color=self.goods_color[self.goodsstartindex + i])
                console.print(screen, f'{item.defense} ', color=self.goods_color[self.goodsstartindex + i])
                console.print(screen, f'{item.enchant} ', color=self.goods_color[self.goodsstartindex + i])
                console.print(screen, f'{item.money}', color=self.goods_color[self.goodsstartindex + i])
            console.goto(0, int(screen.get_height() / console.baseheight) - 1)
            console.print(screen, 'esc:back b:buy s:sell')
        return 'play'
