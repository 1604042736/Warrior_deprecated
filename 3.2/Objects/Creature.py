from Objects.Falling import Falling
from Objects.Unit import Unit


class Creature(Unit):
    """生物"""
    instances = []

    def __init__(self, type_: str, x=0, y=0, z=0, parent: "Unit" = None) -> None:
        super().__init__(type_, x, y, z, parent)
        Creature.instances.append(self)
        self.hp = 10  # 生命值
        self.fallings = self.attribute.get("fallings", [])  # 掉落物

    def attack(self, target: "Creature"):
        """攻击"""
        hurt = self.aggressivity-target.defensivepower
        if hurt < 0:
            hurt = 0
        target.hp -= hurt
        if target.hp <= 0:
            target.die()

    @property
    def aggressivity(self):
        """攻击力"""
        return 0

    @property
    def defensivepower(self):
        """防御力"""
        return 0

    def die(self):
        """死亡"""
        Creature.instances.remove(self)
        Unit.instances.remove(self)
        for falling in self.fallings:
            Falling(falling, self.x, self.y, self.z)
