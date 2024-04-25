import sys
import platform

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# from centicube.centicube import *
from loadingUI import Ui_SlashScreen
from mainUI import Ui_MainWindow

class loadingUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SlashScreen()
        self.ui.setupUi(self)
        
        self.show()