# codingchallenge
Code for Coding Challenge 2020

Pathfinder Programming Challenge

## Overview

These instructions describe using the Python program code prepared to solve a path-finding problem,
as requested in the coding challenge received on January 8, 2020. 

## Problem Statement

-   given a graph, i.e. a list of locations (nodes) and a list of available 
    connections (edges) between locations.
-   given cost for using each connection (edge) between locations.

## Task Statement 

-   write a function that finds a path between any two nodes.
-   write a function that finds the cheapest path between two nodes. 
-   design a (simple) Abstract Data Type to represent the graph.

## Available functions

-   Graph(list_of_nodes) creates Graph class object, saves the list of 
    nodes.
-   add_node(node) adds node if it doesn't exist already in the Graph class 
    object.
-   rem_node(node) removes node and all the edges corresponding to it. 
-   get_nodes() returns list of nodes from the Graph class object. 
-   add_edge(node1,node2,cost) adds edge from 'node1' to 'node2', adds the 
    edge using cost, adds node1 and node2 (if not existing yet). If cost not specified, cost=1. 
-   rem_edge(node1,node2) removes edge between node1 and node2. 
-   import_edges(edges_list) adds the edges from the list, their costs and 
    the corresponding nodes (if not existing yet); the edges_list must respect the same input format as in add_edge. 
-   adjacency() returns a boolean adjacency matrix of all the nodes.
-   BFS_explore(start) returns list of nodes of the graph explored using 
    Breadth-First Search starting from the node 'start'.
-   BFS_shortest_path(start,end) returns the shortest path from node 'start'
    to node 'end' computed using BFS algorithm.
-   BFS_cheapest_path(start,end) returns the cheapest path and its cost
    from node 'start' to node 'end' computed using BFS algorithm with
    the idea of Dijkstra algorithm.

## Running the program 

1)  Clone the git repository to your local machine.
2)  Open BFS_pathfinder.py file in your preferred IDE.
3)  Correct the input data: edges list.
4)  Correct, add or toggle line comment for the commands to process the 
    input data.
5)  Save the BFS_pathfinder.py file and run it.