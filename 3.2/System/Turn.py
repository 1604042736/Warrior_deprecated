from Objects.Unit import Unit

from System.Key import Key


class Turn:
    """回合"""
    times = 0  # 当前次数

    __instance = None
    __new_count = 0

    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        cls.__new_count += 1
        return cls.__instance

    def __init__(self) -> None:
        if self.__new_count > 1:
            return
        Key().connect(self)

    def keyPress(self, action):
        if action in ["move_north", "move_south", "move_east", "move_west"]:
            for unit in Unit.instances:
                unit.next_turn()
