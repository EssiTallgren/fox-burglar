from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem

from collision_detection import CollisionDetection


class Enemy(QGraphicsPixmapItem):
    """ Positive direction in the map is to the right and down. In this case we only observe
    the horizontal movement. """

    def __init__(self, world):
        super().__init__()
        self.world = world
        self.collision = CollisionDetection()

        self.direction = 1
        self.setPixmap(QPixmap('./src/graphics/police_right.png').scaledToHeight(144))

    def update_position(self):
        if self.collision.check_right(self.world, self, 144, 144) == True or self.x() > self.world.x*100 - 144:
            self.direction = -1
            self.setPixmap(QPixmap('./src/graphics/police_left.png').scaledToHeight(144))

        if self.collision.check_left(self.world, self, 144) == True or self.x() <= 0:
            self.direction = 1
            self.setPixmap(QPixmap('./src/graphics/police_right.png').scaledToHeight(144))

        if self.direction == 1:
            self.setX(self.x() + 4)

        if self.direction == -1:
            self.setX(self.x() - 4)
