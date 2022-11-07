# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'djikstra.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys

import networkx as nx
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib import pyplot as plt
#from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvas

class Ui_Dijsktra(object):
    def setupUi(self, Dijsktra):
        Dijsktra.setObjectName("Dijsktra")
        Dijsktra.resize(1295, 777)
        self.centralwidget = QtWidgets.QWidget(Dijsktra)
        self.centralwidget.setObjectName("centralwidget")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(661, 480, 41, 191))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(800, 490, 31, 21))
        self.label_8.setObjectName("label_8")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 670, 951, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(350, 600, 71, 20))
        self.label_11.setObjectName("label_11")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(140, 490, 461, 91))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit_3")
        self.src = QtWidgets.QTextEdit(self.centralwidget)
        self.src.setGeometry(QtCore.QRect(760, 510, 104, 31))
        self.src.setObjectName("src")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(690, 560, 75, 31))
        self.pushButton.setObjectName("pushButton")
        self.hamil = QtWidgets.QPushButton(self.centralwidget)
        self.hamil.setGeometry(QtCore.QRect(690, 620, 111, 31))
        self.hamil.setObjectName("hamil")
        self.run_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_button.setGeometry(QtCore.QRect(850, 560, 75, 31))
        self.run_button.setObjectName("run_button")
        self.newnode_text = QtWidgets.QTextEdit(self.centralwidget)
        self.newnode_text.setGeometry(QtCore.QRect(1107, 100, 71, 41))
        self.newnode_text.setObjectName("newnode_text")
        self.remove_edge = QtWidgets.QPushButton(self.centralwidget)
        self.remove_edge.setGeometry(QtCore.QRect(1170, 360, 81, 31))
        self.remove_edge.setObjectName("remove_edge")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1101, 230, 121, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1031, 280, 71, 19))
        self.label_4.setObjectName("label_4")
        self.node2_text = QtWidgets.QTextEdit(self.centralwidget)
        self.node2_text.setGeometry(QtCore.QRect(1121, 300, 71, 41))
        self.node2_text.setObjectName("node2_text")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(420, 10, 51, 19))
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1120, 40, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1211, 280, 79, 19))
        self.label_6.setObjectName("label_6")
        self.graph_view = QtWidgets.QGraphicsView(self.centralwidget)
        self.graph_view.setGeometry(QtCore.QRect(20, 30, 791, 431))
        self.graph_view.setObjectName("graph_view")
        self.weight_text = QtWidgets.QTextEdit(self.centralwidget)
        self.weight_text.setGeometry(QtCore.QRect(1211, 300, 71, 41))
        self.weight_text.setObjectName("weight_text")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1121, 280, 71, 19))
        self.label_5.setObjectName("label_5")
        self.addnode_button = QtWidgets.QPushButton(self.centralwidget)
        self.addnode_button.setGeometry(QtCore.QRect(1066, 150, 81, 31))
        self.addnode_button.setObjectName("addnode_button")
        self.node1_text = QtWidgets.QTextEdit(self.centralwidget)
        self.node1_text.setGeometry(QtCore.QRect(1031, 300, 71, 41))
        self.node1_text.setObjectName("node1_text")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1170, 150, 81, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.resetgraph_button = QtWidgets.QPushButton(self.centralwidget)
        self.resetgraph_button.setGeometry(QtCore.QRect(1090, 420, 111, 41))
        self.resetgraph_button.setObjectName("resetgraph_button")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(940, 20, 41, 651))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.connect_button = QtWidgets.QPushButton(self.centralwidget)
        self.connect_button.setGeometry(QtCore.QRect(1040, 360, 100, 27))
        self.connect_button.setObjectName("connect_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1110, 80, 101, 20))
        self.label.setObjectName("label")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(20, 470, 941, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.travelsales = QtWidgets.QPushButton(self.centralwidget)
        self.travelsales.setGeometry(QtCore.QRect(820, 620, 121, 31))
        self.travelsales.setObjectName("travelsales")
        Dijsktra.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Dijsktra)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1295, 21))
        self.menubar.setObjectName("menubar")
        Dijsktra.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Dijsktra)
        self.statusbar.setObjectName("statusbar")
        Dijsktra.setStatusBar(self.statusbar)



        self.error_dialog = QtWidgets.QErrorMessage()

        self.plot_canvas = PlotCanvas(self.centralwidget)
        self.plot_canvas.setGeometry(QtCore.QRect(20, 30, 891, 431))
        self.plot_canvas.setObjectName("plot_canvas")

        self.retranslateUi(Dijsktra)
        QtCore.QMetaObject.connectSlotsByName(Dijsktra)

    def retranslateUi(self, Dijsktra):
        _translate = QtCore.QCoreApplication.translate
        Dijsktra.setWindowTitle(_translate("Dijsktra", "Dijkstra"))
        self.addnode_button.setText(_translate("Dijsktra", "Add Node"))
        self.newnode_text.setHtml(_translate("Dijsktra",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("Dijsktra", "Node Name"))
        self.label_2.setText(_translate("Dijsktra", "New Node"))
        self.label_3.setText(_translate("Dijsktra", "Connect Nodes"))
        self.label_4.setText(_translate("Dijsktra", "Node 1"))
        self.label_5.setText(_translate("Dijsktra", "Node 2"))
        self.label_6.setText(_translate("Dijsktra", "Weight"))
        self.label_7.setText(_translate("Dijsktra", "Graph"))
        self.label_8.setText(_translate("Dijsktra", "Run"))

        self.run_button.setText(_translate("Dijsktra", "DFS"))
        self.label_11.setText(_translate("Dijsktra", "Information"))
        self.connect_button.setText(_translate("Dijsktra", "Connect"))
        self.resetgraph_button.setText(_translate("Dijsktra", "Reset Graph"))
        self.pushButton.setText(_translate("Dijsktra", "BFS"))

        self.hamil.setText(_translate("Dijsktra", "Hamiltonian Cycle"))
        self.travelsales.setText(_translate("Dijsktra", "Travelling Salesperson"))
        self.remove_edge.setText(_translate("Dijsktra", "Disconnect"))
        self.pushButton_3.setText(_translate("Dijsktra", "Remove Node"))


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
    main = Ui_Dijsktra()
    main.setupUi(ui)
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()