# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginzZjomr.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import image_rc

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(600, 600)
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"#frame.QFrame{\n"
"border-top-right-radius: 50px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-bottom-left-radius: 50px;\n"
"border: 2px solid rgb(0, 170, 127);\n"
"}")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.label_image = QLabel(self.frame)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setGeometry(QRect(0, 0, 291, 581))
        self.label_image.setStyleSheet(u"border-image: url(:/image/resources/pic/lib4.jpg);\n"
"border-bottom-left-radius: 50px; ")
        self.label_Dangnhap = QLabel(self.frame)
        self.label_Dangnhap.setObjectName(u"label_Dangnhap")
        self.label_Dangnhap.setGeometry(QRect(320, 140, 161, 41))
        font = QFont()
        font.setFamilies([u"Agbalumo"])
        font.setPointSize(22)
        self.label_Dangnhap.setFont(font)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(320, 210, 231, 31))
        self.lineEdit.setStyleSheet(u"border: none;\n"
"background-color: rgb(255, 255, 255);\n"
"padding-bottom: 7px;\n"
"color: rgb(0, 0, 0);\n"
"border-bottom:2px solid rgb(0, 170, 127);")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(320, 330, 231, 41))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
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
"    color: rgb(255, 255, 255); /* M\u00e0u ch\u1eef khi hover */\n"
"}")
        self.label_ForgotPw = QLabel(self.frame)
        self.label_ForgotPw.setObjectName(u"label_ForgotPw")
        self.label_ForgotPw.setGeometry(QRect(320, 380, 91, 16))
        self.label_ForgotPw.setStyleSheet(u"QLabel:hover {\n"
"	color: rgb(0, 170, 127);\n"
"}")
        self.label_Signin = QLabel(self.frame)
        self.label_Signin.setObjectName(u"label_Signin")
        self.label_Signin.setGeometry(QRect(460, 380, 91, 16))
        self.label_Signin.setAutoFillBackground(False)
        self.label_Signin.setStyleSheet(u"QLabel:hover {\n"
"	color: rgb(0, 170, 127);\n"
"}")
        self.label_Signin.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_Exit = QLabel(self.frame)
        self.label_Exit.setObjectName(u"label_Exit")
        self.label_Exit.setGeometry(QRect(538, 20, 21, 21))
        self.label_Exit.setStyleSheet(u"border-image: url(:/icon/resources/icon-pack/exit_icon.png);")
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(320, 260, 231, 31))
        self.lineEdit_2.setStyleSheet(u"border: none;\n"
"background-color: rgb(255, 255, 255);\n"
"padding-bottom: 7px;\n"
"color: rgb(0, 0, 0);\n"
"border-bottom:2px solid rgb(0, 170, 127);")
        self.Rem_ckBox = QCheckBox(self.frame)
        self.Rem_ckBox.setObjectName(u"Rem_ckBox")
        self.Rem_ckBox.setGeometry(QRect(320, 300, 231, 20))

        self.verticalLayout.addWidget(self.frame)

        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"MainWindow", None))
        self.label_image.setText("")
        self.label_Dangnhap.setText(QCoreApplication.translate("Login", u"\u0110\u0102NG NH\u1eacP", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Login", u"T\u00ean \u0111\u0103ng nh\u1eadp ho\u1eb7c Email", None))
        self.pushButton.setText(QCoreApplication.translate("Login", u"\u0110\u0103ng nh\u1eadp", None))
        self.label_ForgotPw.setText(QCoreApplication.translate("Login", u"Qu\u00ean m\u1eadt kh\u1ea9u?", None))
        self.label_Signin.setText(QCoreApplication.translate("Login", u"\u0110\u0103ng k\u00fd", None))
        self.label_Exit.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Login", u"M\u1eadt kh\u1ea9u", None))
        self.Rem_ckBox.setText(QCoreApplication.translate("Login", u"Nh\u1edb sau khi \u0111\u0103ng nh\u1eadp", None))
    # retranslateUi

