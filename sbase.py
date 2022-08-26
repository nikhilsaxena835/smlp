
from PyQt5.QtCore import QPropertyAnimation, QParallelAnimationGroup, QTimeLine, QPointF
from PyQt5.QtWidgets import QGraphicsScene, QApplication, QGraphicsTextItem, QGraphicsObject

import bubble_sort
from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow():
    lable_map = {}
    arr = None
    next = False
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1322, 887)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.next_step = QtWidgets.QPushButton(self.centralwidget)
        self.next_step.setGeometry(QtCore.QRect(800, 690, 75, 23))
        self.next_step.setObjectName("next_step")
        self.Home = QtWidgets.QPushButton(self.centralwidget)
        self.Home.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.Home.setObjectName("Home")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(130, 10, 75, 23))
        self.reset.setObjectName("reset")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(1110, 600, 201, 221))
        self.groupBox.setObjectName("groupBox")
        self.bubble = QtWidgets.QRadioButton(self.groupBox)
        self.bubble.setGeometry(QtCore.QRect(20, 40, 82, 17))
        self.bubble.setObjectName("bubble")
        self.selection = QtWidgets.QRadioButton(self.groupBox)
        self.selection.setGeometry(QtCore.QRect(20, 70, 101, 17))
        self.selection.setObjectName("selection")
        self.insertion = QtWidgets.QRadioButton(self.groupBox)
        self.insertion.setGeometry(QtCore.QRect(20, 100, 101, 17))
        self.insertion.setObjectName("insertion")
        self.merge = QtWidgets.QRadioButton(self.groupBox)
        self.merge.setGeometry(QtCore.QRect(20, 130, 82, 17))
        self.merge.setObjectName("merge")
        self.quick = QtWidgets.QRadioButton(self.groupBox)
        self.quick.setGeometry(QtCore.QRect(20, 160, 82, 17))
        self.quick.setObjectName("quick")
        self.heap = QtWidgets.QRadioButton(self.groupBox)
        self.heap.setGeometry(QtCore.QRect(20, 190, 82, 17))
        self.heap.setObjectName("heap")
        self.ins_but = QtWidgets.QPushButton(self.centralwidget)
        self.ins_but.setGeometry(QtCore.QRect(1240, 530, 75, 31))
        self.ins_but.setObjectName("ins_but")
        self.inp_arr = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inp_arr.setGeometry(QtCore.QRect(1083, 530, 141, 31))
        self.inp_arr.setObjectName("inp_arr")
        self.insert_info = QtWidgets.QLabel(self.centralwidget)
        self.insert_info.setGeometry(QtCore.QRect(1090, 490, 221, 31))
        self.insert_info.setObjectName("insert_info")
        self.start_but = QtWidgets.QPushButton(self.centralwidget)
        self.start_but.setGeometry(QtCore.QRect(1130, 820, 75, 23))
        self.start_but.setObjectName("start_but")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(80, 70, 1151, 181))
        self.graphicsView.setObjectName("graphicsView")

        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.graphicsView.show()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1322, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.ins_but.clicked.connect(self.createArray)
        self.start_but.clicked.connect(self.start_sequence)
        self.next_step.clicked.connect(self.setNext)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.next_step.setText(_translate("MainWindow", "Next"))
        self.Home.setText(_translate("MainWindow", "Home"))
        self.reset.setText(_translate("MainWindow", "Reset"))
        self.groupBox.setTitle(_translate("MainWindow", "Select Sorting Algorithm"))
        self.bubble.setText(_translate("MainWindow", "Bubble Sort"))
        self.selection.setText(_translate("MainWindow", "Selection Sort"))
        self.insertion.setText(_translate("MainWindow", "Insertion Sort"))
        self.merge.setText(_translate("MainWindow", "Merge Sort"))
        self.quick.setText(_translate("MainWindow", "Quick Sort"))
        self.heap.setText(_translate("MainWindow", "Heap Sort"))
        self.ins_but.setText(_translate("MainWindow", "Insert"))
        self.insert_info.setText(_translate("MainWindow", "Fill array elements.Eg: \"5,3,4,7,9,5,1,6,0\""))
        self.start_but.setText(_translate("MainWindow", "Start"))



    def createArray(self):
        inpstr = self.inp_arr.toPlainText()
        self.arr = inpstr.split(",")
        count = 0
        for i in self.arr:
            self.arr[count] = int(self.arr[count])
            count = count + 1
        print(self.arr)
        self.sketch(self.arr)

    def sketch(self,arr):
        self.scene.clear()

        forward = 100
        for i in arr:
            label = self.getLabel(i)
            self.lable_map[i] = label
            pos_point = QtCore.QPoint(forward, 160)
            label.setPos(pos_point)
            forward = forward + 70
            self.scene.addItem(label)
        print(self.lable_map)



    def start_sequence(self):
        bubble_sort.bubble.bubbleSort(self, self.arr)

    def onbtnclick(self, larger, smaller):
        print(smaller, larger)

        # animation = QPropertyAnimation(
        #     self,
        #     propertyName=b"pos",
        #     targetObject=label_larger,
        #     startValue=start_pos,
        #     endValue=end_pos,
        #     duration=8000,
        # )

        self.swap_elements(larger, smaller)
        while(self.next == False):
            pass


    def getLabel(self, i):
        label = QGraphicsTextItem(str(i))
        return label

    def swap_elements(self,element1, element2):
                element2_ref = self.lable_map[element2]
                element1_ref = self.lable_map[element1]
                p1 = element1_ref.pos()
                p2 = element2_ref.pos()
                element1_ref.setPos(p2)
                element2_ref.setPos(p1)

    def setNext(self):
        self.next_step = True