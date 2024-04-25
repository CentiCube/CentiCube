import sys
import platform

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# from centicube.centicube import *
from .view.loadingUI import Ui_SlashScreen
from .view.mainUI import Ui_MainWindow
# from core import *
# from model import *
# from view import *

# from view.mainView import *

class loadingUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SlashScreen()
        self.ui.setupUi(self)
        
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.show()

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        self.show()

def main() -> None:
    App = QApplication(sys.argv)
    Window = loadingUI()
    sys.exit(App.exec_())