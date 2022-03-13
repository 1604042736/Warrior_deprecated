import os

from pygame.locals import *


class ContiunePlaying:
    def __init__(self):
        self.button_index = 0
        self.saves = []

    def updata(self, screen, console, event):
        if event.type == KEYDOWN:
            if event.key == K_DOWN and self.saves:
                self.button_index = (self.button_index + 1) % len(self.saves)
            elif event.key == K_UP and self.saves:
                self.button_index = (self.button_index - 1) % len(self.saves)
            elif event.key == K_KP_ENTER and self.saves:
                return 'play', self.saves[self.button_index]
            elif event.key == K_ESCAPE:
                return 'homepage', None
        self.saves = os.listdir('data/save')
        self.button_color = [(200, 200, 200)] * len(self.saves)
        self.change_button()
        if not self.saves:
            console.print_center(screen, "You don't have saves yet", 1, 0, color=(0, 0, 255))
        else:
            for i in range(len(self.saves)):
                console.goto(0, i)
                console.print(screen, f'{self.saves[i]}', color=self.button_color[i])
        console.goto(0, int(screen.get_height() / console.baseheight) - 1)
        console.print(screen, 'enter:join the save  esc:back')
        return 'contiuneplaying', None

    def change_button(self):
        try:
            self.button_color = [(200, 200, 200)] * len(self.saves)
            self.button_color[self.button_index] = (255, 255, 255)
        except:
            pass
