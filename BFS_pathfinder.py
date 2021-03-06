# define the graph class
class Graph():

    # initialization
    def __init__ (self, list_of_nodes = []):
        self.list_of_nodes = list_of_nodes
        # just checking 
        # print(self.graph_data)
        # create the variable list for nodes, edges and costs
        self.nodes = []
        self.edges = []
        self.costs = []
        self.neighbours = []
        self.import_nodes()

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
    
    # define nodes' import from list of nodes as method
    def import_nodes(self):
        #print("Importing nodes")
        # import the nodes from the graph data
        for node in self.list_of_nodes:
            # check that the node doesn't repeat 
            if node not in self.nodes:
                # add the node to the nodes list at the end
                self.add_node(node)
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
        self.neighbours = [[False for row in range(0,len(self.nodes))] for column in range(0,len(self.nodes))]
        # use each node for rows of matrix
        for node1 in self.nodes:
            # use each element for columns of matrix
            for node2 in self.nodes:
                # the indexes are needed to assign the boolean values
                # to the corresponding rows and columns
                row = self.nodes.index(node1)
                column = self.nodes.index(node2)
                # the main diagonal is False, as we assume there are no self-directed edges
                if row != column:
                    # assign the boolean value of connection
                    self.neighbours[row][column] = [node1, node2] in self.edges
        return self.neighbours

    # define importing the list of edges all together
    def import_edges(self, edges_list):
        # select every edge from the list
        for node1, node2, cost in edges_list:
            # add the edge
            self.add_edge(node1,node2,cost)

    # define BFS exploring algorithm, i.e. visiting 
    # all the nodes of the graph using BFS
    def BFS_explore(self, start):
        # keep track of all visited nodes
        explored = []
        # keep track of nodes to be checked
        queue = [start]

        # keep looping until there are nodes still to be checked
        while queue:
            # pop shallowest node (first node) from queue
            node = queue.pop(0)
            #print('Node', node)
            #print('Explored',explored)
            if node not in explored:
                # add node to list of checked nodes
                explored.append(node)
                # the index for assosiating the neighbours matrix with the nodes list
                index = self.nodes.index(node)
                # iterator
                a = 0
                # put in the queue only if there is edge
                for check in graph.neighbours[index]:
                    if check:
                        queue.append(self.nodes[a])
                    # increment
                    a += 1
            #print('Queue', queue)
        return explored
    
    # define the BFS algorithm to find the shortest path between 2 nodes
    def BFS_shortest_path(self, start, end):
        # keep track of all visited nodes
        explored = []
        # keep track of nodes to be checked
        queue = [[start]]

        # keep looping until all the possible paths have been checked
        while queue:
            # pop shallowest node (first node) from queue
            path = queue.pop(0)
            #print('Path', [path])
            #print('Explored',explored)
            node = path[-1]
            if node not in explored:
                # the index for assosiating the neighbours matrix with the nodes list
                index = self.nodes.index(node)
                # iterator
                a = 0
                # go through all neighbour nodes, construct a new path and
                # push it into the queue
                for check in graph.neighbours[index]:
                    new_path = list(path)
                    if check:
                        new_path.append(self.nodes[a])
                        queue.append(new_path)
                        # return path if the edge connects to the end
                        if self.nodes[a] == end:
                            return new_path
                    # increment
                    a += 1
                # add node to list of checked nodes
                explored.append(node)
            #print('Queue', queue)
        return "No connecting path"

    # define the BFS algorithm to find the shortest path between 2 nodes
    def BFS_cheapest_path(self, start, end):
        # keep track of all visited nodes
        explored = []
        # keep track of nodes to be checked
        queue = [[start]]
        # set the path cost to infinity for all the nodes
        path_cost = [float('inf') for i in self.nodes]
        # set cost for starting node as 0
        path_cost[self.nodes.index(start)] = 0
        
        node = start
        # for the output
        cheapest_path = [[],float('inf')]

        # keep looping until all the possible paths have been checked
        while queue:
            # pop shallowest node (first node) from queue
            path = queue.pop(0)
            node = path[-1]
            if node not in explored:
                # the index for assosiating the neighbours matrix with the nodes list
                index = self.nodes.index(node)
                # iterator
                a = 0
                # go through all neighbour nodes, construct a new path and
                # push it into the queue
                for check in graph.neighbours[index]:
                    if check:
                        new_path = list(path)
                        # save the parameters from the lists, 
                        # to make code more readable
                        iterator_node = self.nodes[a]
                        cost_index = self.edges.index([node, iterator_node])
                        new_path.append(iterator_node)
                        temp = self.costs[cost_index] + path_cost[index]
                        if temp < path_cost[a]:
                            path_cost[a] = temp
                        queue.append(new_path)
                        # save path if the edge connects to the end
                        if self.nodes[a] == end:
                            # but make sure it is the cheapest
                            if path_cost[a] < cheapest_path[1]:
                                cheapest_path = [new_path, path_cost[a]]
                    # increment
                    a += 1
                # add node to list of checked nodes
                explored.append(node)
        return cheapest_path

    '''
    # define dijkstra algorithm for the cheapest path
    def dijkstra(self, start, end):
        # keep track of all visited nodes
        explored = []
        # keep track of nodes to be checked
        queue = self.nodes.copy()
        distances = list(self.nodes)
        previous_nodes = list(self.nodes)
        node = start
        
        # set the distance to infinity for all the nodes
        for i in range(len(self.nodes)):
            distances[i] = float('inf')
            previous_nodes[i] = None
        # set distance 0 for starting node
        distances[self.nodes.index(node)] = 0
        
        while queue:
            #explored.append(node)
            print('Explored', explored)
            for i in queue:
                if distances[self.nodes.index(i)] < distances[self.nodes.index(node)]:
                    node = i
            print(distances)
            print(distances.index(min(distances)))
            node = self.nodes[distances.index(min(distances))]
            queue.remove(node)
            # the index for assosiating the neighbours matrix with the nodes list
            index = self.nodes.index(node)
            if distances[index] == float('inf'):
                break
            
            # iterator
            a = 0
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for check in graph.neighbours[index]:
                if check:
                    iterator_node = self.nodes[a]
                    cost_index = self.edges.index([node, iterator_node])
                    cost = self.costs[cost_index]
                    cost = distances[index] + cost
                    if cost < distances[a]:
                        distances[a] = cost
                        previous_nodes[a] = node
                        #node = self.nodes[a]
                         
                    # return path if the edge connects to the end
                    #if node == end:
                    #   return new_path
                # increment
                a += 1
            # add node to list of checked nodes
            explored.append(node)
        path = []
        node = end
        while previous_nodes[self.nodes.index(node)] is not None:
            path.append(node)
            node = previous_nodes[self.nodes.index(node)]
        if path:
            path = node + path
        return path
        
        #print('Queue', queue)
        #return "No connecting path"

  '''          


graph = Graph()
edges_list = ([
    ("a", "b", 5),  ("a", "d", 1),  ("b", "a", 3), ("b", "c", 1),
    ("c", "a", 10), ("c", "g", 4), ("d", "e", 3),  ("e", "c", 2),
    ("f", "a", 2), ("f", "d", 7), ("f", "g", 4), ("g", "c", 1),
    ("g", "e", 1), ("g", "f", 1)])
graph.import_edges(edges_list)
print(graph.import_nodes())
print('Get nodes')
print(graph.get_nodes())
print('Get edges')
print(graph.get_edges())
print('Get costs')
print(graph.get_costs())
print('Get adjacency matrix as boolean')
for i in graph.adjacency():
    print(i)
print('Get adjacency matrix as 0/1')
for i in graph.adjacency():
    print(list(map(int,i)))
print()
print('BFS exploring starting from g')
print(graph.BFS_explore('g'))
print('BFS path d, f')
print(graph.BFS_shortest_path('d','f')) 
print(graph.nodes)
print()
print(graph.BFS_cheapest_path('a','e'))
#print(graph.dijkstra('d','f'))