from collections import defaultdict

color_list = ["gold", "violet", "violet", "violet", "limegreen", "limegreen", "darkorange"]


class GFG:
	def __init__(self,graph):
		self.graph = graph
		self.ppl = len(graph)
		self.jobs = len(graph[0])
	def bpm(self, u, matchR, seen):
		for v in range(self.jobs):
			if self.graph[u][v] and seen[v] == False:
				seen[v] = True
				if matchR[v] == -1 or self.bpm(matchR[v],
											matchR, seen):
					matchR[v] = u
					return True
		return False
	def maxBPM(self):
		matchR = [-1] * self.jobs

		result = 0
		for i in range(self.ppl):
			seen = [False] * self.jobs
			if self.bpm(i, matchR, seen):
				result += 1
		return result



MAX = 100
n = 0
store = [0] * MAX

graph = [[0 for i in range(MAX)] for j in range(MAX)]
d = [0] * MAX

def is_clique(b):
	for i in range(1, b):
		for j in range(i + 1, b):
			if (graph[store[i]][store[j]] == 0):
				return False
	
	return True
def maxCliques(i, l):

	max_ = 0
	for j in range(i + 1, n + 1):
		store[l] = j
		if (is_clique(l + 1)):
			max_ = max(max_, l)
			max_ = max(max_, maxCliques(j, l + 1))
		
	return max_


class Graph:

	def __init__(self, vertices):
		self.V = vertices 
		self.graph = defaultdict(list)

	def DFSUtil(self, v, visited):
		visited[v] = True
		for i in self.graph[v]:
			if visited[i] == False:
				self.DFSUtil(i, visited)

	def isConnected(self):
		visited = [False]*(self.V)
		for i in range(self.V):
			if len(self.graph[i]) > 1:
				break
		if i == self.V-1:
			return True
		self.DFSUtil(i, visited)
		for i in range(self.V):
			if visited[i] == False and len(self.graph[i]) > 0:
				return False

		return True

	def isEulerian(self):
		if self.isConnected() == False:
			return 0
		else:
			odd = 0
			for i in range(self.V):
				if len(self.graph[i]) % 2 != 0:
					odd += 1
			if odd == 0:
				return 2
			elif odd == 2:
				return 1
			elif odd > 2:
				return 0

	def test(self):
		res = self.isEulerian()
		if res == 0:
			print("graph is not Eulerian")
		elif res == 1:
			print("graph has a Euler path")
		else:
			print("graph has a Euler cycle")



	def addEdge(self, u, v):
		self.graph[u].append(v)

	def printVertexCover(self):

		visited = [False] * (self.V)
		for u in range(self.V):

			if not visited[u]:

				for v in self.graph[u]:
					if not visited[v]:
						visited[v] = True
						visited[u] = True
						break
		for j in range(self.V):
			if visited[j]:
				print(j, end = ' ')
				
		print()

	def graphSets(self,graph):

		if (len(graph) == 0):
			return []

		if (len(graph) == 1):
			return [list(graph.keys())[0]]

		vCurrent = list(graph.keys())[0]
		graph2 = dict(graph)

		del graph2[vCurrent]
		res1 = self.graphSets(graph2)
		for v in graph[vCurrent]:
			if (v in graph2):
				del graph2[v]
		res2 = [vCurrent] + self.graphSets(graph2)
		if (len(res1) > len(res2)):
			return res1
		return res2

		graph = dict([])
		for i in range(len(E)):
			v1, v2 = E[i]

			if (v1 not in graph):
				graph[v1] = []
			if (v2 not in graph):
				graph[v2] = []

			graph[v1].append(v2)
			graph[v2].append(v1)
		maximalIndependentSet = graphSets(graph)

		for i in maximalIndependentSet:
			print(i, end=" ")


# Planarity
def Regions(Vertices, Edges) :

	R = Edges + 2 - Vertices

	return R




