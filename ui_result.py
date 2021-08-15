# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resultyOpOVh.ui'
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


class Ui_Result(object):
    def setupUi(self, Result):
        if Result.objectName():
            Result.setObjectName(u"Result")
        Result.resize(1500, 120)
        self.centralwidget = QWidget(Result)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(38, 56, 90);\n"
"	border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 40, 71, 31))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(39, 247, 195);")
        self.label_result_2 = QLabel(self.frame)
        self.label_result_2.setObjectName(u"label_result_2")
        self.label_result_2.setGeometry(QRect(80, 40, 1391, 31))
        self.label_result_2.setFont(font)
        self.label_result_2.setStyleSheet(u"color: rgb(198, 203, 207);")
        self.pushButton_close = QPushButton(self.frame)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setGeometry(QRect(1370, 10, 101, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        self.pushButton_close.setFont(font1)
        self.pushButton_close.setStyleSheet(u"background-color: rgb(105, 121, 175);\n"
"color: rgb(39, 247, 195);")

        self.verticalLayout.addWidget(self.frame)

        Result.setCentralWidget(self.centralwidget)

        self.retranslateUi(Result)

        QMetaObject.connectSlotsByName(Result)
    # setupUi

    def retranslateUi(self, Result):
        Result.setWindowTitle(QCoreApplication.translate("Result", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Result", u"<html><head/><body><p><span style=\" font-weight:600;\">Res</span>ult:</p></body></html>", None))
        self.label_result_2.setText(QCoreApplication.translate("Result", u"<html><head/><body><p>The result will appear here after calculation...</p><p><br/></p></body></html>", None))
        self.pushButton_close.setText(QCoreApplication.translate("Result", u"CLOSE", None))
    # retranslateUi

