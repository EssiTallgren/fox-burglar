from PyQt5.Qt import QGraphicsItem
from PyQt5.QtWidgets import QGraphicsPixmapItem


class CollisionDetection:

    """ Here we check the position of the fox or enemy and compare it to other blocks
    If the border coordinates are (almost) the same, it means the items are touching and the
    function returns TRUE. Checking trap, enemy and victory is only needed for the fox. """
    def __init__(self):
        self.block_size = 100

    def check_bottom(self, world, animal, height, width):
        for block in world.ground_blocks:
            x = block.x()
            y = block.y()
            x_animal = animal.x()
            y_animal_bottom = animal.y() + height
            if width < 100:
                width = 100
            if y + 4 > y_animal_bottom and y - 4 < y_animal_bottom and x_animal >= x - width + 1 and x_animal <= x + self.block_size - 1:
                if y_animal_bottom - y < 4 or y_animal_bottom - y > -4:
                    animal.setY(y - height)
                return True
        return False

    def check_above(self, world, animal, width):
        for block in world.ground_blocks:
            x = block.x()
            y = block.y() + self.block_size
            x_animal = animal.x()
            y_animal = animal.y()
            if width < 100:
                width = 100
            if y + 4 > y_animal and y - 4 < y_animal and x_animal >= x - width + 1 and x_animal <= x + self.block_size - 1:
                if y_animal - y < 4 or y_animal - y > -4:
                    animal.setY(y)
                return True
        return False

    def check_right(self, world, animal, height, width):
        for block in world.ground_blocks:
            x_right = block.x() - width
            y = block.y()
            x_animal = animal.x()
            y_animal = animal.y()
            if x_right + 4 > x_animal and x_right - 4 < x_animal and y_animal > y - height + 1 and y_animal < y + self.block_size:
                if x_animal - x_right or x_animal - x_right > - 4:
                    animal.setX(x_right)
                return True
        return False

    def check_left(self, world, animal, height):
        for block in world.ground_blocks:
            x_left = block.x() + self.block_size
            y = block.y()
            x_animal_right = animal.x()
            y_animal = animal.y()
            if x_left + 4 > x_animal_right and x_left - 4 < x_animal_right and y_animal >= y - height + 1 and y_animal < y + self.block_size:
                if x_animal_right - x_left or x_animal_right - x_left > - 4:
                    animal.setX(x_left)
                return True
        return False

    def check_trap_collision(self, world, fox):
        for trap in world.traps:
            if fox.collidesWithItem(trap):
                return True
        return False

    def check_enemy_collision(self, world, fox):
        for enemy in world.enemies:
            if fox.collidesWithItem(enemy):
                return True
        return False

    def check_victory(self, world, fox):
        if fox.collidesWithItem(world.treasure):
            return True
        return False
