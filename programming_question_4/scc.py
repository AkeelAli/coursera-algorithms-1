class Node:
    
    def __init__(self, node_id):
        self.node_id = node_id
        self.is_explored = 0
        self.finishing_time = -1
        self.leader_id = -1
        self.edge_ids = [] #outgoing edges

    def add_edge(self, edge_id):
        self.edge_ids.append(edge_id)

    def __str__(self):
        string = "[%d: " % self.node_id
        for edge in self.edge_ids:
            string += "%d " % edge
        string += "]"

        return string


class Graph:
    
    def __init__(self):
        self.node_hash = {} # { node_id : Node }

    def add_node(self, node):
        if isinstance(node, Node):
            self.node_hash[node.node_id] = node
        else:
            print "ERROR: adding node to Graph that isn't instance of Node class"

    def contains_node(self, node_id):
        if node_id in self.node_hash:
            return True
        else:
            return False

    def __str__(self):
        string = ""
        for node_id in self.node_hash:
            string += str(self.node_hash[node_id]) + "\n"
        
        return string

def build_graph(filename):
    graph = Graph()

    f = open(filename, 'r')

    lines = f.readlines();
    for line in lines:
        tail_id = int(line.split(' ')[0])
        head_id = int(line.split(' ')[1])

        if graph.contains_node(tail_id):
            graph.node_hash[tail_id].add_edge(head_id)
            
            if not graph.contains_node(head_id):
                graph.add_node(Node(head_id))
        
        else:
            tail_node = Node(tail_id)
            tail_node.add_edge(head_id)
            graph.add_node(tail_node)
            
            if not graph.contains_node(head_id):
                graph.add_node(Node(head_id))
            
    f.close()

    return graph


graph = build_graph('sample.txt')

print graph
