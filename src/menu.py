import os
from threading import Thread

from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from world import World

class Menu(QWidget):
    """Here we make the menu widget and take the user to different levels or info window."""

    def __init__(self):
        super().__init__()
        self.initUI()
        self.world = None
        self.control = None

    def initUI(self):
        # Making the main menu window graphics and buttons.
        self.lvl1 = QPushButton('Level 1', self)
        self.lvl1.move(100, 250)
        self.lvl1.clicked.connect(self.level_1)

        self.lvl2 = QPushButton('Level 2', self)
        self.lvl2.move(100, 350)
        self.lvl2.clicked.connect(self.level_2)

        self.lvl3 = QPushButton('Level 3', self)
        self.lvl3.move(100, 450)
        self.lvl3.clicked.connect(self.level_3)

        self.controls = QPushButton('Ingame info', self)
        self.controls.move(100, 550)
        self.controls.clicked.connect(self.controls_window)

        self.exit = QPushButton('Exit', self)
        self.exit.move(100, 650)
        self.exit.clicked.connect(exit)

        self.setFixedSize(856, 856)
        self.setWindowTitle('Fox Burglar - Main menu')

        imag = QImage('./src/graphics/mainmenu.png')
        image = imag.scaled(QSize(856, 856))
        palette = QPalette()
        palette.setBrush(10, QBrush(image))
        self.setPalette(palette)

        self.sound()

        self.show()

    def real_sound(self):
        # The games music, using pygame library
        pygame.mixer.init()
        pygame.mixer.music.load("./src/sound/menu_music.mp3")
        pygame.mixer.music.play(-1)

    def sound(self):
        # By using threading we can play the music, with it not interfering with the gameplay
        global player_thread
        player_thread = Thread(target = self.real_sound)
        player_thread.start()

    def level_1(self):
        self.world = World(self, './src/maps/level1_map.txt')
        self.hide()

    def level_2(self):
        self.world = World(self, './src/maps/level2_map.txt')
        self.hide()

    def level_3(self):
        self.world = World(self, './src/maps/level3_map.txt')
        self.hide()

    def controls_window(self):
        # The window with the controls info
        self.control = QWidget()
        self.control.setFixedSize( 856, 856)
        self.control.setWindowTitle('Fox Burglar - Controls')

        self.back = QPushButton('Back to menu', self.control)
        self.back.move(70, 600)
        self.back.clicked.connect(self.move)

        self.exit = QPushButton('Exit', self.control)
        self.exit.move(70, 700)
        self.exit.clicked.connect(exit)

        imag = QImage('./src/graphics/controls_window.png')
        image = imag.scaled(QSize(856, 856))
        palette = QPalette()
        palette.setBrush(10, QBrush(image))
        self.control.setPalette(palette)

        self.control.show()
        self.hide()

    def move(self):
        # Moves from the control window back to menu
        self.control.close()
        self.show()



