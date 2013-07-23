class Edge:
	def __init__(self, id1, id2):
		self.id1 = id1
		self.id2 = id2
	
	def __str__(self):
		return "(%d,%d)" % (self.id1, self.id2)

#complex vertex
class CVertex:
	def __init__(self, id):
		self.size = 0
		self.vertices = []
		self.add_vertex(id)

		self.num_edges = 0
		self.edges = []

	def add_vertex(self, id):
		self.vertices.append(id)
		self.size += 1

	def add_edge(self, edge):
		self.edges.append(edge)
		self.num_edges +=1

	def get_id(self):
		return self.vertices[0]
	
	def __str__(self):
		str = ""
		for 

class Graph:
	def __init__(self):
		self.num_edges = 0
		self.edges = []
		self.num_vertices = 0
		self.cVertices = []

	def add_edge(self, edge):
		self.edges.append(edge)
		self.num_edges += 1

	def add_cVertex(self, cVertex):
		self.cVertices.append(cVertex)
		self.num_vertices += 1

	def is_edge_in_graph(self, in_edge):
		for edge in self.edges:
			if edge.id1 == in_edge.id2 and edge.id2 == in_edge.id1:
				return True
			if edge.id1 == in_edge.id1 and edge.id2 == in_edge.id2:
				return True

		return False
	
	def __str__(self):
		
			


def build_graph_from_file(filename):
	f = open(filename, 'r')

	graph = Graph()

	for line in f.readlines():
		line_list = line.split('\t')
		vertex_id = int(line_list[0])

		vertex = CVertex(vertex_id)

		for i in range(1,len(line_list)):
			if line_list[i] != '\n':
				edge = Edge(vertex_id, int(line_list[i]))
				vertex.add_edge(edge)
				if not graph.is_edge_in_graph(edge):
					graph.add_edge(edge)
			
		graph.add_cVertex(vertex)

	f.close()

	return graph

graph = build_graph_from_file("kargerMinCut.txt")

print graph
