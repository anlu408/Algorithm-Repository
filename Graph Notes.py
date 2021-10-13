'''
Graph- nonlinear data structure consisting of a finite set of verticies and a set of edges that connect a pair of nodes

Terminology
Vertices- Node of the Graph
Edge- Line connecting pairs of vertices
Unweighted graph- Graph which does not have a weight associated with any edge
Weighted Graph- a weight associated with any edge
Undirected Graph- Edges of graph without direction associated with them
Directed Graph- Edges with a direction
Cyclic Graph- A graph with at least 1 group.
Acyclic Graph- Graph with no loop
Tree- A special case of acyclic graph

Types
Directed & Weighted
    -Positive: Graph has weights with positive numbers and associated direction
    -Negative: At least one weight is negative and includes associated direction
Directed & Unweighted- A graph with no weight associated, but with edges that have direction associated with them.
Undirected and Weighted
    -Positive: Weights are positive numbers with no direction
    -Negative: At least one weight is negative and no direction
Undirected and Unweighted- A graph with no weight or direction associated with them.

Representation
Adjacency Matrix- An Adjacency matrix is a square matrix or 2D array. Elements of the matrix (0- False, 1- True) indicate whether pairs of vertices are adjacent or not in the Graph
Adjacency List- A collection of unorder lists representing a graph. Each list describes neighbors of a vertex. A linked list is used

'''
