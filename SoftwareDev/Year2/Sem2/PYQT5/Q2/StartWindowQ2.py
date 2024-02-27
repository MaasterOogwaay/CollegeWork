from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

from incr_decr_addToUI import *

app = QApplication([])
w=QMainWindow()
w.setWindowTitle('Incrementer')
ex = Ui_MainWindow()
ex.setupUi(w)
w.resize(300,300)
w.show()
app.exec_()
