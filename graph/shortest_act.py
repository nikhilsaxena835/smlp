from collections import defaultdict

class Graph():

		def __init__(self, vertices):
			self.V = vertices
			self.graph = [[0 for column in range(vertices)]
						  for row in range(vertices)]

		def printSolution(self, dist):
			print("Vertex \t Distance from Source")
			for node in range(self.V):
				print(node, "\t\t", dist[node])

		def minDistance(self, dist, sptSet):

			min = 1e7

			for v in range(self.V):
				if dist[v] < min and sptSet[v] == False:
					min = dist[v]
					min_index = v

			return min_index

		def dijkstra(self, src):

			dist = [1e7] * self.V
			dist[src] = 0
			sptSet = [False] * self.V

			for cout in range(self.V):

				u = self.minDistance(dist, sptSet)

				sptSet[u] = True

				for v in range(self.V):
					if (self.graph[u][v] > 0 and
							sptSet[v] == False and
							dist[v] > dist[u] + self.graph[u][v]):
						dist[v] = dist[u] + self.graph[u][v]

		def floyd_warshall(G, nV):
			distance = list(map(lambda i: list(map(lambda j: j, i)), G))

			# Adding vertices individually
			for k in range(nV):
				for i in range(nV):
					for j in range(nV):
						distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

		def bellman_ford(self, src):
				dist = [float("Inf")] * self.V
				dist[src] = 0
				for _ in range(self.V - 1):
					for s, d, w in self.graph:
						if dist[s] != float("Inf") and dist[s] + w < dist[d]:
							dist[d] = dist[s] + w

				for s, d, w in self.graph:
					if dist[s] != float("Inf") and dist[s] + w < dist[d]:
						print("Graph contains negative weight cycle")
						return
				self.print_solution(dist)