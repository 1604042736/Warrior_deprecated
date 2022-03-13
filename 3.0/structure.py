import json
from globals import Globals
from item import Item


class Structure:
    '''
    建筑结构
    '''

    def __init__(self, name, x=0, y=0, z=0,use=None):
        self.texture = Globals.texture
        self.structure = [[[]]]  # 结构[z][y][x]
        self.x, self.y, self.z = x, y, z
        self.config = json.load(
            open(f'data\structure\{name}.json', encoding='utf-8'))
        self.__dict__ |= self.config
        for zi, z in enumerate(self.structure):
            for yi, y in enumerate(z):
                for xi, x in enumerate(y):
                    self.structure[zi][yi][xi] = Item(x)
        self.use=use    #使用结构
        self.xl=len(self.structure[0][0])   #长
        self.yl=len(self.structure[0])  #宽
        self.zl=len(self.structure) #高

        Globals.structures.append(self)

    def use_structure(self):
        '''
        使用建筑
        '''
        if self.use!=None:
            return self.use()