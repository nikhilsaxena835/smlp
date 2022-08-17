# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sortbase.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QParallelAnimationGroup, QPoint


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1225, 887)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 190, 1071, 80))
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 410, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onbtnclick)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1225, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "1"))
        self.label_4.setText(_translate("MainWindow", "2"))
        self.label_3.setText(_translate("MainWindow", "3"))
        self.label_2.setText(_translate("MainWindow", "4"))
        self.label.setText(_translate("MainWindow", "5"))
        self.label_6.setText(_translate("MainWindow", "6"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

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