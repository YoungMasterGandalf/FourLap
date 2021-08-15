# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screendcGdev.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(687, 397)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowframe = QFrame(self.centralwidget)
        self.dropShadowframe.setObjectName(u"dropShadowframe")
        self.dropShadowframe.setStyleSheet(u"QFrame{\n"
"	\n"
"	\n"
"	background-color: rgb(38, 56, 90);\n"
"	\n"
"	color: rgb(198, 203, 207);\n"
"	border-radius: 10px;\n"
"}")
        self.dropShadowframe.setFrameShape(QFrame.StyledPanel)
        self.dropShadowframe.setFrameShadow(QFrame.Raised)
        self.label_laplace = QLabel(self.dropShadowframe)
        self.label_laplace.setObjectName(u"label_laplace")
        self.label_laplace.setGeometry(QRect(170, 120, 441, 91))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(36)
        self.label_laplace.setFont(font)
        self.label_laplace.setStyleSheet(u"color: rgb(39, 247, 195);")
        self.label_laplace.setAlignment(Qt.AlignCenter)
        self.label_fourier = QLabel(self.dropShadowframe)
        self.label_fourier.setObjectName(u"label_fourier")
        self.label_fourier.setGeometry(QRect(90, 60, 341, 81))
        self.label_fourier.setFont(font)
        self.label_fourier.setStyleSheet(u"color: rgb(39, 247, 195);")
        self.label_fourier.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowframe)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(70, 290, 531, 23))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	background-color: rgb(105, 121, 175);\n"
"	color: rgb(200,200,200);\n"
"	border-style:none;\n"
"	border-radius: 10px;\n"
"	text-align:center;\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.489, x2:1, y2:0.477, stop:0 rgba(37, 241, 190, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.dropShadowframe)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(0, 320, 671, 20))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(8)
        self.label_loading.setFont(font1)
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.dropShadowframe)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(20, 350, 631, 20))
        self.label_credits.setFont(font1)
        self.label_credits.setStyleSheet(u"color: rgb(103, 119, 172);")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_description = QLabel(self.dropShadowframe)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(0, 210, 661, 41))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(16)
        self.label_description.setFont(font2)
        self.label_description.setStyleSheet(u"color: rgb(101, 116, 168);")
        self.label_description.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.dropShadowframe)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_laplace.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-weight:600;\">Lap</span>lace</p></body></html>", None))
        self.label_fourier.setText(QCoreApplication.translate("SplashScreen", u"Four<strong>ier", None))
        self.label_loading.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))
        self.label_credits.setText(QCoreApplication.translate("SplashScreen", u"<strong>Created</strong> by: Daniel Chmurny", None))
        self.label_description.setText(QCoreApplication.translate("SplashScreen", u"<strong>Transform</strong> and chill", None))
    # retranslateUi

