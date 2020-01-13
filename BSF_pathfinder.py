from collections import defaultdict
# define the graph class
class Graph():

    # initialization
    def __init__ (self, graph_data):
        self.graph_data = graph_data
        # just checking 
        # print(self.graph_data)
        # create the variable list for nodes, edges and cost
        self.nodes = []
        self.edges = []
        self.costs = []

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
    def add_edge(self, node1, node2, cost = 1):
        # add the edge to the edges list
        self.edges.append([str(node1), str(node2)])
        # get the index of the edge to assign the cost
        index = self.edges.index([str(node1), str(node2)])
        # assign the cost
        self.costs.insert(index,cost)
        print(self.edges)
        print(self.costs)

    # define removing the edge between 2 nodes
    def rem_edge(self, node1, node2):
        index = self.edges.index([str(node1), str(node2)])
        self.costs.pop(index)
        print(self.costs)
        self.edges.remove([node1,node2])
        print(self.edges)

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
graph.add_edge('1','2', 5)
graph.add_edge('2','1', 1)
graph.rem_edge('1','2')