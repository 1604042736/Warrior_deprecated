import json
import os

from PyQt5.QtCore import QEvent, QObject, Qt
from PyQt5.QtWidgets import QWidget


class Key(QObject):
    """按键管理系统"""
    keybindings: dict = json.load(
        open(os.path.join("Data", "Keybindings.json"), encoding="utf-8"))

    KEY_STR = {}  # 按键对应的字符串
    for key, val in Qt.__dict__.items():
        if key.split("_")[0] == "Key":
            KEY_STR[val] = key.split("_", 1)[-1]

    __instance = None
    __new_count = 0

    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        cls.__new_count += 1
        return cls.__instance

    def __init__(self) -> None:
        if Key.__new_count > 1:
            return
        super().__init__()
        self.connect_obj = []  # 连接的obj
        self.state = "default"  # 状态
        self.qobject: str = ""

    def connect(self, obj):
        self.connect_obj.append(obj)

    def disconnect(self, obj):
        if obj in self.connect_obj:
            self.connect_obj.remove(obj)

    def judge(self, keystr: str, autorepeat: bool = False):
        """根据按键字符串决定行为"""
        for action, val in self.keybindings.items():
            if keystr in val["keys"] and self.check(val.get("condition", {})):
                repeat = val.get("repeat", False)
                if repeat:
                    self.do(val.get("do", []))
                    self.send(action)
                elif not repeat and not autorepeat:
                    self.do(val.get("do", []))
                    self.send(action)

    def check(self, condition: dict):
        """检查条件是否符合要求"""
        results = []
        for rule in condition.get("rules", []):
            if not self.check(rule.get("condition", {})):
                results.append(False)
                continue

            for key, val in rule.items():
                if key == "condition":
                    continue
                if getattr(self, key, None) != val:
                    results.append(False)
                    break
            else:
                results.append(True)

        standard = condition.get("standard", "all")
        if standard == "any":
            return any(results)
        elif standard == "all":
            return all(results)

    def do(self, actions: list[dict]):
        """按键要做的事"""
        for action in actions:
            if self.check(action.get("condition", {})):
                for key, val in action["change"].items():
                    setattr(self, key, val)

    def send(self, action: str):
        """为连接的obj发送行为信息"""
        for i in self.connect_obj:
            getattr(i, "keyPress", lambda _: 0)(action)

    def eventFilter(self, a0: 'QObject', a1: 'QEvent') -> bool:
        if a1.type() == QEvent.Type.KeyPress:
            keystr = self.KEY_STR.get(a1.key(), "")
            self.qobject = a0.__class__.__name__
            self.judge(keystr, a1.isAutoRepeat())
            if isinstance(a0, QWidget):
                a0.repaint()
        return super().eventFilter(a0, a1)
