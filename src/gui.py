from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.Qt import QGraphicsItem
from PyQt5.QtCore import QSize

from enemy import Enemy
from fox import Fox

from corrupted_file import *


class GUI:
    """Here we set up the items that go on the scene (world). We go trough the map file
    and put the items on the locations that are indicated on the map file."""

    def __init__(self, world):
        self.world = world

    def create_map(self, filename):
        # Here we go through the map file and with its directions we put the objects in the scene.
        x = 0
        y = 0
        try:
            file = open(filename, 'r')
            while True:
                line = file.readline()
                if line == '': # Check if it is the end of file
                    file.close()
                    if self.world.fox == None:
                        raise CorruptedChessFileError("Map does not have player")
                    if self.world.treasure == None:
                        raise CorruptedChessFileError("Map does not have victory")
                    return x, y
                else:
                    x = 0
                    line = line.strip()
                    line = line.split(' ')
                    for letter in line:
                        if letter == '.':
                            # Empty space
                            pass

                        elif letter == 'g':
                            # Groundblock with grass
                            grassblock = QGraphicsPixmapItem()
                            grassblock.setPos(100*x, 100*y)
                            grassblock.setPixmap(QPixmap('./src/graphics/ground1_lvl1.png'))
                            self.world.addItem(grassblock)
                            self.world.ground_blocks.append(grassblock)

                        elif letter == 'G':
                            # Solid groundblock
                            block = QGraphicsPixmapItem()
                            block.setPos(100*x, 100*y)
                            block.setPixmap(QPixmap('./src/graphics/ground2_lvl1.png'))
                            self.world.addItem(block)
                            self.world.ground_blocks.append(block)

                        elif letter == 'R':
                            # Rock block
                            rock = QGraphicsPixmapItem()
                            rock.setPos(100*x, 100*y)
                            rock.setPixmap(QPixmap('./src/graphics/rok.png'))
                            self.world.addItem(rock)
                            self.world.ground_blocks.append(rock)

                        elif letter == 'E':
                            # Enemy
                            doggy = Enemy(self.world)
                            doggy.setPos(100*x, 100*y - 44)
                            self.world.addItem(doggy)
                            self.world.enemies.append(doggy)

                        elif letter == 'V':
                            # Victory (a treasure that the fox steals)
                            tresure = QGraphicsPixmapItem()
                            tresure.setPos(100*x, 100*y)
                            tresure.setPixmap(QPixmap('./src/graphics/treasure.png'))
                            self.world.addItem(tresure)
                            self.world.treasure = tresure

                        elif letter == 'T':
                            # Trap
                            trap = QGraphicsPixmapItem()
                            trap.setPos(100*x, 100*y + 30)
                            trap.setPixmap(QPixmap('./src/graphics/trap.png').scaledToWidth(100))
                            self.world.addItem(trap)
                            self.world.traps.append(trap)


                        elif letter == 'F':
                            # Fox, the player
                            foxy = Fox(self.world)
                            foxy.setPos(100*x, 100*y + 16)
                            self.world.addItem(foxy)
                            self.world.fox = foxy

                        else:
                            raise CorruptedChessFileError("Wrong letter in file")

                        x += 1
                    y += 1

        except OSError:
            raise CorruptedChessFileError("Unknown file")
