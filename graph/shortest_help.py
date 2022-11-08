import networkx.algorithms.operators
from PyQt5 import QtWidgets
import sys
import networkx as nx
from graph.shortest import Ui_Shortest
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
        print("Constr")
        super(GUI, self).__init__()
        self.setup_gui()

    def setup_gui(self):
        """Initializer of GUI.
        """

        self.form = Ui_Shortest()
        self.form.setupUi(self)
        self.G = nx.Graph()

        # Controllers
        self.form.addnode_button.clicked.connect(self.add_new_node)
        self.form.connect_button.clicked.connect(self.connect_nodes)

        self.form.resetgraph_button.clicked.connect(self.reset)

        self.form.pushButton_3.clicked.connect(self.remove_node)
        self.form.remove_edge.clicked.connect(self.disconnect_nodes)


        self.form.pushButton.clicked.connect(self.dijkstra)
        self.form.pushButton_2.clicked.connect(self.bellford)

        self.form.pushButton_4.clicked.connect(self.floyd)



    def show_dialog(self, message):
        """Opening a new error window with a given error message.
        Args:
            message (string): error text.
        """
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    def add_new_node(self):
        """ Adding a new node to the Graph.
        """

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




    def dijkstra(self):
        node1 = str(self.form.src.toPlainText())
        node2 = str(self.form.dest.toPlainText())
        ans = networkx.algorithms.shortest_paths.dijkstra_path(self.G, node1, node2)
        self.form.textEdit_3.setText(str(ans))

    def bellford(self):
        node1 = str(self.form.src.toPlainText())
        node2 = str(self.form.dest.toPlainText())
        ans = networkx.bellman_ford_path(self.G, node1, node2)
        self.form.textEdit_3.setText(str(ans))


    def floyd(self):

        ans = networkx.algorithms.shortest_paths.floyd_warshall(self.G)
        print(ans)
        self.form.textEdit_3.setText(str(ans))

"""mainloop = QtWidgets.QApplication([])
run_app = GUI()
run_app.show()
sys.exit(mainloop.exec_())"""