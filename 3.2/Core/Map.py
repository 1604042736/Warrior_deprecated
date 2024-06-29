from Core.Tile import Tile


class Map:
    """游戏地图"""
    instance: "Map" = None

    def __init__(self, length=32, width=32, height=1) -> None:
        self.length = length  # 长
        self.width = width  # 宽
        self.height = height  # 高
        self.blocks: dict[tuple[int, int, int], Block] = {}
        for x in range(self.length):
            for y in range(self.width):
                for z in range(self.height):
                    self.blocks[(x, y, z)] = Block(x, y, z)
        Map.instance = self

    def moveable(self, x: int, y: int, z: int) -> bool:
        """
        判断能否移动到对应坐标
        坐标应该为全局坐标
        """
        if (x, y, z)not in self.blocks:
            return False
        return True


class Block:
    """地图每一个位置都是一个块"""

    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.tile = Tile(0, 0)
