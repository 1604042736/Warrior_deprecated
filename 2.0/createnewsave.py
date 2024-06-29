import json
import os

from pygame.locals import *


class CreateNewSave:
    def updata(self, screen, console, event):
        i = 0
        while True:
            if not os.path.exists(f'data/save/region{i}'):
                break
            i += 1
        if event.type == KEYDOWN:
            if event.key == K_KP_ENTER:
                os.makedirs(f'data/save/region{i}')
                saveinfo = {'lvl': 1,
                            'money': 100,
                            'heart': [100, 100],
                            'attack': [1, 100],
                            'defense': [1, 100],
                            'things': [['None', 0, 0, 'None']] * 6,
                            'bag': []}
                json.dump(saveinfo, open(f'data/save/region{i}/config.json', mode='w', encoding='utf-8'))
                return 'homepage'
            elif event.key == K_ESCAPE:
                return 'homepage'
        console.goto(0, 0)
        console.print(screen, 'Save Path: data/save')
        console.goto(0, 1)
        console.print(screen, f'Save Name: region{i}')
        console.goto(0, 2)
        console.print(screen,
                      'If you want to change the name, please modify it in the archive directory after it is created',
                      color=(255, 0, 0))
        console.goto(0, int(screen.get_height() / console.baseheight) - 1)
        console.print(screen, 'enter:create  esc:back')
        return 'createnewsave'
