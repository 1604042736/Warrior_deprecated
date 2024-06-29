import json

from item import *


class Player:
    def __init__(self, config):
        self.money = int(config['money'])
        self.heart = config['heart']
        self.attack = config['attack']
        self.defense = config['defense']
        self.lvl = config['lvl']
        self.things = []
        for i in config['things']:
            self.things.append(Item(i[0], int(i[1]), int(i[2]), i[3]))
        self.bag = []
        for i in config['bag']:
            self.bag.append(Item(i[0], int(i[1]), int(i[2]), i[3]))

    def save(self, savepath):
        savedict = {'money': self.money,
                    'heart': self.heart,
                    'attack': self.attack,
                    'defense': self.defense,
                    'lvl': self.lvl,
                    'things': [[i.name, i.attack, i.defense, i.enchant] for i in self.things],
                    'bag': [[i.name, i.attack, i.defense, i.enchant] for i in self.bag]}
        json.dump(savedict, open(f'{savepath}/config.json', encoding='utf-8', mode='w'))
