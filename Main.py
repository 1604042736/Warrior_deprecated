import sys

import multitasking

from Core.Camera import Camera
from Core.Map import Map
from Gui.MapDisplay import MapDisplay
from Objects.Animal import Animal
from Objects.Player import Player
from System.Application import Application
from System.Turn import Turn


def main():
    app = Application(sys.argv)
    Turn()

    map = Map()
    player = Player()
    for i in range(10):
        Animal("Pig", i)

    camera = Camera()
    camera.follow(player)

    mapdisplay = MapDisplay(map, camera)
    mapdisplay.show()

    app.exec()
    multitasking.killall(None, None)


if __name__ == "__main__":
    main()
