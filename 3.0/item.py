import json
from globals import Globals


class Item:
    '''
    游戏中物品的基类
    '''

    def __init__(self, name):
        self.texture = Globals.texture
        self.localmap = Globals.localmap
        self.window = Globals.window
        self.heart = 100
        self.attack = 0  # 攻击力
        self.defense = 0  # 防御力
        self.part = []  # 穿戴部位
        self.value = 0  # 价值
        self.realname = name.split('#')[0]  # 实际的名称
        self.weight = 1  # 重量
        self.eat=0   #减少的饥饿度,0为不能吃
        self.drink=0  #同上
        self.config = json.load(
            open(f'data\\item\\{name.split("#")[0]}.json', encoding='utf-8'))
        self.__dict__ |= self.config
        self.name = self.config['name']  # 显示的名称
        self.image = self.texture[self.config['texture_index']]
        for colors in self.config['replace_colors']:
            self.image = self.texture.replace_color(
                self.image, tuple(colors[0]), tuple(colors[1]))

    def __str__(self):
        text = f'{self.name}->'
        for key in ('realname', 'heart', 'attack', 'defense'):
            val = self.__dict__[key]
            text += f'{key}={val},'
        return text
