import time

from PyQt5.QtGui import QBrush
from PyQt5.QtWidgets import QGraphicsScene, QApplication, QGraphicsTextItem, QGraphicsRectItem

import bubble_sort
from PyQt5 import QtCore, QtWidgets, QtGui


class Ui_MainWindow():
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
        self.graphicsView.setGeometry(QtCore.QRect(80, 70, 1151, 411))
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
        self.scene.setSceneRect(-150,150,360,180)

        self.buttonGroup = QtWidgets.QButtonGroup(self.centralwidget)
        self.buttonGroup.setObjectName("groupBox")

        self.buttonGroup.addButton(self.bubble, 1)
        self.buttonGroup.addButton(self.selection, 2)
        self.buttonGroup.addButton(self.insertion, 3)
        self.buttonGroup.addButton(self.merge, 4)
        self.buttonGroup.addButton(self.quick, 5)


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
        #convert all array elements from string type to integer type
        for i in self.arr:
            self.arr[count] = int(self.arr[count])
            count = count + 1
        print(self.arr)
        self.sketch(self.arr)


    def sketch(self,arr):
        self.scene.clear()
        data_list = arr
        canvas_height = 411
        canvas_width = 1151
        x_width = 100 / (len(data_list) + 1)
        #offset = 10
        offset = 0
        spacing = 10
        xoff = 0
        print(x_width)
        # create a normalized size so it fills screen better
        normalized_data = [i / max(data_list) for i in data_list]
        for i, height in enumerate(normalized_data):
            # top left
            x0 = (i * x_width) + offset + spacing
            y0 = canvas_height - (height * 100)
            offset = 18
            # bottom right
            #x1 = ((height + 1) * x_width) + offset
            x1 = 50 + xoff
            y1 = 100
            xoff = 20
            print(x0, y0, x1, y1,i, height)
            # draws the rectangles
            ritem = self.scene.addRect(QtCore.QRectF(x0, y0, x1, y1), pen=QtGui.QPen(), brush=QtGui.QBrush(QtCore.Qt.red))
            label = QtWidgets.QLabel(str(data_list[i]))
            litem = self.scene.addWidget(label)
            litem.setPos(x0 + 2, y0)
            #ritem.setPos(x1, 100)

            print("the pos is ",ritem.x(),ritem.y())
            





        # updates the whole window
        QApplication.processEvents()




    def start_sequence(self):
        button_id = self.buttonGroup.checkedId()
        print(button_id)
        if button_id == 1:
            bubble_sort.bubble.bubbleSort(self, self.arr)
        if button_id == 2:
            pass
        if button_id == 3:
            pass
        if button_id == 4:
            pass


    def getLabel(self, i, flag):
        if flag is False:
            label = QGraphicsTextItem(str(i))
            label.setHtml("<div style='background:#00ff00;'>" + str(i) + "</div>");
        else:
            label = QGraphicsTextItem(str(i))
            label.setHtml("<div style='background:#ff0000;'>" + str(i) + "</div>");

        return label

    def setNext(self):
        self.next_step = True

    def anim_store(self, sort_list, swaplist):
        block = 0
        i = 1
        list_length = len(sort_list)
        print("list length is ", list_length)
        while(i < list_length):
            QApplication.processEvents()
            print("Swap or not", swaplist[i][2])

            if swaplist[i][2] == 1:
                swap_larger = swaplist[i][0]
                swap_smaller = swaplist[i][1]
                print("Swap elements")

                self.resketch(sort_list[i], swap_larger, swap_smaller)
            else:
                self.sketch(sort_list[i])
                print("Dont swap")
                time.sleep(2)
            i = i + 1
        self.sketch(sort_list[list_length-1])

    def resketch(self, arr, swap_larger, swap_smaller):
        self.scene.clear()

        forward = 100
        for i in range(0, len(arr)):
                if i == swap_larger or i == swap_smaller:
                    label = self.getLabel(arr[i], True)
                    print("RAN")
                else:
                    label = self.getLabel(arr[i], False)
                self.scene.addItem(label)
                pos_point = QtCore.QPoint(forward, 160)
                label.setPos(pos_point)
                forward = forward + 70

# 2,1,7,5,3
