# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splash_screen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen: QtWidgets.QMainWindow):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(687, 397)
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropShadowframe = QtWidgets.QFrame(self.centralwidget)
        self.dropShadowframe.setStyleSheet("QFrame{\n"
"    \n"
"    \n"
"    background-color: rgb(38, 56, 90);\n"
"    \n"
"    color: rgb(198, 203, 207);\n"
"    border-radius: 10px;\n"
"}")
        self.dropShadowframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.dropShadowframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.dropShadowframe.setObjectName("dropShadowframe")
        self.label_laplace = QtWidgets.QLabel(self.dropShadowframe)
        self.label_laplace.setGeometry(QtCore.QRect(170, 120, 441, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        self.label_laplace.setFont(font)
        self.label_laplace.setStyleSheet("color: rgb(39, 247, 195);")
        self.label_laplace.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_laplace.setObjectName("label_laplace")
        self.label_fourier = QtWidgets.QLabel(self.dropShadowframe)
        self.label_fourier.setGeometry(QtCore.QRect(90, 60, 341, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        self.label_fourier.setFont(font)
        self.label_fourier.setStyleSheet("color: rgb(39, 247, 195);")
        self.label_fourier.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_fourier.setObjectName("label_fourier")
        self.progressBar = QtWidgets.QProgressBar(self.dropShadowframe)
        self.progressBar.setGeometry(QtCore.QRect(70, 290, 531, 23))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    \n"
"    background-color: rgb(105, 121, 175);\n"
"    color: rgb(200,200,200);\n"
"    border-style:none;\n"
"    border-radius: 10px;\n"
"    text-align:center;\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    \n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.489, x2:1, y2:0.477, stop:0 rgba(37, 241, 190, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_loading = QtWidgets.QLabel(self.dropShadowframe)
        self.label_loading.setGeometry(QtCore.QRect(0, 320, 671, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.label_loading.setFont(font)
        self.label_loading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_loading.setObjectName("label_loading")
        self.label_credits = QtWidgets.QLabel(self.dropShadowframe)
        self.label_credits.setGeometry(QtCore.QRect(20, 350, 631, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(103, 119, 172);")
        self.label_credits.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_credits.setObjectName("label_credits")
        self.label_description = QtWidgets.QLabel(self.dropShadowframe)
        self.label_description.setGeometry(QtCore.QRect(0, 210, 661, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_description.setFont(font)
        self.label_description.setStyleSheet("color: rgb(101, 116, 168);")
        self.label_description.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_description.setObjectName("label_description")
        self.verticalLayout.addWidget(self.dropShadowframe)
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen: QtWidgets.QMainWindow):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.label_laplace.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Lap</span>lace</p></body></html>"))
        self.label_fourier.setText(_translate("SplashScreen", "Four<strong>ier"))
        self.label_loading.setText(_translate("SplashScreen", "loading..."))
        self.label_credits.setText(_translate("SplashScreen", "<strong>Created</strong> by: Daniel Chmurny"))
        self.label_description.setText(_translate("SplashScreen", "<strong>Transform</strong> and chill"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SplashScreen = QtWidgets.QMainWindow()
    ui = Ui_SplashScreen()
    ui.setupUi(SplashScreen)
    SplashScreen.show()
    sys.exit(app.exec())

