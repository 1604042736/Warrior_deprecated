from globals import Globals
from item import Item


class Creature(Item):
    '''
    生物的基类
    '''
    map = {}  # 保存生物名称

    def __init__(self, name, x=0, y=0, z=0):
        self.hungry=0 #饥饿度
        self.thirsty=0  #口渴度
        self.dropobj = []  # 掉落物
        if name not in Creature.map:
            Creature.map[name] = 0
        realname = f'{name}#{Creature.map[name]}'
        Creature.map[name] += 1
        super().__init__(realname)
        self.realname = realname
        self.x, self.y, self.z = x, y, z
        self._x, self._y, self._z = self.x, self.y, self.z  # 纪录上一次位置
        self.uncross = []  # 不可以跨过的
        self.attackable = []  # 可以攻击的
        self.isAttack = False  # 是否处于攻击状态
        self.dead = False  # 是否死亡

    def collision(self):
        '''
        检测碰撞
        '''
        if not self.localmap:
            self.localmap = Globals.localmap
        # 是否越界
        key = f'{self.x}_{self.y}_{self.z}'
        if key not in self.localmap:
            # 恢复
            self.x, self.y, self.z = self._x, self._y, self._z
            if not self.uphill():   #不能上坡
                if not self.downhill(): #不能下坡
                    return
        try:
            for index, item in enumerate(self.localmap[f'{self.x}_{self.y}_{self.z}']):
                name = item.realname.split('#')[0]
                if name in self.uncross:
                    self.x, self.y,self.z = self._x, self._y,self._z
                    break
                if self.isAttack and name in self.attackable:
                    item.heart = item.heart-self.attack+item.defense
                    if item.heart <= 0:  # 死亡
                        self.localmap[f'{item.x}_{item.y}_{item.z}'].pop(index)
                        item.dead = True
                        #处理掉落物
                        for obj in item.dropobj:
                            # 先把他当成生物把[doge]
                            Globals.items.append(
                                Creature(obj, item.x, item.y, item.z))
        except:
            pass

    def uphill(self):
        '''
        上坡
        '''
        try:
            key = f'{self.x}_{self.y}_{self.z}'
            for item in self.localmap[key]:
                if item.realname=='uphill':
                    self.z+=1
                    key = f'{self.x}_{self.y}_{self.z}'
                    if key in self.localmap:
                        return True
                    else:
                        self.z-=1
        except:
            pass

    def downhill(self):
        '''
        下坡
        '''
        try:
            key = f'{self.x}_{self.y}_{self.z}'
            for item in self.localmap[key]:
                if item.realname=='downhill':
                    self.z-=1
                    key = f'{self.x}_{self.y}_{self.z}'
                    if key in self.localmap:
                        return True
                    else:
                        self.z+=1
        except:
            pass

    def __str__(self):
        text=super().__str__()
        for key in ('hungry','thirsty'):
            val = self.__dict__[key]
            text += f'{key}={val},'
        return text