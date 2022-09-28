from PyQt5 import QtWidgets
import sys
import networkx as nx
from graph_ui import Ui_Dijsktra


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

        self.form = Ui_Dijsktra()
        self.form.setupUi(self)
        self.G = nx.Graph()

        # Controllers
        self.form.addnode_button.clicked.connect(self.add_new_node)
        self.form.connect_button.clicked.connect(self.connect_nodes)
        self.form.run_button.clicked.connect(self.BFS)
        self.form.resetgraph_button.clicked.connect(self.reset)
        self.form.pushButton.clicked.connect(self.DFS)

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

    def BFS(self):
        """Takes source and destination from user and runs the Dijkstra algorithm to calculate shortest path.
        """

        node = str(self.form.source_text.toPlainText())

        result = 'The BFS traversal is '
        self.form.source_text.clear()

        visited = []  # List for visited nodes.
        queue = []
        if not node:
            self.show_dialog("Empty argument.")
            return

        graph = nx.convert.to_dict_of_lists(self.G)

        visited.append(node)
        queue.append(node)
        print(graph)
        print(type(graph))

        while queue:  # Creating loop to visit each node
            m = queue.pop(0)

            result = result + " - >" + m

            for neighbour in graph[m]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)


        self.form.result_text.setText(result)


    def DFS(self):
        start = self.form.source_text.toPlainText()
        self.form.source_text.clear()
        result = 'The DFS traversal is '
        graph = nx.convert.to_dict_of_lists(self.G)

        stack, path = [start], []

        while stack:
            vertex = stack.pop()
            if vertex in path:
                continue
            path.append(vertex)
            result = result + "->" + vertex
            for neighbor in graph[vertex]:
                stack.append(neighbor)
        self.form.result_text.setText(result)
        return path



    def reset(self):
        """Resets the existing graph.
        """
        self.G = nx.Graph()
        self.form.plot_canvas.plot(self.G)


mainloop = QtWidgets.QApplication([])
run_app = GUI()
run_app.show()
sys.exit(mainloop.exec_())

