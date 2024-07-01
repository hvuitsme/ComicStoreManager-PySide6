# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'forgotpwlSIucc.ui'
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

class Ui_ForgotPw(object):
    def setupUi(self, ForgotPw):
        if not ForgotPw.objectName():
            ForgotPw.setObjectName(u"ForgotPw")
        ForgotPw.resize(601, 600)
        self.centralwidget = QWidget(ForgotPw)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-top-right-radius: 50px;\n"
"background-color: rgb(255, 210, 178);\n"
"border-bottom-left-radius: 50px;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.label_image = QLabel(self.frame)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setGeometry(QRect(0, 0, 291, 591))
        self.label_image.setStyleSheet(u"border-image: url(:/image/resources/pic/lib3.jpg);\n"
"border-top-right-radius: 0px; ")
        self.label_QuenMK = QLabel(self.frame)
        self.label_QuenMK.setObjectName(u"label_QuenMK")
        self.label_QuenMK.setGeometry(QRect(320, 140, 231, 41))
        font = QFont()
        font.setFamilies([u"Agbalumo"])
        font.setPointSize(22)
        self.label_QuenMK.setFont(font)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(320, 220, 231, 31))
        self.lineEdit.setStyleSheet(u"border: none;\n"
"background-color: rgb(255, 210, 178);\n"
"padding-bottom: 7px;\n"
"color: rgb(0, 0, 0);\n"
"border-bottom:2px solid rgb(170, 0, 0);")
        self.Btn_fgpw = QPushButton(self.frame)
        self.Btn_fgpw.setObjectName(u"Btn_fgpw")
        self.Btn_fgpw.setGeometry(QRect(320, 290, 231, 41))
        self.Btn_fgpw.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 210, 178);\n"
"    color: black; /* M\u00e0u ch\u1eef */\n"
"    border: 2px solid #008080; /* M\u00e0u xanh m\u00f2ng k\u00e9t cho vi\u1ec1n */\n"
"	border-radius: 10px;\n"
"    padding: 2px 2px; /* Kho\u1ea3ng c\u00e1ch b\u00ean trong */\n"
"    font-size: 20px; /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    transition: background-color 0.3s ease; /* Hi\u1ec7u \u1ee9ng chuy\u1ec3n \u0111\u1ed5i m\u00e0u n\u1ec1n */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 255, 255); /* M\u00e0u xanh m\u00f2ng k\u00e9t khi hover */\n"
"    color: black; /* M\u00e0u ch\u1eef khi hover */\n"
"}")
        self.label_title = QLabel(self.frame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(320, 340, 101, 16))
        self.label_title.setStyleSheet(u"")
        self.label_Login = QLabel(self.frame)
        self.label_Login.setObjectName(u"label_Login")
        self.label_Login.setGeometry(QRect(424, 340, 91, 16))
        self.label_Login.setAutoFillBackground(False)
        self.label_Login.setStyleSheet(u"QLabel:hover{\n"
"	color: rgb(170, 255, 255);\n"
"}")
        self.label_Exit = QLabel(self.frame)
        self.label_Exit.setObjectName(u"label_Exit")
        self.label_Exit.setGeometry(QRect(538, 20, 21, 21))
        self.label_Exit.setStyleSheet(u"border-image: url(:/icon/resources/icon-pack/exit_icon.png)")
        self.label_Return = QLabel(self.frame)
        self.label_Return.setObjectName(u"label_Return")
        self.label_Return.setGeometry(QRect(310, 20, 21, 21))
        self.label_Return.setStyleSheet(u"border-image: url(:/icon/resources/icon-pack/arrow_icon.png);")

        self.verticalLayout.addWidget(self.frame)

        ForgotPw.setCentralWidget(self.centralwidget)

        self.retranslateUi(ForgotPw)

        QMetaObject.connectSlotsByName(ForgotPw)
    # setupUi

    def retranslateUi(self, ForgotPw):
        ForgotPw.setWindowTitle(QCoreApplication.translate("ForgotPw", u"MainWindow", None))
        self.label_image.setText("")
        self.label_QuenMK.setText(QCoreApplication.translate("ForgotPw", u"QU\u00caN M\u1eacT KH\u1ea8U", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("ForgotPw", u"T\u00ean \u0111\u0103ng nh\u1eadp ho\u1eb7c Email", None))
        self.Btn_fgpw.setText(QCoreApplication.translate("ForgotPw", u"X\u00e1c nh\u1eadn", None))
        self.label_title.setText(QCoreApplication.translate("ForgotPw", u"\u0110\u00e3 nh\u1edb m\u1eadt kh\u1ea9u?", None))
        self.label_Login.setText(QCoreApplication.translate("ForgotPw", u"\u0110\u0103ng nh\u1eadp ngay", None))
        self.label_Exit.setText("")
        self.label_Return.setText("")
    # retranslateUi

