import sys, os, shutil, json, time, random
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from __pyqt__.Warrior import *
from Player import *


class Warrior(QWidget, Ui_Warrior):
    def __init__(self, config):
        super().__init__()
        self.setupUi(self)
        self.config = config
        self.set_lw_gamelist()

        self.pb_singleplayer.clicked.connect(lambda: self.sw_main.setCurrentIndex(1))
        self.pb_back.clicked.connect(lambda: self.sw_main.setCurrentIndex(0))
        self.pb_newgame.clicked.connect(lambda: self.sw_main.setCurrentIndex(2))
        self.pb_canel.clicked.connect(lambda: self.sw_main.setCurrentIndex(1))
        self.pb_del.clicked.connect(lambda: self.sw_main.setCurrentIndex(3))
        self.pb_no.clicked.connect(lambda: self.sw_main.setCurrentIndex(1))
        self.pb_back_2.clicked.connect(lambda: self.sw_main.setCurrentIndex(1))
        self.pb_openfoder.clicked.connect(
            lambda: os.startfile(self.config['path'] + f'\\saves\\{self.lw_gamelist.currentItem().text()}'))
        self.pb_yes.clicked.connect(self.delgame)
        self.pb_create.clicked.connect(self.newgame)
        self.pb_edit.clicked.connect(self.edit)
        self.pb_startgame.clicked.connect(self.startgame)
        self.pb_back_3.clicked.connect(self.backandsave)

        self.pb_back_4.clicked.connect(lambda: self.sw_main.setCurrentIndex(5))
        self.pb_back_5.clicked.connect(lambda: self.sw_main.setCurrentIndex(5))
        self.pb_back_6.clicked.connect(lambda: self.sw_main.setCurrentIndex(5))
        self.pb_back_7.clicked.connect(lambda: self.sw_main.setCurrentIndex(5))
        self.pb_go.clicked.connect(lambda: self.sw_main.setCurrentIndex(6))
        self.pb_enchant.clicked.connect(lambda: self.sw_main.setCurrentIndex(7))
        self.pb_equip.clicked.connect(lambda: self.sw_main.setCurrentIndex(8))
        self.pb_shop.clicked.connect(lambda: self.sw_main.setCurrentIndex(9))
        self.pb_search.clicked.connect(self.search)

        self.lw_gamelist.itemClicked.connect(self.lw_gamelist_itemClicked)

    def startgame(self):
        name = self.lw_gamelist.currentItem().text()
        gamepath = self.config['path'] + f'\\saves\\{name}'
        self.player = Player(json.load(open(gamepath + '\\config.json', encoding='utf-8')))
        self.set_playerinfo()
        self.set_lw_things()
        self.set_lw_bag()
        self.set_lw_enchant()
        self.set_lw_goods()
        self.sw_main.setCurrentIndex(5)

    def set_playerinfo(self):
        self.label_playername.setText(f'玩家名: {self.player.config["playername"]}')
        self.label_lvl.setText(f'等级: {self.player.config["lvl"]}')
        self.label_money.setText(f'金币: {self.player.config["money"]}')
        self.label_heart.setText(f'血量: {"/".join([str(i) for i in self.player.config["heart"]])}')
        self.label_attack.setText(f'攻击力: {"/".join([str(i) for i in self.player.config["attack"]])}')
        self.label_defense.setText(f'防御力: {"/".join([str(i) for i in self.player.config["defense"]])}')

    def search(self):
        self.searchthread = Search()
        self.searchthread.AddMoney.connect(self.player.addmoney)
        self.searchthread.Finished.connect(self.finishsearch)
        self.searchthread.start()
        self.pb_attack.setEnabled(False)
        self.pb_search.setEnabled(False)
        self.pb_back_4.setEnabled(False)

    def finishsearch(self):
        self.pb_attack.setEnabled(True)
        self.pb_search.setEnabled(True)
        self.pb_back_4.setEnabled(True)
        self.set_playerinfo()

    def set_lw_things(self):
        self.lw_things.clear()
        self.lw_enchantthing.clear()
        for i in self.player.config['things']:
            self.lw_things.addItem(' '.join([str(j) for j in i]))
            self.lw_enchantthing.addItem(' '.join([str(j) for j in i]))

    def set_lw_bag(self):
        self.lw_bag.clear()
        self.lw_bag_2.clear()
        for i in self.player.config['bag']:
            self.lw_bag.addItem(' '.join([str(j) for j in i]))
            self.lw_bag_2.addItem(' '.join([str(j) for j in i]))

    def set_lw_enchant(self):
        self.lw_enchant.clear()
        for i in self.player.chant:
            self.lw_enchant.addItem(' '.join([str(j) for j in i]))

    def set_lw_goods(self):
        self.lw_goods.clear()
        for i in self.player.goods:
            self.lw_goods.addItem(' '.join([str(j) for j in i]))

    def backandsave(self):
        json.dump(self.player.config, open(self.player.config['path'] + '\\config.json', mode='w', encoding='utf-8'))
        self.sw_main.setCurrentIndex(1)

    def delgame(self):
        gamename = self.lw_gamelist.currentItem().text()
        shutil.rmtree(self.config['path'] + f'\\saves\\{gamename}')
        self.set_lw_gamelist()
        self.sw_main.setCurrentIndex(1)

    def newgame(self):
        name = self.le_name.text()
        path = self.config['path'] + f'\\saves\\{name}'
        os.makedirs(path)
        playerinitinfo = {
            'path': path,
            'playername': self.config['path'].split('\\')[-1],
            'lvl': 0,
            'money': 100,
            'heart': [100, 100],
            'attack': [1, 100],
            'defense': [1, 100],
            'things': [['nothing', 'nothing', 0, 0] for i in range(9)],
            'bag': []
        }
        json.dump(playerinitinfo, open(path + '\\config.json', mode='w', encoding='utf-8'))
        self.set_lw_gamelist()
        self.sw_main.setCurrentIndex(1)

    def edit(self):
        self.le_name_2.setText(self.lw_gamelist.currentItem().text())
        self.sw_main.setCurrentIndex(4)

    def lw_gamelist_itemClicked(self):
        self.pb_startgame.setEnabled(True)
        self.pb_del.setEnabled(True)
        self.pb_edit.setEnabled(True)

    def set_lw_gamelist(self):
        self.lw_gamelist.clear()
        savespath = self.config['path'] + '\\saves'
        if not os.path.exists(savespath):
            os.makedirs(savespath)
        for i in os.listdir(savespath):
            if os.path.isdir(savespath + '\\' + i):
                self.lw_gamelist.addItem(i)

    def resizeEvent(self, QResizeEvent):
        self.sw_main.resize(self.width(), self.height())


class Search(QThread):
    AddMoney = pyqtSignal(int)
    Finished = pyqtSignal()

    def run(self):
        time.sleep(random.uniform(0, 1))
        self.AddMoney.emit(random.randint(0, 100))
        self.Finished.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    warrior = Warrior({'path': sys.argv[1]})
    warrior.show()
    sys.exit(app.exec_())
