import networkx.algorithms.operators
from PyQt5 import QtWidgets
import sys
import networkx as nx
from baseg import Ui_Basic
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
        self.form.pushButton.clicked.connect(self.DFS)
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

                'Make changes here so that the string variable above is filled with the formatted data in the print'
                if (distance[i][j] == 99999):
                    print("%7s" % ("INF"), end=" ")

                else:
                    print("%7d\t" % (distance[i][j]), end=' ')
                    if j == nV - 1:
                        print()
        return string

    ''' Check if this vertex is an adjacent vertex
            of the previously added vertex and is not
            included in the path earlier '''

    def hamil_handler(self):
        d_of_lists = nx.convert.to_dict_of_lists(self.G)
        graph = [[key] + val for key, val in d_of_lists.items()]
        print(graph)
        n = self.G.number_of_nodes()
        print(n)
        self.findHamiltonianPaths(graph, n)



    def hamiltonianPaths(self, graph, v, visited, path, n):

        # if all the vertices are visited, then the Hamiltonian path exists
        if len(path) == n:
            # print the Hamiltonian path
            print(path)
            return

        # Check if every edge starting from vertex `v` leads to a solution or not
        for x in graph[v]:
            w = int(x)
            print(x)
            # process only unvisited vertices as the Hamiltonian
            # path visit each vertex exactly once
            if not visited[w]:
                visited[w] = True
                path.append(w)

                # check if adding vertex `w` to the path leads to the solution or not
                self.hamiltonianPaths(graph, w, visited, path, n)

                # backtrack
                visited[w] = False
                path.pop()

    def findHamiltonianPaths(self, graph, n):

        # start with every node
        for start in range(n):
            # add starting node to the path
            path = [start]

            # mark the start node as visited
            visited = [False] * n

            visited[start] = True
            print(visited)
            self.hamiltonianPaths(graph, start, visited, path, n)

    def travellingSalesmanProblem(self, graph, src, V):

        # store all vertex apart from source vertex
        vertex = []
        print(src, type(src))
        s = int(src)
        for i in range(V):
            if i != s:
                vertex.append(i)

        # store minimum weight Hamiltonian Cycle
        min_path = maxsize
        next_permutation = permutations(vertex)
        for i in next_permutation:

            # store current Path weight(cost)
            current_pathweight = 0

            # compute current path weight
            k = s
            for j in i:
                current_pathweight += graph[k][j]
                k = j
            current_pathweight += graph[k][s]

            # update minimum
            min_path = min(min_path, current_pathweight)

        result = 'The path is ' + min_path
        self.form.result_text.setText(result)
        return min_path

    def tsphandler(self):
        d_of_lists = nx.convert.to_dict_of_lists(self.G)
        graph = [[key] + val for key, val in d_of_lists.items()]
        start = self.form.textEdit.toPlainText()

        self.form.textEdit.clear()
        print(graph)
        n = self.G.number_of_nodes()

        print(n)
        self.travellingSalesmanProblem(graph, start, n)

    def nodeconnectivity(self):
        r = approximation.node_connectivity(self.G)
        print(r)
        s = "The node connectivity is : " + str(r)
        self.form.textEdit_3.setText(s)

    def tsphandler2(self):
        l = approximation.traveling_salesman_problem(self.G)
        print(l)

    def complement(self):
        self.G = networkx.algorithms.operators.complement(self.G)
        self.form.plot_canvas.plot(self.G)

    def planarity(self):
        ans = nx.is_planar(self.G)
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
            x = x + ", " + i
        s = "The vertex cover set is : " + x
        self.form.textEdit_3.setText(s)

    def kcomplement(self):
        ans = networkx.algorithms.connectivity.k_components(self.G)
        self.form.textEdit_3.setText(str(ans))

    def ind_set(self):
        ans = networkx.algorithms.approximation.maximum_independent_set
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




mainloop = QtWidgets.QApplication([])
run_app = GUI()
run_app.show()
sys.exit(mainloop.exec_())