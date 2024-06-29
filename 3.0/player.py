from PyQt5.QtCore import QRect, Qt
from creature import Creature
from globals import Globals
from item import Item


class Player(Creature):
    '''
    玩家
    '''
    TEXTURE_INDEX = 64  # @
    MAX_COUNT=100   #count的最大值

    def __init__(self, x=0, y=0, z=0):
        super().__init__('player', x, y, z)
        self.bag = [Item('wooden_sword'),Item('meat'),Item('water')]
        self.inventory = {'head': None,
                          'body': None,
                          'leg': None,
                          'foot': None,
                          'lefthand': None,
                          'righthand': None}
        self.attack = 0
        self.defense = 0
        self.heart = 100
        self.attackable = ['pig']  # 可以攻击的
        self.money = 1000
        self.conut=0    #计数

    def keyPress(self, a0):
        self._x, self._y, self._z = self.x, self.y, self.z
        if a0.key() == Qt.Key_8:
            self.y -= 1
        elif a0.key() == Qt.Key_2:
            self.y += 1
        elif a0.key() == Qt.Key_4:
            self.x -= 1
        elif a0.key() == Qt.Key_6:
            self.x += 1
        elif a0.key() == Qt.Key_3:
            self.x += 1
            self.y += 1
        elif a0.key() == Qt.Key_9:
            self.x += 1
            self.y -= 1
        elif a0.key() == Qt.Key_7:
            self.x -= 1
            self.y -= 1
        elif a0.key() == Qt.Key_1:
            self.x -= 1
            self.y += 1
        elif a0.key() == Qt.Key_A:
            self.isAttack = not self.isAttack
        elif a0.key() == Qt.Key_P:
            self.pickup()
        elif a0.key()==Qt.Key_L:
            pass
        elif a0.key()==Qt.Key_M:
            pass
        self.collision()
        self.conut+=1
        if self.conut>self.MAX_COUNT:
            self.thirsty+=1
            self.hungry+=1
            self.conut=0

    def pickup(self):
        '''
        拾起掉落物
        '''
        key = f'{self.x}_{self.y}_{self.z}'
        index=len(self.localmap[key])-1
        while index>=0: #从上到下捡掉落物
            item=self.localmap[key][index]
            if item in Globals.items:  # 所在的地方有掉落物
                self.localmap[key].pop(index)
                item.dead = True
                _item = Item(item.realname)
                self.bag.append(_item)
                break  # 只捡一次
            index-=1

    def get_structure(self):
        '''
        得到所在的结构
        '''
        for structure in Globals.structures:
            x,y,z=structure.x,structure.y,structure.z   #起始位置
            #起始位置的对角位置
            nx=x+structure.xl
            ny=y+structure.yl
            nz=z+structure.zl
            if x<=self.x<=nx and y<=self.y<=ny and z<=self.z<=nz: #在这个结构范围内
                return structure.use_structure()