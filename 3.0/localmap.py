from PyQt5.QtCore import QRect
from creature import Creature
from globals import Globals
from item import Item
from page import Page
from shop import Shop
from structure import Structure
from animal import Animal
from noise import pnoise2


class LocalMap(dict, Page):
    '''
    本地地图
    '''

    def __init__(self):
        self.player = Globals.player
        self.texture = Globals.texture
        self.window = Globals.window
        self.width, self.height = 16, 24
        self.create_world()

        self.camera = self.player  # 摄像机
        self.update = True

    def check_hill(self):
        '''
        检查世界中的上下坡
        详见doc/check_hill.png
        '''
        checked=[]  #已经检查过了的
        for key in list(self.keys()):
            val=self[key]
            x,y,z=key.split('_')
            x=int(x)
            y=int(y)
            z=int(z)
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                key1=f'{x+dx}_{y+dy}_{z+1}'   #上面一层
                key2=f'{x}_{y}_{z+1}'   #该位置的上一层
                if key1 not in checked and key1 in self:    #有上面一层
                    #建造斜坡
                    if key2 not in self:
                        #其实就是为了能够让上一层显示这一层的斜坡
                        self[key2]=[]
                        self[key2].append(Item("downhill")) #在这一层的正上方放下坡
                    val.append(Item("uphill"))  #在这一层放上坡
                    checked.append(key)
                    checked.append(key2)
                key1=f'{x+dx}_{y+dy}_{z-1}'
                key2=f'{x+dx}_{y+dy}_{z}'
                if key1 not in checked and key1 in self:    #有下面一层
                    #同理
                    if key2 not in self:
                        self[key2]=[]
                        self[key2].append(Item("downhill"))
                    self[key1].append(Item("uphill"))
                    checked.append(key)
                    checked.append(key2)

    def create_world(self):
        '''
        创建世界
        '''
        N=6
        #只生成最上层
        for i in range(N):
            for j in range(N):
                x,y=i/N,j/N
                z=int(pnoise2(x,y)*N)
                x,y=i*N,j*N
                #扩大N倍
                for a in range(N):
                    for b in range(N):
                        key = f'{x+a}_{y+b}_{z}'
                        if key not in self:
                            self[key]=[]
                        self[key].append(Item('ground'))
        self.check_hill()
        x,y,z=list(self.items())[0][0].split('_')
        x=int(x)
        y=int(y)
        z=int(z)
        self.player.x,self.player.y,self.player.z=x,y,z
        for i in range(16):
            animal=Animal('pig',x,y,z)
            Globals.animals.append(animal)
            self.place_item(animal)
        for i in range(-5,0):
            for j in range(-5,0):
                key = f'{i}_{j}_0'
                if key not in self:
                    self[key]=[]
                self[key].append(Item('ground'))
        self.place_structure(Structure('shop',-5,-5,0,use=Shop))

    def place_structure(self, structure):
        '''
        放置结构
        '''
        # 一次把结构中的item添加到地图中
        for zi, z in enumerate(structure.structure):
            for yi, y in enumerate(z):
                for xi, x in enumerate(y):
                    self[f'{structure.x+xi}_{structure.y+yi}_{structure.z+zi}'].append(
                        x)

    def place_item(self, item):
        '''
        放置item
        '''
        key = f'{item.x}_{item.y}_{item.z}'
        _key = f'{item._x}_{item._y}_{item._z}'
        try:
            for index, _item in enumerate(self[_key]):
                if _item.realname == item.realname:
                    self[_key].pop(index)
                    if not self[_key]:  # 该方块没有item了
                        self.pop(_key)
                    break
            else:   #窗口大小改变的时侯会进入
                if key!=_key:   #不是第一次
                    return
            if isinstance(item, Creature):  # 是生物
                if not item.dead:
                    try:
                        self[key].append(item)
                    except KeyError:  # 掉出了世界......
                        item.dead = True
            else:
                if key not in self:
                    self[key] = []
                self[key].append(item)
        except KeyError:
            pass

    def draw(self, qp):
        '''
        根据玩家位置调整画图位置
        '''
        # 绘制动物
        if self.update:
            for animal in Globals.animals:
                animal.action()
                self.place_item(animal)
        for item in Globals.items:
            self.place_item(item)
        # 绘制摄像机
        self.place_item(self.camera)
        # 将窗口划分成块
        gamewidth = int(self.window.width()/self.width)
        gameheight = int(self.window.height()/self.height)
        halfgamewidth = int(gamewidth/2)
        halfgameheight = int(gameheight/2)
        halfrealwidth = halfgamewidth*self.width
        halfrealheight = halfgameheight*self.height
        # 绘制世界
        # 计算左上角方块位置
        minx = self.camera.x-halfgamewidth
        miny = self.camera.y-halfgameheight
        # 计算右下角方块位置
        maxx = self.camera.x+halfgamewidth
        maxy = self.camera.y+halfgameheight
        # 绘制这个区间的方块
        for x in range(minx, maxx+1):
            for y in range(miny, maxy+1):
                try:
                    for i in self[f'{x}_{y}_{self.camera.z}']:
                        # 计算与摄像机的相对位置
                        _x = self.camera.x-x
                        _y = self.camera.y-y
                        qp.drawImage(QRect(halfrealwidth-_x*self.width, halfrealheight -
                                     _y*self.height, self.width, self.height), i.image)
                except KeyError:
                    pass
