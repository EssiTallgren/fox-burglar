from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize


class Ending(QWidget):
    """Here is the widget for the ending annotation. Depending on if the user wins or loses
    the game and in wich way, the ending screen varies (the picture for that is the in the
    'background' variable."""

    def __init__(self, menu, background):
        super().__init__()
        self.menu = menu
        self.background = background

        self.setFixedSize(800, 700)

        self.pop_up()

    def pop_up(self):
        imag = QImage(self.background)
        image = imag.scaled(QSize(800, 700))
        palette = QPalette()
        palette.setBrush(10, QBrush(image))
        self.setPalette(palette)

        self.back_to_menu = QPushButton('Back to menu', self)
        self.back_to_menu.move(200, 600)
        self.back_to_menu.clicked.connect(self.to_menu)

        self.start_again = QPushButton('Replay', self)
        self.start_again.move(350,480)
        self.start_again.clicked.connect(self.start)

        self.exit = QPushButton('Exit Game', self)
        self.exit.move(500,600)
        self.exit.clicked.connect(exit)

        self.show()

    def to_menu(self):
        self.menu.show()
        self.menu.initUI()
        self.menu.world.window.close()
        self.close()

    def start(self):
        self.menu.world.fox.setPos(200, 500)
        self.menu.world.timer.start(10)
        self.close()


