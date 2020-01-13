# define the graph class
class Graph():

    # initialization
    def __init__ (self, graph_data):
        self.graph_data = graph_data
        self.nodes = []
        for node in graph_data:
            self.nodes.append(node)
            print(self.nodes)
        self.edges = []
        print(graph_data)

    # define nodes as property
    #@property
    #def nodes(self):
    #    pass

    # define edges as property
    #@property
    #def edges(self):
    #    print(self.edges)

    # define adding the node as method
    def add_node(self, node):
        self.nodes.append(node)
        print("Node {} is added".format(node))
        #print("Current set of nodes:")
    
    # define removing the node as method
    def rem_node(self, node):
        self.nodes.remove(node)
    
    # define nodes output as method
    def get_nodes(self):
        print(self.nodes)

    # define adding the edge between 2 nodes and assing the cost
    def add_edge(self, node1, node2, cost):
        pass

    # define removing the edge between 2 nodes
    def rem_edge(self, node1, node2):
        pass

output= Graph([1,2,'r',3,4,'t',5,6])
#print(output)
output.add_node(1)
output.get_nodes()
output.add_node(2)
output.get_nodes()
output.add_node(6)
output.get_nodes()
output.add_node(3)
output.get_nodes()
output.rem_node(1)
output.get_nodes()
output.rem_node(1)
output.get_nodes()
