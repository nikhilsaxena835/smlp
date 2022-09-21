# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'binary_tree.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QBrush, QPen
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
        self.del_button = QtWidgets.QPushButton(self.centralwidget)
        self.del_button.setGeometry(QtCore.QRect(1080, 350, 75, 31))
        self.del_button.setObjectName("del_button")
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(60, 650, 101, 16))
        self.output_label.setObjectName("output_label")
        self.search_tf = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.search_tf.setGeometry(QtCore.QRect(940, 240, 61, 31))
        self.search_tf.setObjectName("search_tf")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(930, 90, 281, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(930, 310, 281, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(920, 100, 20, 221))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(1200, 100, 20, 211))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.operations_label = QtWidgets.QLabel(self.centralwidget)
        self.operations_label.setGeometry(QtCore.QRect(930, 80, 81, 16))
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

        self.ins_tf_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ins_tf_2.setGeometry(QtCore.QRect(940, 350, 104, 31))
        self.ins_tf_2.setObjectName("ins_tf_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(930, 430, 281, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(920, 320, 20, 121))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(1200, 310, 20, 121))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(990, 110, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(950, 220, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1020, 220, 47, 13))
        self.label_4.setObjectName("label_4")
        self.search_tf_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.search_tf_3.setGeometry(QtCore.QRect(1020, 240, 61, 31))
        self.search_tf_3.setObjectName("search_tf_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1100, 240, 75, 23))
        self.pushButton.setObjectName("pushButton")
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

        self.ins_button.clicked.connect(self.createNode)
        self.pushButton.clicked.connect(self.createEdge)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Graph"))
        self.ins_button.setText(_translate("MainWindow", "Insert Node"))
        self.del_button.setText(_translate("MainWindow", "Delete Node"))
        self.output_label.setText(_translate("MainWindow", "Output Sequence :"))
        self.operations_label.setText(_translate("MainWindow", "Operations"))
        self.info_label.setText(_translate("MainWindow", "Operation Info:"))
        self.back.setText(_translate("MainWindow", "Back"))
        self.reset.setText(_translate("MainWindow", "Reset All"))
        self.label_2.setText(_translate("MainWindow", "Node Value"))
        self.label_3.setText(_translate("MainWindow", "From"))
        self.label_4.setText(_translate("MainWindow", "To"))
        self.pushButton.setText(_translate("MainWindow", "Create Edge"))

    def createNode(self):
        inp = self.ins_tf.toPlainText()
        self.ins_tf.setPlainText("")

        self.vertices[inp] = self.vertexCreator(inp)

        label = QtWidgets.QLabel(inp)
        label.setGeometry(QtCore.QRect(320, 220, 31, 31))
        label.setStyleSheet("border: 3px solid blue; border-radius: 10px;background-color: red")

        self.teset(self.vertices[inp])



    def vertexCreator(self, inp):
        ellipse = self.scene.addEllipse(0, 0, 30, 30)
        ellipse.setFlags(QtWidgets.QGraphicsItem.ItemIsMovable)
        adjustment = QtCore.QPointF(7,7)
        ellipse_pos = ellipse.pos()
        ellipse.setBrush(QBrush(QtCore.Qt.red, style = QtCore.Qt.SolidPattern))
        text = self.scene.addSimpleText(str(inp))
        ellipse_pos = ellipse_pos + adjustment
        text.setPos(ellipse_pos)
        text.setParentItem(ellipse)
        return ellipse

    def teset(self, ellipse):
        ellipse.setBrush(QBrush(QtCore.Qt.green, style = QtCore.Qt.SolidPattern))

    def createEdge(self):
        inp = self.search_tf.toPlainText()
        self.ins_tf.setPlainText("")
        inp2 = self.search_tf_3.toPlainText()
        self.ins_tf.setPlainText("")

        e1 = self.vertices[inp]
        e2 = self.vertices[inp2]
        pos1 = e1.pos()
        pos2 = e2.pos()
        line = QtCore.QLineF(pos1, pos2)
        self.scene.addLine(line, QPen())



