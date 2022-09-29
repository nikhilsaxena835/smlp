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
        self.form.pushButton_3.clicked.connect(self.remove_node)
        self.form.remove_edge.clicked.connect(self.disconnect_nodes)
        self.form.floyd.clicked.connect(self.floyd_warshall)
        self.form.hamil.clicked.connect(self.hamCycle)

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

        node = str(self.form.textEdit.toPlainText())

        result = 'The BFS traversal is '
        self.form.textEdit.clear()

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
        start = self.form.textEdit.toPlainText()
        self.form.textEdit.clear()
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


    def floyd_warshall(self):
        d_of_lists = nx.convert.to_dict_of_lists(self.G)
        res = [[key] + val for key, val in d_of_lists.items()]


        A = nx.adjacency_matrix(self.G)
        print(A)
        print(type(A))
        dist = list(map(lambda i: list(map(lambda j: j, i)), res))

        V = self.G.number_of_nodes()
        for k in range(V):

            # pick all vertices as source one by one
            for i in range(V):

                # Pick all vertices as destination for the
                # above picked source
                for j in range(V):
                    # If vertex k is on the shortest path from
                    # i to j, then update the value of dist[i][j]
                    dist[i][j] = min(dist[i][j],
                                     dist[i][k] + dist[k][j]
                                     )
        result = self.printSolution(dist, V)
        self.form.result_text.setText(result)

    # A utility function to print the solution
    def printSolution(self,distance, nV):
        print("Following matrix shows the shortest distances\
         between every pair of vertices")
        string = "The output matrix : \n"
        for i in range(nV):
            for j in range(nV):
                if (distance[i][j] == 99999):
                    string = string + "INF"

                else:
                    string = string + distance[i][j]

            string = string + ""
        return string

    ''' Check if this vertex is an adjacent vertex
            of the previously added vertex and is not
            included in the path earlier '''

    def isSafe(self, v, pos, path):
        d_of_lists = nx.convert.to_dict_of_lists(self.G)
        graph = [[key] + val for key, val in d_of_lists.items()]
        # Check if current vertex and last vertex
        # in path are adjacent
        if graph[path[pos - 1]][v] == 0:
            return False

        # Check if current vertex not already in path
        for vertex in path:
            if vertex == v:
                return False

        return True

    # A recursive utility function to solve
    # hamiltonian cycle problem
    def hamCycleUtil(self, path, pos):
        d_of_lists = nx.convert.to_dict_of_lists(self.G)
        graph = [[key] + val for key, val in d_of_lists.items()]

        V = self.G.number_of_nodes()
        # base case: if all vertices are
        # included in the path
        if pos == V:
            # Last vertex must be adjacent to the
            # first vertex in path to make a cycle
            if graph[path[pos - 1]][path[0]] == 1:
                return True
            else:
                return False

        # Try different vertices as a next candidate
        # in Hamiltonian Cycle. We don't try for 0 as
        # we included 0 as starting point in hamCycle()
        for v in range(1, V):

            if self.isSafe(v, pos, path) == True:

                path[pos] = v

                if self.hamCycleUtil(path, pos + 1) == True:
                    return True

                # Remove current vertex if it doesn't
                # lead to a solution
                path[pos] = -1

        return False

    def hamCycle(self):
        V = self.G.number_of_nodes()
        path = [-1] * V

        ''' Let us put vertex 0 as the first vertex
            in the path. If there is a Hamiltonian Cycle,
            then the path can be started from any point
            of the cycle as the graph is undirected '''
        path[0] = 0

        if self.hamCycleUtil(path, 1) == False:
            print("Solution does not exist\n")
            return False

        self.printSolution1(path)
        return True

    def printSolution1(self, path):
        print("Solution Exists: Following",
              "is one Hamiltonian Cycle")
        for vertex in path:
            print(vertex, end=" ")
        print(path[0], "\n")


mainloop = QtWidgets.QApplication([])
run_app = GUI()
run_app.show()
sys.exit(mainloop.exec_())

