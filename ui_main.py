# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainrcAJKO.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	\n"
"	\n"
"	background-color: rgb(38, 56, 90);\n"
"	\n"
"	color: rgb(198, 203, 207);\n"
"	border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_fourier = QLabel(self.frame)
        self.label_fourier.setObjectName(u"label_fourier")
        self.label_fourier.setGeometry(QRect(-50, 0, 341, 81))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(36)
        self.label_fourier.setFont(font)
        self.label_fourier.setStyleSheet(u"color: rgb(39, 247, 195);")
        self.label_fourier.setAlignment(Qt.AlignCenter)
        self.label_laplace = QLabel(self.frame)
        self.label_laplace.setObjectName(u"label_laplace")
        self.label_laplace.setGeometry(QRect(90, 60, 371, 81))
        self.label_laplace.setFont(font)
        self.label_laplace.setStyleSheet(u"color: rgb(39, 247, 195);")
        self.label_laplace.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.lineEdit_laplace = QLineEdit(self.frame)
        self.lineEdit_laplace.setObjectName(u"lineEdit_laplace")
        self.lineEdit_laplace.setGeometry(QRect(30, 210, 711, 41))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        self.lineEdit_laplace.setFont(font1)
        self.label_EnterLaplace = QLabel(self.frame)
        self.label_EnterLaplace.setObjectName(u"label_EnterLaplace")
        self.label_EnterLaplace.setGeometry(QRect(30, 170, 621, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        self.label_EnterLaplace.setFont(font2)
        self.label_EnterLaplace.setStyleSheet(u"")
        self.label_EnterFourier = QLabel(self.frame)
        self.label_EnterFourier.setObjectName(u"label_EnterFourier")
        self.label_EnterFourier.setGeometry(QRect(30, 320, 621, 31))
        self.label_EnterFourier.setFont(font2)
        self.label_EnterFourier.setStyleSheet(u"")
        self.lineEdit_fourier = QLineEdit(self.frame)
        self.lineEdit_fourier.setObjectName(u"lineEdit_fourier")
        self.lineEdit_fourier.setGeometry(QRect(30, 360, 711, 41))
        self.lineEdit_fourier.setFont(font1)
        self.pushButton_laplace = QPushButton(self.frame)
        self.pushButton_laplace.setObjectName(u"pushButton_laplace")
        self.pushButton_laplace.setGeometry(QRect(30, 260, 351, 41))
        self.pushButton_laplace.setFont(font1)
        self.pushButton_laplace.setStyleSheet(u"color: rgb(39, 247, 195);\n"
"background-color: rgb(105, 121, 175);")
        self.pushButton_laplaceInverse = QPushButton(self.frame)
        self.pushButton_laplaceInverse.setObjectName(u"pushButton_laplaceInverse")
        self.pushButton_laplaceInverse.setGeometry(QRect(390, 260, 351, 41))
        self.pushButton_laplaceInverse.setFont(font1)
        self.pushButton_laplaceInverse.setStyleSheet(u"color: rgb(39, 247, 195);\n"
"background-color: rgb(105, 121, 175);")
        self.pushButton_fourier = QPushButton(self.frame)
        self.pushButton_fourier.setObjectName(u"pushButton_fourier")
        self.pushButton_fourier.setGeometry(QRect(30, 410, 351, 41))
        self.pushButton_fourier.setFont(font1)
        self.pushButton_fourier.setStyleSheet(u"color: rgb(39, 247, 195);\n"
"background-color: rgb(105, 121, 175);")
        self.pushButton_fourierInverse = QPushButton(self.frame)
        self.pushButton_fourierInverse.setObjectName(u"pushButton_fourierInverse")
        self.pushButton_fourierInverse.setGeometry(QRect(390, 410, 351, 41))
        self.pushButton_fourierInverse.setFont(font1)
        self.pushButton_fourierInverse.setStyleSheet(u"color: rgb(39, 247, 195);\n"
"background-color: rgb(105, 121, 175);")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 470, 71, 31))
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(39, 247, 195);")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 470, 671, 31))
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"")
        self.pushButton_quit = QPushButton(self.frame)
        self.pushButton_quit.setObjectName(u"pushButton_quit")
        self.pushButton_quit.setGeometry(QRect(652, 20, 101, 31))
        self.pushButton_quit.setFont(font1)
        self.pushButton_quit.setStyleSheet(u"background-color: rgb(105, 121, 175);\n"
"color: rgb(39, 247, 195);")
        self.label_laplace.raise_()
        self.label_fourier.raise_()
        self.lineEdit_laplace.raise_()
        self.label_EnterLaplace.raise_()
        self.label_EnterFourier.raise_()
        self.lineEdit_fourier.raise_()
        self.pushButton_laplace.raise_()
        self.pushButton_laplaceInverse.raise_()
        self.pushButton_fourier.raise_()
        self.pushButton_fourierInverse.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton_quit.raise_()

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_fourier.setText(QCoreApplication.translate("MainWindow", u"Four<strong>ier", None))
        self.label_laplace.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Lap</span>lace <span style=\" font-size:10pt;\">ver. 1.1</span></p></body></html>", None))
        self.lineEdit_laplace.setText(QCoreApplication.translate("MainWindow", u"example: t^n (Laplace), 1/(p^2+3*p+2) (inverse Laplace)", None))
        self.label_EnterLaplace.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Enter </span>a function for <span style=\" font-weight:600;\">Lap</span>lace transform or its inverse</p></body></html>", None))
        self.label_EnterFourier.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Enter </span>a function for <span style=\" font-weight:600;\">Lap</span>lace transform or its inverse</p></body></html>", None))
        self.lineEdit_fourier.setText(QCoreApplication.translate("MainWindow", u"example: exp(-x^2) (Fourier),  sqrt(pi)*exp(-(pi*k)^2) (inverse Fourier)", None))
        self.pushButton_laplace.setText(QCoreApplication.translate("MainWindow", u"Laplace", None))
        self.pushButton_laplaceInverse.setText(QCoreApplication.translate("MainWindow", u"Inverse Laplace", None))
        self.pushButton_fourier.setText(QCoreApplication.translate("MainWindow", u"Fourier", None))
        self.pushButton_fourierInverse.setText(QCoreApplication.translate("MainWindow", u"Inverse Fourier", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Res</span>ult:</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>The result will appear in a seperate window...</p><p><br/></p></body></html>", None))
        self.pushButton_quit.setText(QCoreApplication.translate("MainWindow", u"QUIT", None))
    # retranslateUi

