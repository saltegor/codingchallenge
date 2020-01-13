# define the graph class
class Graph():

    # initialization
    def __init__ (self, graph_data):
        self.graph_data = graph_data
        # just checking 
        print(self.graph_data)
        # create the variable list for nodes
        self.nodes = []
        # import the nodes from the graph data
        for node in graph_data:
            # check that the node doesn't repeat
            if node not in self.nodes:
                # add the node to the nodes list at the end
                self.nodes.append(node)
            # otherwise print a message that the node already exists
            else:
                print("Node {} already exists".format(node))
            # just checking the result at every iteration
            print(self.nodes)
        self.edges = []

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
        if node not in self.nodes:
                self.nodes.append(node)
                print("Node {} is added".format(node))
        else:
            print("Node {} already exists".format(node))
        #print("Current set of nodes:")
    
    # define removing the node as method
    def rem_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
        else:
            print("Node {} doesn\'t exist".format(node))
    
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
output.add_node(10)
output.get_nodes()
output.add_node('y')
output.get_nodes()
output.add_node(3)
output.get_nodes()
output.rem_node(1)
output.get_nodes()
output.rem_node(1)
output.get_nodes()
output.rem_node('t')
output.get_nodes()