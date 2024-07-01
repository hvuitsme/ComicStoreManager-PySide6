# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'replacepwtwqSeA.ui'
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

class Ui_ReplacePw(object):
    def setupUi(self, ReplacePw):
        if not ReplacePw.objectName():
            ReplacePw.setObjectName(u"ReplacePw")
        ReplacePw.resize(601, 600)
        self.centralwidget = QWidget(ReplacePw)
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
        self.label_TDMK = QLabel(self.frame)
        self.label_TDMK.setObjectName(u"label_TDMK")
        self.label_TDMK.setGeometry(QRect(320, 140, 231, 41))
        font = QFont()
        font.setFamilies([u"Agbalumo"])
        font.setPointSize(18)
        self.label_TDMK.setFont(font)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(320, 200, 231, 31))
        self.lineEdit.setStyleSheet(u"border: none;\n"
"background-color: rgb(255, 210, 178);\n"
"padding-bottom: 7px;\n"
"color: rgb(0, 0, 0);\n"
"border-bottom:2px solid rgb(170, 0, 0);")
        self.Btn_rplpw = QPushButton(self.frame)
        self.Btn_rplpw.setObjectName(u"Btn_rplpw")
        self.Btn_rplpw.setGeometry(QRect(320, 300, 231, 41))
        self.Btn_rplpw.setStyleSheet(u"QPushButton {\n"
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
        self.label_Exit = QLabel(self.frame)
        self.label_Exit.setObjectName(u"label_Exit")
        self.label_Exit.setGeometry(QRect(538, 20, 21, 21))
        self.label_Exit.setStyleSheet(u"border-image: url(:/icon/resources/icon-pack/exit_icon.png)")
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(320, 250, 231, 31))
        self.lineEdit_2.setStyleSheet(u"border: none;\n"
"background-color: rgb(255, 210, 178);\n"
"padding-bottom: 7px;\n"
"color: rgb(0, 0, 0);\n"
"border-bottom:2px solid rgb(170, 0, 0);")

        self.verticalLayout.addWidget(self.frame)

        ReplacePw.setCentralWidget(self.centralwidget)

        self.retranslateUi(ReplacePw)

        QMetaObject.connectSlotsByName(ReplacePw)
    # setupUi

    def retranslateUi(self, ReplacePw):
        ReplacePw.setWindowTitle(QCoreApplication.translate("ReplacePw", u"MainWindow", None))
        self.label_image.setText("")
        self.label_TDMK.setText(QCoreApplication.translate("ReplacePw", u"THAY \u0110\u1ed4I M\u1eacT KH\u1ea8U", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("ReplacePw", u"Nh\u1eadp m\u1eadt kh\u1ea9u m\u1edbi", None))
        self.Btn_rplpw.setText(QCoreApplication.translate("ReplacePw", u"X\u00e1c nh\u1eadn", None))
        self.label_Exit.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("ReplacePw", u"X\u00e1c nh\u1eadn m\u1eadt kh\u1ea9u m\u1edbi", None))
    # retranslateUi

