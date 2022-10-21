# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import os
import subprocess
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

from lists import stack_base, qbase, ll
from graph import basegclass, shortest_help, graph

from sort.gui_based_sorts import sortmain
from trees import avl, binary_tree
import searches


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1339, 891)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 300, 1281, 501))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.stack_menu = QtWidgets.QPushButton(self.centralwidget)
        self.stack_menu.setGeometry(QtCore.QRect(50, 70, 75, 23))
        self.stack_menu.setObjectName("stack_menu")
        self.queue_menu = QtWidgets.QPushButton(self.centralwidget)
        self.queue_menu.setGeometry(QtCore.QRect(50, 120, 75, 23))
        self.queue_menu.setObjectName("queue_menu")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 20, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 70, 101, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 120, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 170, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(350, 60, 111, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(150, 20, 20, 251))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(310, 30, 20, 241))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(50, 220, 75, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(540, 30, 20, 241))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(350, 100, 141, 23))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(350, 140, 121, 23))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(570, 60, 75, 23))
        self.pushButton_17.setObjectName("pushButton_17")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(370, 20, 71, 21))

        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(580, 30, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(670, 30, 20, 241))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(720, 30, 541, 231))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1339, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        self.stack_menu.clicked.connect(self.stackstart)
        self.queue_menu.clicked.connect(self.queuestart)
        self.pushButton_7.clicked.connect(self.llstart)
        self.pushButton_11.clicked.connect(self.searches)
        self.pushButton_3.clicked.connect(self.binarytree)
        self.pushButton_4.clicked.connect(self.avltree)
        self.pushButton_10.clicked.connect(self.graph_basic_start)
        self.pushButton_12.clicked.connect(self.graph_shortest)
        self.pushButton_13.clicked.connect(self.graph_misc)
        self.pushButton_17.clicked.connect(self.sortstart)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.stack_menu.setText(_translate("MainWindow", "Stack"))
        self.queue_menu.setText(_translate("MainWindow", "Queue"))
        self.label.setText(_translate("MainWindow", "Lists"))
        self.label_2.setText(_translate("MainWindow", "Trees"))
        self.pushButton_3.setText(_translate("MainWindow", "Binary Search Tree"))
        self.pushButton_4.setText(_translate("MainWindow", "AVL Tree"))
        self.pushButton_7.setText(_translate("MainWindow", "Linked List"))
        self.pushButton_10.setText(_translate("MainWindow", "Basic Operations"))
        self.pushButton_11.setText(_translate("MainWindow", "Searching"))
        self.pushButton_12.setText(_translate("MainWindow", "Shortest Paths Algorithms"))
        self.pushButton_13.setText(_translate("MainWindow", "Misc"))
        self.pushButton_17.setText(_translate("MainWindow", "Sorting"))
        self.label_5.setText(_translate("MainWindow", "Graphs"))
        self.label_6.setText(_translate("MainWindow", "Sorting"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#63336f;\">Features List</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; color:#63336f;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Stack - </span><span style=\" font-size:10pt; color:#3b8d7b;\">All Stack operations</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Queue - </span><span style=\" font-size:10pt; color:#33a270;\">All Queue operations</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Linked List - </span><span style=\" font-size:10pt; color:#408d58;\">Singly Linked List, Doubly Linked List, Circular Linked List</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Searching - </span><span style=\" font-size:10pt; color:#6a8c22;\">Linear Search, Binary Search</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Tree - </span><span style=\" font-size:10pt; color:#b6bc38;\">Tree operations</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Graph Basic Operations - </span><span style=\" font-size:10pt; color:#c6bc2d;\">Complement, Connectivity, Nature of graph etc.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Shortest Paths Algorithms - </span><span style=\" font-size:10pt; color:#b4531b;\">Djikstra, Bellman Ford, Floyd Warshall</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Misc - </span><span style=\" font-size:10pt; color:#ce5d25;\">DFS,BFS, Travelling Salesperson, Hamiltonian Path</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Sorting - </span><span style=\" font-size:10pt; color:#de4d1c;\">Bubble, Selection, Insertion, Quick, Merge etc.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))

    def stackstart(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = stack_base.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def queuestart(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = qbase.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def llstart(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = ll.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def graph_basic_start(self):
        self.obj = basegclass.GUI()
        self.obj.show()
        """self.MainWindow = QtWidgets.QMainWindow()
        self.ui = baseg.Ui_Basic()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()"""

    def graph_misc(self):
        self.obj = graph.GUI()
        self.obj.show()
        """self.MainWindow = QtWidgets.QMainWindow()
        self.ui = graph_ui.Ui_Dijsktra()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()"""

    def graph_shortest(self):
        self.obj = shortest_help.GUI()
        self.obj.show()
        """self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Shortest()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()"""

    def avltree(self):

        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = avl.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def binarytree(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = binary_tree.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def searches(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = searches.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def sortstart(self):
        sortmain.startevent()
        #os.system("sort/gui_based_sorts/sortmain.py")
        #subprocess.Popen(['python', 'sort/gui_based_sorts/sortmain.py'])
