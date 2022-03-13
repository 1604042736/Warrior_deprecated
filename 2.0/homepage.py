import sys

from pygame.locals import *


class Homepage:
    def __init__(self):
        self.homepage_line = 20
        self.button_num = 4
        self.button_color = [(200, 200, 200)] * self.button_num
        self.button_index = 0
        self.change_button()

    def updata(self, screen, console, event):
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                self.button_index = (self.button_index + 1) % self.button_num
            elif event.key == K_UP:
                self.button_index = (self.button_index - 1) % self.button_num
            elif event.key == K_KP_ENTER:
                if self.button_index == 0:
                    return 'contiuneplaying'
                elif self.button_index == 1:
                    return 'createnewsave'
                elif self.button_index == 2:
                    return 'about'
                elif self.button_index == 3:
                    sys.exit()
            self.change_button()
        console.print_center(screen, 'Welcome to Warrior', self.homepage_line, 0)
        console.print_center(screen, 'Contiune Playing', self.homepage_line, 6, color=self.button_color[0])
        console.print_center(screen, 'Create New Save', self.homepage_line, 7, color=self.button_color[1])
        console.print_center(screen, 'About', self.homepage_line, 8, color=self.button_color[2])
        console.print_center(screen, 'Quit', self.homepage_line, 9, color=self.button_color[3])
        console.goto(0, int(screen.get_height() / console.baseheight) - 1)
        console.print(screen, 'Made By YongjianWang')
        return 'homepage'

    def change_button(self):
        self.button_color = [(200, 200, 200)] * self.button_num
        self.button_color[self.button_index] = (255, 255, 255)
