# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'choose_spdvZwHT.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import image_rc

class Ui_Choose_sp(object):
    def setupUi(self, Choose_sp):
        if not Choose_sp.objectName():
            Choose_sp.setObjectName(u"Choose_sp")
        Choose_sp.resize(798, 585)
        self.centralwidget = QWidget(Choose_sp)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(525, 30, 111, 16))
        self.Search = QLineEdit(self.frame)
        self.Search.setObjectName(u"Search")
        self.Search.setGeometry(QRect(10, 10, 511, 31))
        self.Search.setStyleSheet(u"border: 2px solid rgb(0, 170, 127);")
        self.tb_choose = QTableWidget(self.frame)
        self.tb_choose.setObjectName(u"tb_choose")
        self.tb_choose.setGeometry(QRect(10, 50, 511, 471))
        self.tb_choose.setStyleSheet(u"#tb_choose.QTableWidget{\n"
"	border: 2px solid rgb(0, 170, 127)\n"
"}")
        self.tb_choosed = QTableWidget(self.frame)
        self.tb_choosed.setObjectName(u"tb_choosed")
        self.tb_choosed.setGeometry(QRect(519, 50, 252, 482))
        self.tb_choosed.setStyleSheet(u"#tb_choosed.QTableWidget{\n"
"	border: 2px solid rgb(0, 170, 127)\n"
"}")
        self.Btn_Buy = QPushButton(self.frame)
        self.Btn_Buy.setObjectName(u"Btn_Buy")
        self.Btn_Buy.setGeometry(QRect(10, 530, 161, 31))
        self.Btn_Buy.setStyleSheet(u"border:2px solid rgb(0, 170, 127);\n"
"border-radius: 15px;")
        self.Btn_Rent = QPushButton(self.frame)
        self.Btn_Rent.setObjectName(u"Btn_Rent")
        self.Btn_Rent.setGeometry(QRect(180, 530, 171, 31))
        self.Btn_Rent.setStyleSheet(u"border:2px solid rgb(0, 170, 127);\n"
"border-radius: 15px;")
        self.sl_choose = QSpinBox(self.frame)
        self.sl_choose.setObjectName(u"sl_choose")
        self.sl_choose.setGeometry(QRect(360, 530, 151, 31))
        self.sl_choose.setMinimum(1)
        self.spinBox_quantity = QSpinBox(self.frame)
        self.spinBox_quantity.setObjectName(u"spinBox_quantity")
        self.spinBox_quantity.setGeometry(QRect(701, 123, 61, 21))
        self.pd_buy_rent = QLabel(self.frame)
        self.pd_buy_rent.setObjectName(u"pd_buy_rent")
        self.pd_buy_rent.setGeometry(QRect(530, 93, 231, 21))
        self.pd_price = QLabel(self.frame)
        self.pd_price.setObjectName(u"pd_price")
        self.pd_price.setGeometry(QRect(530, 123, 161, 21))
        self.pd_name = QLabel(self.frame)
        self.pd_name.setObjectName(u"pd_name")
        self.pd_name.setGeometry(QRect(530, 60, 201, 21))
        self.frm_sum = QFrame(self.frame)
        self.frm_sum.setObjectName(u"frm_sum")
        self.frm_sum.setGeometry(QRect(519, 530, 252, 31))
        self.frm_sum.setStyleSheet(u"#frm_sum.QFrame{\n"
"	border: 2px solid rgb(0, 170, 127)\n"
"}")
        self.frm_sum.setFrameShape(QFrame.StyledPanel)
        self.frm_sum.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frm_sum)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(5, 5, 49, 20))
        font = QFont()
        font.setFamilies([u"Agbalumo"])
        font.setPointSize(11)
        self.label.setFont(font)
        self.sum_price = QLabel(self.frm_sum)
        self.sum_price.setObjectName(u"sum_price")
        self.sum_price.setGeometry(QRect(50, 5, 197, 20))
        self.sum_price.setFont(font)
        self.pd_del = QLabel(self.frame)
        self.pd_del.setObjectName(u"pd_del")
        self.pd_del.setGeometry(QRect(740, 60, 21, 21))
        self.pd_del.setStyleSheet(u"border-image: url(:/icon/resources/icon-pack/exit_icon.png);")

        self.verticalLayout.addWidget(self.frame)

        Choose_sp.setCentralWidget(self.centralwidget)

        self.retranslateUi(Choose_sp)

        QMetaObject.connectSlotsByName(Choose_sp)
    # setupUi

    def retranslateUi(self, Choose_sp):
        Choose_sp.setWindowTitle(QCoreApplication.translate("Choose_sp", u"Ch\u1ecdn s\u1ea3n ph\u1ea9m", None))
        self.label_18.setText(QCoreApplication.translate("Choose_sp", u"S\u1ea3n ph\u1ea9m \u0111\u00e3 ch\u1ecdn:", None))
        self.Search.setPlaceholderText(QCoreApplication.translate("Choose_sp", u"T\u00ecm ki\u1ebfm s\u1ea3n ph\u1ea9m, T\u00e1c gi\u1ea3, Nh\u00e0 ph\u00e1t h\u00e0nh,...", None))
        self.Btn_Buy.setText(QCoreApplication.translate("Choose_sp", u"Mua", None))
        self.Btn_Rent.setText(QCoreApplication.translate("Choose_sp", u"Thu\u00ea", None))
        self.pd_buy_rent.setText("")
        self.pd_price.setText("")
        self.pd_name.setText("")
        self.label.setText(QCoreApplication.translate("Choose_sp", u"T\u1ed5ng:", None))
        self.sum_price.setText("")
        self.pd_del.setText("")
    # retranslateUi

