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
    QVBoxLayout,
    QWidget,
)
from .resources import resources


class Ui_SlashScreen(object):
    def setupUi(self, SlashScreen):
        if not SlashScreen.objectName():
            SlashScreen.setObjectName("SlashScreen")
        SlashScreen.resize(720, 405)
        SlashScreen.setStyleSheet(
            "background-color: none;\n"
            "border-radius: 0px;\n"
            "border-style: none;\n"
            "color: rgb(255, 255, 255);\n"
            "text-align: center;"
        )
        self.centralwidget = QWidget(SlashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.MainFrame = QFrame(self.centralwidget)
        self.MainFrame.setObjectName("MainFrame")
        self.MainFrame.setStyleSheet(
            "QFrame {\n" "	background-color: rgb(50, 165, 230);\n" "}"
        )
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.appLogo = QLabel(self.MainFrame)
        self.appLogo.setObjectName("appLogo")
        self.appLogo.setGeometry(QRect(-30, 0, 405, 405))
        self.appLogo.setStyleSheet("background-color: none;")
        self.appLogo.setPixmap(QPixmap(":/Logo/images/CentiCube.png"))
        self.appLogo.setScaledContents(True)
        self.appName = QLabel(self.MainFrame)
        self.appName.setObjectName("appName")
        self.appName.setGeometry(QRect(290, 125, 350, 150))
        font = QFont()
        font.setFamilies(["Bahnschrift"])
        font.setPointSize(48)
        font.setBold(True)
        font.setUnderline(False)
        self.appName.setFont(font)
        self.appName.setStyleSheet(
            "background-color: none;\n" "color: rgba(255, 255, 255, 255);"
        )
        self.appName.setTextFormat(Qt.RichText)
        self.appName.setScaledContents(True)
        self.appName.setAlignment(Qt.AlignCenter)
        self.appDesc = QLabel(self.MainFrame)
        self.appDesc.setObjectName("appDesc")
        self.appDesc.setGeometry(QRect(300, 210, 341, 50))
        font1 = QFont()
        font1.setFamilies(["Bahnschrift"])
        font1.setPointSize(12)
        self.appDesc.setFont(font1)
        self.appDesc.setStyleSheet(
            "background-color: none;\n" "color: rgb(200, 200, 200);"
        )
        self.appDesc.setAlignment(Qt.AlignCenter)
        self.appVersion = QLabel(self.MainFrame)
        self.appVersion.setObjectName("appVersion")
        self.appVersion.setGeometry(QRect(610, 130, 71, 150))
        font2 = QFont()
        font2.setFamilies(["Bahnschrift"])
        font2.setPointSize(24)
        font2.setBold(True)
        font2.setUnderline(False)
        self.appVersion.setFont(font2)
        self.appVersion.setStyleSheet(
            "background-color: none;\n" "color: rgba(0, 190, 255, 255);"
        )
        self.appVersion.setTextFormat(Qt.RichText)
        self.appVersion.setScaledContents(True)
        self.appVersion.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.MainFrame)

        SlashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SlashScreen)

        QMetaObject.connectSlotsByName(SlashScreen)

    # setupUi

    def retranslateUi(self, SlashScreen):
        SlashScreen.setWindowTitle(
            QCoreApplication.translate("SlashScreen", "MainWindow", None)
        )
        self.appLogo.setText("")
        self.appName.setText(
            QCoreApplication.translate("SlashScreen", "CentiCube", None)
        )
        self.appDesc.setText(
            QCoreApplication.translate(
                "SlashScreen", "Control Your Own Minecraft Server", None
            )
        )
        self.appVersion.setText(QCoreApplication.translate("SlashScreen", "1.0", None))

    # retranslateUi
