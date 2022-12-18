import os

from PIL import Image, ImageQt


class Tile(ImageQt.ImageQt):
    """瓦片贴图"""
    PATH = os.path.join("Data", "Pictures", "Tilemap.bmp")  # 瓦片图片路径
    WIDTH = 8  # 单个瓦片宽度
    HEIGHT = 12  # 单个瓦片高度

    image = Image.open(PATH)
    tiles = [[None for _ in range(16)]for _ in range(16)]
    for i in range(16):
        for j in range(16):
            tiles[i][j] = image.crop((j*WIDTH,
                                     i*HEIGHT,
                                     (j+1)*WIDTH,
                                     (i+1)*HEIGHT))
    image.close()

    def __init__(self, row, col, background_color=(0, 0, 0), color=(255, 255, 255)) -> None:
        """创建一个瓦片对象

        Args:
            row (int): 对应瓦片的行
            col (int): 对应瓦片的列
            background_color (tuple): 背景色
            color (tuple): 前景色
        """
        background_color = tuple(background_color)
        color = tuple(color)

        image = Tile.tiles[row][col]
        w, h = image.size[0], image.size[1]
        for x in range(w):
            for y in range(h):
                r, g, b = image.getpixel((x, y))
                if (r, g, b) == (255, 0, 255):
                    image.putpixel((x, y), background_color)
                elif (r, g, b) == (255, 255, 255):
                    image.putpixel((x, y), color)
        super().__init__(image)
