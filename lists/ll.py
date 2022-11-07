# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'll.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import math
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QLineF, QPointF
from PyQt5.QtGui import QPolygonF, QPen, QBrush
from PyQt5.QtWidgets import QGraphicsScene


class Ui_MainWindow(object):

    llist = []
    mode = -1
    head = None


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1240, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.scene = QGraphicsScene()
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(40, 60, 711, 441))
        self.graphicsView.setStyleSheet("")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setScene(self.scene)
        self.graphicsView.show()


        self.ins_tf = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ins_tf.setGeometry(QtCore.QRect(820, 70, 71, 31))
        self.ins_tf.setObjectName("ins_tf")
        self.ins_atbeg = QtWidgets.QPushButton(self.centralwidget)
        self.ins_atbeg.setGeometry(QtCore.QRect(930, 70, 111, 31))
        self.ins_atbeg.setObjectName("ins_atbeg")
        self.ins_atlast = QtWidgets.QPushButton(self.centralwidget)
        self.ins_atlast.setGeometry(QtCore.QRect(930, 120, 75, 31))
        self.ins_atlast.setObjectName("ins_atlast")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(800, 30, 281, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(790, 300, 281, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(800, 500, 281, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(790, 40, 20, 121))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(1070, 40, 20, 121))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(790, 160, 16, 351))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(1070, 150, 20, 361))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.operations_label = QtWidgets.QLabel(self.centralwidget)
        self.operations_label.setGeometry(QtCore.QRect(820, 50, 81, 16))
        self.operations_label.setObjectName("operations_label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(120, 530, 631, 91))
        self.textEdit.setObjectName("textEdit")
        self.info_label = QtWidgets.QLabel(self.centralwidget)
        self.info_label.setGeometry(QtCore.QRect(10, 540, 81, 16))
        self.info_label.setObjectName("info_label")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.back.setObjectName("back")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(140, 10, 75, 23))
        self.reset.setObjectName("reset")

        self.ins_afterloc = QtWidgets.QPushButton(self.centralwidget)
        self.ins_afterloc.setGeometry(QtCore.QRect(930, 350, 141, 31))
        self.ins_afterloc.setObjectName("ins_afterloc")
        self.del_frombeg = QtWidgets.QPushButton(self.centralwidget)
        self.del_frombeg.setGeometry(QtCore.QRect(930, 170, 121, 31))
        self.del_frombeg.setObjectName("del_frombeg")
        self.del_fromlast = QtWidgets.QPushButton(self.centralwidget)
        self.del_fromlast.setGeometry(QtCore.QRect(930, 220, 111, 31))
        self.del_fromlast.setObjectName("del_fromlast")
        self.del_atloc = QtWidgets.QPushButton(self.centralwidget)
        self.del_atloc.setGeometry(QtCore.QRect(930, 430, 121, 31))
        self.del_atloc.setObjectName("del_atloc")
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(930, 260, 75, 31))
        self.search.setObjectName("search")
        self.ins_tf_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ins_tf_2.setGeometry(QtCore.QRect(820, 120, 71, 31))
        self.ins_tf_2.setObjectName("ins_tf_2")
        self.ins_tf_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ins_tf_3.setGeometry(QtCore.QRect(820, 350, 71, 31))
        self.ins_tf_3.setObjectName("ins_tf_3")
        self.ins_tf_4 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ins_tf_4.setGeometry(QtCore.QRect(820, 430, 71, 31))
        self.ins_tf_4.setObjectName("ins_tf_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(820, 330, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(820, 410, 47, 13))
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(830, 520, 281, 151))
        self.groupBox.setObjectName("groupBox")
        self.sll = QtWidgets.QRadioButton(self.groupBox)
        self.sll.setGeometry(QtCore.QRect(20, 30, 111, 17))
        self.sll.setObjectName("sll")
        self.dll = QtWidgets.QRadioButton(self.groupBox)
        self.dll.setGeometry(QtCore.QRect(20, 60, 111, 17))
        self.dll.setObjectName("dll")
        self.cll = QtWidgets.QRadioButton(self.groupBox)
        self.cll.setGeometry(QtCore.QRect(20, 90, 131, 17))
        self.cll.setObjectName("cll")
        self.cdll = QtWidgets.QRadioButton(self.groupBox)
        self.cdll.setGeometry(QtCore.QRect(20, 120, 151, 17))
        self.cdll.setObjectName("cdll")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.ins_atbeg.clicked.connect(self.insbeg)
        self.ins_atlast.clicked.connect(self.inslast)
        self.ins_afterloc.clicked.connect(self.insatloc)
        self.del_frombeg.clicked.connect(self.delfrombeg)
        self.del_fromlast.clicked.connect(self.delfromlast)
        self.del_atloc.clicked.connect(self.delatloc)
        self.search.clicked.connect(self.searchop)

        self.buttonGroup = QtWidgets.QButtonGroup(self.centralwidget)
        self.buttonGroup.setObjectName("groupBox")

        self.buttonGroup.addButton(self.sll, 1)
        self.buttonGroup.addButton(self.dll, 2)
        self.buttonGroup.addButton(self.cll, 3)
        self.buttonGroup.addButton(self.cdll, 4)
        self.buttonGroup.buttonClicked.connect(self.setmode)
        self.show_dialog("Do not proceed without selecting a list type. \n")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Linked List"))
        self.ins_atbeg.setText(_translate("MainWindow", "Insert At Beginning"))
        self.ins_atlast.setText(_translate("MainWindow", "Insert At Last"))

        self.operations_label.setText(_translate("MainWindow", "Operations"))
        self.info_label.setText(_translate("MainWindow", "Operation Info:"))
        self.back.setText(_translate("MainWindow", "Back"))
        self.reset.setText(_translate("MainWindow", "Reset All"))
        self.ins_afterloc.setText(_translate("MainWindow", "Insert After Location"))
        self.del_frombeg.setText(_translate("MainWindow", "Delete From Beginning"))
        self.del_fromlast.setText(_translate("MainWindow", "Delete From Last"))
        self.del_atloc.setText(_translate("MainWindow", "Delete At Location"))
        self.search.setText(_translate("MainWindow", "Search"))
        self.label.setText(_translate("MainWindow", "Value"))
        self.label_2.setText(_translate("MainWindow", "Position"))
        self.groupBox.setTitle(_translate("MainWindow", "Mode"))
        self.sll.setText(_translate("MainWindow", "Singly Linked List"))
        self.dll.setText(_translate("MainWindow", "Doubly Linked List"))
        self.cll.setText(_translate("MainWindow", "Circular Linked List"))
        self.cdll.setText(_translate("MainWindow", "Circular Doubly Linked List"))

    def show_dialog(self, message):
        """Opening a new error window with a given error message.
        Args:
            message (string): error text.
        """
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Information")
        msg.setInformativeText(message)
        msg.setWindowTitle("Please keep in mind!")
        msg.exec_()

    def insbeg(self):
        node = self.ins_tf.toPlainText()
        self.ins_tf.setPlainText("")
        self.llist.append(int(node))
        self.sketch()

    def inslast(self):
        node = self.ins_tf.toPlainText()
        self.ins_tf.setPlainText("")
        self.llist.append(int(node))
        self.sketch()

    def insatloc(self):
        node = self.ins_tf3.toPlainText()
        pos = self.ins_tf_4.toPlainText()
        self.ins_tf.setPlainText("")
        self.llist.insert(int(pos)+1, int(node))
        self.sketch()

    def delfrombeg(self):
        del self.llist[0]
        self.sketch()

    def delfromlast(self):
        self.llist.pop()
        self.sketch()

    def delatloc(self):
        node = self.ins_tf3.toPlainText()
        self.ins_tf.setPlainText("")
        self.llist.remove(int(node))
        self.sketch()

    def setmode(self):
        button_id = self.buttonGroup.checkedId()
        print(button_id)
        if button_id == 1:
            self.mode = 1

        if button_id == 2:
            self.mode = 2


        if button_id == 3:
            self.mode = 3

        if button_id == 4:
            self.mode = 4



    def sketch(self):
        self.scene.clear()
        painter = QtGui.QPainter()
        defx = 100
        defy = 470
        head = QtWidgets.QLabel("Head")
        head.setStyleSheet("border: 3px solid blue; border-radius: 10px;background-color: rgb(37, 255, 37)")
        self.scene.addWidget(head)
        prev = head
        next = None
        for i in self.llist:
            label = QtWidgets.QLabel(str(i))
            if self.mode == 1:
                point = self.scene.addWidget(label)
                point.setPos(defx, defy)
                start = prev.pos()
                dest = point.pos()
                self.DrawLineWithArrow(painter, start, dest)
                prev = point

            if self.mode == 2:
                point = self.scene.addWidget(label)
                point.setPos(defx, defy)
                start = prev.pos()
                dest = point.pos()
                self.DrawLineWithArrow(painter, start, dest)
                self.DrawLineWithArrow(painter, dest, start)
                prev = point

            if self.mode == 3:
                point = self.scene.addWidget(label)
                point.setPos(defx, defy)
                start = prev.pos()
                dest = point.pos()
                self.DrawLineWithArrow(painter, start, dest)
                prev = point
                if (len(self.llist) > 1):
                    self.DrawLineWithArrow(painter, prev.pos, head.pos)

            if self.mode == 4:
                point = self.scene.addWidget(label)
                point.setPos(defx, defy)
                start = prev.pos()
                dest = point.pos()
                self.DrawLineWithArrow(painter, start, dest)
                self.DrawLineWithArrow(painter, dest, start)
                prev = point
                if (len(self.llist) > 1):
                    self.DrawLineWithArrow(painter, prev.pos, head.pos)



            point = self.scene.addWidget(label)
            point.setPos(defx, defy)
            defx = defx+100

    def DrawLineWithArrow(self, painter, end, start):
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        arrowSize = 40
        painter.setPen(QtCore.Qt.black)
        painter.setBrush(QtCore.Qt.black)
        line = QLineF(start,end)
        angle = math.atan2(-line.dy(), line.dx())
        arrow1 = line.p1() + QPointF(math.sin(angle + math.pi / 3) * arrowSize,
                                        math.cos(angle + math.pi / 3) * arrowSize)

        arrowP2 = line.p1() + QPointF(math.sin(angle + math.pi - math.pi / 3) * arrowSize,
                                      math.cos(angle + math.pi - math.pi / 3) * arrowSize)

        arrowHead = QPolygonF([line.p1(), arrow1, arrowP2])
        """obj = painter.drawLine(line)
        obj2 = painter.drawPolygon(arrowHead)"""
        self.scene.addLine(line, QPen(QtCore.Qt.black))
        self.scene.addPolygon(arrowHead)


    def searchop(self):
        pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = QtWidgets.QMainWindow()
    main = Ui_MainWindow()
    main.setupUi(ui)
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()