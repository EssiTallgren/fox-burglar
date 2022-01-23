from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem

from collision_detection import CollisionDetection


class Fox(QGraphicsPixmapItem):
    # Positive moving direction is to right and down

    pixels = 6 # The amount the player moves per frame, aka speed.
    gravity = 0.4 # Slows down the upwards speed when jumping and causes the downwards speed when falling
    jump_timer = 0
    jump_pixels = 14
    jumping = False
    falling_timer = 16

    def __init__(self, world):
        super().__init__()
        self.world = world
        self.collision = CollisionDetection()

        self.setPixmap(QPixmap('./src/graphics/foxy_right.png').scaledToWidth(100))

    def update_position(self, keys):

        movement_horizontal = 0

        if Qt.Key_A in keys:
            if self.collision.check_left(self.world, self, 84) == False and self.x() > 0:
                movement_horizontal -= Fox.pixels
                self.setPixmap(QPixmap('./src/graphics/foxy_left.png').scaledToWidth(100))
                self.setX(self.x() + movement_horizontal)
            else:
                pass

        if Qt.Key_D in keys:
            if self.collision.check_right(self.world, self, 84, 100) == False and self.x() < self.world.x*100 - 100:
                movement_horizontal += Fox.pixels
                self.setPixmap(QPixmap('./src/graphics/foxy_right.png').scaledToWidth(100))
                self.setX(self.x() + movement_horizontal)
            else:
                pass
        # jumping functions
        if Qt.Key_Space in keys:
            if self.collision.check_bottom(self.world, self, 84, 100) == True and self.collision.check_above(self.world, self, 100) == False:
                Fox.jumping = True
                Fox.jump_timer = 0

        if Fox.jump_timer == 38 or self.collision.check_above(self.world, self, 100) == True:
            Fox.jumping = False
            Fox.jump_pixels = 10

        if Qt.Key_Escape in keys:
            self.world.timer.stop()
            self.world.menu.show()
            self.world.menu.initUI()
            self.world.window.close()

        # Falling functions
        if self.collision.check_bottom(self.world, self, 84, 100) == False and self.jumping == False:
            self.setY(self.y() + 10 - Fox.falling_timer*Fox.gravity)
            if Fox.falling_timer > 5:
                Fox.falling_timer -= 1

        if self.collision.check_bottom(self.world, self, 84, 100) == True:
            Fox.falling_timer = 16

        self.drop()
        self.jump()
        self.enemy_touch()
        self.trap_touch()
        self.treasure_touch()

    def jump(self):
        if Fox.jumping == True:
            if Fox.jump_timer < 38:
                self.setY(self.y() - Fox.jump_pixels)
                if Fox.jump_pixels > 4:
                    Fox.jump_pixels -= Fox.gravity
                Fox.jump_timer += 1

    def enemy_touch(self):
        if self.collision.check_enemy_collision(self.world, self) == True:
            self.world.loss_victory('./src/graphics/police_oh_nou.png')
            self.world.timer.stop()

    def trap_touch(self):
        if self.collision.check_trap_collision(self.world, self) == True:
            self.world.loss_victory('./src/graphics/trap_ouchie.png')
            self.world.timer.stop()

    def treasure_touch(self):
        if self.collision.check_victory(self.world, self) == True:
            self.world.loss_victory('./src/graphics/victory.png')
            self.world.timer.stop()

    def drop(self):
        if self.y() > self.world.y*100:
            self.world.loss_victory('./src/graphics/off_the_map.png')
            self.world.timer.stop()









