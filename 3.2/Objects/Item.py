import os

from Core.Material import Material
from Core.Tile import Tile

from Objects.Object import Object


class Item(Object):
    """有材料的物品"""

    def __init__(self, type_: str, material: Material | str = "None", parent: "Object" = None) -> None:
        super().__init__(type_, parent)
        if isinstance(material, str):
            material = Material(material)
        self.material = material
        if self.material:
            self.tile = Tile(
                **(self.attribute.get("Tile", {"row": 0, "col": 0}) | {"color": self.material.color}))
        self.wearable = self.attribute.get("wearable", False)
        self.aggressivity = self.attribute.get("base_aggressivity", 0)
        self.defensivepower = self.attribute.get("base_defensivepower", 0)

    def __str__(self):
        if self.material:
            return f"{self.material} {super().__str__()}"
        else:
            return super().__str__()
