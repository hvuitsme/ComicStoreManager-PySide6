# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signiniTSntw.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import image_rc

class Ui_Signin(object):
    def setupUi(self, Signin):
        if not Signin.objectName():
            Signin.setObjectName(u"Signin")
        Signin.resize(600, 600)
        self.centralwidget = QWidget(Signin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"#frame.QFrame{\n"
"	border-top-right-radius: 50px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-bottom-left-radius: 50px;\n"
"	border:2px solid rgb(0, 170, 127);\n"
"}")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.label_image = QLabel(self.frame)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setGeometry(QRect(2, 2, 291, 576))
        self.label_image.setStyleSheet(u"#label_image.QLabel{\n"
"border-image: url(:/image/resources/pic/c6e98c7fe62448b1c87bdab855727124.jpg);\n"
"border-bottom-left-radius: 48px;\n"
"}")
        self.label_Dangky = QLabel(self.frame)
        self.label_Dangky.setObjectName(u"label_Dangky")
        self.label_Dangky.setGeometry(QRect(320, 140, 161, 41))
        font = QFont()
        font.setFamilies([u"Agbalumo"])
        font.setPointSize(22)
        self.label_Dangky.setFont(font)
        self.Btn_Signin = QPushButton(self.frame)
        self.Btn_Signin.setObjectName(u"Btn_Signin")
        self.Btn_Signin.setGeometry(QRect(320, 430, 231, 41))
        self.Btn_Signin.setStyleSheet(u"QPushButton {\n"
"    color: black; /* M\u00e0u ch\u1eef */\n"
"    border: 2px solid #008080; /* M\u00e0u xanh m\u00f2ng k\u00e9t cho vi\u1ec1n */\n"
"	border-radius: 10px;\n"
"    padding: 2px 2px; /* Kho\u1ea3ng c\u00e1ch b\u00ean trong */\n"
"    font-size: 20px; /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    transition: background-color 0.3s ease; /* Hi\u1ec7u \u1ee9ng chuy\u1ec3n \u0111\u1ed5i m\u00e0u n\u1ec1n */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 170, 127); /* M\u00e0u xanh m\u00f2ng k\u00e9t khi hover */\n"
"    color: white; /* M\u00e0u ch\u1eef khi hover */\n"
"}")
        self.label_title = QLabel(self.frame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(330, 480, 121, 16))
        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(320, 370, 231, 31))
        self.lineEdit_4.setStyleSheet(u"border: none;\n"
"padding-bottom: 7px;\n"
"color: rgb(0, 0, 0);\n"
"border-bottom:2px solid rgb(0, 170, 127);")
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(320, 320, 231, 31))
        self.lineEdit_3.setStyleSheet(u"border: none;\n"
"padding-bottom: 7px;\n"
"color: rgb(0, 0, 0);\n"
"border-bottom:2px solid rgb(0, 170, 127);")
        self.label_Exit = QLabel(self.frame)
        self.label_Exit.setObjectName(u"label_Exit")
        self.label_Exit.setGeometry(QRect(540, 20, 21, 21))
        self.label_Exit.setStyleSheet(u"border-image: url(:/icon/resources/icon-pack/exit_icon.png);")
        self.label_Return = QLabel(self.frame)
        self.label_Return.setObjectName(u"label_Return")
        self.label_Return.setGeometry(QRect(310, 20, 21, 21))
        self.label_Return.setStyleSheet(u"border-image: url(:/icon/resources/icon-pack/arrow_icon.png);")
        self.label_Login = QLabel(self.frame)
        self.label_Login.setObjectName(u"label_Login")
        self.label_Login.setGeometry(QRect(450, 480, 91, 16))
        self.label_Login.setStyleSheet(u"QLabel:hover{\n"
"	color: rgb(170, 255, 255);\n"
"}")
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(320, 270, 231, 31))
        self.lineEdit_2.setStyleSheet(u"border: none;\n"
"padding-bottom: 7px;\n"
"color: rgb(0, 0, 0);\n"
"border-bottom:2px solid rgb(0, 170, 127);")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(320, 220, 231, 31))
        self.lineEdit.setStyleSheet(u"border: none;\n"
"padding-bottom: 7px;\n"
"color: rgb(0, 0, 0);\n"
"border-bottom:2px solid rgb(0, 170, 127);")

        self.verticalLayout.addWidget(self.frame)

        Signin.setCentralWidget(self.centralwidget)

        self.retranslateUi(Signin)

        QMetaObject.connectSlotsByName(Signin)
    # setupUi

    def retranslateUi(self, Signin):
        Signin.setWindowTitle(QCoreApplication.translate("Signin", u"MainWindow", None))
        self.label_image.setText("")
        self.label_Dangky.setText(QCoreApplication.translate("Signin", u"\u0110\u0102NG K\u00dd", None))
        self.Btn_Signin.setText(QCoreApplication.translate("Signin", u"\u0110\u0103ng k\u00fd", None))
        self.label_title.setText(QCoreApplication.translate("Signin", u"B\u1ea1n \u0111\u00e3 c\u00f3 t\u00e0i kho\u1ea3n ?", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Signin", u"Nh\u1eadp l\u1ea1i m\u1eadt kh\u1ea9u", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Signin", u"M\u1eadt kh\u1ea9u", None))
        self.label_Exit.setText("")
        self.label_Return.setText("")
        self.label_Login.setText(QCoreApplication.translate("Signin", u"\u0110\u0103ng nh\u1eadp ngay", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Signin", u"Username", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Signin", u"Email", None))
    # retranslateUi

