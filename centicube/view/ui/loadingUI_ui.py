# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loadingUI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
    QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_SlashScreen(object):
    def setupUi(self, SlashScreen):
        if not SlashScreen.objectName():
            SlashScreen.setObjectName(u"SlashScreen")
        SlashScreen.resize(720, 405)
        SlashScreen.setStyleSheet(u"background-color: none;\n"
"border-radius: 0px;\n"
"border-style: none;\n"
"color: rgb(255, 255, 255);\n"
"text-align: center;")
        self.centralwidget = QWidget(SlashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.MainFrame = QFrame(self.centralwidget)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(50, 165, 230);\n"
"}")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.appLogo = QLabel(self.MainFrame)
        self.appLogo.setObjectName(u"appLogo")
        self.appLogo.setGeometry(QRect(-30, 0, 405, 405))
        self.appLogo.setStyleSheet(u"background-color: none;")
        self.appLogo.setPixmap(QPixmap(u":/Logo/images/CentiCube.png"))
        self.appLogo.setScaledContents(True)
        self.appName = QLabel(self.MainFrame)
        self.appName.setObjectName(u"appName")
        self.appName.setGeometry(QRect(290, 125, 350, 150))
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(48)
        font.setBold(True)
        font.setUnderline(False)
        self.appName.setFont(font)
        self.appName.setStyleSheet(u"background-color: none;\n"
"color: rgba(255, 255, 255, 255);")
        self.appName.setTextFormat(Qt.RichText)
        self.appName.setScaledContents(True)
        self.appName.setAlignment(Qt.AlignCenter)
        self.appDesc = QLabel(self.MainFrame)
        self.appDesc.setObjectName(u"appDesc")
        self.appDesc.setGeometry(QRect(300, 210, 341, 50))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(12)
        self.appDesc.setFont(font1)
        self.appDesc.setStyleSheet(u"background-color: none;\n"
"color: rgb(200, 200, 200);")
        self.appDesc.setAlignment(Qt.AlignCenter)
        self.appVersion = QLabel(self.MainFrame)
        self.appVersion.setObjectName(u"appVersion")
        self.appVersion.setGeometry(QRect(610, 130, 71, 150))
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(24)
        font2.setBold(True)
        font2.setUnderline(False)
        self.appVersion.setFont(font2)
        self.appVersion.setStyleSheet(u"background-color: none;\n"
"color: rgba(0, 190, 255, 255);")
        self.appVersion.setTextFormat(Qt.RichText)
        self.appVersion.setScaledContents(True)
        self.appVersion.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.MainFrame)

        SlashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SlashScreen)

        QMetaObject.connectSlotsByName(SlashScreen)
    # setupUi

    def retranslateUi(self, SlashScreen):
        SlashScreen.setWindowTitle(QCoreApplication.translate("SlashScreen", u"MainWindow", None))
        self.appLogo.setText("")
        self.appName.setText(QCoreApplication.translate("SlashScreen", u"CentiCube", None))
        self.appDesc.setText(QCoreApplication.translate("SlashScreen", u"Control Your Own Minecraft Server", None))
        self.appVersion.setText(QCoreApplication.translate("SlashScreen", u"1.0", None))
    # retranslateUi

