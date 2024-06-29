from about import *
from console import *
from contiuneplaying import *
from createnewsave import *
from homepage import *
from play import *
import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 618), pygame.DOUBLEBUF | pygame.RESIZABLE)
    pygame.display.set_caption('Warrior')
    console = Console()
    homepage = Homepage()
    about = About()
    createnewsave = CreateNewSave()
    contiuneplaying = ContiunePlaying()
    play = None
    page = 'homepage'
    while True:
        event = pygame.event.wait()
        if event.type == QUIT:
            sys.exit()
        if page == 'homepage':
            page = homepage.updata(screen, console, event)
        elif page == 'about':
            page = about.updata(screen, console, event)
        elif page == 'createnewsave':
            page = createnewsave.updata(screen, console, event)
        elif page == 'contiuneplaying':
            page, savename = contiuneplaying.updata(screen, console, event)
            if savename:
                play = Play(f'data/save/{savename}')
        elif page == 'play':
            page = play.updata(screen, console, event)
        pygame.display.update()
        screen.fill([0, 0, 0])


if __name__ == '__main__':
    main()
