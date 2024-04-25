# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loadingUIQjvhfY.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QLabel,
    QMainWindow,
    QSizePolicy,
    QWidget,
)
from .resources import resources


class Ui_SlashScreen(object):
    def setupUi(self, SlashScreen):
        if not SlashScreen.objectName():
            SlashScreen.setObjectName("SlashScreen")
        SlashScreen.resize(960, 540)
        self.centralwidget = QWidget(SlashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(120, 60, 720, 405))
        self.frame.setStyleSheet(
            "QFrame {\n"
            "	background-color: rgba(0, 30, 100, 255);\n"
            "	border-style: none;\n"
            "	border-radius: 15px;\n"
            "}"
        )
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.logo = QLabel(self.frame)
        self.logo.setObjectName("logo")
        self.logo.setGeometry(QRect(0, 0, 405, 405))
        self.logo.setStyleSheet("background-color: none;")
        self.logo.setPixmap(QPixmap(":/Logo/CentiCube.png"))
        self.logo.setScaledContents(True)
        self.appName = QLabel(self.frame)
        self.appName.setObjectName("appName")
        self.appName.setGeometry(QRect(370, 140, 321, 121))
        font = QFont()
        font.setFamilies(["Bahnschrift"])
        font.setPointSize(48)
        font.setBold(True)
        font.setUnderline(False)
        self.appName.setFont(font)
        self.appName.setStyleSheet("color: rgba(255, 255, 255, 255);")
        self.appName.setTextFormat(Qt.RichText)
        self.appName.setScaledContents(True)
        self.appName.setAlignment(Qt.AlignCenter)
        SlashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SlashScreen)

        QMetaObject.connectSlotsByName(SlashScreen)

    # setupUi

    def retranslateUi(self, SlashScreen):
        SlashScreen.setWindowTitle(
            QCoreApplication.translate("SlashScreen", "MainWindow", None)
        )
        self.logo.setText("")
        self.appName.setText(
            QCoreApplication.translate("SlashScreen", "CentiCube", None)
        )

    # retranslateUi
