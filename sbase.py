# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sortbase.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QParallelAnimationGroup, QPoint


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1322, 887)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(270, 60, 781, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(800, 690, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 10, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(1110, 600, 201, 221))
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 101, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 100, 101, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 130, 82, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_5.setGeometry(QtCore.QRect(20, 160, 82, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_6.setGeometry(QtCore.QRect(20, 190, 82, 17))
        self.radioButton_6.setObjectName("radioButton_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1240, 530, 75, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(1120, 530, 104, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1120, 500, 111, 21))
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1322, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.onbtnclick)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "3"))
        self.label_4.setText(_translate("MainWindow", "2"))
        self.label_3.setText(_translate("MainWindow", "1"))
        self.label_2.setText(_translate("MainWindow", "4"))
        self.label.setText(_translate("MainWindow", "7"))
        self.label_6.setText(_translate("MainWindow", "6"))
        self.label_7.setText(_translate("MainWindow", "8"))
        self.label_8.setText(_translate("MainWindow", "5"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_2.setText(_translate("MainWindow", "Home"))
        self.pushButton_3.setText(_translate("MainWindow", "Reset"))
        self.groupBox.setTitle(_translate("MainWindow", "Select Sorting Algorithm"))
        self.radioButton.setText(_translate("MainWindow", "Bubble Sort"))
        self.radioButton_2.setText(_translate("MainWindow", "Selection Sort"))
        self.radioButton_3.setText(_translate("MainWindow", "Insertion Sort"))
        self.radioButton_4.setText(_translate("MainWindow", "Merge Sort"))
        self.radioButton_5.setText(_translate("MainWindow", "Quick Sort"))
        self.radioButton_6.setText(_translate("MainWindow", "Heap Sort"))
        self.pushButton_4.setText(_translate("MainWindow", "Insert"))
        self.label_9.setText(_translate("MainWindow", "Fill array elements one by one"))



    def onbtnclick(self):

        # x1 = self.label_6.x()
        # y1 = self.label_6.y()
        # x2 = self.label_3.x()
        # y2 = self.label_3.y()
        #
        # point1 = QPoint(x1, y1 - 5)
        # point2 = QPoint(x1-x2, y1 - 5)
        # point3 = QPoint(x1-x2, y1)
        # self.doanim(start_pos, point1)
        # self.doanim(point1,point2)
        # self.doanim(point2, point3)


        start_pos = self.label_6.pos()

        end_pos = self.label_3.pos()
        animation_group = QParallelAnimationGroup(self)

        animation = QPropertyAnimation(
            self,
            propertyName=b"pos",
            targetObject=self.label_6,
            startValue=start_pos,
            endValue=end_pos,
            duration=8000,
        )

        animation2 = QPropertyAnimation(
            self,
            propertyName=b"pos",
            targetObject=self.label_3,
            startValue=end_pos,
            endValue=start_pos,
            duration=8000,
        )
        animation_group.addAnimation(animation)
        animation_group.addAnimation(animation2)
        animation_group.start(QParallelAnimationGroup.DeleteWhenStopped)


    # def doanim(self, start_pos, end_pos):
    #     animation_group = QParallelAnimationGroup(self)
    #
    #     animation = QPropertyAnimation(
    #         self,
    #         propertyName=b"pos",
    #         targetObject=self.label_6,
    #         startValue=start_pos,
    #         endValue=end_pos,
    #         duration=8000,
    #     )
    #
    #     animation2 = QPropertyAnimation(
    #         self,
    #         propertyName=b"pos",
    #         targetObject=self.label_3,
    #         startValue=end_pos,
    #         endValue=start_pos,
    #         duration=8000,
    #     )
    #     animation_group.addAnimation(animation)
    #     animation_group.addAnimation(animation2)
    #     animation_group.start(QParallelAnimationGroup.DeleteWhenStopped)