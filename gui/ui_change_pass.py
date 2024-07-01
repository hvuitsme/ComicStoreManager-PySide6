# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_passfWwCqX.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import image_rc

class Ui_ChangePass(object):
    def setupUi(self, ChangePass):
        if not ChangePass.objectName():
            ChangePass.setObjectName(u"ChangePass")
        ChangePass.resize(220, 220)
        self.verticalLayout = QVBoxLayout(ChangePass)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(ChangePass)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border: 3px solid rgb(0, 170, 127)")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 40, 181, 28))
        self.lineEdit.setStyleSheet(u"border: none;\n"
"background-color: rgb(255, 255, 255);\n"
"padding-bottom: 7px;\n"
"color: rgb(0, 0, 0);\n"
"border-bottom:2px solid rgb(0, 128, 128);")
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 80, 181, 28))
        self.lineEdit_2.setStyleSheet(u"border: none;\n"
"background-color: rgb(255, 255, 255);\n"
"padding-bottom: 7px;\n"
"color: rgb(0, 0, 0);\n"
"border-bottom:2px solid rgb(0, 128, 128);")
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(10, 120, 181, 28))
        self.lineEdit_3.setStyleSheet(u"border: none;\n"
"background-color: rgb(255, 255, 255);\n"
"padding-bottom: 7px;\n"
"color: rgb(0, 0, 0);\n"
"border-bottom:2px solid rgb(0, 128, 128);")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 161, 83, 29))
        font = QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"    color: black; /* M\u00e0u ch\u1eef */\n"
"    border: 2px solid #008080; /* M\u00e0u xanh m\u00f2ng k\u00e9t cho vi\u1ec1n */\n"
"	border-radius: 10px;\n"
"    padding: 2px 2px; /* Kho\u1ea3ng c\u00e1ch b\u00ean trong */\n"
"    /*font-size: 20px;  K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    transition: background-color 0.3s ease; /* Hi\u1ec7u \u1ee9ng chuy\u1ec3n \u0111\u1ed5i m\u00e0u n\u1ec1n */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 128, 128);/* M\u00e0u xanh m\u00f2ng k\u00e9t khi hover */\n"
"    color: white; /* M\u00e0u ch\u1eef khi hover */\n"
"}")
        self.label_Exit = QLabel(self.frame)
        self.label_Exit.setObjectName(u"label_Exit")
        self.label_Exit.setGeometry(QRect(170, 10, 21, 20))
        self.label_Exit.setStyleSheet(u"border-image: url(:/icon/resources/icon-pack/exit_icon.png);")

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(ChangePass)

        QMetaObject.connectSlotsByName(ChangePass)
    # setupUi

    def retranslateUi(self, ChangePass):
        ChangePass.setWindowTitle(QCoreApplication.translate("ChangePass", u"Form", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("ChangePass", u"Nh\u1eadp m\u1eadt kh\u1ea9u hi\u1ec7n t\u1ea1i", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("ChangePass", u"Nh\u1eadp m\u1eadt kh\u1ea9u m\u1edbi", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("ChangePass", u"Nh\u1eadp l\u1ea1i m\u1eadt kh\u1ea9u m\u1edbi", None))
        self.pushButton.setText(QCoreApplication.translate("ChangePass", u"Thay \u0111\u1ed5i", None))
        self.label_Exit.setText("")
    # retranslateUi

