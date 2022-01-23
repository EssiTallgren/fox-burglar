import sys

from PyQt5.QtWidgets import QApplication

from menu import Menu


def main():
    global app
    app = QApplication(sys.argv)
    mainmenu = Menu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()