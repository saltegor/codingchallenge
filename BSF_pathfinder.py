# define the graph class
class Graph():

    # initialization
    def __init__ (self, graph_data = []):
        self.graph_data = graph_data
        # just checking 
        # print(self.graph_data)
        # create the variable list for nodes, edges and costs
        self.nodes = []
        self.edges = []
        self.costs = []
        self.neighbours = []

    # define adding the node as method
    def add_node(self, node):
        #print("Add node {}".format(node))
        # check that the node doesn't repeat
        if str(node) not in self.nodes:
            # add the node to the end of the list
            self.nodes.append(str(node))
            #print("Node {} is added".format(str(node)))
        else:
            # print a message that the node is already in the list, 
            # as it cannot be added more than once
            print("Node {} already exists".format(str(node)))
    
    # define removing the node as method
    def rem_node(self, node):
        #print("Remove node {}".format(node))
        # check that the node exists in the list
        if str(node) in self.nodes:
            # remove the node from the list (assuming there are 
            # no self-directed edges)
            self.nodes.remove(node)
            # remove all the edges with the corresponding node
            for i in self.nodes:
                # remove the edges from this node to any other
                self.rem_edge(node,i)
                # remove the edges from any node to this node
                self.rem_edge(i,node)
            #print("Removed node {}".format(str(node)))
        else:
            # in case there is no such node, print the message
            print("Node {} doesn\'t exist".format(str(node)))
    
    # define nodes' import from graph data as method
    def import_nodes(self):
        #print("Importing nodes")
        # import the nodes from the graph data
        for node in self.graph_data:
            # check that the node doesn't repeat 
            if node not in self.nodes:
                # add the node to the nodes list at the end
                self.add_node(node)
                #self.nodes.append(str(node))
                # just checking the result at every iteration
                #print(self.nodes)
        return self.nodes
    
    # define nodes output as method
    def get_nodes(self):
        #print("Get nodes")
        return self.nodes

    # define edges output as method
    def get_edges(self):
        #print("Get edges")
        return self.edges
    
    # define costs output as method
    def get_costs(self):
        #print("Get costs")
        return self.costs

    # define adding the edge between 2 nodes and assing the cost
    def add_edge(self, node1, node2, cost = 1):
        #print("Add edge {}, {}, cost {}".format(node1,node2,cost))
        # check that the edge doesn't repeat
        if [str(node1), str(node2)] not in self.edges:
            # add the edge to the edges list
            self.edges.append([str(node1), str(node2)])
            # get the index of the edge to assign the cost
            index = self.edges.index([str(node1), str(node2)])
            # assign the cost
            self.costs.insert(index,cost)
        else:
            # print a message that the edge is already in the list, 
            # as it cannot be added more than once
            print("Edge {}, {} already exists".format(str(node1), str(node2)))
        # check if the nodes of the edge exist in the nodes list
        # and add the node if missing
        if node1 not in self.nodes:
            self.add_node(node1)
        if node2 not in self.nodes:
            self.add_node(node2)
        #print(self.edges)
        #print(self.costs)

    # define removing the edge between 2 nodes
    def rem_edge(self, node1, node2):
        #print("Remove edge {}, {}".format(node1,node2))
        # check that the edge exists
        if [str(node1), str(node2)] in self.edges:
            # the corresponding index is needed to remove the edge cost from the list
            index = self.edges.index([str(node1), str(node2)])
            # remove the corresponding edge cost from the list
            self.costs.pop(index)
            # remove the edge
            self.edges.remove([node1,node2])
            #print("Edges:")
            #print(self.edges)
            #print("Costs:")
            #print(self.costs)
        else:
            # I keep else: in case I need to print the message of non-existing edge.
            # For now it gets annoying when the node is removed and the program checks
            # all the corresponding edges, so that the message floods the console.
            pass
            #print("Edge {} doesn\'t exist".format([str(node1), str(node2)]))

    # define adjacency matrix output as method
    def adjacency(self):
        # redimension the matrix according to the number of nodes
        self.neighbours = [[False for row in range(0,len(self.nodes))] for line in range(0,len(self.nodes))]
        # use each node for rows of matrix
        for node1 in self.nodes:
            # use each element for lines of matrix
            for node2 in self.nodes:
                # the indexes are needed to assign the boolean values
                # to the corresponding rows and lines
                row = self.nodes.index(node1)
                line = self.nodes.index(node2)
                # the main diagonal is False, as we assume there are no self-directed edges
                if not row == line:
                    # assign the boolean value of connection
                    self.neighbours[row][line] = [node1, node2] in self.edges
        return self.neighbours

    # define importing the list of edges all together
    def import_edges(self, edges_list):
        # select every edge from the list
        for node1, node2, cost in edges_list:
            # add the edge
            self.add_edge(node1,node2,cost)


graph = Graph()
edges_list = ([
    ("a", "b", 5),  ("a", "d", 1),  ("b", "a", 3), ("b", "c", 1),
    ("c", "a", 10), ("c", "g", 4), ("d", "e", 3),  ("e", "c", 2),
    ("f", "a", 2), ("f", "d", 7), ("f", "g", 4), ("g", "c", 1),
    ("g", "e", 1), ("g", "f", 1)])
graph.import_edges(edges_list)
print(graph.import_nodes())

print(graph.get_nodes())
print(graph.get_edges())
print(graph.get_costs())
print()
for i in graph.adjacency():
    print(list(map(int,i)))