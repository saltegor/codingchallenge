# define the graph class
class Graph():

    # initialization
    def __init__ (self, graph_data):
        self.graph_data = graph_data
        # just checking 
        # print(self.graph_data)
        # create the variable list for nodes, edges and costs
        self.nodes = []
        self.edges = []
        self.costs = []

    # define adding the node as method
    def add_node(self, node):
        #print("Add node {}".format(node))
        # check that the node doesn't repeat
        if str(node) not in self.nodes:
            # add the node to the end of the list
            self.nodes.append(str(node))
            #print("Node {} is added".format(str(node)))
        else:
            # print a message that the node is already in the list, as it cannot be added more than once
            print("Node {} already exists".format(str(node)))
    
    # define removing the node as method
    def rem_node(self, node):
        #print("Remove node {}".format(node))
        # check that the node exists in the list
        if str(node) in self.nodes:
            # remove the node from the list (assuming there are no self-directed edges)
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
            # print a message that the edge is already in the list, as it cannot be added more than once
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


graph = Graph([1,2,'r',3,4,'t',5,6])
print(graph.import_nodes())
graph.add_node(10)
print(graph.get_nodes())
graph.add_edge('1','2', 5)
graph.add_edge('1','2', 5)
graph.add_edge('3','4', 30)
print(graph.get_edges())
print(graph.get_costs())
graph.add_edge('t','3', 12)
graph.add_edge('r','6', 8)
graph.add_edge('r','z', 18)
graph.add_edge('4','2', 9)
graph.add_edge('2','1', 1)
print(graph.get_edges())
print(graph.get_costs())
print(graph.get_nodes())
graph.rem_edge('1','2')
graph.rem_node("1")
print(graph.get_nodes())
graph.rem_node(1)
print(graph.get_nodes())
graph.rem_node('t')
print(graph.get_nodes())