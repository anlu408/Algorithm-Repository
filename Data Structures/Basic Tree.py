class node:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    def __str__(self):
        ret = " " * level + str(self.data) + "\n"
        ret += child.__str__(level + 1)
        return ret

    def addChild (self, node):
        self.children.append(node)
