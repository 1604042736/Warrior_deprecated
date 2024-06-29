from globals import Globals
from page import Page
from list import List

class PauseGame(Page):
    '''
    暂停游戏
    '''
    def __init__(self):
        self.set_list()

    def set_list(self):
        self.list=List(event=self.listevent)
        self.list+=['返回游戏','退出']

    def draw(self, qp):
        self.list.draw(qp)

    def keyPress(self, a0):
        self.list.keyPress(a0)

    def listevent(self,index,item):
        if item=='返回游戏':
            Globals.window.page.pop()
        elif item=='退出':
            Globals.window.exit()