from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import home

class ExampleApp(QtWidgets.QMainWindow, home.Ui_MainWindow):

    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    form = ExampleApp()

    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap('icon.png'))
    form.setWindowIcon(icon)
    app.setStyleSheet("QLabel{font-size: 12pt;}")
    form.show()
    app.exec_()



if __name__ == '__main__':
    main()