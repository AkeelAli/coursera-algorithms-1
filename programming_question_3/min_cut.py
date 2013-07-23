import random

class Edge:
	def __init__(self, id1, id2):
		self.id1 = id1
		self.id2 = id2

        def set_id1(self,id1):
            self.id1 = id1

        def set_id2(self,id2):
            self.id2 = id2
	
	def __str__(self):
		return "(%d,%d)" % (self.id1, self.id2)

#complex vertex
class CVertex:
	def __init__(self, id):
		self.size = 1
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

        def remove_edge(self, edge):
                if edge in self.edges:
                    self.edges.remove(edge)
                    self.num_edges -= 1
                else:
                    print "ERROR: cannot find edge (%d,%d) in CVertex %d" % (edge.id1, edge.id2, self.get_id())


	def get_id(self):
		return self.vertices[0]
	
	def __str__(self):
		string = "%d\t" % self.get_id()
                for edge in self.edges:
                    if edge.id1 == self.get_id():
                        string = string + str(edge.id2) + "\t"
                    else:
                        string = string + str(edge.id1) + "\t"
                return string
                    
                    
		 

class Graph:
	def __init__(self):
		self.num_edges = 0
		self.edges = []
		self.num_vertices = 0
		self.cVertices = []

	def add_edge(self, edge):
		self.edges.append(edge)
		self.num_edges += 1

        def remove_edge(self, edge):
                if edge in self.edges:
                    self.edges.remove(edge)
                    self.num_edges -= 1
                else:
                    print "ERROR: cannot find edge (%d,%d) in graph" % (edge.id1, edge.id2)

                

	def add_cVertex(self, cVertex):
		self.cVertices.append(cVertex)
		self.num_vertices += 1

        def remove_cVertex(self, cVertex):
                if cVertex in self.cVertices:
                    self.cVertices.remove(cVertex)
                    self.num_vertices -= 1
                else:
                    print "ERROR: cannot find vertex %d in graph" % cVertex.get_id()

	def is_edge_in_graph(self, in_edge):
		for edge in self.edges:
			if edge.id1 == in_edge.id2 and edge.id2 == in_edge.id1:
				return True
			if edge.id1 == in_edge.id1 and edge.id2 == in_edge.id2:
				return True

		return False

        def get_cVertex(self, vertex_id):
            for vertex in self.cVertices:
                if vertex.get_id() == vertex_id:
                    return vertex

            print "ERROR: could not find vertex %d" % vertex_id
            return None

        def random_contract(self):
            edge_index = random.randint(0, self.num_edges - 1)

            ran_edge = self.edges[edge_index]
            id1 = ran_edge.id1
            id2 = ran_edge.id2

 #           print "...contracting edge (%d,%d)" % (id1, id2)

            cVertex1 = self.get_cVertex(id1)
            cVertex2 = self.get_cVertex(id2)

            fused_cVertex = CVertex(id1)
            fused_cVertex.add_vertex(id2)

            self.remove_cVertex(cVertex1)
            self.remove_cVertex(cVertex2)

            self.add_cVertex(fused_cVertex)

            #change edge id2 to id1 in all references
            to_remove = []
            for edge in self.edges:
                if edge.id1 == id2:
                    edge.set_id1(id1)
                if edge.id2 == id2:
                    edge.set_id2(id1)
                
                #delete self-edge
                if edge.id1 == edge.id2:
                    to_remove.append(edge)

            for edge in to_remove:        
                self.remove_edge(edge)


	
	def __str__(self):
            string = ""
            for vertex in self.cVertices:
                string = string + str(vertex) + "\n"

            return string
		
			


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


while graph.num_vertices > 2:
    graph.random_contract()
#    print "num vertices left = " + str(graph.num_vertices)

print "min_cut = " + str(graph.num_edges)







