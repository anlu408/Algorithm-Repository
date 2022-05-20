'''
Notes section
BFS- Breadth First Search
An algorithm for traversing Graphs starting at an arbitrary node and exploring
neighbor nodes at the current level before moving to the next level.

Use a queue to enqueue a starting vertex, while the queue isn't empty,
dequeue. If the node the algorithm is currently on is unvisited, mark it
as visited, and enqueue the adjacent nodes.
'''

class graph:
    def __init__(self, dictionary = None):
        if dictionary is None:
            dictionary = {}
        self.dictionary = dictionary

    def add_edge(self,vertex,edge):
        self.dictionary[vertex].append(edge)

    def bfs (self, vertex):
        visited = [vertex]
        queue = [vertex]

        while queue:
            dequeue = queue.pop(0)
            print(dequeue)
            for adjacent_vertex in self.gdict[dequeue]:
                if adjacent_vertex not in visited:
                    visited.append(adjacent_vertex)
                    queue.append(adjacent_vertex)
