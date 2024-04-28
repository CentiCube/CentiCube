# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainLroJeU.ui'
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
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)
from .resources import resources


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        MainWindow.setMinimumSize(QSize(640, 360))
        font = QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(
            "background-color: none;\n"
            "border-style: none;\n"
            "border-radius: 0px;\n"
            "color: rgb(255, 255, 255);\n"
            "text-align: center;\n"
            "padding: 0px;\n"
            "margin: 0px;\n"
            "spacing: 0px;"
        )
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Header = QFrame(self.centralwidget)
        self.Header.setObjectName("Header")
        self.Header.setMinimumSize(QSize(0, 50))
        self.Header.setMaximumSize(QSize(16777215, 50))
        self.Header.setStyleSheet(
            "QFrame {\n"
            "	border-bottom: 0px solid rgb(100, 100, 100);\n"
            "	background-color: rgb(50, 165, 230);\n"
            "	color: rgb(255, 255, 255);\n"
            "}"
        )
        self.Header.setFrameShape(QFrame.StyledPanel)
        self.Header.setFrameShadow(QFrame.Raised)
        self.HeaderLayout = QHBoxLayout(self.Header)
        self.HeaderLayout.setSpacing(5)
        self.HeaderLayout.setObjectName("HeaderLayout")
        self.HeaderLayout.setContentsMargins(0, 0, 0, 0)
        self.CentiCube = QFrame(self.Header)
        self.CentiCube.setObjectName("CentiCube")
        self.CentiCube.setMinimumSize(QSize(150, 50))
        self.CentiCube.setFrameShape(QFrame.StyledPanel)
        self.CentiCube.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.CentiCube)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.appLogo = QLabel(self.CentiCube)
        self.appLogo.setObjectName("appLogo")
        self.appLogo.setMinimumSize(QSize(50, 50))
        self.appLogo.setMaximumSize(QSize(50, 50))
        self.appLogo.setPixmap(QPixmap(":/Logo/images/CentiCube.png"))
        self.appLogo.setScaledContents(True)

        self.horizontalLayout.addWidget(self.appLogo)

        self.appName = QLabel(self.CentiCube)
        self.appName.setObjectName("appName")
        font1 = QFont()
        font1.setFamilies(["Bahnschrift"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.appName.setFont(font1)

        self.horizontalLayout.addWidget(self.appName)

        self.HeaderLayout.addWidget(self.CentiCube)

        self.spacerL = QSpacerItem(100, 50, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.HeaderLayout.addItem(self.spacerL)

        self.Tabs = QFrame(self.Header)
        self.Tabs.setObjectName("Tabs")
        self.Tabs.setMinimumSize(QSize(360, 50))
        self.Tabs.setStyleSheet(
            "QPushButton {\n"
            "	background-color: none;\n"
            "	border-style: none;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "	border-bottom: 2px solid rgb(255, 255, 255);\n"
            "}"
        )
        self.Tabs.setFrameShape(QFrame.StyledPanel)
        self.Tabs.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Tabs)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.dashboardButton = QPushButton(self.Tabs)
        self.dashboardButton.setObjectName("dashboardButton")
        self.dashboardButton.setMinimumSize(QSize(120, 50))
        font2 = QFont()
        font2.setFamilies(["Bahnschrift SemiLight"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.dashboardButton.setFont(font2)
        self.dashboardButton.setStyleSheet(
            "text-align: center;\n" "border-style: none;"
        )
        self.dashboardButton.setIconSize(QSize(20, 20))
        self.dashboardButton.setCheckable(True)
        self.dashboardButton.setChecked(True)

        self.horizontalLayout_3.addWidget(self.dashboardButton)

        self.serverButton = QPushButton(self.Tabs)
        self.serverButton.setObjectName("serverButton")
        self.serverButton.setMinimumSize(QSize(120, 50))
        font3 = QFont()
        font3.setFamilies(["Bahnschrift SemiLight"])
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setKerning(True)
        self.serverButton.setFont(font3)
        self.serverButton.setAutoFillBackground(False)
        self.serverButton.setStyleSheet("text-align: center;\n" "border-style: none;")
        self.serverButton.setIconSize(QSize(20, 20))
        self.serverButton.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.serverButton)

        self.settingButton = QPushButton(self.Tabs)
        self.settingButton.setObjectName("settingButton")
        self.settingButton.setMinimumSize(QSize(120, 50))
        self.settingButton.setFont(font2)
        self.settingButton.setStyleSheet("text-align: center;\n" "border-style: none;")
        self.settingButton.setIconSize(QSize(20, 20))
        self.settingButton.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.settingButton)

        self.HeaderLayout.addWidget(self.Tabs)

        self.spacerR = QSpacerItem(100, 50, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.HeaderLayout.addItem(self.spacerR)

        self.Windows = QFrame(self.Header)
        self.Windows.setObjectName("Windows")
        self.Windows.setStyleSheet(
            "QPushButton {\n"
            "	background-color: none;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(0, 145, 225);\n"
            "}"
        )
        self.Windows.setFrameShape(QFrame.StyledPanel)
        self.Windows.setFrameShadow(QFrame.Raised)
        self.WindowButton = QHBoxLayout(self.Windows)
        self.WindowButton.setSpacing(5)
        self.WindowButton.setObjectName("WindowButton")
        self.WindowButton.setContentsMargins(0, 0, 0, 0)
        self.minButton = QPushButton(self.Windows)
        self.minButton.setObjectName("minButton")
        self.minButton.setMinimumSize(QSize(50, 50))
        self.minButton.setMaximumSize(QSize(50, 50))
        icon = QIcon()
        icon.addFile(
            ":/Icons/icons/Minimize_White.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.minButton.setIcon(icon)
        self.minButton.setIconSize(QSize(20, 20))
        self.minButton.setCheckable(True)

        self.WindowButton.addWidget(self.minButton)

        self.maxButton = QPushButton(self.Windows)
        self.maxButton.setObjectName("maxButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxButton.sizePolicy().hasHeightForWidth())
        self.maxButton.setSizePolicy(sizePolicy)
        self.maxButton.setMinimumSize(QSize(50, 50))
        self.maxButton.setMaximumSize(QSize(50, 50))
        icon1 = QIcon()
        icon1.addFile(
            ":/Icons/icons/Maximize_White.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.maxButton.setIcon(icon1)
        self.maxButton.setIconSize(QSize(20, 20))
        self.maxButton.setCheckable(True)

        self.WindowButton.addWidget(self.maxButton)

        self.closeButton = QPushButton(self.Windows)
        self.closeButton.setObjectName("closeButton")
        self.closeButton.setMinimumSize(QSize(50, 50))
        self.closeButton.setMaximumSize(QSize(50, 50))
        self.closeButton.setStyleSheet(
            "QPushButton:hover {\n" "	background-color: rgb(255, 45, 45);\n" "}"
        )
        icon2 = QIcon()
        icon2.addFile(":/Icons/icons/Close_White.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon2)
        self.closeButton.setIconSize(QSize(20, 20))
        self.closeButton.setCheckable(True)

        self.WindowButton.addWidget(self.closeButton)

        self.HeaderLayout.addWidget(self.Windows)

        self.verticalLayout.addWidget(self.Header)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName("Pages")
        self.dashboardPage = QWidget()
        self.dashboardPage.setObjectName("dashboardPage")
        self.dashboardLabel = QLabel(self.dashboardPage)
        self.dashboardLabel.setObjectName("dashboardLabel")
        self.dashboardLabel.setGeometry(QRect(320, 180, 341, 111))
        font4 = QFont()
        font4.setFamilies(["Bahnschrift"])
        font4.setPointSize(40)
        font4.setBold(True)
        self.dashboardLabel.setFont(font4)
        self.dashboardLabel.setScaledContents(True)
        self.dashboardLabel.setAlignment(Qt.AlignCenter)
        self.Pages.addWidget(self.dashboardPage)
        self.serverPage = QWidget()
        self.serverPage.setObjectName("serverPage")
        self.serverLabel = QLabel(self.serverPage)
        self.serverLabel.setObjectName("serverLabel")
        self.serverLabel.setGeometry(QRect(320, 180, 341, 111))
        self.serverLabel.setFont(font4)
        self.serverLabel.setScaledContents(True)
        self.serverLabel.setAlignment(Qt.AlignCenter)
        self.Pages.addWidget(self.serverPage)

        self.verticalLayout.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.appLogo.setText("")
        self.appName.setText(
            QCoreApplication.translate("MainWindow", "CentiCube", None)
        )
        self.dashboardButton.setText(
            QCoreApplication.translate("MainWindow", "Dashboard", None)
        )
        self.serverButton.setText(
            QCoreApplication.translate("MainWindow", "Servers", None)
        )
        self.settingButton.setText(
            QCoreApplication.translate("MainWindow", "Settings", None)
        )
        self.minButton.setText("")
        self.maxButton.setText("")
        self.closeButton.setText("")
        self.dashboardLabel.setText(
            QCoreApplication.translate("MainWindow", "Dashboard", None)
        )
        self.serverLabel.setText(
            QCoreApplication.translate("MainWindow", "Server Page", None)
        )

    # retranslateUi
