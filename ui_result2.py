# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Result(object):
    def setupUi(self, Result):
        Result.setObjectName("Result")
        Result.resize(1500, 120)
        self.centralwidget = QtWidgets.QWidget(Result)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(38, 56, 90);\n"
"    border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 40, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(39, 247, 195);")
        self.label.setObjectName("label")
        self.label_result_2 = QtWidgets.QLabel(self.frame)
        self.label_result_2.setGeometry(QtCore.QRect(80, 40, 1391, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_result_2.setFont(font)
        self.label_result_2.setStyleSheet("color: rgb(198, 203, 207);")
        self.label_result_2.setObjectName("label_result_2")
        self.pushButton_close = QtWidgets.QPushButton(self.frame)
        self.pushButton_close.setGeometry(QtCore.QRect(1370, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setStyleSheet("background-color: rgb(105, 121, 175);\n"
"color: rgb(39, 247, 195);")
        self.pushButton_close.setObjectName("pushButton_close")
        self.verticalLayout.addWidget(self.frame)
        Result.setCentralWidget(self.centralwidget)

        self.retranslateUi(Result)
        QtCore.QMetaObject.connectSlotsByName(Result)

    def retranslateUi(self, Result):
        _translate = QtCore.QCoreApplication.translate
        Result.setWindowTitle(_translate("Result", "MainWindow"))
        self.label.setText(_translate("Result", "<html><head/><body><p><span style=\" font-weight:600;\">Res</span>ult:</p></body></html>"))
        self.label_result_2.setText(_translate("Result", "<html><head/><body><p>The result will appear here after calculation...</p><p><br/></p></body></html>"))
        self.pushButton_close.setText(_translate("Result", "CLOSE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Result = QtWidgets.QMainWindow()
    ui = Ui_Result()
    ui.setupUi(Result)
    Result.show()
    sys.exit(app.exec_())

