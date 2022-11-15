import networkx.algorithms.operators
from PyQt5 import QtWidgets
import sys
import networkx as nx
from graph.baseg import Ui_Basic
from sys import maxsize
from itertools import permutations
from networkx.algorithms import approximation

class GUI(QtWidgets.QMainWindow):
    """Main GUI class to handle UI and controller functions.
    Args:
        QtWidgets.QMainWindow()
    """

    def __init__(self):
        """Constructor of GUI.
        """
        super(GUI, self).__init__()
        self.setup_gui()

    def setup_gui(self):
        """Initializer of GUI.
        """

        self.form = Ui_Basic()
        self.form.setupUi(self)
        self.G = nx.Graph()

        # Controllers
        self.form.addnode_button.clicked.connect(self.add_new_node)
        self.form.connect_button.clicked.connect(self.connect_nodes)

        self.form.resetgraph_button.clicked.connect(self.reset)

        self.form.pushButton_3.clicked.connect(self.remove_node)
        self.form.remove_edge.clicked.connect(self.disconnect_nodes)

        self.form.pushButton.clicked.connect(self.complement)
        self.form.pushButton_2.clicked.connect(self.nodeconnectivity)
        self.form.pushButton_15.clicked.connect(self.planarity)
        self.form.pushButton_4.clicked.connect(self.minmaxmatching)
        self.form.pushButton_5.clicked.connect(self.vertexcover)
        self.form.pushButton_6.clicked.connect(self.kcomplement)
        self.form.pushButton_7.clicked.connect(self.ind_set)
        self.form.pushButton_8.clicked.connect(self.maxclique)
        self.form.pushButton_9.clicked.connect(self.diameter)
        self.form.pushButton_10.clicked.connect(self.isbipartite)
        self.form.pushButton_11.clicked.connect(self.coloring)
        self.form.pushButton_14.clicked.connect(self.iseularian)


    def show_dialog(self, message):

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    def add_new_node(self):
        print("Add new")
        new_node = str(self.form.newnode_text.toPlainText())
        if not new_node:
            self.form.newnode_text.clear()
            self.show_dialog("Empty argument.")
            return

        self.form.newnode_text.clear()

        if self.G.has_node(new_node):
            self.show_dialog(f"{new_node} is already constructed.")

        else:
            self.G.add_node(new_node)
            self.form.plot_canvas.plot(self.G)

    def connect_nodes(self):

        node1 = str(self.form.node1_text.toPlainText())
        node2 = str(self.form.node2_text.toPlainText())
        weight = str(self.form.weight_text.toPlainText())
        self.form.node1_text.clear()
        self.form.node2_text.clear()
        self.form.weight_text.clear()

        if not node1 or not node2 or not weight:
            self.show_dialog("Empty argument.")
            return

        try:
            weight = int(weight)
        except:
            self.show_dialog("Weight should be an integer.")
            return

        if self.G.has_edge(node1, node2):
            self.show_dialog(f"Edge: {node1, node2} is already constructed.")

        else:
            self.G.add_edge(node1, node2, weight=weight)
            self.form.plot_canvas.plot(self.G)

    def reset(self):
        """Resets the existing graph.
        """
        self.G = nx.Graph()
        self.form.plot_canvas.plot(self.G)

    def remove_node(self):
        new_node = str(self.form.newnode_text.toPlainText())
        if not new_node:
            self.form.newnode_text.clear()
            self.show_dialog("Empty argument.")
            return

        self.form.newnode_text.clear()

        if self.G.has_node(new_node):
            self.G.remove_node(new_node)
            self.form.plot_canvas.plot(self.G)


        else:
            self.show_dialog(f"{new_node} is doeesn't exist.")

    def disconnect_nodes(self):
        """Connects two nodes with a given weight.
                """
        node1 = str(self.form.node1_text.toPlainText())
        node2 = str(self.form.node2_text.toPlainText())
        weight = str(self.form.weight_text.toPlainText())
        self.form.node1_text.clear()
        self.form.node2_text.clear()
        self.form.weight_text.clear()

        if not node1 or not node2 or not weight:
            self.show_dialog("Empty argument.")
            return

        try:
            weight = int(weight)
        except:
            self.show_dialog("Weight should be an integer.")
            return

        if self.G.has_edge(node1, node2):
            self.G.remove_edge(node1,node2)
            self.form.plot_canvas.plot(self.G)

        else:
            self.show_dialog(f"Edge: {node1, node2} doesn't exist.")




    def nodeconnectivity(self):
        r = approximation.node_connectivity(self.G)
        print(r)
        s = "The node connectivity is : " + str(r)
        self.form.textEdit_3.setText(s)


    def complement(self):
        self.G = networkx.algorithms.operators.complement(self.G)
        self.form.plot_canvas.plot(self.G)

    def planarity(self):
        ans, dump = nx.check_planarity(self.G, False)
        s = "The graph is "
        if ans is True:
            s = s + "Planar"
        else:

            s = s + "Not Planar"
        self.form.textEdit_3.setText(s)

    def minmaxmatching(self):
        ans = networkx.algorithms.approximation.min_maximal_matching(self.G)
        self.form.textEdit_3.setText(str(ans))

    def vertexcover(self):
        ans = networkx.algorithms.approximation.min_weighted_vertex_cover(self.G)
        x = ""
        for i in ans:
            x = x + " " + i
        s = "The vertex cover set is : " + x
        self.form.textEdit_3.setText(s)

    def kcomplement(self):
        ans = networkx.algorithms.connectivity.k_components(self.G)
        self.form.textEdit_3.setText(str(ans))

    def ind_set(self):
        ans = networkx.algorithms.approximation.maximum_independent_set(self.G)
        self.form.textEdit_3.setText(str(ans))

    def maxclique(self):
        ans = networkx.algorithms.approximation.max_clique(self.G)
        self.form.textEdit_3.setText(str(ans))

    def diameter(self):
        ans = networkx.algorithms.diameter(self.G)
        self.form.textEdit_3.setText(str(ans))

    def coloring(self):
        ans = networkx.algorithms.coloring.greedy_color(self.G, strategy="largest_first")
        self.form.textEdit_3.setText(str(ans))

    def isbipartite(self):
        ans = networkx.algorithms.is_bipartite(self.G)
        self.form.textEdit_3.setText(str(ans))

    def iseularian(self):
        ans = networkx.algorithms.is_eulerian(self.G)
        self.form.textEdit_3.setText(str(ans))




"""mainloop = QtWidgets.QApplication([])
run_app = GUI()
run_app.show()
sys.exit(mainloop.exec_())"""