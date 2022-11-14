import sys
import time

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QGraphicsScene, QApplication
from trees import tree

'''
node_map stores the labels in a key value pair. nodes is a list of nodes that is ordered. This helps to recreate the binary tree everytime sketch is called.
line_map stores the lines in a key value pair. During deletion we also want to remove lines. This dictionary helps there
'''
class Ui_MainWindow(object):
    row = 0
    col = 0
    first = 0
    node_map = {}
    nodes = []
    line_map = {}
    realtree = tree.Tree()
    root = None
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

        self.ins_button.clicked.connect(self.check_discrepancy)

        self.ins_tf = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ins_tf.setGeometry(QtCore.QRect(990, 140, 104, 31))
        self.ins_tf.setObjectName("ins_tf")
        self.del_tf = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.del_tf.setGeometry(QtCore.QRect(990, 200, 104, 31))
        self.del_tf.setObjectName("del_tf")
        self.del_button = QtWidgets.QPushButton(self.centralwidget)
        self.del_button.setGeometry(QtCore.QRect(1120, 200, 75, 31))
        self.del_button.setObjectName("del_button")

        self.del_button.clicked.connect(self.check_discrepancy2)

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
        self.textEdit.setGeometry(QtCore.QRect(140, 620, 711, 91))
        self.textEdit.setObjectName("textEdit")
        self.info_label = QtWidgets.QLabel(self.centralwidget)
        self.info_label.setGeometry(QtCore.QRect(30, 620, 81, 16))
        self.info_label.setObjectName("info_label")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.back.setObjectName("back")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(140, 10, 75, 23))
        self.reset.setObjectName("reset")
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
        self.buttonGroup = QtWidgets.QButtonGroup(self.centralwidget)
        self.buttonGroup.setObjectName("groupBox")

        self.buttonGroup.addButton(self.preorder, 1)
        self.buttonGroup.addButton(self.post, 2)
        self.buttonGroup.addButton(self.inorder, 3)
        self.buttonGroup.addButton(self.level, 4)
        self.buttonGroup.buttonClicked.connect(self.traverse_out)

        self.textEdit.setText("Binary Search Tree is a node-based binary tree data structure which has the following "
                              "properties:The left subtree of a node contains only nodes with keys lesser than "
                              "the node’s key. The right subtree of a node contains only nodes with keys greater than "
                              "the node’s key. The left and right subtree each must also be a binary search tree.")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Binary Search Tree"))
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

        self.nodes.append(inp)

        self.textEdit.setText("Inserting a value in the correct position is similar to searching because we try to "
                              "maintain the rule that the left subtree is lesser than root and the right subtree is "
                              "larger than root.We keep going to either right subtree or left subtree depending on "
                              "the value and when we reach a point left or right subtree is null, "
                              "we put the new node there.")

        if(self.first == 0):
            self.first = self.first+1
            #self.realtree = tree.Tree()
            self.root = self.realtree.createNode(inp)
            self.sketch()
        else:
            self.root = self.realtree.insert(self.root, inp)
            self.sketch()

    def del_clicked(self):
        inp = self.del_tf.toPlainText()
        inp = int(inp)
        self.del_tf.setPlainText("")

        self.root = self.realtree.delete_Node(self.root, inp)
        print("nodes before ", self.nodes)
        self.nodes.remove(inp)
        print("nodes after ", self.nodes)
        self.textEdit.setText("In a binary search tree, we must delete a node from the tree by keeping in mind that the "
                              "property of BST is not violated. To delete a node from BST, there are three possible "
                              "situations occur -The node to be deleted is the leaf node, or, "
                              "The node to be deleted has only one child, and, "
                              "The node to be deleted has two children")

        self.sketch()

    def sketch(self, mark=None, color=0):
        firsts = 0
        self.scene.clear()
        print("The list is ", self.nodes)

        for key in self.nodes:
            print("key inserting now is ", key)
            label = QtWidgets.QLabel(str(key))
            if color == 0 or mark != key:
                label = self.createLabel(str(key), "green")
            elif (color == 1) and (mark == key):
                label = self.createLabel(str(key), "red")

            if (firsts == 0):
                point = self.scene.addWidget(label)
                self.node_map[key] = point
                point.setPos(0, 0)
                firsts = 1
            else:
                parent = self.getParent(key)
                print(parent)
                parentlabel = self.node_map[parent]
                x = parentlabel.x()
                y = parentlabel.y()

                point = self.scene.addWidget(label)
                self.node_map[key] = point
                if (parent > key):
                    point.setPos(x - 40, y + 50)
                else:
                    point.setPos(x + 40, y + 50)

                self.addLinetoNodes(x, y, point, key)

    def getParent(self, target):
        parent, node = None, self.root
        while True:
            print(target, node.data)
            if node is None:
                print("Node is none no parent")
                return None

            if node.data == target:
                print("Node found")
                return parent.data

            if target < node.data:
                print("Key less than node.data")
                parent, node = node, node.left
            else:
                print("Key more than node.data")
                parent, node = node, node.right

    def addLinetoNodes(self,x1, y1, point, key):
        x2 = point.x()
        y2 = point.y()
        line = QtWidgets.QGraphicsLineItem(x1, y1, x2, y2)
        self.line_map[key] = line
        self.scene.addItem(line)

    def check_discrepancy(self):
        inp = self.ins_tf.toPlainText()
        if inp.isnumeric() == True:
            self.insert_clicked()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Error")
            message = "Please enter a numeric value only"
            msg.setInformativeText(message)
            msg.setWindowTitle("Error")
            msg.exec_()
            return

    def check_discrepancy2(self):
        inp2 = self.del_tf.toPlainText()
        if inp2.isnumeric() == True:
            self.del_clicked()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Error")
            message = "Please enter a numeric value only"
            msg.setInformativeText(message)
            msg.setWindowTitle("Error")
            msg.exec_()
            return

    def createLabel(self, key, color):
        label = QtWidgets.QLabel(key)
        label.setGeometry(QtCore.QRect(320, 220, 31, 31))
        if(color == "green"):
            label.setStyleSheet("border: 3px solid blue; border-radius: 10px;background-color: rgb(37, 255, 37)")
        else:
            label.setStyleSheet("border: 3px solid blue; border-radius: 10px;background-color: red")
        return label


    def traverse_out(self):
        button_id = self.buttonGroup.checkedId()
        print(button_id)
        self.output_tf.setPlainText("")
        if button_id == 1:
            path = self.realtree.traversePreorder(self.root)
            for key in path:
                self.output_seq(key)
                self.anim_traverse(key)
                QApplication.processEvents()
                time.sleep(1)
            path.clear()

        if button_id == 2:
            path = self.realtree.traversePostorder(self.root)
            for key in path:
                self.output_seq(key)
                self.anim_traverse(key)
                QApplication.processEvents()
                time.sleep(1)
            path.clear()

        if button_id == 3:
            path = self.realtree.traverseInorder(self.root)
            for key in path:
                self.output_seq(key)
                self.anim_traverse(key)
                QApplication.processEvents()
                time.sleep(1)
            path.clear()

        if button_id == 4:
            path = self.realtree.levelOrderTraversal(self.root)
            for key in path:
                self.output_seq(key)
                self.anim_traverse(key)
                QApplication.processEvents()
                time.sleep(1)
            path.clear()


    def anim_traverse(self, key):
        self.sketch(key, color=1)

    def output_seq(self, key):
        prev = self.output_tf.toPlainText()
        string = prev + str(key) + "->"
        self.output_tf.appendPlainText(string)

def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = QtWidgets.QMainWindow()
    main = Ui_MainWindow()
    main.setupUi(ui)
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
