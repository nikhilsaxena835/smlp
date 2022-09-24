import qbase

import avl
import binary_tree
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
#import sys

#from PyQt5.QtGui import QPixmap, QPalette
#from PyQt5.QtWidgets import QApplication, QScrollArea, QLabel, QPushButton
import graph_base
import sbase
import stack_base
import test

class ExampleApp(QtWidgets.QMainWindow, test.Ui_MainWindow):

    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()