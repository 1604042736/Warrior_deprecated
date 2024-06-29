from Objects.Item import Item
from Objects.Unit import Unit


class Falling(Unit):
    """掉落物"""
    instances: list["Falling"] = []

    def __init__(self, type_: str, x=0, y=0, z=0, parent: "Unit" = None) -> None:
        super().__init__(type_, x, y, z, parent)
        Falling.instances.append(self)

    def pickup(self, target):
        """拾起"""
        Falling.instances.remove(self)
        Unit.instances.remove(self)
        target.inventory.append(Item(self._type))
