import sys
import platform

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from .view.loadingUI import Ui_SlashScreen
from .view.mainUI import Ui_MainWindow

loadingPercent = 0


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


class loadingUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SlashScreen()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

        self.show()

    def progress(self):
        global loadingPercent

        if loadingPercent > 100:
            self.timer.stop()

            self.main = MainWindow()
            self.main.show()

            self.close()
        loadingPercent += 1


def main() -> None:
    App = QApplication(sys.argv)
    Window = loadingUI()
    sys.exit(App.exec_())
