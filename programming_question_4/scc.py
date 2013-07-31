import resource
import sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, 2**30))
sys.setrecursionlimit(10**6)

class Node:
    
    def __init__(self, node_id):
        self.node_id = node_id
        self.is_explored = False
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

def build_graph(filename, reverse):
    graph = Graph()

    f = open(filename, 'r')

    lines = f.readlines();
    for line in lines:
        if reverse:
            head_id = int(line.split(' ')[0])
            tail_id = int(line.split(' ')[1])
        else:
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

def DFS(graph, node_id):
    global finishing_time
    #
    #global graph_update
    global node_ids_by_finishing_time
    #

    node = graph.node_hash[node_id]
    node.is_explored = True
    node.leader_id = source
    #
    #graph_update.node_hash[node_id].leader_id = source
    #

    for edge_id in node.edge_ids:
        edge_node = graph.node_hash[edge_id]
        if not edge_node.is_explored:
            DFS(graph, edge_id)

    finishing_time += 1
    node.finishing_time = finishing_time
    #print "%d finished" % node_id
    #
    #graph_update.node_hash[node_id].finishing_time = finishing_time
    node_ids_by_finishing_time.append(node_id)
    #


def Kosaraju(graph, ordered_id_list = None):
    global source

    graph_size = len(graph.node_hash)
    if ordered_id_list:
        for i in reversed(ordered_id_list):
            node = graph.node_hash[i]
            if not node.is_explored:
                source = i
                DFS(graph, i)

    else:

        for i in range(graph_size, 0, -1):
            node = graph.node_hash[i]
            if not node.is_explored:
                #print "processing %d" % i
                source = i
                DFS(graph, i)


def group_by_leaders(graph):
    #list indexed by leader_id and giving you number of followers part of the scc
    leaders = []
    leaders.append(0) #leader_id 0 does not exist

    for i in range(1, len(graph.node_hash)+1):
        leaders.append(0)

    for node_id in graph.node_hash:
        leader_id = graph.node_hash[node_id].leader_id
        leaders[leader_id] += 1

    return leaders

def find_min(largest_list):
    minimum = largest_list[0]
    for i in largest_list:
        if i < minimum:
            minimum = i
    return minimum

def find_largest_sccs(leaders_list, num):
    min_accepted = 0
    largest = []

    for size in leaders_list:
        if len(largest) < num:
            largest.append(size)
            min_accepted = find_min(largest)
        else:
            if size > min_accepted:
                largest[largest.index(min_accepted)] = size
                min_accepted = find_min(largest)

    return largest




graph = build_graph('SCC.txt', True)
print "Finished building graph rev"

finishing_time = 0
source = 0
node_ids_by_finishing_time = []

Kosaraju(graph)
print "Finished first Kosaraju pass"

f = open('node_ids_by_finishing_time.txt','w')

for node_id in node_ids_by_finishing_time:
    f.write(str(node_id))
    f.write(str('\n'))

f.close()

#graph = build_graph('SCC.txt', False)
#print "Finished building graph"

#Kosaraju(graph, node_ids_by_finishing_time)
#print "Finished second Kosaraju pass"

#leaders = group_by_leaders(graph)

#print find_largest_sccs(leaders, 5)


