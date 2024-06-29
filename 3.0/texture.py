from PIL import Image, ImageQt


class Texture(list):
    '''
    关于贴图的一些操作
    '''

    def __init__(self):
        self.width = 8
        self.height = 12
        image = Image.open(r'data\art\curses_640x300.bmp')
        for i in range(16):
            for j in range(16):
                _ = (j*self.width, i*self.height, (j+1)
                     * self.width, (i+1)*self.height)
                self.append(ImageQt.ImageQt(image.crop(_)))

    def replace_color(self, image, oldcolor, newcolor):
        '''
        替换图片中的颜色
        '''
        if isinstance(image, int):
            image = ImageQt.fromqimage(self[image])
        elif isinstance(image, ImageQt.QImage):
            image = ImageQt.fromqimage(image)
        w, h = image.size[0], image.size[1]
        for x in range(w):
            for y in range(h):
                r, g, b = image.getpixel((x, y))
                if (r, g, b) == oldcolor:
                    image.putpixel((x, y), newcolor)
        return ImageQt.ImageQt(image)
