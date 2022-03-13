import pygame


class Console:
    def __init__(self):
        self.size = 16
        self.cursor = [0, 0]
        self.font = pygame.font.Font('./data/font/minecraft.ttf', self.size)
        self.baseadvance = self.font.metrics('a')[0][4]
        self.baseheight = self.font.get_linesize()

    def goto(self, x, y):
        self.cursor = [x, y]

    def print(self, screen, text, color=(255, 255, 255)):
        # https://blog.csdn.net/qq_41556318/article/details/86303502
        for i in text:
            surface = self.font.render(i, True, color)
            metrics = self.font.metrics(i)
            advance = metrics[0][4]
            screen.blit(surface, (self.cursor[0] * self.baseadvance - int((advance - self.baseadvance) / 2),
                                  self.cursor[1] * self.baseheight))
            self.cursor[0] += 1
            '''if self.cursor[0] > int(screen.get_width() / self.baseadvance):
                self.cursor[0] = 0
                self.cursor[1] += 1'''

    def print_center(self, screen, text, line, num, color=(255, 255, 255)):
        self.goto(int((screen.get_width() / self.baseadvance - len(text)) / 2),
                  int((screen.get_height() / self.baseheight - line) / 2) + num)
        self.print(screen, text, color=color)
