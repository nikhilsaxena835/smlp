# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stack.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsScene


class Ui_MainWindow(object):
    pstack = []
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1240, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.scene = QGraphicsScene()
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(40, 60, 851, 561))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setScene(self.scene)
        self.graphicsView.show()


        self.ins_button = QtWidgets.QPushButton(self.centralwidget)
        self.ins_button.setGeometry(QtCore.QRect(1120, 140, 75, 31))
        self.ins_button.setObjectName("ins_button")
        self.ins_tf = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ins_tf.setGeometry(QtCore.QRect(990, 140, 104, 31))
        self.ins_tf.setObjectName("ins_tf")
        self.del_button = QtWidgets.QPushButton(self.centralwidget)
        self.del_button.setGeometry(QtCore.QRect(1020, 230, 75, 31))
        self.del_button.setObjectName("del_button")
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(1020, 280, 75, 31))
        self.search_button.setObjectName("search_button")
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(60, 650, 101, 16))
        self.output_label.setObjectName("output_label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(930, 90, 281, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(930, 220, 281, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(930, 420, 281, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(920, 100, 20, 121))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(1200, 100, 20, 121))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(920, 220, 16, 211))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(1200, 210, 20, 221))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.operations_label = QtWidgets.QLabel(self.centralwidget)
        self.operations_label.setGeometry(QtCore.QRect(950, 110, 81, 16))
        self.operations_label.setObjectName("operations_label")
        self.output_tf = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.output_tf.setGeometry(QtCore.QRect(170, 640, 691, 31))
        self.output_tf.setObjectName("output_tf")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(170, 700, 691, 131))
        self.textEdit.setObjectName("textEdit")
        self.info_label = QtWidgets.QLabel(self.centralwidget)
        self.info_label.setGeometry(QtCore.QRect(60, 710, 81, 16))
        self.info_label.setObjectName("info_label")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.back.setObjectName("back")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(140, 10, 75, 23))
        self.reset.setObjectName("reset")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1020, 330, 75, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1020, 380, 75, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(130, 480, 691, 16))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1240, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.ins_button.clicked.connect(self.spush)
        self.del_button.clicked.connect(self.spop)
        self.search_button.clicked.connect(self.s_top)
        self.pushButton.clicked.connect(self.isempty)
        self.pushButton_2.clicked.connect(self.lsize)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Binary Tree"))
        self.ins_button.setText(_translate("MainWindow", "Push"))
        self.del_button.setText(_translate("MainWindow", "Pop"))
        self.search_button.setText(_translate("MainWindow", "Top"))
        self.output_label.setText(_translate("MainWindow", "Output :"))
        self.operations_label.setText(_translate("MainWindow", "Operations"))
        self.info_label.setText(_translate("MainWindow", "Operation Info:"))
        self.back.setText(_translate("MainWindow", "Back"))
        self.reset.setText(_translate("MainWindow", "Reset All"))
        self.pushButton.setText(_translate("MainWindow", "IsEmpty"))
        self.pushButton_2.setText(_translate("MainWindow", "Size"))

    def spush(self):
        element = self.ins_tf.toPlainText()
        self.ins_tf.setPlainText('')
        self.pstack.append(element)
        self.sketch()

    def sketch(self):
        defx = 450
        defy = 470

        top = self.s_top()

        self.scene.clear()
        for i in self.pstack:
            label = QtWidgets.QLabel(str(i))
            if i == top:
                label.setStyleSheet("border: 3px solid blue; border-radius: 10px;background-color: rgb(37, 255, 37)")

            point = self.scene.addWidget(label)
            point.setPos(defx, defy)
            defy = defy - 30

    def lsize(self):
        string = "Size of the stack is " + str(len(self.pstack))
        self.output_tf.setPlainText(string)
        return len(self.pstack)

    def s_top(self):
        length = self.lsize()
        string = "Top of the stack is " + self.pstack[length-1]
        self.output_tf.setPlainText(string)
        return self.pstack[length - 1]

    def spop(self):
        length = self.lsize()
        self.pstack.pop(length-1)
        self.sketch()

    def isempty(self):
        if self.lsize()>0:
            self.output_tf.setPlainText("Stack not empty")
        else:
            self.output_tf.setPlainText("Stack is Empty")


