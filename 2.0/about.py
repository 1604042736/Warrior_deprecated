from pygame.locals import *


class About:
    def updata(self, screen, console, event):
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return 'homepage'
        console.print_center(screen, 'Warrior[Version 1.0]', 3, 0)
        console.print_center(screen, 'Python[Version 3.9.1]', 3, 1)
        console.print_center(screen, 'Pygame[Version 2.0.1]', 3, 2)
        console.goto(0, int(screen.get_height() / console.baseheight) - 1)
        console.print(screen, 'esc:back')
        return 'about'
