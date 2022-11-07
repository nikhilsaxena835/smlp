# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graph.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
import networkx as nx
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib import pyplot as plt
#from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvas

class Ui_Basic(object):
    def setupUi(self, Basic):
        Basic.setObjectName("Basic")
        Basic.resize(1298, 776)
        self.centralwidget = QtWidgets.QWidget(Basic)
        self.centralwidget.setObjectName("centralwidget")
        self.node1_text = QtWidgets.QTextEdit(self.centralwidget)
        self.node1_text.setGeometry(QtCore.QRect(1031, 290, 71, 41))
        self.node1_text.setObjectName("node1_text")
        self.node2_text = QtWidgets.QTextEdit(self.centralwidget)
        self.node2_text.setGeometry(QtCore.QRect(1121, 290, 71, 41))
        self.node2_text.setObjectName("node2_text")
        self.addnode_button = QtWidgets.QPushButton(self.centralwidget)
        self.addnode_button.setGeometry(QtCore.QRect(1066, 140, 81, 31))
        self.addnode_button.setObjectName("addnode_button")
        self.newnode_text = QtWidgets.QTextEdit(self.centralwidget)
        self.newnode_text.setGeometry(QtCore.QRect(1107, 90, 71, 41))
        self.newnode_text.setObjectName("newnode_text")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1110, 70, 101, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1120, 30, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1101, 220, 121, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1031, 270, 71, 19))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1121, 270, 71, 19))
        self.label_5.setObjectName("label_5")
        self.weight_text = QtWidgets.QTextEdit(self.centralwidget)
        self.weight_text.setGeometry(QtCore.QRect(1211, 290, 71, 41))
        self.weight_text.setObjectName("weight_text")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1211, 270, 79, 19))
        self.label_6.setObjectName("label_6")
        self.graph_view = QtWidgets.QGraphicsView(self.centralwidget)
        self.graph_view.setGeometry(QtCore.QRect(20, 20, 891, 431))
        self.graph_view.setObjectName("graph_view")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(420, 0, 51, 19))
        self.label_7.setObjectName("label_7")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(940, 10, 41, 461))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 470, 41, 211))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(111, 480, 31, 21))
        self.label_8.setObjectName("label_8")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(20, 460, 1271, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(21, 680, 1271, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(600, 560, 71, 20))
        self.label_11.setObjectName("label_11")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(410, 580, 461, 91))
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName("textEdit_3")
        self.connect_button = QtWidgets.QPushButton(self.centralwidget)
        self.connect_button.setGeometry(QtCore.QRect(1040, 350, 100, 27))
        self.connect_button.setObjectName("connect_button")
        self.resetgraph_button = QtWidgets.QPushButton(self.centralwidget)
        self.resetgraph_button.setGeometry(QtCore.QRect(1090, 410, 111, 41))
        self.resetgraph_button.setObjectName("resetgraph_button")
        self.remove_edge = QtWidgets.QPushButton(self.centralwidget)
        self.remove_edge.setGeometry(QtCore.QRect(1170, 350, 81, 31))
        self.remove_edge.setObjectName("remove_edge")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1170, 140, 81, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 510, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 510, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(670, 510, 171, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1030, 510, 75, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(130, 510, 91, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(440, 510, 111, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(850, 510, 75, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(1120, 510, 75, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(230, 510, 81, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(560, 510, 91, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(940, 510, 75, 31))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(1210, 510, 75, 31))
        self.pushButton_15.setObjectName("pushButton_15")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(1270, 470, 41, 211))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        Basic.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Basic)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1298, 21))
        self.menubar.setObjectName("menubar")
        Basic.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Basic)
        self.statusbar.setObjectName("statusbar")
        Basic.setStatusBar(self.statusbar)



        self.plot_canvas = PlotCanvas(self.centralwidget)
        self.plot_canvas.setGeometry(QtCore.QRect(190, 30, 891, 431))
        self.plot_canvas.setObjectName("plot_canvas")



        self.retranslateUi(Basic)
        QtCore.QMetaObject.connectSlotsByName(Basic)

    def retranslateUi(self, Basic):
        _translate = QtCore.QCoreApplication.translate
        Basic.setWindowTitle(_translate("Basic", "MainWindow"))
        self.addnode_button.setText(_translate("Basic", "Add Node"))
        self.newnode_text.setHtml(_translate("Basic", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'DejaVu Sans\'; font-size:12pt;\"><br /></p></body></html>"))
        self.label.setText(_translate("Basic", "Node Name"))
        self.label_2.setText(_translate("Basic", "New Node"))
        self.label_3.setText(_translate("Basic", "Connect Nodes"))
        self.label_4.setText(_translate("Basic", "Node 1"))
        self.label_5.setText(_translate("Basic", "Node 2"))
        self.label_6.setText(_translate("Basic", "Weight"))
        self.label_7.setText(_translate("Basic", "Graph"))
        self.label_8.setText(_translate("Basic", "Run"))
        self.label_11.setText(_translate("Basic", "Information"))
        self.connect_button.setText(_translate("Basic", "Connect"))
        self.resetgraph_button.setText(_translate("Basic", "Reset Graph"))
        self.remove_edge.setText(_translate("Basic", "Disconnect"))
        self.pushButton_3.setText(_translate("Basic", "Remove Node"))
        self.pushButton.setText(_translate("Basic", "Complement"))
        self.pushButton_2.setText(_translate("Basic", "Node Connectivity"))
        self.pushButton_4.setText(_translate("Basic", "Minimal Maximal Matching"))
        self.pushButton_5.setText(_translate("Basic", "Vertex Cover"))
        self.pushButton_6.setText(_translate("Basic", "K- Components"))
        self.pushButton_7.setText(_translate("Basic", "Independent Set"))
        self.pushButton_8.setText(_translate("Basic", "Max Clique"))
        self.pushButton_9.setText(_translate("Basic", "Diameter"))
        self.pushButton_10.setText(_translate("Basic", "IsBipartite"))
        self.pushButton_11.setText(_translate("Basic", "Coloring"))
        self.pushButton_12.setText(_translate("Basic", "Strongly Connected"))
        self.pushButton_13.setText(_translate("Basic", "Weakly Connected"))
        self.pushButton_14.setText(_translate("Basic", "Is Eularian"))
        self.pushButton_15.setText(_translate("Basic", "Planarity"))

class PlotCanvas(FigureCanvas):  # By inheriting the FigureCanvas class, this class is both a PyQt5 Qwidget and a Matplotlib FigureCanvas, which is the key to connecting pyqt5 and matplotlib
    """A UI element to plotting networkx graph on window.
    """

    def __init__(self, parent=None):
        """Constructor of PlotCanvas class.

        Args:
            parent (optional): Parent should be Qt widget. Defaults to None.
        """
        FigureCanvas.__init__(self)
        self.setParent(parent)
        self.figure = plt.figure()
        FigureCanvas.updateGeometry(self)

    def plot(self, G):
        """Plotting all nodes and edges of graph with labels.

        Args:
            G (nx.Graph): Graph.
        """
        self.figure.clf()
        pos = nx.spring_layout(G, seed=42)

        # Drawing graph on canvas in UI.
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        nx.draw(G, pos, with_labels=True, font_size=11, node_size=150, node_color="r", font_color="w")
        self.draw_idle()

def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = QtWidgets.QMainWindow()
    main = Ui_Basic()
    main.setupUi(ui)
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()