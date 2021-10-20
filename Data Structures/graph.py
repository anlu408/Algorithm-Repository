class graph:
    def __init__(self, dictionary = None):
        if dictionary is None:
            dictionary = {}
        self.dictionary = dictionary

    def add_edge(self,vertex,edge):
        self.dictionary[vertex].append(edge)
