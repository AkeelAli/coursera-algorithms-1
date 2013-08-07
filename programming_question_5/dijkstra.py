distances = {}

class Node:
    
    def __init__(self, id):
        self.id = id
        self.edge_tuples = []

    def add_edge(self, id, cost):
        self.edge_tuples.append((id,cost))

    
    def get_dist(self):
        return distances[self.id]

    def set_dist(self, dist):
        distances[self.id] = dist


# list of pointers to unvisited nodes
Q = []

def build_graph(filename):
    global Q
    global distances

    graph = {}
    
    f = open(filename, 'r')

    lines = f.readlines()

    for line in lines:
        items = line.split('\t')
        node_id = int(items[0])
        node = Node(node_id)

        for i in range(1,len(items)):
            split = items[i].split(',')
            if len(split) != 2:
                continue
            
            neighbour_id = int(split[0])
            edge_cost = int(split[1])

            node.add_edge(neighbour_id, edge_cost)

        graph[node_id] = node
        distances[node_id] = 1000000 #infinity
        Q.append(node)

    f.close()

    return graph

def extract_lowest_distance_node():
    global Q
    lowest_distance = 1000000
    lowest_node = None

    for node in Q:
        dist = node.get_dist() 
        if dist < lowest_distance:
            lowest_distance = dist
            lowest_node = node
    
    if lowest_node is not None: 
        Q.remove(lowest_node)

    return lowest_node


def dijkstra(graph, source_id):
    #set distance of source node to 0
    distances[source_id] = 0

    while len(Q) > 0:
        node = extract_lowest_distance_node()

        if node is None or node.get_dist() == 1000000:
            return

        for edge_tuple in node.edge_tuples:
            neighbour_node = graph[edge_tuple[0]]
            new_dist = node.get_dist() + edge_tuple[1]

            if new_dist < neighbour_node.get_dist():
                neighbour_node.set_dist(new_dist)

graph = build_graph('dijkstraData.txt')

dijkstra(graph, 1)

print distances[7]
print distances[37]
print distances[59]
print distances[82]
print distances[99]
print distances[115]
print distances[133]
print distances[165]
print distances[188]
print distances[197]
