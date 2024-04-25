# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loadingUIbMvoVU.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QProgressBar, QSizePolicy, QVBoxLayout, QWidget)

class Ui_SlashScreen(object):
    def setupUi(self, SlashScreen):
        if not SlashScreen.objectName():
            SlashScreen.setObjectName(u"SlashScreen")
        SlashScreen.resize(720, 360)
        self.centralwidget = QWidget(SlashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadow = QFrame(self.centralwidget)
        self.dropShadow.setObjectName(u"dropShadow")
        self.dropShadow.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(0, 60, 90);\n"
"	color: rgb(222, 222, 222);\n"
"	border-radius: 10px;\n"
"}")
        self.dropShadow.setFrameShape(QFrame.StyledPanel)
        self.dropShadow.setFrameShadow(QFrame.Raised)
        self.appName = QLabel(self.dropShadow)
        self.appName.setObjectName(u"appName")
        self.appName.setGeometry(QRect(0, 100, 700, 100))
        font = QFont()
        font.setPointSize(42)
        font.setBold(True)
        self.appName.setFont(font)
        self.appName.setLayoutDirection(Qt.LeftToRight)
        self.appName.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.appName.setAlignment(Qt.AlignCenter)
        self.loadingBar = QProgressBar(self.dropShadow)
        self.loadingBar.setObjectName(u"loadingBar")
        self.loadingBar.setGeometry(QRect(100, 300, 500, 10))
        self.loadingBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgb(0, 150, 240);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 255, 255), stop:1 rgba(0, 255, 255, 255));\n"
"}")
        self.loadingBar.setValue(24)

        self.verticalLayout.addWidget(self.dropShadow)

        SlashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SlashScreen)

        QMetaObject.connectSlotsByName(SlashScreen)
    # setupUi

    def retranslateUi(self, SlashScreen):
        SlashScreen.setWindowTitle(QCoreApplication.translate("SlashScreen", u"MainWindow", None))
        self.appName.setText(QCoreApplication.translate("SlashScreen", u"<strong>CentiCube</strong>", None))
    # retranslateUi

