# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splashLFbOPc.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QProgressBar, QSizePolicy, QVBoxLayout, QWidget)
import image_rc

class Ui_Splash(object):
    def setupUi(self, Splash):
        if not Splash.objectName():
            Splash.setObjectName(u"Splash")
        Splash.resize(397, 435)
        self.centralwidget = QWidget(Splash)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(0, 390, 377, 23))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(76, 202, 255);\n"
"	color: rgb(170, 85, 127);\n"
"	border-radius: 11px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.545, x2:1, y2:0.511, stop:0 rgba(204, 100, 204, 255), stop:1 rgba(183, 255, 241, 255));\n"
"	border-radius: 11px;\n"
"}")
        self.progressBar.setValue(24)
        self.label = QLabel(self.dropShadowFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 374, 31))
        font = QFont()
        font.setFamilies([u"Agbalumo"])
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(57, 255, 173);")
        self.label.setAlignment(Qt.AlignCenter)
        self.image = QLabel(self.dropShadowFrame)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(8, 30, 364, 358))
        self.image.setStyleSheet(u"border-radius: 20px;\n"
"border-image: url(:/image/resources/pic/slash.jpg);")
        self.image.setScaledContents(True)
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(160, 370, 61, 16))
        self.label_loading.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_loading_2 = QLabel(self.dropShadowFrame)
        self.label_loading_2.setObjectName(u"label_loading_2")
        self.label_loading_2.setGeometry(QRect(230, 100, 61, 61))
        self.label_loading_2.setStyleSheet(u"border-image: url(:/icon/icon-pack/loading.png);")

        self.verticalLayout.addWidget(self.dropShadowFrame)

        Splash.setCentralWidget(self.centralwidget)

        self.retranslateUi(Splash)

        QMetaObject.connectSlotsByName(Splash)
    # setupUi

    def retranslateUi(self, Splash):
        Splash.setWindowTitle(QCoreApplication.translate("Splash", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Splash", u"V\u01af\u1edcN TRUY\u1ec6N THIEU NANG", None))
        self.image.setText("")
        self.label_loading.setText(QCoreApplication.translate("Splash", u"LOADING", None))
        self.label_loading_2.setText("")
    # retranslateUi
    
# class Splash(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_Splash()
#         self.ui.setupUi(self)

# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     MainWindow = Splash()
#     MainWindow.show()
#     sys.exit(app.exec())