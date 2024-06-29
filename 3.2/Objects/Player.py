from Gui.AttackIndicator import AttackIndicator
from Gui.EquipmentViewer import EquipmentViewer
from Gui.InventoryViewer import InventoryViewer
from Gui.Pickuper import Pickuper
from System.Key import Key

from Objects.Creature import Creature
from Objects.Item import Item
from Objects.Unit import Unit


class Player(Creature):
    """玩家"""
    __instance = None
    __new_count = 0

    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        cls.__new_count += 1
        return cls.__instance

    def __init__(self, x=0, y=0, z=0, parent: "Unit" = None) -> None:
        if self.__new_count > 1:
            return
        super().__init__("Player", x, y, z, parent)
        self.inventory = [Item("Sword", "Wood")]*10
        self.equipments = {
            "head": None,
            "body": None,
            "leg": None,
            "feet": None,
            "left_hand": None,
            "right_hand": Item("Sword", "Wood"),
        }
        Key().connect(self)

    def equip(self, bodypart, equipment):
        if self.equipments[bodypart]:
            self.inventory.append(self.equipments[bodypart])
        self.equipments[bodypart] = equipment
        if equipment in self.inventory:
            self.inventory.remove(equipment)

    def keyPress(self, action: str):
        if action == "move_north":
            self.y += 1
        elif action == "move_south":
            self.y -= 1
        elif action == "move_east":
            self.x += 1
        elif action == "move_west":
            self.x -= 1
        elif action == "view_equipment":
            self.equipmentviewer = EquipmentViewer(self)
            self.equipmentviewer.show()
        elif action == "quit_view_equipment":
            self.equipmentviewer.close()
        elif action == "view_inventory":
            self.inventoryviewer = InventoryViewer(self)
            self.inventoryviewer.show()
        elif action == "quit_view_inventory":
            self.inventoryviewer.close()
        elif action == "indicate_attack":
            self.attackindicator = AttackIndicator(self)
            self.attackindicator.show()
        elif action == "quit_indicate_attack":
            self.attackindicator.close()
        elif action == "pickup":
            self.pickuper = Pickuper(self)
            self.pickuper.show()
        elif action == "quit_pickup":
            self.pickuper.hide()

    @property
    def aggressivity(self):
        if self.equipments["right_hand"] != None:
            return self.equipments["right_hand"].aggressivity
        return super().aggressivity

    @property
    def defensivepower(self):
        dp = 0
        for i in ["head", "body", "feet", "leg"]:
            if self.equipments[i] != None:
                dp += self.equipments[i].defensivepower
        return dp
