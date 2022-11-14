# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sortbase.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsScene, QApplication, QGraphicsTextItem


class Ui_MainWindow(object):
    ind = -1
    s = "Element found at : "
    arr = []
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1322, 887)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 70, 901, 171))
        self.graphicsView.setObjectName("graphicsView")

        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.graphicsView.show()


        self.Home = QtWidgets.QPushButton(self.centralwidget)
        self.Home.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.Home.setObjectName("Home")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(130, 10, 75, 23))
        self.reset.setObjectName("reset")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(1000, 70, 201, 221))
        self.groupBox.setObjectName("groupBox")
        self.binary = QtWidgets.QRadioButton(self.groupBox)
        self.binary.setGeometry(QtCore.QRect(20, 40, 101, 17))
        self.binary.setObjectName("binary")
        self.linear = QtWidgets.QRadioButton(self.groupBox)
        self.linear.setGeometry(QtCore.QRect(20, 70, 101, 17))
        self.linear.setObjectName("linear")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 47, 13))
        self.label_4.setObjectName("label_4")
        self.plainTextEdit_1 = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit_1.setGeometry(QtCore.QRect(90, 110, 61, 31))
        self.plainTextEdit_1.setObjectName("plainTextEdit_1")
        self.ins_but = QtWidgets.QPushButton(self.centralwidget)
        self.ins_but.setGeometry(QtCore.QRect(870, 310, 75, 31))
        self.ins_but.setObjectName("ins_but")
        self.inp_arr = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inp_arr.setGeometry(QtCore.QRect(713, 310, 141, 31))
        self.inp_arr.setObjectName("inp_arr")
        self.insert_info = QtWidgets.QLabel(self.centralwidget)
        self.insert_info.setGeometry(QtCore.QRect(720, 270, 221, 31))
        self.insert_info.setObjectName("insert_info")
        self.start_but = QtWidgets.QPushButton(self.centralwidget)
        self.start_but.setGeometry(QtCore.QRect(60,170, 75, 23))
        self.start_but.setObjectName("start_but")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 140, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 140, 47, 13))
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 300, 641, 91))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 270, 81, 16))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1261, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.buttonGroup = QtWidgets.QButtonGroup(self.centralwidget)
        self.buttonGroup.setObjectName("groupBox")

        self.buttonGroup.addButton(self.binary, 1)
        self.buttonGroup.addButton(self.linear, 2)


        self.ins_but.clicked.connect(self.createArray)
        self.start_but.clicked.connect(self.start_sequence)




        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Home.setText(_translate("MainWindow", "Home"))
        self.reset.setText(_translate("MainWindow", "Reset"))
        self.groupBox.setTitle(_translate("MainWindow", "Select Searching Algorithm"))
        self.binary.setText(_translate("MainWindow", "Binary Search"))
        self.linear.setText(_translate("MainWindow", "Linear Search"))

        self.ins_but.setText(_translate("MainWindow", "Insert"))
        self.insert_info.setText(_translate("MainWindow", "Fill array elements.Eg: \"5,3,4,7,9,5,1,6,0\""))
        self.start_but.setText(_translate("MainWindow", "Start"))
        self.label_4.setText(_translate("MainWindow", "Find :"))
        self.label_3.setText(_translate("MainWindow", "Operation Info:"))

    def createArray(self):
        inpstr = self.inp_arr.toPlainText()
        self.arr = inpstr.split(",")
        count = int(0)
        #convert all array elements from string type to integer type
        for i in self.arr:
            self.arr[count] = int(self.arr[count])
            count = count + 1
        print(self.arr)
        self.sketch(self.arr)


    def start_sequence(self):
        button_id = self.buttonGroup.checkedId()
        toFind = self.plainTextEdit_1.toPlainText()
        toFind = int(toFind)
        self.plainTextEdit_1.setPlainText("")
        arr = self.arr.copy()
        print(button_id)
        if button_id == 1:
            self.binary_resketch(arr,toFind)
        if button_id == 2:
            self.linear_resketch(arr,toFind)


    def sketch(self,arr):
        self.scene.clear()

        forward = 100
        for i in range(0, len(arr)):
            print("RAN")
            label = self.getLabel(arr[i], False)
            label = self.scene.addWidget(label)
            pos_point = QtCore.QPoint(forward, 160)
            label.setPos(pos_point)
            forward = forward + 70

    def getLabel(self, i, flag):
        if flag is False:
            label = QtWidgets.QLabel(str(i))
            label.setStyleSheet("border: 3px solid blue; border-radius: 10px; background-color: lightblue")
        elif flag == 3:
            label = QtWidgets.QLabel(str(i))
            label.setStyleSheet("border: 3px solid blue; border-radius: 10px; background-color: red")
        else:
            label = QtWidgets.QLabel(str(i))
            label.setStyleSheet("border: 3px solid blue; border-radius: 10px; background-color: green")
        label.setGeometry(QtCore.QRect(190, 280, 41, 31))
        return label

    def linear_resketch(self, arr, toFind):
        self.scene.clear()
        count = -1

        for j in range(0, len(arr)):
            self.scene.clear()
            count = count + 1
            forward = 100
            QApplication.processEvents()
            time.sleep(1)
            for i in range(0, len(arr)):
                print("Draw")
                if i == toFind:
                    label = self.getLabel(arr[i], True)
                    self.ind = arr.index(i)
                    self.s = self.s + str(self.ind)
                    self.plainTextEdit.setPlainText(self.s)

                elif i == arr[count]:
                    label = self.getLabel(arr[i], 3)
                else:
                    label = self.getLabel(arr[i], False)
                label = self.scene.addWidget(label)
                pos_point = QtCore.QPoint(forward, 160)
                label.setPos(pos_point)
                forward = forward + 70
            if self.ind != -1:
                break

    def binary_resketch(self, arr, toFind):
        print("binary search")
        self.scene.clear()
        count = -1
        forward = 100
        lo = 0
        hi = len(arr) - 1
        for j in range(0, len(arr)):
            QApplication.processEvents()
            time.sleep(1)
            count = count + 1
            mid = int((hi+lo)/2)
            if arr[mid] < toFind:
                lo = mid + 1
            else:
                hi = mid

            for i in range(0, len(arr)):

                if i == arr[lo] or i == arr[hi]:
                    label = self.getLabel(arr[i], 3)


                if arr[lo] == toFind:
                    label = self.getLabel(arr[i], True)
                    self.s = self.s + str(i)
                    self.plainTextEdit.setPlainText(self.s)

                if arr[hi] == toFind:
                    label = self.getLabel(arr[hi], True)
                    self.s = self.s + str(i)
                    self.plainTextEdit.setPlainText(self.s)

                else:
                    label = self.getLabel(arr[i], False)

                label = self.scene.addWidget(label)
                pos_point = QtCore.QPoint(forward, 160)
                label.setPos(pos_point)
                forward = forward + 70


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = QtWidgets.QMainWindow()
    main = Ui_MainWindow()
    main.setupUi(ui)
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()