# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(720, 405)
        MainWindow.setMinimumSize(QSize(720, 405))
        font = QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: none;\n"
"border-style: none;\n"
"border-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"text-align: center;\n"
"padding: 0px;\n"
"margin: 0px;\n"
"spacing: 0px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Header = QFrame(self.centralwidget)
        self.Header.setObjectName(u"Header")
        self.Header.setMinimumSize(QSize(0, 50))
        self.Header.setMaximumSize(QSize(16777215, 50))
        self.Header.setStyleSheet(u"QFrame {\n"
"	border-bottom: 0px solid rgb(100, 100, 100);\n"
"	background-color: rgb(50, 165, 230);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Header.setFrameShape(QFrame.StyledPanel)
        self.Header.setFrameShadow(QFrame.Raised)
        self.HeaderLayout = QHBoxLayout(self.Header)
        self.HeaderLayout.setSpacing(5)
        self.HeaderLayout.setObjectName(u"HeaderLayout")
        self.HeaderLayout.setContentsMargins(0, 0, 0, 0)
        self.CentiCube = QFrame(self.Header)
        self.CentiCube.setObjectName(u"CentiCube")
        self.CentiCube.setMinimumSize(QSize(150, 50))
        self.CentiCube.setFrameShape(QFrame.StyledPanel)
        self.CentiCube.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.CentiCube)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.appLogo = QLabel(self.CentiCube)
        self.appLogo.setObjectName(u"appLogo")
        self.appLogo.setMinimumSize(QSize(50, 50))
        self.appLogo.setMaximumSize(QSize(50, 50))
        self.appLogo.setPixmap(QPixmap(u":/Logo/images/CentiCube.png"))
        self.appLogo.setScaledContents(True)

        self.horizontalLayout.addWidget(self.appLogo)

        self.appName = QLabel(self.CentiCube)
        self.appName.setObjectName(u"appName")
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.appName.setFont(font1)

        self.horizontalLayout.addWidget(self.appName)


        self.HeaderLayout.addWidget(self.CentiCube)

        self.spacerL = QSpacerItem(100, 50, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HeaderLayout.addItem(self.spacerL)

        self.Tabs = QFrame(self.Header)
        self.Tabs.setObjectName(u"Tabs")
        self.Tabs.setMinimumSize(QSize(360, 50))
        self.Tabs.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
"	border-style: none;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	border-bottom: 2px solid rgb(255, 255, 255);\n"
"}")
        self.Tabs.setFrameShape(QFrame.StyledPanel)
        self.Tabs.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Tabs)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.dashboardButton = QPushButton(self.Tabs)
        self.dashboardButton.setObjectName(u"dashboardButton")
        self.dashboardButton.setMinimumSize(QSize(120, 50))
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift SemiLight"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.dashboardButton.setFont(font2)
        self.dashboardButton.setStyleSheet(u"text-align: center;\n"
"border-style: none;")
        self.dashboardButton.setIconSize(QSize(20, 20))
        self.dashboardButton.setCheckable(True)
        self.dashboardButton.setChecked(True)

        self.horizontalLayout_3.addWidget(self.dashboardButton)

        self.serverButton = QPushButton(self.Tabs)
        self.serverButton.setObjectName(u"serverButton")
        self.serverButton.setMinimumSize(QSize(120, 50))
        font3 = QFont()
        font3.setFamilies([u"Bahnschrift SemiLight"])
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setKerning(True)
        self.serverButton.setFont(font3)
        self.serverButton.setAutoFillBackground(False)
        self.serverButton.setStyleSheet(u"text-align: center;\n"
"border-style: none;")
        self.serverButton.setIconSize(QSize(20, 20))
        self.serverButton.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.serverButton)

        self.settingButton = QPushButton(self.Tabs)
        self.settingButton.setObjectName(u"settingButton")
        self.settingButton.setMinimumSize(QSize(120, 50))
        self.settingButton.setFont(font2)
        self.settingButton.setStyleSheet(u"text-align: center;\n"
"border-style: none;")
        self.settingButton.setIconSize(QSize(20, 20))
        self.settingButton.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.settingButton)


        self.HeaderLayout.addWidget(self.Tabs)

        self.spacerR = QSpacerItem(100, 50, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HeaderLayout.addItem(self.spacerR)

        self.Windows = QFrame(self.Header)
        self.Windows.setObjectName(u"Windows")
        self.Windows.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 145, 225);\n"
"}")
        self.Windows.setFrameShape(QFrame.StyledPanel)
        self.Windows.setFrameShadow(QFrame.Raised)
        self.WindowButton = QHBoxLayout(self.Windows)
        self.WindowButton.setSpacing(5)
        self.WindowButton.setObjectName(u"WindowButton")
        self.WindowButton.setContentsMargins(0, 0, 0, 0)
        self.minButton = QPushButton(self.Windows)
        self.minButton.setObjectName(u"minButton")
        self.minButton.setMinimumSize(QSize(50, 50))
        self.minButton.setMaximumSize(QSize(50, 50))
        icon = QIcon()
        icon.addFile(u":/Icons/icons/Minimize_White.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minButton.setIcon(icon)
        self.minButton.setIconSize(QSize(20, 20))
        self.minButton.setCheckable(True)

        self.WindowButton.addWidget(self.minButton)

        self.maxButton = QPushButton(self.Windows)
        self.maxButton.setObjectName(u"maxButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxButton.sizePolicy().hasHeightForWidth())
        self.maxButton.setSizePolicy(sizePolicy)
        self.maxButton.setMinimumSize(QSize(50, 50))
        self.maxButton.setMaximumSize(QSize(50, 50))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/icons/Maximize_White.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maxButton.setIcon(icon1)
        self.maxButton.setIconSize(QSize(20, 20))
        self.maxButton.setCheckable(True)

        self.WindowButton.addWidget(self.maxButton)

        self.closeButton = QPushButton(self.Windows)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(50, 50))
        self.closeButton.setMaximumSize(QSize(50, 50))
        self.closeButton.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(255, 45, 45);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/icons/Close_White.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon2)
        self.closeButton.setIconSize(QSize(20, 20))
        self.closeButton.setCheckable(True)

        self.WindowButton.addWidget(self.closeButton)


        self.HeaderLayout.addWidget(self.Windows)


        self.verticalLayout.addWidget(self.Header)

        self.Pages = QWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.verticalLayout_2 = QVBoxLayout(self.Pages)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Page = QStackedWidget(self.Pages)
        self.Page.setObjectName(u"Page")
        self.Page.setStyleSheet(u"* {\n"
"	color: rgb(150, 150, 150)\n"
"}\n"
"\n"
"QWidget {\n"
"	background-color: rgb(240, 240, 240);\n"
"}")
        self.dashboardPage = QWidget()
        self.dashboardPage.setObjectName(u"dashboardPage")
        self.dashboardPage.setEnabled(True)
        self.gridLayout = QGridLayout(self.dashboardPage)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.dashboardLabel = QLabel(self.dashboardPage)
        self.dashboardLabel.setObjectName(u"dashboardLabel")
        font4 = QFont()
        font4.setFamilies([u"Bahnschrift"])
        font4.setPointSize(40)
        font4.setBold(True)
        self.dashboardLabel.setFont(font4)
        self.dashboardLabel.setScaledContents(True)
        self.dashboardLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.dashboardLabel, 1, 0, 1, 1)

        self.dashboardDIsplay = QFrame(self.dashboardPage)
        self.dashboardDIsplay.setObjectName(u"dashboardDIsplay")
        self.dashboardDIsplay.setMinimumSize(QSize(0, 50))
        self.dashboardDIsplay.setMaximumSize(QSize(16777215, 50))
        font5 = QFont()
        font5.setFamilies([u"Bahnschrift Light"])
        self.dashboardDIsplay.setFont(font5)
        self.dashboardDIsplay.setStyleSheet(u"* {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(100, 100, 100)\n"
"}")
        self.dashboardDIsplay.setFrameShape(QFrame.StyledPanel)
        self.dashboardDIsplay.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.dashboardDIsplay)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.newServerDashboard = QPushButton(self.dashboardDIsplay)
        self.newServerDashboard.setObjectName(u"newServerDashboard")
        self.newServerDashboard.setMinimumSize(QSize(100, 40))
        self.newServerDashboard.setMaximumSize(QSize(16777215, 40))
        font6 = QFont()
        font6.setFamilies([u"Bahnschrift SemiBold"])
        font6.setBold(True)
        self.newServerDashboard.setFont(font6)
        icon3 = QIcon()
        icon3.addFile(u":/Icons/icons/Add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.newServerDashboard.setIcon(icon3)
        self.newServerDashboard.setIconSize(QSize(20, 20))
        self.newServerDashboard.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.newServerDashboard)

        self.overviewDashboard = QPushButton(self.dashboardDIsplay)
        self.overviewDashboard.setObjectName(u"overviewDashboard")
        self.overviewDashboard.setMinimumSize(QSize(100, 50))
        self.overviewDashboard.setMaximumSize(QSize(16777215, 50))
        self.overviewDashboard.setFont(font6)
        self.overviewDashboard.setStyleSheet(u"* {\n"
"	border-bottom: 3px solid rgb(50, 165, 230);\n"
"}")

        self.horizontalLayout_2.addWidget(self.overviewDashboard)

        self.pushButton = QPushButton(self.dashboardDIsplay)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 50))
        self.pushButton.setMaximumSize(QSize(16777215, 50))
        self.pushButton.setFont(font6)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.spacerD = QSpacerItem(402, 47, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.spacerD)


        self.gridLayout.addWidget(self.dashboardDIsplay, 0, 0, 1, 1)

        self.Page.addWidget(self.dashboardPage)
        self.settingPage = QWidget()
        self.settingPage.setObjectName(u"settingPage")
        self.Page.addWidget(self.settingPage)
        self.serverPage = QWidget()
        self.serverPage.setObjectName(u"serverPage")
        self.gridLayout_2 = QGridLayout(self.serverPage)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.serverDisplay = QFrame(self.serverPage)
        self.serverDisplay.setObjectName(u"serverDisplay")
        self.serverDisplay.setMinimumSize(QSize(0, 50))
        self.serverDisplay.setMaximumSize(QSize(16777215, 50))
        self.serverDisplay.setStyleSheet(u"* {\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.serverDisplay.setFrameShape(QFrame.StyledPanel)
        self.serverDisplay.setFrameShadow(QFrame.Raised)
        self.newServer = QPushButton(self.serverDisplay)
        self.newServer.setObjectName(u"newServer")
        self.newServer.setGeometry(QRect(10, 5, 100, 40))
        self.newServer.setStyleSheet(u"* {\n"
"\n"
"}")
        self.newServer.setIcon(icon3)
        self.newServer.setIconSize(QSize(20, 20))
        self.scrollArea = QScrollArea(self.serverDisplay)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(130, 0, 831, 50))
        self.scrollArea.setMinimumSize(QSize(0, 50))
        self.scrollArea.setMaximumSize(QSize(16777215, 50))
        self.scrollArea.setStyleSheet(u"* {\n"
"\n"
"}")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.sampleServer = QWidget()
        self.sampleServer.setObjectName(u"sampleServer")
        self.sampleServer.setGeometry(QRect(0, 0, 831, 50))
        self.scrollArea.setWidget(self.sampleServer)

        self.gridLayout_2.addWidget(self.serverDisplay, 0, 0, 1, 1)

        self.Utility = QFrame(self.serverPage)
        self.Utility.setObjectName(u"Utility")
        self.Utility.setMinimumSize(QSize(0, 35))
        self.Utility.setMaximumSize(QSize(16777215, 35))
        self.Utility.setStyleSheet(u"* {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-top: 2px solid rgb(50, 165, 230);\n"
"}")
        self.Utility.setFrameShape(QFrame.StyledPanel)
        self.Utility.setFrameShadow(QFrame.Raised)
        self.overviewButton = QPushButton(self.Utility)
        self.overviewButton.setObjectName(u"overviewButton")
        self.overviewButton.setGeometry(QRect(20, 0, 75, 35))
        self.overviewButton.setMaximumSize(QSize(16777215, 35))
        self.overviewButton.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.Utility, 1, 0, 1, 1)

        self.serverRender = QStackedWidget(self.serverPage)
        self.serverRender.setObjectName(u"serverRender")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.serverRender.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.serverRender.addWidget(self.page_2)

        self.gridLayout_2.addWidget(self.serverRender, 2, 0, 1, 1)

        self.Page.addWidget(self.serverPage)

        self.verticalLayout_2.addWidget(self.Page)


        self.verticalLayout.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Page.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.appLogo.setText("")
        self.appName.setText(QCoreApplication.translate("MainWindow", u"CentiCube", None))
        self.dashboardButton.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.serverButton.setText(QCoreApplication.translate("MainWindow", u"Servers", None))
        self.settingButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.minButton.setText("")
        self.maxButton.setText("")
        self.closeButton.setText("")
        self.dashboardLabel.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.newServerDashboard.setText(QCoreApplication.translate("MainWindow", u"New Server", None))
        self.overviewDashboard.setText(QCoreApplication.translate("MainWindow", u"Overview", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Server", None))
        self.newServer.setText(QCoreApplication.translate("MainWindow", u"New Server", None))
        self.overviewButton.setText(QCoreApplication.translate("MainWindow", u"Overview", None))
    # retranslateUi

