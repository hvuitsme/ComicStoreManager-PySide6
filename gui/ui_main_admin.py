# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_adminCyNesl.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import image_rc

class Ui_Main_Admin(object):
    def setupUi(self, Main_Admin):
        if not Main_Admin.objectName():
            Main_Admin.setObjectName(u"Main_Admin")
        Main_Admin.resize(1290, 927)
        self.centralwidget = QWidget(Main_Admin)
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
"background-color: rgb(162, 255, 236);")
        self.Main_PD.setFrameShape(QFrame.NoFrame)
        self.stackedWidget = QStackedWidget(self.Main_PD)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(9, 9, 971, 841))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.Table_sanpham = QTableWidget(self.page)
        self.Table_sanpham.setObjectName(u"Table_sanpham")
        self.Table_sanpham.setGeometry(QRect(0, 0, 971, 701))
        self.Table_sanpham.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-1, 710, 971, 131))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.Btn_Add_Pd = QPushButton(self.frame_2)
        self.Btn_Add_Pd.setObjectName(u"Btn_Add_Pd")
        self.Btn_Add_Pd.setGeometry(QRect(130, 90, 111, 31))
        self.Btn_Add_Pd.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Del_Pd = QPushButton(self.frame_2)
        self.Btn_Del_Pd.setObjectName(u"Btn_Del_Pd")
        self.Btn_Del_Pd.setGeometry(QRect(250, 90, 111, 31))
        self.Btn_Del_Pd.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Update = QPushButton(self.frame_2)
        self.Btn_Update.setObjectName(u"Btn_Update")
        self.Btn_Update.setGeometry(QRect(10, 90, 111, 31))
        self.Btn_Update.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.lineEdit_ProductID = QLineEdit(self.frame_2)
        self.lineEdit_ProductID.setObjectName(u"lineEdit_ProductID")
        self.lineEdit_ProductID.setGeometry(QRect(12, 13, 328, 31))
        self.lineEdit_ProductID.setStyleSheet(u"border:2px solid rgb(0, 170, 127);")
        self.lineEdit_ProductName = QLineEdit(self.frame_2)
        self.lineEdit_ProductName.setObjectName(u"lineEdit_ProductName")
        self.lineEdit_ProductName.setGeometry(QRect(12, 53, 328, 31))
        self.lineEdit_ProductName.setStyleSheet(u"border:2px solid rgb(0, 170, 127);")
        self.lineEdit_ImagePath = QLineEdit(self.frame_2)
        self.lineEdit_ImagePath.setObjectName(u"lineEdit_ImagePath")
        self.lineEdit_ImagePath.setGeometry(QRect(390, 13, 211, 31))
        self.lineEdit_ImagePath.setStyleSheet(u"border:2px solid rgb(0, 170, 127);")
        self.lineEdit_Price = QLineEdit(self.frame_2)
        self.lineEdit_Price.setObjectName(u"lineEdit_Price")
        self.lineEdit_Price.setGeometry(QRect(610, 13, 351, 31))
        self.lineEdit_Price.setStyleSheet(u"border:2px solid rgb(0, 170, 127);")
        self.Btn_SelectImage = QPushButton(self.frame_2)
        self.Btn_SelectImage.setObjectName(u"Btn_SelectImage")
        self.Btn_SelectImage.setGeometry(QRect(350, 12, 31, 31))
        self.Btn_SelectImage.setStyleSheet(u"QPushButton{\n"
"	border:2px solid rgb(0, 170, 127);\n"
"	border-radius: 10px;\n"
"	image: url(:/icon/resources/icon-pack/images-outline.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"	image: url(:/icon/resources/icon-pack/images-outline.png);\n"
"}")
        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(370, 96, 61, 16))
        self.Author = QComboBox(self.frame_2)
        self.Author.setObjectName(u"Author")
        self.Author.setGeometry(QRect(350, 57, 191, 22))
        self.Author.setStyleSheet(u"background-color: rgb(197, 197, 197);")
        self.Pub = QComboBox(self.frame_2)
        self.Pub.setObjectName(u"Pub")
        self.Pub.setGeometry(QRect(550, 57, 201, 22))
        self.Pub.setStyleSheet(u"background-color: rgb(197, 197, 197);")
        self.Genre = QComboBox(self.frame_2)
        self.Genre.setObjectName(u"Genre")
        self.Genre.setGeometry(QRect(760, 57, 201, 22))
        self.Genre.setLayoutDirection(Qt.LeftToRight)
        self.Genre.setStyleSheet(u"background-color: rgb(197, 197, 197);")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.Table_nv = QTableWidget(self.page_2)
        self.Table_nv.setObjectName(u"Table_nv")
        self.Table_nv.setGeometry(QRect(0, 0, 971, 701))
        self.Table_nv.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3 = QFrame(self.page_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 710, 971, 131))
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.Btn_Add_Nv = QPushButton(self.frame_3)
        self.Btn_Add_Nv.setObjectName(u"Btn_Add_Nv")
        self.Btn_Add_Nv.setGeometry(QRect(130, 90, 111, 31))
        self.Btn_Add_Nv.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Del_Nv = QPushButton(self.frame_3)
        self.Btn_Del_Nv.setObjectName(u"Btn_Del_Nv")
        self.Btn_Del_Nv.setGeometry(QRect(250, 90, 111, 31))
        self.Btn_Del_Nv.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Update_Nv = QPushButton(self.frame_3)
        self.Btn_Update_Nv.setObjectName(u"Btn_Update_Nv")
        self.Btn_Update_Nv.setGeometry(QRect(10, 90, 111, 31))
        self.Btn_Update_Nv.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.lineEdit_NvName = QLineEdit(self.frame_3)
        self.lineEdit_NvName.setObjectName(u"lineEdit_NvName")
        self.lineEdit_NvName.setGeometry(QRect(14, 13, 301, 31))
        self.lineEdit_NvName.setStyleSheet(u"border:2px solid rgb(0, 170, 127);")
        self.lineEdit_ImagePath_2 = QLineEdit(self.frame_3)
        self.lineEdit_ImagePath_2.setObjectName(u"lineEdit_ImagePath_2")
        self.lineEdit_ImagePath_2.setGeometry(QRect(715, 13, 241, 31))
        self.lineEdit_ImagePath_2.setStyleSheet(u"border:2px solid rgb(0, 170, 127);")
        self.Btn_SelectImage_Nv = QPushButton(self.frame_3)
        self.Btn_SelectImage_Nv.setObjectName(u"Btn_SelectImage_Nv")
        self.Btn_SelectImage_Nv.setGeometry(QRect(680, 13, 31, 31))
        self.Btn_SelectImage_Nv.setStyleSheet(u"QPushButton{\n"
"	border:2px solid rgb(0, 170, 127);\n"
"	border-radius: 10px;\n"
"	image: url(:/icon/resources/icon-pack/images-outline.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"	image: url(:/icon/resources/icon-pack/images-outline.png);\n"
"}")
        self.Status_Nv = QComboBox(self.frame_3)
        self.Status_Nv.addItem("")
        self.Status_Nv.addItem("")
        self.Status_Nv.setObjectName(u"Status_Nv")
        self.Status_Nv.setGeometry(QRect(685, 57, 271, 22))
        self.Status_Nv.setStyleSheet(u"background-color: rgb(197, 197, 197);")
        self.lineEdit_NvUsername = QLineEdit(self.frame_3)
        self.lineEdit_NvUsername.setObjectName(u"lineEdit_NvUsername")
        self.lineEdit_NvUsername.setGeometry(QRect(320, 13, 351, 31))
        self.lineEdit_NvUsername.setStyleSheet(u"border:2px solid rgb(0, 170, 127);")
        self.lineEdit_NvEmail = QLineEdit(self.frame_3)
        self.lineEdit_NvEmail.setObjectName(u"lineEdit_NvEmail")
        self.lineEdit_NvEmail.setGeometry(QRect(14, 50, 301, 31))
        self.lineEdit_NvEmail.setStyleSheet(u"border:2px solid rgb(0, 170, 127);")
        self.lineEdit_NvPass = QLineEdit(self.frame_3)
        self.lineEdit_NvPass.setObjectName(u"lineEdit_NvPass")
        self.lineEdit_NvPass.setGeometry(QRect(320, 50, 351, 31))
        self.lineEdit_NvPass.setStyleSheet(u"border:2px solid rgb(0, 170, 127);")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.Table_tonkho = QTableWidget(self.page_3)
        self.Table_tonkho.setObjectName(u"Table_tonkho")
        self.Table_tonkho.setGeometry(QRect(0, 0, 971, 741))
        self.Table_tonkho.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_4 = QFrame(self.page_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(-1, 749, 971, 91))
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.lineEdit_Quantt = QLineEdit(self.frame_4)
        self.lineEdit_Quantt.setObjectName(u"lineEdit_Quantt")
        self.lineEdit_Quantt.setGeometry(QRect(160, 10, 221, 31))
        self.lineEdit_Quantt.setStyleSheet(u"border:2px solid rgb(0, 170, 127);")
        self.Btn_Update_Inv = QPushButton(self.frame_4)
        self.Btn_Update_Inv.setObjectName(u"Btn_Update_Inv")
        self.Btn_Update_Inv.setGeometry(QRect(10, 50, 111, 31))
        self.Btn_Update_Inv.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.ID_Inv = QComboBox(self.frame_4)
        self.ID_Inv.setObjectName(u"ID_Inv")
        self.ID_Inv.setGeometry(QRect(10, 14, 141, 22))
        self.ID_Inv.setStyleSheet(u"background-color: rgb(197, 197, 197);")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.Table_lshd = QTableWidget(self.page_4)
        self.Table_lshd.setObjectName(u"Table_lshd")
        self.Table_lshd.setGeometry(QRect(0, 260, 971, 581))
        self.Table_lshd.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_5 = QFrame(self.page_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 0, 971, 241))
        self.frame_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 11, 71, 71))
        self.label_4.setStyleSheet(u"border-image: url(:/icon/resources/icon-pack/wallet-solid.svg);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(560, 11, 71, 71))
        self.label_5.setStyleSheet(u"border-image: url(:/icon/resources/icon-pack/hand-holding-dollar-solid.svg);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(768, 11, 71, 71))
        self.label_6.setStyleSheet(u"border-image: url(:/icon/resources/icon-pack/hand-holding-solid.svg);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(350, 11, 71, 71))
        self.label_7.setStyleSheet(u"border-image: url(:/icon/resources/icon-pack/user-group-solid.svg);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(560, 90, 71, 21))
        font = QFont()
        font.setFamilies([u"Agbalumo"])
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 90, 91, 21))
        self.label_9.setFont(font)
        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(768, 90, 71, 21))
        self.label_10.setFont(font)
        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(350, 90, 91, 21))
        self.label_11.setFont(font)
        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 200, 91, 31))
        self.label_12.setFont(font)
        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 130, 71, 71))
        self.label_13.setStyleSheet(u"border-image: url(:/icon/resources/icon-pack/file-circle-check-solid.svg);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.tt_price = QLabel(self.frame_5)
        self.tt_price.setObjectName(u"tt_price")
        self.tt_price.setGeometry(QRect(100, 11, 231, 71))
        self.tt_price.setStyleSheet(u"border-bottom: 2px solid rgb(0, 170, 127);\n"
"border-radius: none;")
        self.mber = QLabel(self.frame_5)
        self.mber.setObjectName(u"mber")
        self.mber.setGeometry(QRect(432, 11, 101, 71))
        self.mber.setStyleSheet(u"border-bottom: 2px solid rgb(0, 170, 127);\n"
"border-radius: none;")
        self.qtt_sell = QLabel(self.frame_5)
        self.qtt_sell.setObjectName(u"qtt_sell")
        self.qtt_sell.setGeometry(QRect(642, 11, 101, 71))
        self.qtt_sell.setStyleSheet(u"border-bottom: 2px solid rgb(0, 170, 127);\n"
"border-radius: none;")
        self.qtt_rent = QLabel(self.frame_5)
        self.qtt_rent.setObjectName(u"qtt_rent")
        self.qtt_rent.setGeometry(QRect(850, 11, 101, 71))
        self.qtt_rent.setStyleSheet(u"border-bottom: 2px solid rgb(0, 170, 127);\n"
"border-radius: none;")
        self.qtt_order = QLabel(self.frame_5)
        self.qtt_order.setObjectName(u"qtt_order")
        self.qtt_order.setGeometry(QRect(102, 130, 101, 71))
        self.qtt_order.setStyleSheet(u"border-bottom: 2px solid rgb(0, 170, 127);\n"
"border-radius: none;")
        self.label = QLabel(self.page_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 242, 101, 16))
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.Table_NhaPh = QTableWidget(self.page_5)
        self.Table_NhaPh.setObjectName(u"Table_NhaPh")
        self.Table_NhaPh.setGeometry(QRect(0, 0, 971, 741))
        self.Table_NhaPh.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_6 = QFrame(self.page_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 750, 971, 91))
        self.frame_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.Btn_Update_Pub = QPushButton(self.frame_6)
        self.Btn_Update_Pub.setObjectName(u"Btn_Update_Pub")
        self.Btn_Update_Pub.setGeometry(QRect(10, 50, 111, 31))
        self.Btn_Update_Pub.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Add_Pub = QPushButton(self.frame_6)
        self.Btn_Add_Pub.setObjectName(u"Btn_Add_Pub")
        self.Btn_Add_Pub.setGeometry(QRect(130, 50, 111, 31))
        self.Btn_Add_Pub.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Del_Pub = QPushButton(self.frame_6)
        self.Btn_Del_Pub.setObjectName(u"Btn_Del_Pub")
        self.Btn_Del_Pub.setGeometry(QRect(250, 50, 111, 31))
        self.Btn_Del_Pub.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.lineEdit_PubID = QLineEdit(self.frame_6)
        self.lineEdit_PubID.setObjectName(u"lineEdit_PubID")
        self.lineEdit_PubID.setGeometry(QRect(10, 10, 141, 31))
        self.lineEdit_PubID.setStyleSheet(u"border:2px solid rgb(0, 170, 127);")
        self.lineEdit_PubName = QLineEdit(self.frame_6)
        self.lineEdit_PubName.setObjectName(u"lineEdit_PubName")
        self.lineEdit_PubName.setGeometry(QRect(160, 10, 328, 31))
        self.lineEdit_PubName.setStyleSheet(u"border:2px solid rgb(0, 170, 127);")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.Table_tacgia = QTableWidget(self.page_6)
        self.Table_tacgia.setObjectName(u"Table_tacgia")
        self.Table_tacgia.setGeometry(QRect(0, 0, 971, 741))
        self.Table_tacgia.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_7 = QFrame(self.page_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(0, 750, 971, 91))
        self.frame_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.Btn_Update_Auth = QPushButton(self.frame_7)
        self.Btn_Update_Auth.setObjectName(u"Btn_Update_Auth")
        self.Btn_Update_Auth.setGeometry(QRect(10, 50, 111, 31))
        self.Btn_Update_Auth.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Add_Auth = QPushButton(self.frame_7)
        self.Btn_Add_Auth.setObjectName(u"Btn_Add_Auth")
        self.Btn_Add_Auth.setGeometry(QRect(130, 50, 111, 31))
        self.Btn_Add_Auth.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Del_Auth = QPushButton(self.frame_7)
        self.Btn_Del_Auth.setObjectName(u"Btn_Del_Auth")
        self.Btn_Del_Auth.setGeometry(QRect(250, 50, 111, 31))
        self.Btn_Del_Auth.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.lineEdit_AuthN = QLineEdit(self.frame_7)
        self.lineEdit_AuthN.setObjectName(u"lineEdit_AuthN")
        self.lineEdit_AuthN.setGeometry(QRect(160, 10, 328, 31))
        self.lineEdit_AuthN.setStyleSheet(u"border:2px solid rgb(0, 170, 127);")
        self.lineEdit_AuthID = QLineEdit(self.frame_7)
        self.lineEdit_AuthID.setObjectName(u"lineEdit_AuthID")
        self.lineEdit_AuthID.setGeometry(QRect(10, 10, 141, 31))
        self.lineEdit_AuthID.setStyleSheet(u"border:2px solid rgb(0, 170, 127);")
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.Table_theloai = QTableWidget(self.page_7)
        self.Table_theloai.setObjectName(u"Table_theloai")
        self.Table_theloai.setGeometry(QRect(0, 0, 971, 741))
        self.Table_theloai.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_8 = QFrame(self.page_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(0, 750, 971, 91))
        self.frame_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.Btn_Update_Genre = QPushButton(self.frame_8)
        self.Btn_Update_Genre.setObjectName(u"Btn_Update_Genre")
        self.Btn_Update_Genre.setGeometry(QRect(10, 50, 111, 31))
        self.Btn_Update_Genre.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Add_Genre = QPushButton(self.frame_8)
        self.Btn_Add_Genre.setObjectName(u"Btn_Add_Genre")
        self.Btn_Add_Genre.setGeometry(QRect(130, 50, 111, 31))
        self.Btn_Add_Genre.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Del_Genre = QPushButton(self.frame_8)
        self.Btn_Del_Genre.setObjectName(u"Btn_Del_Genre")
        self.Btn_Del_Genre.setGeometry(QRect(250, 50, 111, 31))
        self.Btn_Del_Genre.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.lineEdit_GenreN = QLineEdit(self.frame_8)
        self.lineEdit_GenreN.setObjectName(u"lineEdit_GenreN")
        self.lineEdit_GenreN.setGeometry(QRect(160, 10, 328, 31))
        self.lineEdit_GenreN.setStyleSheet(u"border:2px solid rgb(0, 170, 127);")
        self.lineEdit_GenreID = QLineEdit(self.frame_8)
        self.lineEdit_GenreID.setObjectName(u"lineEdit_GenreID")
        self.lineEdit_GenreID.setGeometry(QRect(10, 10, 141, 31))
        self.lineEdit_GenreID.setStyleSheet(u"border:2px solid rgb(0, 170, 127);")
        self.stackedWidget.addWidget(self.page_7)
        self.userInfo = QFrame(self.frame)
        self.userInfo.setObjectName(u"userInfo")
        self.userInfo.setGeometry(QRect(10, 40, 251, 361))
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
        self.label_2 = QLabel(self.userInfo)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 240, 81, 21))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_Username = QLabel(self.userInfo)
        self.label_Username.setObjectName(u"label_Username")
        self.label_Username.setGeometry(QRect(90, 240, 151, 21))
        self.label_Username.setFont(font1)
        self.label_3 = QLabel(self.userInfo)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 270, 41, 21))
        self.label_3.setFont(font1)
        self.label_Email = QLabel(self.userInfo)
        self.label_Email.setObjectName(u"label_Email")
        self.label_Email.setGeometry(QRect(55, 270, 191, 21))
        self.label_Email.setFont(font1)
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
        self.label_Icon2 = QLabel(self.userInfo)
        self.label_Icon2.setObjectName(u"label_Icon2")
        self.label_Icon2.setGeometry(QRect(146, 330, 21, 21))
        self.label_Icon2.setFont(font1)
        self.label_Icon2.setStyleSheet(u"border-image: url(:/icon/resources/icon-pack/exit-outline.svg);")
        self.label_CPass = QLabel(self.userInfo)
        self.label_CPass.setObjectName(u"label_CPass")
        self.label_CPass.setGeometry(QRect(66, 300, 101, 21))
        self.label_CPass.setFont(font1)
        self.label_CPass.setStyleSheet(u"QLabel:hover{\n"
"	color: rgb(255, 85, 255);\n"
"}")
        self.label_Icon = QLabel(self.userInfo)
        self.label_Icon.setObjectName(u"label_Icon")
        self.label_Icon.setGeometry(QRect(166, 300, 21, 21))
        self.label_Icon.setFont(font1)
        self.label_Icon.setStyleSheet(u"border-image: url(:/icon/resources/icon-pack/lock-closed-outline.svg);")
        self.label_Logout = QLabel(self.userInfo)
        self.label_Logout.setObjectName(u"label_Logout")
        self.label_Logout.setGeometry(QRect(100, 330, 41, 21))
        self.label_Logout.setFont(font1)
        self.label_Logout.setStyleSheet(u"QLabel:hover{\n"
"	color: rgb(255, 85, 255);\n"
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
        self.Btn_Pd = QPushButton(self.frame)
        self.Btn_Pd.setObjectName(u"Btn_Pd")
        self.Btn_Pd.setGeometry(QRect(10, 410, 251, 41))
        self.Btn_Pd.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Nv = QPushButton(self.frame)
        self.Btn_Nv.setObjectName(u"Btn_Nv")
        self.Btn_Nv.setGeometry(QRect(10, 460, 251, 41))
        self.Btn_Nv.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Inventory = QPushButton(self.frame)
        self.Btn_Inventory.setObjectName(u"Btn_Inventory")
        self.Btn_Inventory.setGeometry(QRect(10, 510, 251, 41))
        self.Btn_Inventory.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Pub = QPushButton(self.frame)
        self.Btn_Pub.setObjectName(u"Btn_Pub")
        self.Btn_Pub.setGeometry(QRect(10, 610, 251, 41))
        self.Btn_Pub.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Auth = QPushButton(self.frame)
        self.Btn_Auth.setObjectName(u"Btn_Auth")
        self.Btn_Auth.setGeometry(QRect(10, 660, 251, 41))
        self.Btn_Auth.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Revenue = QPushButton(self.frame)
        self.Btn_Revenue.setObjectName(u"Btn_Revenue")
        self.Btn_Revenue.setGeometry(QRect(10, 560, 251, 41))
        self.Btn_Revenue.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Genre = QPushButton(self.frame)
        self.Btn_Genre.setObjectName(u"Btn_Genre")
        self.Btn_Genre.setGeometry(QRect(10, 710, 251, 41))
        self.Btn_Genre.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")

        self.verticalLayout.addWidget(self.frame)

        Main_Admin.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main_Admin)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Main_Admin)
    # setupUi

    def retranslateUi(self, Main_Admin):
        Main_Admin.setWindowTitle(QCoreApplication.translate("Main_Admin", u"Th\u01b0 vi\u1ec7n tr\u1ef1c tuy\u1ebfn", None))
        self.Btn_Add_Pd.setText(QCoreApplication.translate("Main_Admin", u"Th\u00eam", None))
        self.Btn_Del_Pd.setText(QCoreApplication.translate("Main_Admin", u"Xo\u00e1", None))
        self.Btn_Update.setText(QCoreApplication.translate("Main_Admin", u"C\u1eadp nh\u1eadt", None))
        self.lineEdit_ProductID.setPlaceholderText(QCoreApplication.translate("Main_Admin", u"M\u00e3 s\u1ea3n ph\u1ea9m", None))
        self.lineEdit_ProductName.setPlaceholderText(QCoreApplication.translate("Main_Admin", u"T\u00ean s\u1ea3n ph\u1ea9m", None))
        self.lineEdit_ImagePath.setPlaceholderText(QCoreApplication.translate("Main_Admin", u"\u0110\u01b0\u1eddng d\u1eabn \u1ea3nh", None))
        self.lineEdit_Price.setPlaceholderText(QCoreApplication.translate("Main_Admin", u"Gi\u00e1", None))
        self.Btn_SelectImage.setText("")
        self.label_18.setText("")
        self.Author.setPlaceholderText(QCoreApplication.translate("Main_Admin", u"T\u00e1c gi\u1ea3", None))
        self.Pub.setPlaceholderText(QCoreApplication.translate("Main_Admin", u"Nh\u00e0 xu\u1ea5t b\u1ea3n", None))
        self.Genre.setPlaceholderText(QCoreApplication.translate("Main_Admin", u"Th\u1ec3 lo\u1ea1i", None))
        self.Btn_Add_Nv.setText(QCoreApplication.translate("Main_Admin", u"Th\u00eam", None))
        self.Btn_Del_Nv.setText(QCoreApplication.translate("Main_Admin", u"Xo\u00e1", None))
        self.Btn_Update_Nv.setText(QCoreApplication.translate("Main_Admin", u"C\u1eadp nh\u1eadt", None))
        self.lineEdit_NvName.setPlaceholderText(QCoreApplication.translate("Main_Admin", u"T\u00ean nh\u00e2n vi\u00ean", None))
        self.lineEdit_ImagePath_2.setPlaceholderText(QCoreApplication.translate("Main_Admin", u"\u0110\u01b0\u1eddng d\u1eabn \u1ea3nh", None))
        self.Btn_SelectImage_Nv.setText("")
        self.Status_Nv.setItemText(0, QCoreApplication.translate("Main_Admin", u"Admin", None))
        self.Status_Nv.setItemText(1, QCoreApplication.translate("Main_Admin", u"Nh\u00e2n vi\u00ean", None))

        self.Status_Nv.setPlaceholderText(QCoreApplication.translate("Main_Admin", u"Ch\u1ee9c v\u1ee5", None))
        self.lineEdit_NvUsername.setPlaceholderText(QCoreApplication.translate("Main_Admin", u"Username", None))
        self.lineEdit_NvEmail.setPlaceholderText(QCoreApplication.translate("Main_Admin", u"Email", None))
        self.lineEdit_NvPass.setPlaceholderText(QCoreApplication.translate("Main_Admin", u"Password", None))
        self.lineEdit_Quantt.setPlaceholderText(QCoreApplication.translate("Main_Admin", u"S\u1ed1 l\u01b0\u1ee3ng", None))
        self.Btn_Update_Inv.setText(QCoreApplication.translate("Main_Admin", u"C\u1eadp nh\u1eadt", None))
        self.ID_Inv.setPlaceholderText(QCoreApplication.translate("Main_Admin", u"ID s\u1ea3n ph\u1ea9m", None))
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("Main_Admin", u"\u0110\u00e3 mua", None))
        self.label_9.setText(QCoreApplication.translate("Main_Admin", u"Doanh thu", None))
        self.label_10.setText(QCoreApplication.translate("Main_Admin", u"\u0110\u00e3 thu\u00ea", None))
        self.label_11.setText(QCoreApplication.translate("Main_Admin", u"Nh\u00e2n vi\u00ean", None))
        self.label_12.setText(QCoreApplication.translate("Main_Admin", u"\u0110\u01a1n h\u00e0ng", None))
        self.label_13.setText("")
        self.tt_price.setText("")
        self.mber.setText("")
        self.qtt_sell.setText("")
        self.qtt_rent.setText("")
        self.qtt_order.setText("")
        self.label.setText(QCoreApplication.translate("Main_Admin", u"L\u1ecbch s\u1eed ho\u1ea1t \u0111\u1ed9ng:", None))
        self.Btn_Update_Pub.setText(QCoreApplication.translate("Main_Admin", u"C\u1eadp nh\u1eadt", None))
        self.Btn_Add_Pub.setText(QCoreApplication.translate("Main_Admin", u"Th\u00eam", None))
        self.Btn_Del_Pub.setText(QCoreApplication.translate("Main_Admin", u"Xo\u00e1", None))
        self.lineEdit_PubID.setPlaceholderText(QCoreApplication.translate("Main_Admin", u"ID", None))
        self.lineEdit_PubName.setPlaceholderText(QCoreApplication.translate("Main_Admin", u"Nh\u00e0 ph\u00e1t h\u00e0nh", None))
        self.Btn_Update_Auth.setText(QCoreApplication.translate("Main_Admin", u"C\u1eadp nh\u1eadt", None))
        self.Btn_Add_Auth.setText(QCoreApplication.translate("Main_Admin", u"Th\u00eam", None))
        self.Btn_Del_Auth.setText(QCoreApplication.translate("Main_Admin", u"Xo\u00e1", None))
        self.lineEdit_AuthN.setPlaceholderText(QCoreApplication.translate("Main_Admin", u"T\u00ean t\u00e1c gi\u1ea3", None))
        self.lineEdit_AuthID.setPlaceholderText(QCoreApplication.translate("Main_Admin", u"ID", None))
        self.Btn_Update_Genre.setText(QCoreApplication.translate("Main_Admin", u"C\u1eadp nh\u1eadt", None))
        self.Btn_Add_Genre.setText(QCoreApplication.translate("Main_Admin", u"Th\u00eam", None))
        self.Btn_Del_Genre.setText(QCoreApplication.translate("Main_Admin", u"Xo\u00e1", None))
        self.lineEdit_GenreN.setPlaceholderText(QCoreApplication.translate("Main_Admin", u"T\u00ean th\u1ec3 lo\u1ea1i", None))
        self.lineEdit_GenreID.setPlaceholderText(QCoreApplication.translate("Main_Admin", u"ID", None))
        self.Avatar.setText("")
        self.label_2.setText(QCoreApplication.translate("Main_Admin", u"Username:", None))
        self.label_Username.setText("")
        self.label_3.setText(QCoreApplication.translate("Main_Admin", u"Email:", None))
        self.label_Email.setText("")
        self.Avatar_change.setText("")
        self.label_Icon2.setText("")
        self.label_CPass.setText(QCoreApplication.translate("Main_Admin", u"\u0110\u1ed5i m\u1eadt kh\u1ea9u", None))
        self.label_Icon.setText("")
        self.label_Logout.setText(QCoreApplication.translate("Main_Admin", u"Tho\u00e1t", None))
#if QT_CONFIG(tooltip)
        self.label_Exit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_Exit.setText("")
        self.label_Minimize.setText("")
        self.Btn_Pd.setText(QCoreApplication.translate("Main_Admin", u"Qu\u1ea3n l\u00fd s\u1ea3n ph\u1ea9m", None))
        self.Btn_Nv.setText(QCoreApplication.translate("Main_Admin", u"Qu\u1ea3n l\u00fd nh\u00e2n vi\u00ean", None))
        self.Btn_Inventory.setText(QCoreApplication.translate("Main_Admin", u"Qu\u1ea3n l\u00fd t\u1ed3n kho", None))
        self.Btn_Pub.setText(QCoreApplication.translate("Main_Admin", u"Qu\u1ea3n l\u00fd Publisher", None))
        self.Btn_Auth.setText(QCoreApplication.translate("Main_Admin", u"Qu\u1ea3n l\u00fd Author", None))
        self.Btn_Revenue.setText(QCoreApplication.translate("Main_Admin", u"Doanh thu", None))
        self.Btn_Genre.setText(QCoreApplication.translate("Main_Admin", u"Qu\u1ea3n l\u00fd th\u1ec3 lo\u1ea1i truy\u1ec7n", None))
    # retranslateUi

