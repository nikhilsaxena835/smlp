# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'queue.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsScene


class Ui_MainWindow(object):
    pqueue = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1240, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.scene = QGraphicsScene()
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 60, 761, 471))
        self.graphicsView.setStyleSheet("")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setScene(self.scene)
        self.graphicsView.show()

        self.ins_button = QtWidgets.QPushButton(self.centralwidget)
        self.ins_button.setGeometry(QtCore.QRect(1020, 110, 75, 31))
        self.ins_button.setObjectName("ins_button")
        self.ins_tf = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ins_tf.setGeometry(QtCore.QRect(890, 110, 104, 31))
        self.ins_tf.setObjectName("ins_tf")
        self.del_button = QtWidgets.QPushButton(self.centralwidget)
        self.del_button.setGeometry(QtCore.QRect(920, 200, 75, 31))
        self.del_button.setObjectName("del_button")
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(920, 250, 75, 31))
        self.search_button.setObjectName("search_button")
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(840, 450, 101, 16))
        self.output_label.setObjectName("output_label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(830, 60, 281, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(830, 190, 281, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(830, 430, 281, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(820, 70, 20, 121))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(1100, 70, 20, 121))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(820, 190, 16, 241))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(1100, 180, 20, 261))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.operations_label = QtWidgets.QLabel(self.centralwidget)
        self.operations_label.setGeometry(QtCore.QRect(850, 80, 81, 16))
        self.operations_label.setObjectName("operations_label")
        self.output_tf = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.output_tf.setGeometry(QtCore.QRect(850, 470, 261, 31))
        self.output_tf.setObjectName("output_tf")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(120, 540, 651, 81))
        self.textEdit.setObjectName("textEdit")
        self.info_label = QtWidgets.QLabel(self.centralwidget)
        self.info_label.setGeometry(QtCore.QRect(10, 550, 81, 16))
        self.info_label.setObjectName("info_label")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.back.setObjectName("back")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(140, 10, 75, 23))
        self.reset.setObjectName("reset")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(920, 300, 75, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(920, 350, 75, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(920, 400, 75, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(670, 140, 20, 311))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1145, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.ins_button.clicked.connect(self.enqueue)
        self.del_button.clicked.connect(self.checker)
        self.search_button.clicked.connect(self.printFront)
        self.pushButton.clicked.connect(self.printRear)
        self.pushButton_2.clicked.connect(self.printSize)
        self.pushButton_3.clicked.connect(self.isempty)
        self.reset.clicked.connect(self.clearall)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stack"))
        self.ins_button.setText(_translate("MainWindow", "Enqueue"))
        self.del_button.setText(_translate("MainWindow", "Dequeue"))
        self.search_button.setText(_translate("MainWindow", "Front"))
        self.output_label.setText(_translate("MainWindow", "Output :"))
        self.operations_label.setText(_translate("MainWindow", "Operations"))
        self.info_label.setText(_translate("MainWindow", "Operation Info:"))
        self.back.setText(_translate("MainWindow", "Back"))
        self.reset.setText(_translate("MainWindow", "Reset All"))
        self.pushButton.setText(_translate("MainWindow", "Rear"))
        self.pushButton_2.setText(_translate("MainWindow", "Size"))
        self.pushButton_3.setText(_translate("MainWindow", "IsEmpty"))

    def clearall(self):
        self.scene.clear()
        self.output_tf.setPlainText('')
        self.textEdit.setPlainText('')

    def checker(self):
        if(len(self.pqueue) == 1):
            self.clearall()
            self.pqueue.pop()

        else:
            self.dequeue()

    def enqueue(self):
        element = self.ins_tf.toPlainText()
        self.ins_tf.setPlainText('')
        self.pqueue.append(element)
        self.sketch()
        self.textEdit.setText("")
        self.textEdit.setText(
            "Adds (or stores) an element to the end of the queue.")

    def dequeue(self):
        self.pqueue.pop(0)
        self.sketch()
        self.textEdit.setText("")
        self.textEdit.setText(
            "Removes (or access) the first element from the queue.")

    def printFront(self):
        front = self.front_rear(1)
        string = "Front is " + front
        self.output_tf.setPlainText(string)
        self.textEdit.setText("")


    def printRear(self):
        rear = self.front_rear(2)
        string = "Rear is " + rear
        self.output_tf.setPlainText(string)
        self.textEdit.setText("")


    def printSize(self):
        size = self.lsize()
        string = "Size is " + str(size)
        self.output_tf.setPlainText(string)

    def isempty(self):
        if self.lsize()>0:
            self.output_tf.setPlainText("Queue is not Empty")


    def sketch(self):
        defx = 600
        defy = 280
        length = self.lsize()
        front = self.front_rear(1)
        rear = self.front_rear(2)
        self.scene.clear()
        for i in reversed(self.pqueue):
            label = QtWidgets.QLabel(str(i))
            if i == rear:
                label.setStyleSheet("border: 3px solid blue; border-radius: 10px;background-color: red")
            if i == front:
                label.setStyleSheet("border: 3px solid blue; border-radius: 10px;background-color: rgb(37, 255, 37)")

            point = self.scene.addWidget(label)
            point.setPos(defx, defy)
            defx = defx - 50

    def lsize(self):
        return len(self.pqueue)

    def front_rear(self, mode):
        length = self.lsize()
        if mode == 1:
            return self.pqueue[0]

        if mode == 2:
            return self.pqueue[length-1]



def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = QtWidgets.QMainWindow()
    main = Ui_MainWindow()
    main.setupUi(ui)
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
