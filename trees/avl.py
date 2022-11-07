import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QGraphicsScene, QApplication
from trees import avl_tree


# exception handling for insertion and deletion when no input is given in the text field.

'''
node_map stores the labels in a key value pair. nodes is a list of nodes that is ordered. This helps to recreate the 
binary tree everytime sketch is called. line_map stores the lines in a key value pair. During deletion we also want 
to remove lines. This dictionary helps there.
'''


class Ui_MainWindow(object):
    root = None
    rightend = 0
    h = 0
    realtree = avl_tree.AVLTree()
    firsts = 0
    count = 0

    def setupUi(self, MainWindow):
        '''
        Nodes are drawn on the QGraphicsScene which is contained in the QGraphicsView container.
        The window associated with this view is central widget that is the main window of the program.
        Retranslate is used to rename the GUI elements currently. It will be removed later.
        setSceneRect is not used and should be left commented for future.
        '''

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1240, 900)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.scene = QGraphicsScene()
        #self.scene.setSceneRect(40,60,851,561)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(40, 60, 851, 561))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setScene(self.scene)
        self.graphicsView.show()

        self.ins_button = QtWidgets.QPushButton(self.centralwidget)
        self.ins_button.setGeometry(QtCore.QRect(1120, 140, 75, 31))
        self.ins_button.setObjectName("ins_button")

        self.ins_button.clicked.connect(self.insert_clicked)

        self.ins_tf = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ins_tf.setGeometry(QtCore.QRect(990, 140, 104, 31))
        self.ins_tf.setObjectName("ins_tf")
        self.del_tf = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.del_tf.setGeometry(QtCore.QRect(990, 200, 104, 31))
        self.del_tf.setObjectName("del_tf")
        self.del_button = QtWidgets.QPushButton(self.centralwidget)
        self.del_button.setGeometry(QtCore.QRect(1120, 200, 75, 31))
        self.del_button.setObjectName("del_button")




        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(1120, 260, 75, 31))
        self.search_button.setObjectName("search_button")
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(890, 560, 101, 16))
        self.output_label.setObjectName("output_label")
        self.search_tf = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.search_tf.setGeometry(QtCore.QRect(990, 260, 104, 31))
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
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(930, 520, 281, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
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
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(920, 320, 16, 211))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(1200, 310, 20, 221))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.operations_label = QtWidgets.QLabel(self.centralwidget)
        self.operations_label.setGeometry(QtCore.QRect(950, 110, 81, 16))
        self.operations_label.setObjectName("operations_label")
        self.output_tf = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.output_tf.setGeometry(QtCore.QRect(990, 550, 221, 31))
        self.output_tf.setObjectName("output_tf")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(140, 590, 711, 91))
        self.textEdit.setObjectName("textEdit")
        self.info_label = QtWidgets.QLabel(self.centralwidget)
        self.info_label.setGeometry(QtCore.QRect(30, 560, 81, 16))
        self.info_label.setObjectName("info_label")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.back.setObjectName("back")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(140, 10, 75, 23))
        self.reset.setObjectName("reset")
        self.buttonGroup = QtWidgets.QButtonGroup(self.centralwidget)
        self.buttonGroup.setObjectName("groupBox")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(940, 330, 251, 191))
        self.groupBox.setObjectName("groupBox")

        self.level = QtWidgets.QRadioButton(self.groupBox)
        self.level.setGeometry(QtCore.QRect(60, 140, 131, 17))
        self.level.setObjectName("level")
        self.preorder = QtWidgets.QRadioButton(self.groupBox)
        self.preorder.setGeometry(QtCore.QRect(60, 80, 131, 17))
        self.preorder.setObjectName("preorder")
        self.post = QtWidgets.QRadioButton(self.groupBox)
        self.post.setGeometry(QtCore.QRect(60, 110, 121, 17))
        self.post.setObjectName("post")
        self.inorder = QtWidgets.QRadioButton(self.groupBox)
        self.inorder.setGeometry(QtCore.QRect(60, 50, 121, 17))
        self.inorder.setObjectName("inorder")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1240, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.buttonGroup.addButton(self.preorder, 1)
        self.buttonGroup.addButton(self.post, 2)
        self.buttonGroup.addButton(self.inorder, 3)
        self.buttonGroup.addButton(self.level, 4)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AVL Tree"))
        self.ins_button.setText(_translate("MainWindow", "Insert Node"))
        self.del_button.setText(_translate("MainWindow", "Delete Node"))
        self.search_button.setText(_translate("MainWindow", "Search Node"))
        self.output_label.setText(_translate("MainWindow", "Output Sequence :"))
        self.operations_label.setText(_translate("MainWindow", "Operations"))
        self.info_label.setText(_translate("MainWindow", "Operation Info:"))
        self.back.setText(_translate("MainWindow", "Back"))
        self.reset.setText(_translate("MainWindow", "Reset All"))
        self.groupBox.setTitle(_translate("MainWindow", "Mode for Search operation"))
        self.level.setText(_translate("MainWindow", "Level Order Traversal"))
        self.preorder.setText(_translate("MainWindow", "Pre-order Traversal"))
        self.post.setText(_translate("MainWindow", "Post-order Traversal"))
        self.inorder.setText(_translate("MainWindow", "Inorder Traversal"))

    def insert_clicked(self):
        inp = self.ins_tf.toPlainText()
        inp = int(inp)
        self.ins_tf.setPlainText("")

        self.root = self.realtree.insert_node(self.root, inp)
        self.h = 0
        self.count = 0
        self.scene.clear()
        self.sketch(self.root, 2, 0, 0)


    def createLabel(self, key, color):
        label = QtWidgets.QLabel(key)
        label.setGeometry(QtCore.QRect(320, 220, 31, 31))
        if(color == "green"):
            label.setStyleSheet("border: 3px solid blue; border-radius: 10px;background-color: rgb(37, 255, 37)")
        else:
            label.setStyleSheet("border: 3px solid blue; border-radius: 10px;background-color: red")
        return label

    def sketch(self, root, l, x, y):

        print(root.key)
        label = self.createLabel(str(root.key), "green")
        point = self.scene.addWidget(label)


        if l == 2:
            print("I run once")
            x = point.pos().x()
            y = point.pos().y()
            print(x,y)

        if l == 1:
            print("This is l")
            print(x, y)
            point.setPos(x - 40, y + 40)
            self.scene.addLine(x, y, x - 40, y + 40)
            print("Inserting", root.key)
            x = point.pos().x()
            y = point.pos().y()
            print(x, y)

        if l == 0:
            print("This is r")
            point.setPos(x + 40, y + 40)
            self.scene.addLine(x, y, x + 40, y + 40)
            print("Inserting", root.key)
            x = point.pos().x()
            y = point.pos().y()

        if root.left:
            print("This is lr")
            self.sketch(root.left, 1, x, y)

        if root.right:
            print("This is rr")
            self.sketch(root.right, 0, x, y)

def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = QtWidgets.QMainWindow()
    main = Ui_MainWindow()
    main.setupUi(ui)
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
'''

'''