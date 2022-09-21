# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'binary_tree.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QGraphicsScene


class Ui_MainWindow(object):
    vertices = {}
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1240, 900)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.scene = QGraphicsScene()
        # self.scene.setSceneRect(40,60,851,561)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(40, 60, 851, 561))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setScene(self.scene)
        self.graphicsView.show()


        self.ins_button = QtWidgets.QPushButton(self.centralwidget)
        self.ins_button.setGeometry(QtCore.QRect(1110, 140, 75, 31))
        self.ins_button.setObjectName("ins_button")
        self.ins_tf = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ins_tf.setGeometry(QtCore.QRect(990, 140, 104, 31))
        self.ins_tf.setObjectName("ins_tf")




        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1240, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.ins_button.clicked.connect(self.createNode)



        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setObjectName("output_label")
        self.label2.setGeometry(QtCore.QRect(60, 650, 101, 16))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Graph"))
        self.ins_button.setText(_translate("MainWindow", "Insert Node"))


    def createNode(self):
        inp = self.ins_tf.toPlainText()
        self.ins_tf.setPlainText("")
        self.search_tf_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.search_tf_3.setGeometry(QtCore.QRect(1020, 240, 61, 31))
        self.search_tf_3.setObjectName("search_tf_3")
        label = QtWidgets.QLabel(inp)
        label.setGeometry(QtCore.QRect(320, 220, 31, 31))
        label.setStyleSheet("border: 3px solid blue; border-radius: 10px;background-color: red")
        self.scene.clear()
        label2 = QtWidgets.QLabel(self.centralwidget)
        label2.setObjectName("output_label")
        label2.setGeometry(QtCore.QRect(60, 650, 101, 16))
        point = self.scene.addWidget(label)
        self.vertices[inp] = point
        print(point)








