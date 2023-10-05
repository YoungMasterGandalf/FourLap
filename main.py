import sys
import platform
#from PySide2 import QtCore, QtGui, QtWidgets
#from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
#from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
#from PySide2.QtWidgets import *
from sympy import *
from sympy.abc import *
from PyQt6 import QtCore, QtGui, QtWidgets

## ==> SPLASH SCREEN
from ui_splash_screen2 import Ui_SplashScreen

## ==> MAIN WINDOW
from ui_main2 import Ui_MainWindow

## ==> RESULT WINDOW
from ui_result2 import Ui_Result

## ==> GLOBALS
counter = 0

# YOUR APPLICATION
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # set fixed window size
        self.setFixedSize(800,600)  

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # QUIT button function append
        self.ui.pushButton_quit.clicked.connect(self.konec)

        # Laplace transform button append
        self.ui.pushButton_laplace.clicked.connect(self.action_laplace)

        # inverse Laplace transform button append
        self.ui.pushButton_laplaceInverse.clicked.connect(self.action_laplace_inverse)

        # Fourier transform button append
        self.ui.pushButton_fourier.clicked.connect(self.action_fourier)

        # inverse Fourier transform button append
        self.ui.pushButton_fourierInverse.clicked.connect(self.action_fourier_inverse)

    # Show result window function 
    def show_result(self,vysledek):

        self.res = Result(vysledek)
        self.res.show()

        
        


    def konec(self):
        # QUIT button action -> exits application
        sys.exit()

    def action_laplace(self):

        

        lap_input = self.ui.lineEdit_laplace.text() # gets users input from lineEdit
        lap_input = lap_input.lower()   # lowers all strings
        lap_input = lap_input.replace("^","**") # changes "^" for "**"
        lap_input = lap_input.replace("j","1j") # replace of complex unit so as program can read it properly

        lap_result = str(laplace_transform(lap_input,t,p)).replace("**","^")    # Laplace transform
        lap_result = lap_result.replace("I","i")

        #self.ui.label_2.setText(lap_result) # rewrites the result label
        self.show_result(lap_result)
        

    def action_laplace_inverse(self):

        lap_inv_input = self.ui.lineEdit_laplace.text() # gets users input from lineEdit
        lap_inv_input = lap_inv_input.lower()   # lowers all strings
        lap_inv_input = lap_inv_input.replace("^","**") # changes "^" for "**"
        lap_inv_input = lap_inv_input.replace("j","1j") # replace of complex unit so as program can read it properly

        lap_inv_result = str(inverse_laplace_transform(lap_inv_input,p,t)).replace("**","^")    # inverse Laplace transform
        lap_inv_result = lap_inv_result.replace("I","i")

        #self.ui.label_2.setText(lap_inv_result) # rewrites the result label
        self.show_result(lap_inv_result)

    def action_fourier(self):

        four_input = self.ui.lineEdit_fourier.text() # gets users input from lineEdit
        #four_input = four_input.lower()   # lowers all strings
        four_input = four_input.replace("^","**") # changes "^" for "**"
        four_input = four_input.replace("j","1j") 
        four_input = four_input.replace("delta","DiracDelta")


        four_result = str(fourier_transform(four_input,x,k)).replace("**","^")    # Fourier transform
        four_result = four_result.replace("I","i")

        #self.ui.label_2.setText(four_result) # rewrites the result label
        self.show_result(four_result)

    def action_fourier_inverse(self):

        four_inv_input = self.ui.lineEdit_fourier.text() # gets users input from lineEdit
        #four_inv_input = four_inv_input.lower()   # lowers all strings
        four_inv_input = four_inv_input.replace("^","**") # changes "^" for "**"
        four_inv_input = four_inv_input.replace("j","1j")
        four_inv_input = four_inv_input.replace("delta","DiracDelta")

        four_inv_result = str(inverse_fourier_transform(four_inv_input,k,x)).replace("**","^")    # inverse Fourier transform
        four_inv_result = four_inv_result.replace("I","i")

        #self.ui.label_2.setText(four_inv_result) # rewrites the result label
        self.show_result(four_inv_result)
    

  

        

        


# SPLASH SCREEN
class SplashScreen(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)



        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 60))
        self.ui.dropShadowframe.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>Transform</strong> and chill")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>Loading</strong> Four<strong>ier </strong> and <strong>Lap</strong>lace"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>Loading</strong> user interface"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

        

    ## ==> APP FUNCTIONS
    ########################################################################

    
    


    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1

    
# RESULT SCREEN
class Result(QtWidgets.QMainWindow):
    def __init__(self,vysledek):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_Result()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # CLOSE button function append
        self.ui.pushButton_close.clicked.connect(self.konec)

        self.ui.label_result_2.setText(vysledek)

                
    
    # Function for CLOSE button
    def konec(self):
        # CANCEL button action -> exits application
        self.close()

    
    
    

    


    




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())