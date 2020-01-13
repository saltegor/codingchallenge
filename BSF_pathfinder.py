# define the graph class
class Graph():

    # initialization
    def __init__ (self, graph_data):
        self.graph_data = graph_data
        # just checking 
        print(self.graph_data)
        # create the variable list for nodes
        self.nodes = []
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
        # check that the node doesn't repeat
        if str(node) not in self.nodes:
                self.nodes.append(str(node))
                print("Node {} is added".format(str(node)))
        else:
            print("Node {} already exists".format(str(node)))
    
    # define removing the node as method
    def rem_node(self, node):
        if str(node) in self.nodes:
            self.nodes.remove(node)
            print("Removed node {}".format(str(node)))
        else:
            print("Node {} doesn\'t exist".format(str(node)))
    
    # define nodes import from graph data as method
    def import_nodes(self):
        # import the nodes from the graph data
        for node in self.graph_data:
            # check that the node doesn't repeat
            if node not in self.nodes:
                # add the node to the nodes list at the end
                self.nodes.append(str(node))
                # just checking the result at every iteration
                print(self.nodes)
        return self.nodes
    
    # define nodes output as method
    def get_nodes(self):
        return self.nodes

    # define adding the edge between 2 nodes and assing the cost
    def add_edge(self, node1, node2, cost):
        pass

    # define removing the edge between 2 nodes
    def rem_edge(self, node1, node2):
        pass

graph = Graph([1,2,'r',3,4,'t',5,6])
print(graph.import_nodes())

graph.add_node(1)
print(graph.get_nodes())
graph.add_node(10)
print(graph.get_nodes())
graph.add_node('1')
print(graph.get_nodes())
graph.add_node(3)
print(graph.get_nodes())
graph.rem_node("1")
print(graph.get_nodes())
graph.rem_node(1)
print(graph.get_nodes())
graph.rem_node('t')
print(graph.get_nodes())