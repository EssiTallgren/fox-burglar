from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize, QTimer, Qt

from gui import GUI
from ending import Ending


class World(QGraphicsScene):
    """Here we set up the graphics view and timer for it. We visualize the items that are
    put on the scene in the GUI class and take in the keypressevents."""

    def __init__(self, menu, levelfile):
        super().__init__()
        self.gui = GUI(self)
        self.menu = menu
        self.levelmap = levelfile
        self.keys = set()

        self.x = 0
        self.y = 0
        self.window = None

        self.treasure = None
        self.ground_blocks = []
        self.enemies = []
        self.traps = []
        self.fox = None

        self.level_view()

        self.timer = QTimer(self)
        self.timer.start(10)
        self.timer.timeout.connect(self.window_update)

    def level_view(self):
        self.x, self.y = self.gui.create_map(self.levelmap)
        self.window = QGraphicsView(self)
        self.window.setWindowFlags(Qt.FramelessWindowHint)
        self.window.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.window.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.window.setFixedSize(1500, 800)
        self.setSceneRect(0, 0, self.x*100, self.y*100)

        self.window.setStyleSheet(''' color: none; background-image: url(./src/graphics/level1_background.png); border: none;''')

        self.window.show()

    def keyPressEvent(self, e):
        self.keys.add(e.key())

    def keyReleaseEvent(self, e):
        self.keys.remove(e.key())

    def window_update(self):
        self.update()
        for enemy in self.enemies:
            enemy.update_position()
        self.fox.update_position(self.keys)
        self.window.centerOn(self.fox.pos())

    def loss_victory(self, background):
        ending = Ending(self.menu, background)
        position = self.window.mapToScene(350, 0)
        ending.move(position.toPoint())
        self.addWidget(ending, Qt.Widget)