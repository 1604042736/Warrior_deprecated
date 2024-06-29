import json
import os

from PyQt5.QtCore import QCoreApplication

_translate = QCoreApplication.translate


class Material:
    """材料"""
    MATERIALS_PATH = os.path.join("Data", "Materials")

    def __init__(self, type_: str) -> None:
        self._type = type_
        if type_ == "None":
            self.attribute = {"name": ""}
        else:
            self.attribute = json.load(
                open(os.path.join(self.MATERIALS_PATH, f"{type_}.json"), encoding="utf-8"))
        self.color = tuple(self.attribute.get("color", (255, 255, 255)))
        self.name = _translate(
            "Material", self.attribute.get("name", self._type))

    def __str__(self) -> str:
        return self.name

    def __bool__(self) -> bool:
        return self._type != "None"
