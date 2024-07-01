# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_employeeHZgeOg.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QDateEdit,
    QFrame, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import image_rc

class Ui_Main_Employee(object):
    def setupUi(self, Main_Employee):
        if not Main_Employee.objectName():
            Main_Employee.setObjectName(u"Main_Employee")
        Main_Employee.resize(1290, 930)
        self.centralwidget = QWidget(Main_Employee)
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
        self.Table_Sp = QTableWidget(self.page)
        self.Table_Sp.setObjectName(u"Table_Sp")
        self.Table_Sp.setGeometry(QRect(0, 20, 541, 661))
        self.Table_Sp.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.frame_3 = QFrame(self.page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 730, 971, 111))
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.Btn_Edit_Kh = QPushButton(self.frame_3)
        self.Btn_Edit_Kh.setObjectName(u"Btn_Edit_Kh")
        self.Btn_Edit_Kh.setGeometry(QRect(130, 70, 111, 31))
        self.Btn_Edit_Kh.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Del_Hd = QPushButton(self.frame_3)
        self.Btn_Del_Hd.setObjectName(u"Btn_Del_Hd")
        self.Btn_Del_Hd.setGeometry(QRect(250, 70, 111, 31))
        self.Btn_Del_Hd.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Paym_Kh = QPushButton(self.frame_3)
        self.Btn_Paym_Kh.setObjectName(u"Btn_Paym_Kh")
        self.Btn_Paym_Kh.setGeometry(QRect(10, 70, 111, 31))
        self.Btn_Paym_Kh.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Kh_name = QLineEdit(self.frame_3)
        self.Kh_name.setObjectName(u"Kh_name")
        self.Kh_name.setGeometry(QRect(14, 30, 301, 31))
        self.Kh_name.setStyleSheet(u"border:2px solid rgb(0, 170, 127);")
        self.Kh_phone = QLineEdit(self.frame_3)
        self.Kh_phone.setObjectName(u"Kh_phone")
        self.Kh_phone.setGeometry(QRect(320, 30, 321, 31))
        self.Kh_phone.setStyleSheet(u"border:2px solid rgb(0, 170, 127);")
        self.Kh_Addr = QLineEdit(self.frame_3)
        self.Kh_Addr.setObjectName(u"Kh_Addr")
        self.Kh_Addr.setGeometry(QRect(650, 30, 311, 31))
        self.Kh_Addr.setStyleSheet(u"border:2px solid rgb(0, 170, 127);")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(14, 10, 131, 16))
        self.Btn_Clr = QPushButton(self.frame_3)
        self.Btn_Clr.setObjectName(u"Btn_Clr")
        self.Btn_Clr.setGeometry(QRect(370, 70, 31, 31))
        self.Btn_Clr.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"	image: url(:/icon/resources/icon-pack/repeat-outline.svg);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"	image: url(:/icon/resources/icon-pack/repeat-outline.svg);\n"
"}")
        self.Rent_St = QDateEdit(self.frame_3)
        self.Rent_St.setObjectName(u"Rent_St")
        self.Rent_St.setGeometry(QRect(557, 70, 110, 31))
        self.Rent_St.setStyleSheet(u"border: 2px solid rgb(0, 170, 127);")
        self.Rent_End = QDateEdit(self.frame_3)
        self.Rent_End.setObjectName(u"Rent_End")
        self.Rent_End.setGeometry(QRect(750, 70, 110, 31))
        self.Rent_End.setStyleSheet(u"#Rent_End.QDateEdit{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"}")
        self.label_st = QLabel(self.frame_3)
        self.label_st.setObjectName(u"label_st")
        self.label_st.setGeometry(QRect(487, 76, 68, 20))
        self.label_end = QLabel(self.frame_3)
        self.label_end.setObjectName(u"label_end")
        self.label_end.setGeometry(QRect(697, 76, 51, 20))
        self.Btn_Save = QPushButton(self.frame_3)
        self.Btn_Save.setObjectName(u"Btn_Save")
        self.Btn_Save.setGeometry(QRect(450, 70, 31, 31))
        self.Btn_Save.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"	image: url(:/icon/resources/icon-pack/checkmark-outline.svg);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"	image: url(:/icon/resources/icon-pack/checkmark-outline.svg);\n"
"}")
        self.Btn_re_prt_bill = QPushButton(self.frame_3)
        self.Btn_re_prt_bill.setObjectName(u"Btn_re_prt_bill")
        self.Btn_re_prt_bill.setGeometry(QRect(410, 70, 31, 31))
        self.Btn_re_prt_bill.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"	image: url(:/icon/resources/icon-pack/file-invoice-solid.svg);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"	image: url(:/icon/resources/icon-pack/file-invoice-solid.svg);\n"
"}")
        self.Table_Hd = QTableWidget(self.page)
        self.Table_Hd.setObjectName(u"Table_Hd")
        self.Table_Hd.setGeometry(QRect(550, 20, 421, 371))
        self.Table_Hd.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.Table_Hd_2 = QTableWidget(self.page)
        self.Table_Hd_2.setObjectName(u"Table_Hd_2")
        self.Table_Hd_2.setGeometry(QRect(550, 410, 421, 311))
        self.Table_Hd_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(550, 392, 71, 16))
        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(550, 0, 61, 16))
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 101, 16))
        self.frame_5 = QFrame(self.page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 680, 541, 41))
        self.frame_5.setStyleSheet(u"#frame_5.QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-top: 1px solid rgb(0, 170, 127);\n"
"	border-radius: 0px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(5, 5, 50, 31))
        font = QFont()
        font.setFamilies([u"Agbalumo"])
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Tt_price = QLineEdit(self.frame_5)
        self.Tt_price.setObjectName(u"Tt_price")
        self.Tt_price.setGeometry(QRect(60, 5, 471, 31))
        self.Tt_price.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.cld_return = QCalendarWidget(self.page)
        self.cld_return.setObjectName(u"cld_return")
        self.cld_return.setGeometry(QRect(670, 600, 256, 190))
        self.cld_return.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(162, 255, 236);")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.Table_sanpham = QTableWidget(self.page_2)
        self.Table_sanpham.setObjectName(u"Table_sanpham")
        self.Table_sanpham.setGeometry(QRect(0, 0, 971, 701))
        self.Table_sanpham.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_2 = QFrame(self.page_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-1, 710, 971, 131))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.Btn_Del_Pd = QPushButton(self.frame_2)
        self.Btn_Del_Pd.setObjectName(u"Btn_Del_Pd")
        self.Btn_Del_Pd.setGeometry(QRect(130, 90, 111, 31))
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
        self.Author.addItem("")
        self.Author.setObjectName(u"Author")
        self.Author.setGeometry(QRect(350, 57, 191, 22))
        self.Author.setStyleSheet(u"background-color: rgb(197, 197, 197);")
        self.Pub = QComboBox(self.frame_2)
        self.Pub.addItem("")
        self.Pub.addItem("")
        self.Pub.setObjectName(u"Pub")
        self.Pub.setGeometry(QRect(550, 57, 201, 22))
        self.Pub.setStyleSheet(u"background-color: rgb(197, 197, 197);")
        self.Genre = QComboBox(self.frame_2)
        self.Genre.addItem("")
        self.Genre.setObjectName(u"Genre")
        self.Genre.setGeometry(QRect(760, 57, 201, 22))
        self.Genre.setLayoutDirection(Qt.LeftToRight)
        self.Genre.setStyleSheet(u"background-color: rgb(197, 197, 197);")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.Table_b_keeping = QTableWidget(self.page_3)
        self.Table_b_keeping.setObjectName(u"Table_b_keeping")
        self.Table_b_keeping.setGeometry(QRect(0, 0, 971, 776))
        self.Table_b_keeping.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_6 = QFrame(self.page_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 784, 971, 57))
        self.frame_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.Btn_bk_update = QPushButton(self.frame_6)
        self.Btn_bk_update.setObjectName(u"Btn_bk_update")
        self.Btn_bk_update.setGeometry(QRect(10, 13, 111, 31))
        self.Btn_bk_update.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Bk_sl = QLineEdit(self.frame_6)
        self.Bk_sl.setObjectName(u"Bk_sl")
        self.Bk_sl.setGeometry(QRect(130, 13, 328, 31))
        self.Bk_sl.setStyleSheet(u"border:2px solid rgb(0, 170, 127);")
        self.label_19 = QLabel(self.frame_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(370, 96, 61, 16))
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.Table_sell = QTableWidget(self.page_4)
        self.Table_sell.setObjectName(u"Table_sell")
        self.Table_sell.setGeometry(QRect(0, 0, 971, 841))
        self.Table_sell.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.Table_rent = QTableWidget(self.page_5)
        self.Table_rent.setObjectName(u"Table_rent")
        self.Table_rent.setGeometry(QRect(0, 0, 971, 791))
        self.Table_rent.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_7 = QFrame(self.page_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(0, 799, 971, 41))
        self.frame_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.Rent_st = QComboBox(self.frame_7)
        self.Rent_st.addItem("")
        self.Rent_st.setObjectName(u"Rent_st")
        self.Rent_st.setGeometry(QRect(130, 10, 211, 22))
        self.Rent_st.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.Btn_Upd_Rent = QPushButton(self.frame_7)
        self.Btn_Upd_Rent.setObjectName(u"Btn_Upd_Rent")
        self.Btn_Upd_Rent.setGeometry(QRect(10, 5, 111, 31))
        self.Btn_Upd_Rent.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.stackedWidget.addWidget(self.page_6)
        self.userInfo = QFrame(self.frame)
        self.userInfo.setObjectName(u"userInfo")
        self.userInfo.setGeometry(QRect(10, 40, 251, 391))
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
        self.label_2.setGeometry(QRect(10, 270, 81, 21))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_Username = QLabel(self.userInfo)
        self.label_Username.setObjectName(u"label_Username")
        self.label_Username.setGeometry(QRect(90, 270, 151, 21))
        self.label_Username.setFont(font1)
        self.label_3 = QLabel(self.userInfo)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 300, 41, 21))
        self.label_3.setFont(font1)
        self.label_Email = QLabel(self.userInfo)
        self.label_Email.setObjectName(u"label_Email")
        self.label_Email.setGeometry(QRect(55, 300, 187, 21))
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
        self.label_Icon2.setGeometry(QRect(146, 360, 21, 21))
        self.label_Icon2.setFont(font1)
        self.label_Icon2.setStyleSheet(u"border-image: url(:/icon/resources/icon-pack/exit-outline.svg);")
        self.label_CPass = QLabel(self.userInfo)
        self.label_CPass.setObjectName(u"label_CPass")
        self.label_CPass.setGeometry(QRect(66, 330, 101, 21))
        self.label_CPass.setFont(font1)
        self.label_CPass.setStyleSheet(u"QLabel:hover{\n"
"	color: rgb(255, 85, 255);\n"
"}")
        self.label_Icon = QLabel(self.userInfo)
        self.label_Icon.setObjectName(u"label_Icon")
        self.label_Icon.setGeometry(QRect(166, 330, 21, 21))
        self.label_Icon.setFont(font1)
        self.label_Icon.setStyleSheet(u"border-image: url(:/icon/resources/icon-pack/lock-closed-outline.svg);")
        self.label_Logout = QLabel(self.userInfo)
        self.label_Logout.setObjectName(u"label_Logout")
        self.label_Logout.setGeometry(QRect(100, 360, 41, 21))
        self.label_Logout.setFont(font1)
        self.label_Logout.setStyleSheet(u"QLabel:hover{\n"
"	color: rgb(255, 85, 255);\n"
"}")
        self.label_8 = QLabel(self.userInfo)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 240, 31, 21))
        self.label_8.setFont(font1)
        self.label_Name = QLabel(self.userInfo)
        self.label_Name.setObjectName(u"label_Name")
        self.label_Name.setGeometry(QRect(43, 240, 197, 21))
        self.label_Name.setFont(font1)
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
        self.Btn_Pd.setGeometry(QRect(10, 490, 251, 41))
        self.Btn_Pd.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Td = QPushButton(self.frame)
        self.Btn_Td.setObjectName(u"Btn_Td")
        self.Btn_Td.setGeometry(QRect(10, 440, 251, 41))
        self.Btn_Td.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Bkeeping = QPushButton(self.frame)
        self.Btn_Bkeeping.setObjectName(u"Btn_Bkeeping")
        self.Btn_Bkeeping.setGeometry(QRect(10, 540, 251, 41))
        self.Btn_Bkeeping.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Sell = QPushButton(self.frame)
        self.Btn_Sell.setObjectName(u"Btn_Sell")
        self.Btn_Sell.setGeometry(QRect(10, 590, 251, 41))
        self.Btn_Sell.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Report = QPushButton(self.frame)
        self.Btn_Report.setObjectName(u"Btn_Report")
        self.Btn_Report.setGeometry(QRect(10, 690, 251, 41))
        self.Btn_Report.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")
        self.Btn_Rent = QPushButton(self.frame)
        self.Btn_Rent.setObjectName(u"Btn_Rent")
        self.Btn_Rent.setGeometry(QRect(10, 640, 251, 41))
        self.Btn_Rent.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 127);\n"
"}")

        self.verticalLayout.addWidget(self.frame)

        Main_Employee.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main_Employee)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Main_Employee)
    # setupUi

    def retranslateUi(self, Main_Employee):
        Main_Employee.setWindowTitle(QCoreApplication.translate("Main_Employee", u"MainWindow", None))
        self.Btn_Edit_Kh.setText(QCoreApplication.translate("Main_Employee", u"S\u1eeda", None))
        self.Btn_Del_Hd.setText(QCoreApplication.translate("Main_Employee", u"Xo\u00e1", None))
        self.Btn_Paym_Kh.setText(QCoreApplication.translate("Main_Employee", u"Thanh to\u00e1n", None))
        self.Kh_name.setPlaceholderText(QCoreApplication.translate("Main_Employee", u"T\u00ean kh\u00e1ch h\u00e0ng", None))
        self.Kh_phone.setPlaceholderText(QCoreApplication.translate("Main_Employee", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None))
        self.Kh_Addr.setPlaceholderText(QCoreApplication.translate("Main_Employee", u"\u0110\u1ecba ch\u1ec9", None))
        self.label.setText(QCoreApplication.translate("Main_Employee", u"Th\u00f4ng tin kh\u00e1ch h\u00e0ng:", None))
        self.Btn_Clr.setText("")
        self.Rent_St.setDisplayFormat(QCoreApplication.translate("Main_Employee", u"dd/MM/yyyy", None))
        self.Rent_End.setDisplayFormat(QCoreApplication.translate("Main_Employee", u"dd/MM/yyyy", None))
        self.label_st.setText(QCoreApplication.translate("Main_Employee", u"Ng\u00e0y m\u01b0\u1ee3n:", None))
        self.label_end.setText(QCoreApplication.translate("Main_Employee", u"Ng\u00e0y tr\u1ea3:", None))
        self.Btn_Save.setText("")
        self.Btn_re_prt_bill.setText("")
        self.label_6.setText(QCoreApplication.translate("Main_Employee", u"Chi ti\u1ebft \u0111\u01a1n:", None))
        self.label_5.setText(QCoreApplication.translate("Main_Employee", u"\u0110\u01a1n \u0111\u00e3 t\u1ea1o:", None))
        self.label_4.setText(QCoreApplication.translate("Main_Employee", u"Kh\u00e1ch h\u00e0ng ch\u1ecdn:", None))
        self.label_7.setText(QCoreApplication.translate("Main_Employee", u"T\u1ed5ng:", None))
        self.Btn_Del_Pd.setText(QCoreApplication.translate("Main_Employee", u"Xo\u00e1", None))
        self.Btn_Update.setText(QCoreApplication.translate("Main_Employee", u"C\u1eadp nh\u1eadt", None))
        self.lineEdit_ProductID.setPlaceholderText(QCoreApplication.translate("Main_Employee", u"M\u00e3 s\u1ea3n ph\u1ea9m", None))
        self.lineEdit_ProductName.setPlaceholderText(QCoreApplication.translate("Main_Employee", u"T\u00ean s\u1ea3n ph\u1ea9m", None))
        self.lineEdit_ImagePath.setPlaceholderText(QCoreApplication.translate("Main_Employee", u"\u0110\u01b0\u1eddng d\u1eabn \u1ea3nh", None))
        self.lineEdit_Price.setPlaceholderText(QCoreApplication.translate("Main_Employee", u"Gi\u00e1", None))
        self.Btn_SelectImage.setText("")
        self.label_18.setText("")
        self.Author.setItemText(0, "")

        self.Author.setPlaceholderText(QCoreApplication.translate("Main_Employee", u"T\u00e1c gi\u1ea3", None))
        self.Pub.setItemText(0, "")
        self.Pub.setItemText(1, "")

        self.Pub.setPlaceholderText(QCoreApplication.translate("Main_Employee", u"Nh\u00e0 xu\u1ea5t b\u1ea3n", None))
        self.Genre.setItemText(0, "")

        self.Genre.setPlaceholderText(QCoreApplication.translate("Main_Employee", u"Th\u1ec3 lo\u1ea1i", None))
        self.Btn_bk_update.setText(QCoreApplication.translate("Main_Employee", u"C\u1eadp nh\u1eadt", None))
        self.Bk_sl.setPlaceholderText(QCoreApplication.translate("Main_Employee", u"S\u1ed1 l\u01b0\u1ee3ng", None))
        self.label_19.setText("")
        self.Rent_st.setItemText(0, QCoreApplication.translate("Main_Employee", u"\u0110\u00e3 tr\u1ea3", None))

        self.Rent_st.setPlaceholderText(QCoreApplication.translate("Main_Employee", u"Tr\u1ea1ng th\u00e1i", None))
        self.Btn_Upd_Rent.setText(QCoreApplication.translate("Main_Employee", u"C\u1eadp nh\u1eadt", None))
        self.Avatar.setText("")
        self.label_2.setText(QCoreApplication.translate("Main_Employee", u"Username:", None))
        self.label_Username.setText("")
        self.label_3.setText(QCoreApplication.translate("Main_Employee", u"Email:", None))
        self.label_Email.setText("")
        self.Avatar_change.setText("")
        self.label_Icon2.setText("")
        self.label_CPass.setText(QCoreApplication.translate("Main_Employee", u"\u0110\u1ed5i m\u1eadt kh\u1ea9u", None))
        self.label_Icon.setText("")
        self.label_Logout.setText(QCoreApplication.translate("Main_Employee", u"Tho\u00e1t", None))
        self.label_8.setText(QCoreApplication.translate("Main_Employee", u"T\u00ean:", None))
        self.label_Name.setText("")
        self.label_Exit.setText("")
        self.label_Minimize.setText("")
        self.Btn_Pd.setText(QCoreApplication.translate("Main_Employee", u"Qu\u1ea3n l\u00fd s\u1ea3n ph\u1ea9m", None))
        self.Btn_Td.setText(QCoreApplication.translate("Main_Employee", u"T\u1ea1o \u0111\u01a1n", None))
        self.Btn_Bkeeping.setText(QCoreApplication.translate("Main_Employee", u"Nh\u1eadp s\u00e1ch", None))
        self.Btn_Sell.setText(QCoreApplication.translate("Main_Employee", u"\u0110\u00e3 b\u00e1n", None))
        self.Btn_Report.setText(QCoreApplication.translate("Main_Employee", u"B\u00e1o c\u00e1o", None))
        self.Btn_Rent.setText(QCoreApplication.translate("Main_Employee", u"Thu\u00ea/thu h\u1ed3i s\u00e1ch", None))
    # retranslateUi

