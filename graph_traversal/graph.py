class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        edge_list = []
        for edge in self.edges:
            edge_to_append = (edge.value, edge.node_from.value, edge.node_to.value)
            edge_list.append(edge_to_append)
        return edge_list

    def get_adjacency_list(self):
        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indicies of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        # go through the edges
        # for each node record where it points to and the edge value
            # put this in the corresponding index. 
        # We are populating the list with null values. We don't create a 2d list straight away as indexing becomes tricky. 
        # Indstead of at that index the list is equal to None we just put a list inside the list at that index and then append from there. 
        needed_length = self.list_length()
        edge_list = [None] * (needed_length +1)
        #print(edge_list)
        
        for edge in self.edges:
            # check if there is an entry at this index or not.
            if edge_list[edge.node_from.value] != None:
                edge_list[edge.node_from.value].append((edge.node_to.value, edge.value))
            else:
                edge_list[edge.node_from.value] = [(edge.node_to.value, edge.value)]
            
            #print(edge_list)
        
        return edge_list



       
    
    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        list_to_return = [[0,0,0,0,0] for _ in range(self.list_length() +1 )]
        for edge in self.edges:
            list_to_return[edge.node_from.value][edge.node_to.value] = edge.value
        return list_to_return

    def list_length(self):
        max_value = 0
        for node in self.nodes:
            if node.value > max_value:
                max_value = node.value
        #print(max_value)
        return max_value

graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)
# Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
print(graph.get_edge_list())
# Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
# You get none because we are returning an adjacency list. 
# the first none comes about because node 0 (the first node) doesn't actually exist. 
# The second none (at index 2) comes about because the node with value 2 does not go to anything. 1 is connected to 2 but it is not both ways. So because adjacency is in part defined by direction here
# we have a situation where the node at index 2 returns null in this case. 
# the last null comes about here (at index 4) because the node with value 4 also points toward nothing. 
print( graph.get_adjacency_list())
# Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
print( graph.get_adjacency_matrix())

#print(graph.list_length())

## Best way to understand what to do is to draw the data structure. [i] is node and - i -> is edge value 
# [1] - 100 -> [2]
# [1] - 102 -> [4]
# [1] - 101 -> [3]
# [3] - 103 -> [4]