import json
import os

from Core.Tile import Tile
from PyQt5.QtCore import QCoreApplication

_translate = QCoreApplication.translate


class Object:
    """游戏中所有东西的基类"""
    OBJECTS_PATH = os.path.join("Data", "Objects")

    def __init__(self, type_: str, parent: "Object" = None) -> None:
        self.__parent = parent
        self._type = type_
        self.attribute = json.load(
            open(os.path.join(self.OBJECTS_PATH, f"{type_}.json"), encoding="utf-8"))
        self.tile = Tile(**self.attribute.get("Tile", {"row": 0, "col": 0}))
        self.name = _translate(
            "Object", self.attribute.get("name", self._type))

    def __str__(self) -> str:
        return self.name

    @property
    def parent(self):
        return self.__parent
