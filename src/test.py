import unittest

import sys

from PyQt5.QtWidgets import QApplication

from gui import GUI
from world import World
from menu import Menu
from corrupted_file import CorruptedChessFileError


class Test(unittest.TestCase):

    def test_working_map_file(self):
        self.world = World(excecute, './src/maps/level1_map.txt')
        self.gui = GUI(self.world)
        self.assertEqual(self.gui.create_map('./src/maps/level1_map.txt'), (64,10))

    def test_no_victory(self):
        game_map = None
        check_this = None

        try:
            self.world = World(excecute, './src/maps/test_file1.txt')
            self.gui = GUI(self.world)
            game_map = self.gui.create_map('./src/maps/test_file1.txt')
        except CorruptedChessFileError as e:
            check_this = e

        self.assertNotEqual(None, check_this, "A CorruptedChessFileError was not raised.")

    def test_no_player(self):
        game_map = None
        check_this = None

        try:
            self.world = World(excecute, './src/maps/test_file2.txt')
            self.gui = GUI(self.world)
            game_map = self.gui.create_map('./src/maps/test_file2.txt')
        except CorruptedChessFileError as e:
            check_this = e

        self.assertNotEqual(None, check_this, "A CorruptedChessFileError was not raised.")

    def test_wrong_letter_in_file(self):
        game_map = None
        check_this = None

        try:
            self.world = World(excecute, './src/maps/test_file3.txt')
            self.gui = GUI(self.world)
            game_map = self.gui.create_map('./src/maps/test_file3.txt')
        except CorruptedChessFileError as e:
            check_this = e

        self.assertNotEqual(None, check_this, "A CorruptedChessFileError was not raised.")

    def test_not_real_file(self):
        game_map = None
        check_this = None

        try:
            self.world = World(excecute, './src/maps/test_file_not.txt')
            self.gui = GUI(self.world)
            game_map = self.gui.create_map('./src/maps/test_file_not.txt')
        except CorruptedChessFileError as e:
            check_this = e

        self.assertNotEqual(None, check_this, "A CorruptedChessFileError was not raised.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    excecute = Menu()
    unittest.main()