import binary_tree
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
#import sys

#from PyQt5.QtGui import QPixmap, QPalette
#from PyQt5.QtWidgets import QApplication, QScrollArea, QLabel, QPushButton


import sbase
import test
class ExampleApp(QtWidgets.QMainWindow, graph_base.Ui_MainWindow):
class ExampleApp(QtWidgets.QMainWindow, sbase.Ui_MainWindow):

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