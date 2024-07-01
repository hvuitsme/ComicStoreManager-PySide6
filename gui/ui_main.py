# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainImkuHZ.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)
import image_rc

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(1288, 936)
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.Main_PD = QFrame(self.frame)
        self.Main_PD.setObjectName(u"Main_PD")
        self.Main_PD.setGeometry(QRect(270, 40, 991, 861))
        self.Main_PD.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgb(218, 218, 218);")
        self.Main_PD.setFrameShape(QFrame.NoFrame)
        self.layoutWidget = QWidget(self.Main_PD)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 0, 951, 37))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_PD = QLabel(self.layoutWidget)
        self.label_PD.setObjectName(u"label_PD")
        self.label_PD.setStyleSheet(u"border: none;\n"
"padding: 7px 0;")
        self.label_PD.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_PD)

        self.label_Rank = QLabel(self.layoutWidget)
        self.label_Rank.setObjectName(u"label_Rank")
        self.label_Rank.setStyleSheet(u"border: none;\n"
"padding: 7px 0;")
        self.label_Rank.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_Rank)

        self.label_News = QLabel(self.layoutWidget)
        self.label_News.setObjectName(u"label_News")
        self.label_News.setStyleSheet(u"border: none;\n"
"padding: 7px 0;")
        self.label_News.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_News)

        self.stackedWidget = QStackedWidget(self.Main_PD)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(9, 39, 971, 811))
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.label_page_news = QLabel(self.page1)
        self.label_page_news.setObjectName(u"label_page_news")
        self.label_page_news.setGeometry(QRect(8, 5, 961, 801))
        self.label_page_news.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.label_page_rank = QLabel(self.page2)
        self.label_page_rank.setObjectName(u"label_page_rank")
        self.label_page_rank.setGeometry(QRect(8, 5, 961, 801))
        self.label_page_rank.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page2)
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.label_page_pd = QLabel(self.page3)
        self.label_page_pd.setObjectName(u"label_page_pd")
        self.label_page_pd.setGeometry(QRect(8, 5, 961, 801))
        self.label_page_pd.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page3)
        self.userInfo = QFrame(self.frame)
        self.userInfo.setObjectName(u"userInfo")
        self.userInfo.setGeometry(QRect(10, 40, 251, 421))
        self.userInfo.setStyleSheet(u"background-color: rgb(162, 255, 236);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.userInfo.setFrameShape(QFrame.NoFrame)
        self.Avatar = QLabel(self.userInfo)
        self.Avatar.setObjectName(u"Avatar")
        self.Avatar.setGeometry(QRect(10, 10, 231, 221))
        self.Avatar.setStyleSheet(u"QLabel {\n"
"	border-radius: 20px;\n"
"	/*border:2px solid rgb(0, 0, 0);*/\n"
"}")
        self.label = QLabel(self.userInfo)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 250, 31, 21))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label_Name = QLabel(self.userInfo)
        self.label_Name.setObjectName(u"label_Name")
        self.label_Name.setGeometry(QRect(40, 250, 201, 21))
        self.label_Name.setFont(font)
        self.label_2 = QLabel(self.userInfo)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 280, 81, 21))
        self.label_2.setFont(font)
        self.label_Username = QLabel(self.userInfo)
        self.label_Username.setObjectName(u"label_Username")
        self.label_Username.setGeometry(QRect(90, 280, 151, 21))
        self.label_Username.setFont(font)
        self.label_3 = QLabel(self.userInfo)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 310, 41, 21))
        self.label_3.setFont(font)
        self.label_Email = QLabel(self.userInfo)
        self.label_Email.setObjectName(u"label_Email")
        self.label_Email.setGeometry(QRect(55, 310, 191, 21))
        self.label_Email.setFont(font)
        self.label_CPass = QLabel(self.userInfo)
        self.label_CPass.setObjectName(u"label_CPass")
        self.label_CPass.setGeometry(QRect(60, 350, 101, 21))
        self.label_CPass.setFont(font)
        self.label_CPass.setStyleSheet(u"QLabel:hover{\n"
"	color: rgb(255, 85, 255);\n"
"}")
        self.label_Icon = QLabel(self.userInfo)
        self.label_Icon.setObjectName(u"label_Icon")
        self.label_Icon.setGeometry(QRect(160, 350, 21, 21))
        self.label_Icon.setFont(font)
        self.label_Icon.setStyleSheet(u"border-image: url(:/icon/resources/icon-pack/lock-closed-outline.svg);")
        self.label_Icon2 = QLabel(self.userInfo)
        self.label_Icon2.setObjectName(u"label_Icon2")
        self.label_Icon2.setGeometry(QRect(140, 380, 21, 21))
        self.label_Icon2.setFont(font)
        self.label_Icon2.setStyleSheet(u"border-image: url(:/icon/resources/icon-pack/exit-outline.svg);")
        self.label_Logout = QLabel(self.userInfo)
        self.label_Logout.setObjectName(u"label_Logout")
        self.label_Logout.setGeometry(QRect(94, 380, 41, 21))
        self.label_Logout.setFont(font)
        self.label_Logout.setStyleSheet(u"QLabel:hover{\n"
"	color: rgb(255, 85, 255);\n"
"}")
        self.Avatar_change = QLabel(self.userInfo)
        self.Avatar_change.setObjectName(u"Avatar_change")
        self.Avatar_change.setGeometry(QRect(10, 10, 231, 221))
        self.Avatar_change.setStyleSheet(u"QLabel{\n"
"	background-color: none;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    background: url(:/icon/resources/icon-pack/icons8-pencil-80_1.png) center center no-repeat;\n"
"    border-radius: 20px;\n"
"	background-color: rgba(0, 0, 0, 0.2);\n"
"	/* Add a semi-transparent black background with 50% opacity */\n"
"	background-size: 20%; /* Ch\u1ec9nh k\u00edch th\u01b0\u1edbc n\u1ec1n xu\u1ed1ng 20% */\n"
"}")
        self.label_Exit = QLabel(self.frame)
        self.label_Exit.setObjectName(u"label_Exit")
        self.label_Exit.setGeometry(QRect(1238, 10, 21, 21))
        self.label_Exit.setStyleSheet(u"border-image: url(:/icon/resources/icon-pack/exit_icon.png);\n"
"background-color: rgb(255, 0, 0);\n"
"border-radius:10px;")
        self.label_Minimize = QLabel(self.frame)
        self.label_Minimize.setObjectName(u"label_Minimize")
        self.label_Minimize.setGeometry(QRect(1210, 10, 21, 21))
        self.label_Minimize.setStyleSheet(u"background-color: rgb(0, 255, 0);\n"
"border-image: url(:/icon/resources/icon-pack/minimize_icon.png);\n"
"border-radius:10px;")

        self.verticalLayout.addWidget(self.frame)

        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"MainWindow", None))
        self.label_PD.setText(QCoreApplication.translate("Main", u"Tin t\u1ee9c", None))
        self.label_Rank.setText(QCoreApplication.translate("Main", u"B\u1ea3ng x\u1ebfp h\u1ea1ng", None))
        self.label_News.setText(QCoreApplication.translate("Main", u"S\u1ea3n ph\u1ea9m", None))
        self.label_page_news.setText(QCoreApplication.translate("Main", u"tin t\u1ee9c", None))
        self.label_page_rank.setText(QCoreApplication.translate("Main", u"h\u1ea1ng", None))
        self.label_page_pd.setText(QCoreApplication.translate("Main", u"s\u1ea3n ph\u1ea9m", None))
        self.Avatar.setText("")
        self.label.setText(QCoreApplication.translate("Main", u"T\u00ean:", None))
        self.label_Name.setText("")
        self.label_2.setText(QCoreApplication.translate("Main", u"Username:", None))
        self.label_Username.setText("")
        self.label_3.setText(QCoreApplication.translate("Main", u"Email:", None))
        self.label_Email.setText("")
        self.label_CPass.setText(QCoreApplication.translate("Main", u"\u0110\u1ed5i m\u1eadt kh\u1ea9u", None))
        self.label_Icon.setText("")
        self.label_Icon2.setText("")
        self.label_Logout.setText(QCoreApplication.translate("Main", u"Tho\u00e1t", None))
        self.Avatar_change.setText("")
        self.label_Exit.setText("")
        self.label_Minimize.setText("")
    # retranslateUi